def collect_data(angle_range, velocity_range):
    dataset = []

    for angle in angle_range:
        for velocity in velocity_range:
            from projectile_simulation import simulate_projectile
            success, final_position = simulate_projectile(angle, velocity)

            if success:
                dataset.append((angle, velocity, final_position))

    return dataset
