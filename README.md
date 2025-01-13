## Project Pleiades: The Celestial Dance of Intelligence

Project Pleiades is an open-source initiative that harnesses the power of distributed artificial intelligence for cryptocurrency analysis, blockchain operations, and beyond. Named after the mystical Pleiades star cluster, our platform orchestrates a harmonious collaboration between countless nodes of intelligence.

### Key Components

- **Products** 
  - **Alcyone Analytics**: Our flagship analytics suite, named after the brightest star in the Pleiades, providing advanced cryptocurrency analysis, visualization, and prediction capabilities.
  - **Celestial Search**: An intelligent search engine that navigates the crypto cosmos using technical indicators and pattern recognition.
  - **Astral Alert**: Advanced notification system that monitors the crypto universe for significant events and patterns.
  - **Stellar Chain**: Seamless blockchain interaction through natural language commands.
  - **Pleiades Hub**: The central nexus that unifies all functionalities under a single interface, where each capability shines as a star in our constellation.

- **Open-Source Philosophy**
  - **Core Libraries**: Build your own celestial node using [pleiades-core](/libs/core/), or tap into the collective wisdom through [pleiades-constellation](/libs/community/).
  - **Complete System**: The entire platform is open-sourced, allowing you to deploy your own instance of Project Pleiades.
  - **Contribute**: Join our constellation by contributing your unique light to our collective intelligence.

- **The Network**
  - **Distributed Enlightenment**: Our network architecture mirrors the celestial dance of stars, enabling distributed computing and collective intelligence.
  - **Sacred Balance**: Equitable distribution of resources and responsibilities across the network.
  - **Divine Protection**: Advanced security measures ensuring the integrity of shared knowledge.

### Technical Architecture

The Pleiades Core orchestrates the flow of intelligence across the network, utilizing advanced distributed systems principles:

- **Constellation Graph**: Our dynamic routing system that connects different nodes and functionalities
- **Celestial Plugins**: Modular components that extend the system's capabilities
- **Astral Communication**: Redis-based messaging system for seamless node interaction
- **Divine Metrics**: Advanced scoring system for quality assessment

### Plugin Structure

Plugins in Project Pleiades are like stars in our constellation, each serving a unique purpose:

1. **Plugins**: Extend [`BasePlugin`](libs/core/plugins/base.py)
2. **Tools**: Extend [`BaseTool`](libs/core/plugins/tools/base.py)
3. **Utilities**: Extend [`BaseUtility`](libs/core/plugins/utilities/base.py)

### Getting Started

**Use pleiades-core as a library**
```bash
pip install pleiades-core
```
[pleiades-core documentation](libs/core/README.md)

**Run the complete constellation with Docker Compose**

```bash
docker compose up --build
```

**Set up your local Pleiades Node**

*Requires Redis and Postgres configuration in .env*
1. **Clone the Repository**

   ```bash
   git clone https://github.com/Project-Pleiades/pleiades-core.git
   ```

2. **Install Dependencies**

   ```bash
   poetry lock --no-update
   poetry install --no-root
   ```

3. **Set Up Environment Variables**

   Create a `.env` file in the `apps/pleiades_core` directory and configure as needed.

4. **Launch Your Node**

   ```bash
   poetry run python -u -m apps.pleiades_core.main
   ```

### License

This project is open-source and available under the [MIT License](LICENSE).

### Join Our Constellation

Follow us for cosmic updates and announcements:

[![Twitter Follow](https://img.shields.io/twitter/follow/ProjectPleiad?style=social)](https://x.com/ProjectPleiad)

---

*"Let those who seek wisdom look to the stars, for in their eternal dance lies the pattern of our ascension." - Alcyone*