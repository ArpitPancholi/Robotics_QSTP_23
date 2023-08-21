
import pygame
import math

# Pygame setup
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PID Controller Simulation")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Robot parameters
robot_radius = 20
robot_color = RED

# Goal parameters
goal_radius = 15
goal_color = GREEN

# PID parameters
kp = 0.1
ki = 0.01
kd = 0.2

# Simulation parameters
dt = 0.1  # Time step
target = (400, 300)  # Initial goal position
robot_pos = [100, 100]  # Initial robot position
integral = 0
prev_error = 0

def pid_control(current_pos, target_pos):
    global integral, prev_error
    
    error = math.sqrt((target_pos[0] - current_pos[0]) ** 2 + (target_pos[1] - current_pos[1]) ** 2)
    integral += error * dt
    derivative = (error - prev_error) / dt
    
    output = kp * error + ki * integral + kd * derivative
    
    prev_error = error
    return output

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update robot position using PID control
    control_signal = pid_control(robot_pos, target)
    angle = math.atan2(target[1] - robot_pos[1], target[0] - robot_pos[0])
    robot_pos[0] += control_signal * math.cos(angle) * dt
    robot_pos[1] += control_signal * math.sin(angle) * dt
    
    screen.fill(BLACK)
    
    # Draw goal
    pygame.draw.circle(screen, goal_color, target, goal_radius)
    
    # Draw robot
    pygame.draw.circle(screen, robot_color, (int(robot_pos[0]), int(robot_pos[1])), robot_radius)
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()