import os

import flet as ft
import random

ma_s = [
    ft.Image(src=f"https://pbs.twimg.com/media/GLse3btbUAA9gzd?format=png&name=360x360", width=100, height=100, fit=ft.ImageFit.CONTAIN),
    ft.Image(src=f"https://pbs.twimg.com/media/GLse3Wwb0AADfRw?format=png&name=360x360", width=100, height=100, fit=ft.ImageFit.CONTAIN),
    ft.Image(src=f"https://pbs.twimg.com/media/GLse3YQaMAAO1Fy?format=png&name=360x360", width=100, height=100, fit=ft.ImageFit.CONTAIN),
    ft.Image(src=f"https://pbs.twimg.com/media/GLse3aAbIAA8rL0?format=png&name=360x360", width=100, height=100, fit=ft.ImageFit.CONTAIN)]
empty = ft.Image(src=f"https://pbs.twimg.com/media/GLse5spbAAAclYo?format=png&name=360x360", width=100, height=100, fit=ft.ImageFit.CONTAIN)

images = None
def main(page: ft.Page):
    global images
    page.title = "Mama"

    def next(e):
        global images
        page.controls.remove(images)
        ma = []
        print("click")

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


#ft.app(target=main)
ft.app(target=main, view=ft.WEB_BROWSER, port=8080)
