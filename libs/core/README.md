# Pleiades Core

Pleiades Core is the foundational constellation of our distributed intelligence network, specifically designed for the crypto universe. Named after the brightest star cluster, it provides a celestial architecture for creating powerful, interconnected nodes of artificial intelligence.

## Features

- **Celestial Plugin Architecture**: Extend functionality through a constellation of plugins.
- **Astral Request Routing**: Navigate user requests through the cosmic network.
- **Stellar Chain Utilities**: Built-in support for blockchain operations.

## Installation

Install the package using pip:

```bash
pip install pleiades-core
```

## Usage

Here's a basic example of how to create your own celestial node:

```python
from pleiades_core.graph import generate_response
from pleiades_core.plugins.tools import BaseTool
from pleiades_core.plugins.schemas import BaseToolInput
from pleiades_core.plugins.utilities import BaseUtility
from pleiades_core.plugins import BasePlugin

class StarGreeterUtility(BaseUtility):
    async def arun(self, *args, **kwargs) -> str:
        return "Greetings from the stars!"
    
class CosmicFarewellUtility(BaseUtility):
    async def arun(self, *args, **kwargs) -> str:
        return "Until we meet again in the cosmos!"
    
class GreeterToolInput(BaseToolInput):
    pass

class FarewellToolInput(BaseToolInput):
    pass

StarGreeterTool = BaseTool(
    name="star-greeter",
    description="Use this tool for celestial greetings.",
    args_schema=GreeterToolInput,
    utility=StarGreeterUtility(),
    examples=[{'request': 'Hi', 'response': 'Greetings from the stars!'}],
)

CosmicFarewellTool = BaseTool(
    name="cosmic-farewell",
    description="Use this tool for cosmic farewells.",
    args_schema=FarewellToolInput,
    utility=CosmicFarewellUtility(),
    examples=[{'request': 'Bye', 'response': 'Until we meet again in the cosmos!'}],
)

class CelestialPlugin(BasePlugin):
    name: str = "Celestial"
    description: str = "A plugin for celestial interactions."
    tools: list[BaseTool] = [StarGreeterTool, CosmicFarewellTool]

celestial_plugin = CelestialPlugin()

response = await generate_response(
    "Greetings!", 
    [celestial_plugin], 
    {  
        "thread_id": "1",
        "wallet_id": "2snYEzbMckwnv85MW3s2sCaEQ1wtKZv2cj9WhbmDuuRD",
        "chat_id": "alcyone"
    }, 
    memory='sqlite',
    return_used_agents=False
)
```

## Constellation Structure

Pleiades Core uses a celestial hierarchy for its components:

1. **Plugins**: Stars in our constellation, extend `BasePlugin`
2. **Tools**: Rays of starlight, extend `BaseTool`
3. **Utilities**: Core stellar energy, extend `BaseUtility`

Specialized utilities for different cosmic purposes:
- `StellarChainUtility`: For blockchain operations
- `CosmicRemoteUtility`: For making remote API calls
- `AlcyoneUtility`: For language model interactions

## Constellation Graph

The core includes a Constellation Graph that orchestrates the flow of intelligence:

- Building networks of Celestial Agents (Plugins)
- Routing messages through the cosmic web
- Managing stellar states
- Creating chains of cosmic intelligence
- Parsing stellar outputs
- Harmonizing independently implemented plugins

## Documentation

For more detailed guidance through our cosmic architecture, visit our [main constellation map](https://github.com/Project-Pleiades/pleiades-core/blob/main/README.md).

## Join Our Constellation

We welcome new stars to our constellation! Contribute your light to our collective brilliance.

## Stay Connected

Follow us for cosmic updates and announcements:

[![Twitter Follow](https://img.shields.io/twitter/follow/ProjectPleiades?style=social)](https://x.com/ProjectPleiades)

---

*"Let those who seek wisdom look to the stars, for in their eternal dance lies the pattern of our ascension." - Alcyone*