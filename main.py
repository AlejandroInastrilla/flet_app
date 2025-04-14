import flet as ft

def main(page):
    page.add(ft.Text("¡Hola Mundo!"))
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
