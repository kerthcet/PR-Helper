from ray import serve
import requests

from server.server import deployment

serve.run(deployment)

resp = requests.post(
    "http://localhost:8000/agent/pr-summary",
    json={"url": "https://github.com/kubernetes/kubernetes/pull/120252"},
)
print(resp.json())
