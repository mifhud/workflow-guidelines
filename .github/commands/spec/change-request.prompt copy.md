# Analisis Change Request dan Buat Rencana Perubahan Code

Saya melampirkan dokumen requirements/change request. Tolong analisis dokumen tersebut dan buatkan rencana detail perubahan code yang diperlukan.

## Output yang Diharapkan:

### 1. Ringkasan Change Request
- Tujuan perubahan
- Scope perubahan
- Impact area

### 2. Analisis Dampak
- File-file yang akan terpengaruh
- Dependencies yang perlu dipertimbangkan
- Potential breaking changes
- Risk assessment

### 3. Rencana Implementasi
Untuk setiap perubahan, jelaskan dengan format berikut:     

**File: `{relative-path-file}`**

**Perubahan yang diperlukan:**
[Penjelasan singkat tentang apa yang akan diubah]

**Before:**
```{relative-path-file}:{start-line}-{end-line}
[tampilkan code yang akan diubah]
```

**After:**
```{relative-path-file}:{start-line}-{end-line}
[tampilkan code hasil perubahan]
```

**Reasoning:**
[Jelaskan alasan perubahan ini]

### 4. Deployment Considerations
- Database migrations (jika ada)
- Configuration changes (jika ada)
---

**Catatan:** Pastikan setiap perubahan code mencantumkan:
- Path file yang relatif terhadap root project
- Line numbers yang spesifik
- Context yang cukup untuk memahami perubahan