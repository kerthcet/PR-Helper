from abc import ABC, abstractmethod
from typing import Tuple

import torch
import transformers

SYSTEM_PROMPT = "system"
USER_PROMPT = "user"


# TODO: Support in-memory history in the future, then no need to pass-in the history parameter.
class Chat(ABC):
    def __init__(
        self,
        model_name_or_path: str = None,
        task: str = None,
        torch_dtype: torch.dtype = torch.float16,
    ) -> None:
        pass

    @abstractmethod
    def completion(
        self,
        system_prompt: str = None,
        user_prompt: str = None,
    ) -> str:
        """
        Args:
            system_prompt (str): Not all language models support system prompt, e.g. ChatGLM2.
            user_prompt (str):
        """
        pass

    # TODO: Support history conversation in the future.
    @classmethod
    @abstractmethod
    def prompt(
        self,
        system_prompt: str = None,
        user_prompt: str = None,
    ) -> str:
        pass

    # This is low-performance because each time we'll load the model, instead,
    # if possible, call the completion() by the Chat instance.
    @classmethod
    @abstractmethod
    def acompletion(
        cls,
        model_name_or_path: str = None,
        system_prompt: str = None,
        user_prompt: str = None,
    ) -> str:
        pass
