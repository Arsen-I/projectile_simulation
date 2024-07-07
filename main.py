from projectile_simulation import simulate_projectile
from data_collection import collect_data
from neural_network import NeuralNetwork
from reinforcement_agent import ReinforcementLearningAgent


# Example usage
def main():
    # Simulate projectile
    angle = 30
    initial_velocity = 50
    success, final_position = simulate_projectile(angle, initial_velocity)
    if success:
        print(f"The projectile hit the target at position {final_position}")
    else:
        print(f"The projectile fell short at position {final_position}")

    # Collect data
    angle_range = range(20, 71, 10)
    velocity_range = range(30, 101, 10)
    dataset = collect_data(angle_range, velocity_range)

    # Train neural network
    input_size = 2  # angle and velocity
    hidden_size = 8
    output_size = 1  # predicted velocity
    model = NeuralNetwork(input_size, hidden_size, output_size)
    # Training code here

    # Create reinforcement learning agent
    agent = ReinforcementLearningAgent(model)
    # Agent usage code here


if __name__ == "__main__":
    main()