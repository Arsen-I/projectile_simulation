import math


def simulate_projectile(angle_deg, initial_velocity):
    angle_rad = math.radians(angle_deg)
    gravity = 9.81
    time_step = 0.01
    initial_position = (0, 0)
    vx = initial_velocity * math.cos(angle_rad)
    vy = initial_velocity * math.sin(angle_rad)

    t = 0
    while True:
        x = initial_position[0] + vx * t
        y = initial_position[1] + vy * t - 0.5 * gravity * t ** 2

        if x >= 100:  # example distance to target
            return True, (x, y)

        if y < 0:
            return False, (x, y)

        t += time_step
