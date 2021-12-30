# SOAL NOMOR 1

# Memanggil modul Pillow-8.4.0
from PIL import Image, ImageDraw, ImageFilter, ImageFont

# A - Box Blur dengan radius 1 piksel
##### Membuka berkas citra yang akan diolah
pic = Image.open('gambar_nomor_satu.jpg')
##### Melakukan proses Box Blur dengan radius 1 piksel
blurred_pic = pic.filter(ImageFilter.BoxBlur(1))
##### Melakukan inisialisasi gambar yang sudah di blur ke variabel "draw"
draw = ImageDraw.Draw(blurred_pic)

# B - Menambahkan tulisan NAMA dan NIM ke dalam citra hasil blur
##### Inisialisasi tipe font yang akan digunakan beserta ukurannya
font_family = ImageFont.truetype("Shizuru-Regular.ttf", 120)
##### Proses menempatkan tulisan NAMA dan NIM ke dalam citra
draw.text((123,456), "RIVALTINO ARRON_32180050", (7, 8, 9), font=font_family)

# C - Menyimpan citra dengan format ".jpeg" dan dengan kualitas "web_maximum"
blurred_pic.save("hasil_nomor_satu.jpeg", quality="web_maximum")

# Menampilkan citra yang sudah diolah
blurred_pic.show()