
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\gabri\OneDrive - Universidade de Brasília\Área de Trabalho\Tkinter-Designer-master\Telas Geradas\build\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1200x800")
window.configure(bg = "#F1F1F1")


canvas = Canvas(
    window,
    bg = "#F1F1F1",
    height = 800,
    width = 1200,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    687.325927734375,
    463.1461181640625,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    110.0,
    411.0898742675781,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    122.26971435546875,
    53.7078857421875,
    image=image_image_3
)

canvas.create_text(
    17.52813720703125,
    153.70785522460938,
    anchor="nw",
    text="Tipo de material",
    fill="#FFFFFF",
    font=("Inter Bold", 23 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=18.87640380859375,
    y=214.0,
    width=193.4129180908203,
    height=29.3136043548584
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=18.87640380859375,
    y=261.57305908203125,
    width=193.4129180908203,
    height=29.42694091796875
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=341.0,
    y=648.0,
    width=163.0,
    height=29.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=513.0,
    y=649.0,
    width=163.0,
    height=29.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=342.0,
    y=692.0,
    width=163.0,
    height=29.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=513.0,
    y=692.0,
    width=163.0,
    height=29.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    882.2689971923828,
    427.3687515258789,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=735.2682890892029,
    y=410.2950134277344,
    width=294.00141620635986,
    height=32.14747619628906
)

canvas.create_text(
    733.483154296875,
    392.3595886230469,
    anchor="nw",
    text="URI da capa do livro",
    fill="#344054",
    font=("Inter Bold", 11 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    882.2689971923828,
    366.69461822509766,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=735.2682890892029,
    y=349.6208801269531,
    width=294.00141620635986,
    height=32.14747619628906
)

canvas.create_text(
    733.483154296875,
    331.6853942871094,
    anchor="nw",
    text="Localização Física",
    fill="#344054",
    font=("Inter Bold", 11 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    882.2689971923828,
    304.67212677001953,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=735.2682890892029,
    y=287.598388671875,
    width=294.00141620635986,
    height=32.14747619628906
)

canvas.create_text(
    733.483154296875,
    269.6629333496094,
    anchor="nw",
    text="Estado de conservação",
    fill="#344054",
    font=("Inter Bold", 11 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    512.8307647705078,
    613.0737380981445,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=365.8300566673279,
    y=596.0,
    width=294.00141620635986,
    height=32.14747619628906
)

canvas.create_text(
    365.393310546875,
    577.0786743164062,
    anchor="nw",
    text="Data de aquisição",
    fill="#344054",
    font=("Inter Bold", 11 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    512.8307647705078,
    550.0653762817383,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=365.8300566673279,
    y=532.9916381835938,
    width=294.00141620635986,
    height=32.14747619628906
)

canvas.create_text(
    365.393310546875,
    515.0562133789062,
    anchor="nw",
    text="Categoria",
    fill="#344054",
    font=("Inter Bold", 11 * -1)
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    512.8307647705078,
    487.9557876586914,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=365.8300566673279,
    y=470.8820495605469,
    width=294.00141620635986,
    height=32.14747619628906
)

canvas.create_text(
    365.393310546875,
    453.0337219238281,
    anchor="nw",
    text="Descrição",
    fill="#344054",
    font=("Inter Bold", 11 * -1)
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    512.8307647705078,
    427.2815933227539,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=365.8300566673279,
    y=410.2078552246094,
    width=294.00141620635986,
    height=32.14747619628906
)

canvas.create_text(
    365.393310546875,
    391.01123046875,
    anchor="nw",
    text="ISBN",
    fill="#344054",
    font=("Inter Bold", 11 * -1)
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    512.8307647705078,
    367.6355667114258,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=365.8300566673279,
    y=350.56182861328125,
    width=294.00141620635986,
    height=32.14747619628906
)

canvas.create_text(
    365.393310546875,
    331.6853942871094,
    anchor="nw",
    text="Autor",
    fill="#344054",
    font=("Inter Bold", 11 * -1)
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    512.8307647705078,
    304.58499908447266,
    image=entry_image_9
)
entry_9 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_9.place(
    x=365.8300566673279,
    y=287.5112609863281,
    width=294.00141620635986,
    height=32.14747619628906
)

canvas.create_text(
    365.393310546875,
    269.6629333496094,
    anchor="nw",
    text="Título",
    fill="#344054",
    font=("Inter Bold", 11 * -1)
)

canvas.create_text(
    360.0,
    230.5618133544922,
    anchor="nw",
    text="Digite todos os campos.",
    fill="#667085",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    307.41571044921875,
    186.06744384765625,
    anchor="nw",
    text="Livros",
    fill="#344054",
    font=("Inter Bold", 26 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    884.89892578125,
    563.5617980957031,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    885.5169067382812,
    534.3033752441406,
    image=image_image_5
)

canvas.create_text(
    853.4832153320312,
    602.6966552734375,
    anchor="nw",
    text="Título Livro",
    fill="#FFFFFF",
    font=("Inter Bold", 11 * -1)
)

canvas.create_text(
    360.0,
    116.97576904296875,
    anchor="nw",
    text="Cadastro de livros e materiais.",
    fill="#667085",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    360.0,
    72.80899047851562,
    anchor="nw",
    text="Acervo",
    fill="#344054",
    font=("Inter Bold", 33 * -1)
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=272.0,
    y=73.0,
    width=69.0,
    height=68.0
)
window.resizable(False, False)
window.mainloop()