from django.shortcuts import render
import qrcode
import io
from django.http import HttpResponse


def index(request):
    if request.method == 'POST':
        data = request.POST.get('text')
        name = request.POST.get('name')
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        buffer = io.BytesIO()
        img.save(buffer)
        buffer.seek(0)
        response = HttpResponse(buffer, content_type='image/png')
        response['Content-Disposition'] = f'attachment; filename="{name}.png"'
        return response
    return render(request, 'index.html', {
    }
    )
