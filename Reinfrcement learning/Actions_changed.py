import numpy as np
import random

# Define the grid environment
positions = 5  # Initial position 0 to 4
actions = 2    # 0 - Move left, 1 - Move right

# Q-table
Q = np.zeros((positions, actions))

# Define parameters
episodes = 5000  # Number of episodes per training
learning_rate = 0.5
gamma = 0.9      # Discount factor for future rewards
epsilon = 1.0    # Start with full exploration

# Training loop
for episode in range(episodes):
    state = random.randint(0, positions - 1)  # Randomly select an initial position

    while state < positions - 1:  # Until reaching the goal
        # Action selection (Epsilon-greedy policy)
        if random.uniform(0, 1) < epsilon:
            action = random.randint(0, actions - 1)  # Randomly select an action
        else:
            action = np.argmax(Q[state])  # Exploit best known action

        # Take Action  
        if action == 0:  # Move left
            next_state = max(0, state - 1)
        else:  # Move right
            next_state = min(positions - 1, state + 1)

        # Reward structure
        if next_state == positions - 1:
            reward = 10  # Positive reward for reaching the goal
        else:
            reward = -0.1  # Small penalty for each step taken

        # Q-learning update
        Q[state, action] += learning_rate * (
            reward + gamma * np.max(Q[next_state]) - Q[state, action]
        )

        # Transition to the next state
        state = next_state  # Update the current state

    # Decay epsilon
    epsilon *= 0.99  # Decay epsilon

# Show Learned Q-table
print('Q-table:')
print(Q)

# Test the trained agent
state = random.randint(0, positions - 1)  # Start from a random initial position
steps = 0
print("\nAgent path to goal:")

while state < positions - 1:
    action = np.argmax(Q[state])
    if action == 0:  # Move left
        next_state = max(0, state - 1)
    else:  # Move right
        next_state = min(positions - 1, state + 1)

    print(f"Step {steps}: Position {state} -> Action {action} -> Next Position {next_state}")
    state = next_state  # Update the current state
    steps += 1  # Increment step counter

print(f"Reached goal in {steps} steps.")