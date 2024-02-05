from langchain.callbacks.base import BaseCallbackHandler
from langchain.schema import LLMResult
from typing import Dict, List, Any
from collections import deque
import time


class MyCustomHandler(BaseCallbackHandler):
    def __init__(self, queue) -> None:
        super().__init__()
        self._queue = queue
        self._stop_signal = None
        self._start_time = None
        self._first_token_time = None
        self._last_token_time = None
        self._token_times = deque()
        self._num_tokens = 0
        print("Custom handler Initialized")

    def reset(self):
        """Resets all state variables to initial values."""
        self._start_time = None
        self._first_token_time = None
        self._last_token_time = None
        self._token_times.clear()
        self._num_tokens = 0

    def on_llm_start(
        self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> None:
        """Run when LLM starts running."""
        self.reset()
        self._start_time = time.time()
        print("Generation started")

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        """Run when a new token is generated."""
        if self._first_token_time is None:
            self._first_token_time = time.time()
            self._last_token_time = self._first_token_time
            ttft = self._first_token_time - self._start_time
            self._num_tokens += 1
            print(f"Time To First Token (TTFT): {ttft:.5f} seconds")
        else:
            current_time = time.time()
            itl = current_time - self._last_token_time
            self._last_token_time = current_time

            self._token_times.append(itl)
            self._num_tokens += 1
            # print(f"Inter-token latency: {itl:.5f} seconds")
            self._queue.put(token)

    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> None:
        """Run when LLM ends running."""
        latency = self._last_token_time - self._first_token_time
        print(f"Latency: {latency:.5f} seconds")
        print(f"Number of tokens: {self._num_tokens}")
        avg_itl = sum(self._token_times) / (self._num_tokens - 1)
        print(f"Average inter-token latency: {avg_itl:.5f} seconds")
        throughput = self._num_tokens / latency
        print(f"Throughput: {throughput:.2f} tokens/second")
        print("\n\ngeneration concluded")
        self._queue.put(self._stop_signal)
