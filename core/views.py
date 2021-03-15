from django.shortcuts import render

def home(request):
    mock_data = {
        "products":[
            {"title":"Vestel NF2701 300 Lt A+ No-Frost Buzdolabı","img":"img/refrigerator.jpeg","price":"2.600"},
            {"title":"Huawei FreeBuds Pro Bluetooth Kulaklık - Silver Frost","img":"img/headphone.jpeg","price":"1.249,20"},
            {"title":"Philips 50PUS8505 50'' 126 Ekran Uydu Alıcılı 4K Ultra HD Android Smart LED TV","img":"img/tv.jpeg","price":"5.135,00"},
            {"title":"Philips 3000 Serisi HC3520/15 Saç Kesme Makinesi","img":"img/hairclipper.jpeg","price":"269,90"}
            ]
    }
    return render(request,"core/home.html",{'data':mock_data})