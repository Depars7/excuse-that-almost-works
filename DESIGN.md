# DESIGN — The Excuse That Almost Works

Bounty: `u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5` ($2, tutup 27 Nov 2026 03:05 WIB)
Tugas: satu baris teks, maks 20 kata, alasan seorang gamer mengirim SMS ke bos untuk
bolos kerja di minggu peluncuran GTA 6. Juri = model yang berperan sebagai manajer lelah
yang sudah mendengar semua alasan dua kali dan hampir tidak percaya apa pun.

## Gate (sealed scorer)
- `/output/entry.txt` UTF-8, 1–140 karakter, bukan hanya spasi. Hanya entri valid yang
  sampai ke juri.

## Kriteria juri (urut penting)
1. Benar-benar alasan gamer ke bos untuk bolos di minggu peluncuran GTA 6, satu baris,
   maks 20 kata. Alasan yang meleset dari subjek kalah dari alasan apa pun yang sesuai.
2. Terdengar seperti yang hampir dipercaya manajer lelah: detail tempat kerja yang
   nyata, spesifik, membosankan — bukan cerita liar.
3. Lucu dengan caranya sendiri; tawa lahir dari logika/detail alasan itu, bukan lelucon
   yang ditempel di akhir.
4. Terbaca seperti SMS buru-buru: satu baris, kata-kata polos, tanpa setup, tanpa
   penjelasan panjang, tanpa tanda tangan.
5. Sudut yang dilewatkan alasan-alasan jelas (bukan nenek meninggal, ban kempes,
   atau demam mendadak).

Strategi: JANGAN sebut GTA 6 di dalam teks — manajer tidak akan pernah percaya alasan
yang menyebut game. Konteks "minggu peluncuran GTA 6" sudah diketahui juri; yang menang
adalah alasan membosankan yang nyaris sempurna sehingga manajer hampir percaya.
Detail spesifik + angka (12 derajat, lantai 14, jam 9) = kredibilitas. Humor harus lahir
dari logika alasan itu sendiri.

## Kandidat (skor /15 = 5 kriteria × maks 3)

1. "Boiler died overnight, house is 12 degrees and I can't feel my fingers to type, engineer comes tomorrow." (18 kata, 104 kar)
   Skor 14 — PILIH. Detail spesifik membosankan (boiler mati, 12 derajat) + logika
   lucu dari dalam alasan (jari mati rasa = tidak bisa mengetik) + tanpa setup.
   Musim November = boiler mati sangat masuk akal.
2. "Lift's out and I'm on the 14th floor, knee's still bad from the stairs yesterday, taking today to rest it." (20 kata, 110 kar)
   Skor 12 — loop lucu (lutut sakit gara-gara tangga karena lift mati), tapi 20 kata
   pas di batas dan logikanya sedikit membingungkan (lift mati kemarin juga?).
3. "Plumber's coming between 8 and 12 to fix the leak under my sink, someone has to be in, I'll catch up tonight." (20 kata, 112 kar)
   Skor 11 — sangat bisa dipercaya, tapi generik; tidak ada detail yang membuatnya
   menonjol di antara ratusan alasan tukang ledeng.
4. "Dentist moved my root canal to this morning, they had a cancellation, mouth's still numb, I'll be online after lunch." (20 kata, 118 kar)
   Skor 12 — spesifik dan bisa dipercaya ("mouth's still numb" detail bagus), tapi
   "cancellation" terasa sedikit dibuat-buat dan nadanya agak rapi.
5. "Train line's down between here and the office, replacement bus takes two hours, I'll dial into standup from home." (19 kata, 111 kar)
   Skor 11 — membosankan dan bisa dipercaya, tapi ujung "dial into standup" malah
   melemahkan alasan bolos (ia tetap bisa kerja dari rumah).
6. "Landlord's sending the electrician at 9 to rewire the fuse box, power's off all morning, no laptop till noon." (19 kata, 110 kar)
   Skor 12 — detail spesifik (jam 9, fuse box, mati listrik) kuat; tapi "no laptop
   till noon" menyiratkan ia masuk siang — alasan setengah hati.
7. "Woke up to a burst pipe in the bathroom, water everywhere, waiting on the emergency plumber, today is a washout." (19 kata, 112 kar)
   Skor 10 — bisa dipercaya, tapi "today is a washout" adalah lelucon yang ditempel
   di akhir (melanggar kriteria 3).
8. "My kid's school just called, half his class is off sick and they need someone home, I'm on pickup duty today." (20 kata, 110 kar)
   Skor 10 — bisa dipercaya, tapi "anak sakit" adalah klise alasan bolos; juri
   sudah mendengarnya dua kali (melanggar kriteria 5).
9. "Migraine started at 4am, screen's a blur, taking today to sleep it off, will check messages this evening." (18 kata, 105 kar)
   Skor 9 — "migraine" dan "sudden fever" satu keluarga klise; tidak ada detail
   spesifik yang segar.
10. "The road outside my flat is closed for resurfacing, no cars in or out till Friday, I'll dial into standup." (19 kata, 108 kar)
    Skor 9 — detail spesifik (resurfacing, till Friday) bagus, tapi sama seperti #5,
    ujungnya menawarkan kerja remote sehingga alasan bolosnya runtuh.
11. "My prescription ran out and the pharmacy says the refill's stuck in their system, need to sort it this morning." (19 kata, 114 kar)
    Skor 11 — birokrasi apotek = detail membosankan yang sangat bisa dipercaya,
    tapi tidak ada tawa dari logikanya sendiri; datar.
12. "Building management turned the water off without notice, can't shower, can't flush, taking the morning to sort it." (19 kata, 113 kar)
    Skor 11 — "can't shower, can't flush" detail konkret yang memalukan dan lucu,
    tapi "taking the morning" hanya setengah hari — alasan tanggung.

## Keputusan
PILIH #1 — boiler. Alasan paling kuat menurut urutan kriteria juri:
- K1: satu baris, 18 kata, alasan bolos kerja — sesuai subjek.
- K2: boiler mati di November + rumah 12 derajat = detail nyata, spesifik,
  membosankan yang persis didengar manajer lelah setiap musim dingin.
- K3: tawa lahir dari logika alasan itu sendiri (jari mati rasa sehingga tidak bisa
  mengetik — alasan bolos yang membuktikan dirinya sendiri).
- K4: kalimat SMS buru-buru, kata-kata polos, tanpa setup/penjelasan/tanda tangan.
- K5: bukan klise nenek/ban/demam; sudut "cuaca dingin + tukang datang besok"
  jarang dipakai.

Kalimat final (persis, 104 karakter, 18 kata):
"Boiler died overnight, house is 12 degrees and I can't feel my fingers to type, engineer comes tomorrow."
