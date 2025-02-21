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

- Python 3.10+
- Ollama (Local LLM runner)
- PyGame
- GPU with OpenGL support

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/llm-game-engine.git
   cd llm-game-engine
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Ollama**
   - Windows: `winget install Ollama.Ollama`
   - Pull the Mistral model: `ollama pull mistral`

## 🎮 Usage

1. **Start the game**
   ```bash
   python main.py
   ```

2. **Basic Commands**
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
python -m pytest tests/
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