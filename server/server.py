import logging
from ray import serve
from fastapi import FastAPI
from pydantic import BaseModel
import torch

from pipelines.summary_pipeline import SummaryPipeline

app = FastAPI()


# Item helps to constrain the request parameters.
class Item(BaseModel):
    url: str


@serve.deployment(
    route_prefix="/agent",
    ray_actor_options={
        "num_cpus": 1,
        "num_gpus": 1,
    },
    autoscaling_config={"min_replicas": 1, "max_replicas": 1},
)
@serve.ingress(app)
class PRDeployment:
    def __init__(
        self,
        model_name_or_path: str = None,
        task: str = None,
        torch_dtype: torch.dtype = torch.float16,
    ) -> None:
        """
        Args:
            model_name_or_path (str): The model name or the model path.
            task (str): The task defining which pipeline will be returned.
            torch_dtype (torch.dtype): The precision for this model.
        """
        self.summary_pipeline = SummaryPipeline(
            model_name_or_path=model_name_or_path, task=task, torch_dtype=torch_dtype
        )

    # TODO
    @app.get("/pr-review")
    def review(self):
        pass

    @app.post("/pr-summary/")
    def summary(self, item: Item):
        """
        Args:
            item (Item): The POST body should include the url.
        """
        logging.debug("request parameters: {item}")
        return self.summary_pipeline.chat(url=item.url)


deployment = PRDeployment.bind(
    model_name_or_path="/models/llama-2-7b-chat-hf", task="text-generation"
)
