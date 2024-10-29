# 🚀 **RL-RequestMaximizer** 🌐

**An async Python agent that optimizes HTTP requests using Reinforcement Learning (RL).**  
Automatically adjusts request delays and retry counts to improve resilience and boost request success rates in network-constrained or unstable environments.

## 📖 **About the Project**

RL-RequestMaximizer is designed to help API-heavy applications make more reliable HTTP requests by learning the best settings for delay and retries. This async agent uses **Reinforcement Learning** to self-optimize in real time, reducing failures and making network operations smoother and more efficient.

## ✨ **Features**

- **Adaptive Delay & Retry Logic**: Dynamically adjusts based on reward feedback.
- **Reinforcement Learning** 🧠: Self-tunes delay and retries based on request success.
- **Fully Asynchronous** 🔄: Built with `aiohttp` and `asyncio` for high-performance networking.
- **Persistence** 💾: Save and load trained models to retain learning over sessions.

---

## ⚙️ **Installation**

First, clone the repository and navigate to the project directory:

```bash
git clone https://github.com/Armanx200/RL-RequestMaximizer.git
cd RL-RequestMaximizer
```

Then, install the required packages:

```bash
pip install -r requirements.txt
```

---

## 🚀 **Usage**

1. **Train the Agent**: Run `app.py` to start training the RL agent on the request environment.

   ```bash
   python app.py
   ```

   Training progress and agent status will be logged to the console as shown below:

   ```
   Epoch 1/200 | Delay: 0.80 | Max Retries: 3 | Success Count: 800 | Reward: 0.80
   ```

2. **Load a Trained Agent**: To load a previously saved agent for reuse:

   ```python
   agent = RLAgent.load("trained_agent.pkl")
   ```

3. **Customize Parameters**: You can modify the number of requests or training epochs directly in `app.py` as needed.

---

## 📜 **License**

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more information.

---

Happy optimizing! 🚀
