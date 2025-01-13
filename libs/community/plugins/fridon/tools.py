from libs.community.plugins.pleiades.utilities import pleiadesRagUtility
from pleiadesai_core.plugins.schemas import BaseToolInput
from pleiadesai_core.plugins.tools import BaseTool
from pydantic import Field


class pleiadesResponderInput(BaseToolInput):
    question: str = Field(..., description="The question about pleiadesai")


pleiadesResponderTool = BaseTool(
    name="pleiades-responder",
    description="Always use this tool to answer questions before CompleteTool.",
    args_schema=pleiadesResponderInput,
    utility=pleiadesRagUtility(),
    examples=[
        {
            "request": "Who are you?",
            "response": "",
        },
        {
            "request": "What plugins do you have?",
            "response": "",
        },
        {
            "request": "What do you do?",
            "response": "",
        },
        {
            "request": "What is pleiadesai's features?",
            "response": "",
        },
    ],
)


TOOLS = [pleiadesResponderTool]
