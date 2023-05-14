import wpilib  # Importar la biblioteca wpilib

# Crear objeto de robot
robot = wpilib.RobotBase()

# Inicializar mapa SLAM
mapa = robot.initialize_slam_map()

# Mover el robot y actualizar el mapa
robot.drive(2.5, 1.0)  # Mover el robot hacia adelante y a la derecha
mapa = robot.update_slam_map()

# Mover el robot nuevamente y actualizar el mapa
robot.drive(1.0, 3.2)  # Mover el robot hacia adelante y a la izquierda
mapa = robot.update_slam_map()

# Mostrar el mapa SLAM
robot.show_slam_map(mapa)  # Mostrar el mapa generado por el algoritmo SLAM
