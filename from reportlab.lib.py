from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import cm
from datetime import datetime

def generar_informe_usuario(nombre_usuario, prestamos):
    c = canvas.Canvas("C:/Users/SENA/Desktop/informe_biblioteca_usuario.pdf", pagesize=A4)
    width, height = A4


    # Añadir franja de color semitransparente para el texto (verde oscuro)
    c.setFillColorRGB(0, 0.4, 0.2)  # Verde oscuro
    c.rect(0, height - 4*cm, width, 4*cm, fill=True, stroke=False)  # Franja superior

    # Título (Texto en blanco sobre la franja)
    c.setFont("Helvetica-Bold", 22)
    c.setFillColor(colors.white)
    c.drawCentredString(width / 2, height - 2.5*cm, "📚 Informe de Usuario - Biblioteca")

    # Datos del usuario (Texto en blanco sobre la franja)
    c.setFont("Helvetica", 12)
    c.setFillColor(colors.white)
    c.drawString(3*cm, height - 4.7*cm, f"Usuario: {nombre_usuario}")
    c.drawString(3*cm, height - 5.4*cm, f"Fecha de emisión: {datetime.today().strftime('%d/%m/%Y')}")

    # Encabezado de la tabla
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(colors.darkgreen)
    y = height - 6*cm
    c.drawString(3*cm, y, "Título del libro")
    c.drawString(9*cm, y, "Fecha préstamo")
    c.drawString(13*cm, y, "Devolución")
    c.drawString(17*cm, y, "Estado")

    # Línea separadora
    c.setStrokeColor(colors.darkgreen)
    c.line(2.5*cm, y - 5, width - 2.5*cm, y - 5)

    # Contenido de la tabla
    c.setFont("Helvetica", 10)
    c.setFillColor(colors.black)
    y -= 1*cm
    for prestamo in prestamos:
        titulo, fecha_prestamo, fecha_devolucion, estado = prestamo
        c.drawString(3*cm, y, titulo)
        c.drawString(9*cm, y, fecha_prestamo)
        c.drawString(13*cm, y, fecha_devolucion)
        c.drawString(17*cm, y, estado)
        y -= 0.8*cm
        if y < 3*cm:
            c.showPage()
            c.drawImage("fondo.jpg", 0, 0, width=width, height=height)  # Para mantener el fondo
            y = height - 4*cm

    c.showPage()
    c.save()
    print("✅ Informe generado correctamente.")

# Ejemplo de uso
prestamos = [
    ("El Principito", "01/04/2025", "08/04/2025", "Devuelto"),
    ("1984", "05/04/2025", "12/04/2025", "Pendiente"),
    ("Cien años de soledad", "10/04/2025", "17/04/2025", "Devuelto")
]

generar_informe_usuario("Camila Ríos", prestamos)
