from database import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS ofertas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    descripcion TEXT,
    precio DECIMAL(10,2),
    imagen VARCHAR(255)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS reservas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    correo VARCHAR(100),
    telefono VARCHAR(20),
    destino VARCHAR(100),
    fecha DATE,
    personas INT,
    comentario TEXT
)
""")

conn.commit()
cursor.close()
conn.close()

print("Tablas creadas correctamente")