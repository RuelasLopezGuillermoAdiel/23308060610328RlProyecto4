import flet as ft

def main(page: ft.Page):
    page.title = "Registro de eventos"
    
    nombre = ft.TextField(
        label = "escribe el nombre",
        hint_text = "escribe el nombre"
    )
    
    tipo = ft.Dropdown(
        label = "tipos de eventos",
        options = [
            ft.dropdown.Option("Conferencias"),
            ft.dropdown.Option("talleres"),
            ft.dropdown.Option("informativos"),
        ],
        value = "conferencia"
    )
    modalidad = ft.RadioGroup(
        content = ft.Row([
            ft.Radio(value = "Presencial", label = "Presencial"),
            ft.Radio(value = "Virtual", label = "Virtual"),
        ]),
        value = "Presencial"
    )
    inscripcion = ft.Checkbox(
        label = "¿Requieres inscripcion previa?",
        value = False
    )
    duracion = ft.Slider(
        min = 1,
        max = 8,
        divisions = 7,
        label = "{value} horas",
        value = 1
    )
    
    resume = ft.Text(
        value = "",
        size = 16,
        weight = ft.FontWeight.BOLD
    )
    
    def mostrar(e):
        resume.value = (
            "nombre: " + nombre.value + "\n"
            "tipo: " + tipo.value + "\n"
            "Modalidad: " + modalidad.value + "\n"
            "inscripcion previa: " +("si" if inscripcion.value else "no") + "\n"
            "Duracion: " + str(int(duracion.value)) + " horas"
        )
        page.update()
    boton = ft.ElevatedButton(
        "mostrar resumen",
        on_click=mostrar
    )
    page.add(
        ft.Text("formulario de registro de eventos", size = 20, weight = ft.FontWeight.BOLD),
        nombre,
        tipo,
        modalidad,
        inscripcion,
        duracion,
        boton,
        ft.Divider(),
        resume
    )
    
ft.app(target=main)