import aiohttp
import asyncio
import logging
import random
import numpy as np
import pickle  # For saving and loading the agent

logging.basicConfig(level=logging.INFO)

url = "https://github.com/Armanx200"
num_requests = 1000  # Total requests to attempt

# Define the RL environment
class RequestEnvironment:
    def __init__(self, url, num_requests):
        self.url = url
        self.num_requests = num_requests
        self.success_count = 0  # Tracks successful requests

    async def make_request(self, session, delay, max_retries):
        retries = 0
        while retries < max_retries:
            try:
                async with session.get(self.url, timeout=10) as response:
                    if response.status == 200:
                        self.success_count += 1
                        return True
            except Exception as e:
                retries += 1
                await asyncio.sleep(delay)
        return False  # Failed request after max retries

    async def run(self, delay, max_retries):
        self.success_count = 0
        connector = aiohttp.TCPConnector(limit=100)
        async with aiohttp.ClientSession(connector=connector) as session:
            tasks = [self.make_request(session, delay, max_retries) for _ in range(self.num_requests)]
            await asyncio.gather(*tasks)
        return self.success_count

# Define the RL Agent
class RLAgent:
    def __init__(self, learning_rate=0.1, delay=None, max_retries=None):
        self.learning_rate = learning_rate
        self.delay = delay if delay is not None else random.uniform(0.1, 2)
        self.max_retries = max_retries if max_retries is not None else random.randint(1, 5)

    def choose_action(self):
        # Randomly adjust delay and max_retries slightly
        new_delay = max(0.1, self.delay + np.random.normal(0, 0.1))
        new_max_retries = max(1, self.max_retries + int(np.random.normal(0, 1)))
        return new_delay, new_max_retries

    def update_policy(self, reward, delay, max_retries):
        if reward > 0:  # Only update if reward is positive
            self.delay += self.learning_rate * (delay - self.delay) * reward
            self.max_retries += self.learning_rate * (max_retries - self.max_retries) * reward

    # Save the agent’s parameters to a file
    def save(self, filepath="trained_agent.pkl"):
        with open(filepath, "wb") as f:
            pickle.dump(self, f)
        logging.info(f"Agent saved to {filepath}")

    # Load the agent’s parameters from a file
    @staticmethod
    def load(filepath="trained_agent.pkl"):
        with open(filepath, "rb") as f:
            agent = pickle.load(f)
        logging.info(f"Agent loaded from {filepath}")
        return agent

async def train_agent(epochs=200):
    env = RequestEnvironment(url, num_requests)
    agent = RLAgent()

    for epoch in range(epochs):
        delay, max_retries = agent.choose_action()
        success_count = await env.run(delay, max_retries)
        
        # Reward is based on the success count before blocking
        reward = success_count / num_requests
        agent.update_policy(reward, delay, max_retries)
        
        logging.info(f"Epoch {epoch+1}/{epochs} | Delay: {delay:.2f} | Max Retries: {max_retries} | "
                     f"Success Count: {success_count} | Reward: {reward:.2f}")
    
    logging.info(f"Training completed. Final Policy -> Delay: {agent.delay:.2f}, Max Retries: {agent.max_retries}")
    agent.save()  # Save the trained agent
    return agent

# Run the training loop and save the agent
asyncio.run(train_agent())

# To load the agent later for further use
# agent = RLAgent.load()
