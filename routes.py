from fastapi import APIRouter
from database import get_connection

router = APIRouter()


@router.get("/ofertas")
def obtener_ofertas():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ofertas")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data
    except Exception as e:
        return {"error": str(e)}


@router.get("/reservas")
def obtener_reservas():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM reservas")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data
    except Exception as e:
        return {"error": str(e)}


@router.post("/reservas")
def registrar_reserva(reserva: dict):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO reservas(nombre, correo, telefono, destino, fecha, personas, comentario)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            reserva["nombre"],
            reserva["correo"],
            reserva["telefono"],
            reserva["destino"],
            reserva["fecha"],
            reserva["personas"],
            reserva.get("comentario", ""),
        ))

        conn.commit()
        cursor.close()
        conn.close()

        return {"mensaje": "Reserva registrada correctamente"}

    except Exception as e:
        return {"error": str(e)}