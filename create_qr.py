import qrcode


def obtain_data():
    data = input("Introduce la dirección web o el mensaje que quieres utilizar para generar el Código QR : ")
    while len(data) == 0:
        data = input("Por favor, indica el texto: ")
    name = input("¿Cómo quieres llamar a este QR?: ")
    while len(name) == 0:
        name = input("Por favor, indica como quieres llamar a tu código QR: ")
    return data, name


def create_qr_code(data, name):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"{name}.png")


my_data, my_name = obtain_data()
create_qr_code(my_data, my_name)
