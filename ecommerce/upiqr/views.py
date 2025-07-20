import qrcode
from io import BytesIO
from django.shortcuts import render
from django.http import HttpResponse

def qrcode_form(request):
    qr_image_url = None
    data = request.GET.get('data')
    if data:
        qr_image_url = f"/generate_qrcode/?data={data}"
    return render(request, 'qrcode_form.html', {'qr_image_url': qr_image_url})

def generate_qrcode(request):
    data = request.GET.get('data', 'https://example.com')  # default fallback
    qr = qrcode.make(data)

    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    buffer.seek(0)

    return HttpResponse(buffer.read(), content_type="image/png")