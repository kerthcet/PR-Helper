import torch
from langchain import PromptTemplate

from pipelines.pipeline import Pipeline
from pipelines.templates.summary_template import (
    SUMMARY_SYSTEM_PROMPT,
    SUMMARY_USER_PROMPT,
)
from providers.github_provider import get_pr_info
from llms.llama import LlamaChat


class SummaryPipeline(Pipeline):
    """
    SummaryPipeline is used for summary the PR.
    """

    def __init__(
        self,
        model_name_or_path: str = None,
        task: str = None,
        torch_dtype: torch.dtype = torch.float16,
    ) -> None:
        self.llmchat = LlamaChat(
            model_name_or_path=model_name_or_path, task=task, torch_dtype=torch_dtype
        )

    def chat(self, url: str, return_format: str = "yaml") -> str:
        PROMPT = PromptTemplate(
            template=SUMMARY_USER_PROMPT,
            input_variables=[
                "title",
                "description",
                "commit_messages",
                "pr_diffs",
                "format",
            ],
        )

        pr_info = get_pr_info(url=url)
        user_prompt = PROMPT.format(
            title=pr_info["title"],
            description=pr_info["description"],
            commit_messages=pr_info["commit_messages"],
            pr_diffs=pr_info["pr_diffs"],
            format=return_format,
        )

        return self.llmchat.completion(
            system_prompt=SUMMARY_SYSTEM_PROMPT, user_prompt=user_prompt
        )
