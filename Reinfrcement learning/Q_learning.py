import numpy as np
import random

# Define the grid environment
positions = 5  # Initial position 0 to 4
actions = 2    # 0 - Move left, 1 - Move right

# Q-table
Q = np.zeros((positions, actions))

# Define parameters
episodes = 1000  # Number of episodes per training
learning_rate = 0.8
gamma = 0.9      # Discount factor for future rewards
epsilon = 0.3    # Probability of taking a random action (Exploration)

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
        # Simulate environment response (for simplicity, assume moving left or right)      
        if action == 0:
            next_state = max(0, state - 1)  # Move left
        else:
            next_state = min(positions - 1, state + 1)  # Move right

        # Reward structure (for simplicity, assume reaching position 4 is the goal)
        if next_state == positions - 1:  # If goal reached
            reward = 10  # Positive reward for reaching the goal
        else:
            reward = -1  # Negative reward for each step taken

        # Q-learning update
        # Update Q-value using the Q-learning formula
        Q[state, action] += learning_rate * (
            reward + gamma * np.max(Q[next_state]) - Q[state, action]
        )

        # Transition to the next state
        state = next_state  # Update the current state to the next state

# Show Learned Q-table
print('Q-table:')
print(Q)

# Test the trained agent
state = 0  # Start from initial position
steps = 0  # Initialize the counter
print("\nAgent path to goal:")

# Agent path to the goal
while state < positions - 1:
    action = np.argmax(Q[state])
    if action == 0:
        next_state = max(0, state - 1)  # Move left
    else:
        next_state = min(positions - 1, state + 1)  # Move right

    print(f"Step {steps}: Position {state} -> Action {action} -> Next Position {next_state}")
    state = next_state  # Update the current state to the next state
    steps += 1  # Increment step counter

print(f"Reached goal in {steps} steps.")

# Final Q-table
print("\nFinal Q-table:")
print(Q)