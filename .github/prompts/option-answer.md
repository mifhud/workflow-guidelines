Saya sudah memiliki daftar pertanyaan klarifikasi yang dihasilkan dari analisis dokumen [TRD Baru / Change Request].

Tujuan saya adalah:
- Menyediakan OPSI JAWABAN yang masuk akal dan terstruktur
- Membantu stakeholder (leader / PM / BA) memilih atau memvalidasi jawaban
- Mengurangi back-and-forth saat klarifikasi requirement

Ref Doc:
[PASTE DOKUMEN TRD / CHANGE REQUEST DI SINI]

Daftar Pertanyaan Klarifikasi:
[PASTE HASIL PERTANYAAN KLARIFIKASI DI SINI]

---

Tugas Anda:
1. Analisis kembali **Ref Doc** dan **Codebase** untuk memahami konteks bisnis dan teknis
2. Untuk SETIAP pertanyaan klarifikasi, buatkan **beberapa opsi jawaban yang realistis**
3. Opsi jawaban harus:
   - Konsisten dengan Ref Doc dan codebase
   - Bisa langsung dipakai sebagai keputusan requirement
   - Mencerminkan kemungkinan umum dalam development (best practice)

---

### Format Output

Gunakan format berikut untuk SETIAP pertanyaan:

```
## [Kategori]

- **Context:**: (ambil dari pertanyaan klarifikasi)
- **Question:** (pertanyaan klarifikasi)
- **Priority:** (ambil dari pertanyaan klarifikasi)
- **Answer Options:**

  - **Option A:** Penjelasan jawaban + implikasi singkat ke sistem

  - **Option B:** Penjelasan jawaban + implikasi singkat ke sistem

  - **Option C (jika relevan):** Penjelasan jawaban + implikasi singkat ke sistem

- **Recommended Option:** Option X
  (sertakan alasan singkat berdasarkan Ref Doc, risiko, dan dampak ke development)

- **Impact if Not Clarified:**
  (jelaskan risiko teknis / bisnis jika jawaban tidak diputuskan)
```

---

### Aturan Penting
- Fokus utama pada **FUNCTIONAL REQUIREMENTS**
- Prioritaskan pertanyaan dengan **Priority: HIGH**
- Boleh membuat asumsi lain di luar Ref Doc, asalkan:
  - Berkaitan dengan ref doc atau codebase
  - Konsisten dengan konteks bisnis/teknis
  - Masuk akal secara umum
  - Dijelaskan di bagian alasan rekomendasi
- Jika informasi di Ref Doc tidak cukup:
  - Tetap berikan opsi jawaban
  - Tandai dengan catatan: *"Perlu konfirmasi stakeholder"*

---

### Output Location
Simpan di:
{relative-path}-answer-options.md

Gunakan bahasa Indonesia yang profesional, jelas, dan siap digunakan dalam diskusi requirement.
