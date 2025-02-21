# 🎮 AI-Powered RPG Game Engine

A modern, GPU-accelerated game engine that combines the power of Local Language Models (LLM) with traditional game mechanics to create an immersive RPG experience.

## 🚀 Features

- **🧠 AI-Powered Interactions**
  - Natural language command processing via Ollama
  - Dynamic NPC conversations
  - Adaptive game mechanics

- **⚡ High Performance**
  - GPU-accelerated rendering
  - Optimized game loop
  - Efficient state management

- **🎨 Modular Architecture**
  - Agent-based system design
  - Extensible component framework
  - Easy-to-add new features

## 🛠️ Prerequisites

- Python 3.12+
- Ollama (Local LLM runner)
- uv (Fast Python package installer)
- GPU with OpenGL support

## 📦 Installation

1. **Install Ollama**
   ```bash
   # Windows (using winget)
   winget install Ollama.Ollama
   
   # Verify installation
   ollama --version
   
   # Pull the Mistral model
   ollama pull mistral
   ```

2. **Install uv**
   ```bash
   pip install uv
   ```

3. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/llm-game-engine.git
   cd llm-game-engine
   ```

4. **Set up virtual environment with uv**
   ```bash
   # Create and activate virtual environment
   uv venv game_env
   game_env\Scripts\activate  # On Windows
   # source game_env/bin/activate  # On Unix/MacOS
   ```

5. **Install dependencies**
   ```bash
   uv pip install -r requirements.txt
   ```

## 🎮 Running the Game

1. **Make sure Ollama is running**
   The Ollama service should be running in the background.

2. **Start the game**
   ```bash
   uv run main.py
   ```

3. **Basic Commands**
   - Movement: "go left", "move forward", etc.
   - Combat: "attack enemy", "cast fireball", etc.
   - Inventory: "check inventory", "use potion", etc.
   - NPC Interaction: "talk to merchant", "ask about quest", etc.

## 🏗️ Architecture

The engine is built on a modular, agent-based architecture:

- **Input Layer**: Handles user commands and game events
- **AI Layer**: Processes natural language via Ollama
- **Agent Layer**: Manages game logic through specialized agents
- **Game Loop**: Handles rendering and state updates

For detailed architecture information, see [ARCHITECTURE.md](ARCHITECTURE.md).

## 🔧 Development

### Adding New Features

1. Create a new agent in `agents/`
2. Register it with the GameAgent
3. Implement state management
4. Add rendering support

### Running Tests

```bash
uv run -m pytest tests/
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Ollama team for the amazing LLM runtime
- PyGame community for the graphics engine
- All contributors and supporters

## 🚀 Roadmap

- [ ] Multiplayer support
- [ ] Advanced AI-driven NPCs
- [ ] Procedural world generation
- [ ] Quest system
- [ ] Advanced combat mechanics

## 📞 Contact

- GitHub: [your-username](https://github.com/your-username)
- Email: your.email@example.com

## 🐛 Bug Reports

Please use the GitHub issues page to report bugs. 