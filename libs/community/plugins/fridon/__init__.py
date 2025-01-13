from libs.community.plugins.pleiades.tools import TOOLS
from pleiadesai_core.plugins import BasePlugin
from pleiadesai_core.plugins.registry import ensure_plugin_registry
from pleiadesai_core.plugins.tools import BaseTool

plugin_registry = ensure_plugin_registry()


@plugin_registry.register("pleiades")
class pleiadesPlugin(BasePlugin):
    name: str = "pleiades"
    description: str = "Plugin for getting information about pleiadesai."
    owner: str = "2snYEzbMckwnv85MW3s2sCaEQ1wtKZv2cj9WhbmDuuRD"
    tools: list[BaseTool] = TOOLS
    image_url: str = "https://pleiades-ai-assets.s3.eu-central-1.amazonaws.com/agent-avatars/pleiades.png"
