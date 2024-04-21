import flet as ft
import random

ma_s = [
    ft.Image(src=f"image/ma2.png", width=100, height=100, fit=ft.ImageFit.CONTAIN),
    ft.Image(src=f"image/ma1.png", width=100, height=100, fit=ft.ImageFit.CONTAIN),
    ft.Image(src=f"image/ma3.png", width=100, height=100, fit=ft.ImageFit.CONTAIN),
    ft.Image(src=f"image/ma4.png", width=100, height=100, fit=ft.ImageFit.CONTAIN)]
empty = ft.Image(src=f"image/empty.png", width=100, height=100, fit=ft.ImageFit.CONTAIN)

images = None
def main(page: ft.Page):
    global images
    page.title = "Mama"

    def next(e):
        global images
        page.controls.remove(images)
        ma = []

        if random.random() < 0.5:
            letter_count = 3
        else:
            letter_count = 2

        for i in range(letter_count):
            ma.append(random.choice(ma_s))

        if letter_count == 2:
            ma.append(empty)

        ma.append(button)

        images = ft.Row(ma)

        page.controls.append(images)
        page.update()

    button = ft.FilledButton(text="下一步", on_click=next)

    images = ft.Row([ma_s[0], ma_s[1], ma_s[2], button])

    page.controls.append(images)
    page.update()


ft.app(target=main)
