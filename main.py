import flet as ft

def main(page: ft.Page):
    page.bgcolor=ft.colors.PRIMARY_CONTAINER
    t = ft.Text(value="To do list (demo)")
    c1 = ft.Checkbox(label="homework", value=False)
    page.add(t,c1)
    page.update()
ft.app(target=main)