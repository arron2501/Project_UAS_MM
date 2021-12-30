import pydub

audio = pydub.AudioSegment.from_mp3("bensound-sunny.mp3")
ten_seconds = 10 * 1000

# [1] Potong 10 detik awal
first_10_seconds = audio[:ten_seconds]
first_10_seconds.export("[1]potong_10dtk_awal.ogg", format="ogg")

# [2] Potong 5 detik akhir
last_5_seconds = audio[-5000:]
last_5_seconds.export("[2]potong_5dtk_akhir.ogg", format="ogg")

# [3] Volume naik 10 di 10 detik awal
naik10volume_10dtk_awal = first_10_seconds + 10
naik10volume_10dtk_awal.export("[3]naik10volume_10dtk_awal.ogg", format="ogg")

# [4] Volume turun 5 di 5 detik akhir
turun5volume_5dtk_akhir = last_5_seconds - 5
turun5volume_5dtk_akhir.export("[4]turun5volume_5dtk_akhir.ogg", format="ogg")

# [5] Efek crossfade
with_style = naik10volume_10dtk_awal.append(turun5volume_5dtk_akhir, crossfade=1500)
with_style.export("[5]efek_crossfade.ogg", format="ogg")

# [6] Efek reverse
backwards = audio.reverse()
backwards.export("[6]efek_reverse.ogg", format="ogg")