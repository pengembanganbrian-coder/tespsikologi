# Tes Psikologi - Template Deploy GitHub ke Vercel

Template ini dibuat untuk membuat aplikasi tes psikologi berbasis pilihan **Sesuai / Tidak Sesuai**, dengan fitur:

- input identitas peserta;
- pengerjaan tes per halaman;
- skoring otomatis berdasarkan konfigurasi;
- raw score per skala;
- konversi skor/BR jika tabel konversi diisi;
- cetak hasil;
- download hasil JSON;
- opsional kirim hasil ke Google Sheets lewat Google Apps Script.

> Penting: template ini tidak menyertakan item/kunci resmi alat tes berlisensi. Masukkan hanya item, kunci skoring, dan tabel konversi yang memang Anda punya hak/izin pakainya.

---

## 1. Cara edit item dan skoring

Buka file:

```text
src/data/testConfig.js
```

Bagian utama yang perlu diedit:

### A. Identitas tes

```js
export const testInfo = {
  title: 'Tes Psikologi',
  subtitle: 'Skoring otomatis berbasis Sesuai / Tidak Sesuai',
  instruction: '...',
  disclaimer: '...'
};
```

### B. Item tes

```js
export const items = [
  { id: 1, text: 'Isi pernyataan 1 di sini.' },
  { id: 2, text: 'Isi pernyataan 2 di sini.' }
];
```

Kalau tetap ingin 175 item, lanjutkan sampai id 175.

### C. Skala

```js
export const scales = [
  { key: 'A', name: 'Skala A' },
  { key: 'B', name: 'Skala B' }
];
```

### D. Kunci skoring

```js
export const scoringRules = [
  { item: 1, scale: 'A', answer: 'true', weight: 2 },
  { item: 2, scale: 'A', answer: 'false', weight: 1 }
];
```

Keterangan:

- `item`: nomor item;
- `scale`: kode skala;
- `answer`: jawaban yang diberi skor;
  - `true` = Sesuai;
  - `false` = Tidak Sesuai;
- `weight`: bobot skor.

Satu item boleh masuk ke beberapa skala. Tambahkan baris baru saja.

### E. Tabel konversi skor

```js
export const conversionTable = [
  { scale: 'A', rawMin: 0, rawMax: 0, score: 0 },
  { scale: 'A', rawMin: 1, rawMax: 2, score: 35 }
];
```

Kalau raw score 10 sampai 12 menghasilkan BR 75, isi seperti ini:

```js
{ scale: 'A', rawMin: 10, rawMax: 12, score: 75 }
```

---

## 2. Cara jalankan di komputer sendiri

Install Node.js lebih dulu.

Lalu jalankan:

```bash
npm install
npm run dev
```

Buka URL yang muncul, biasanya:

```text
http://localhost:5173
```

---

## 3. Cara upload ke GitHub

1. Buat repository baru di GitHub.
2. Upload semua file dalam folder ini.
3. Pastikan struktur file tetap seperti ini:

```text
index.html
package.json
vercel.json
src/
  config.js
  main.jsx
  styles.css
  data/
    testConfig.js
```

---

## 4. Cara deploy ke Vercel

1. Masuk ke https://vercel.com
2. Klik **Add New Project**.
3. Pilih repository GitHub yang tadi dibuat.
4. Framework akan otomatis terbaca sebagai **Vite**.
5. Klik **Deploy**.
6. Setelah selesai, aplikasi akan punya link publik dari Vercel.

---

## 5. Opsional: kirim hasil ke Google Sheets

Buat Google Sheet, lalu buka **Extensions → Apps Script**.

Tempel kode ini:

```javascript
function doPost(e) {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = ss.getSheetByName('HASIL_WEB');

  if (!sheet) {
    sheet = ss.insertSheet('HASIL_WEB');
    sheet.appendRow([
      'Timestamp',
      'Nama',
      'NIP',
      'Unit',
      'Jabatan',
      'Raw Scores',
      'Converted Scores',
      'Answers JSON'
    ]);
  }

  const data = JSON.parse(e.postData.contents);

  sheet.appendRow([
    new Date(),
    data.identity.nama || '',
    data.identity.nip || '',
    data.identity.unit || '',
    data.identity.jabatan || '',
    JSON.stringify(data.result.rawScores),
    JSON.stringify(data.result.convertedScores),
    JSON.stringify(data.answers)
  ]);

  return ContentService
    .createTextOutput(JSON.stringify({ status: 'success' }))
    .setMimeType(ContentService.MimeType.JSON);
}
```

Deploy Apps Script:

1. Klik **Deploy → New deployment**.
2. Pilih **Web app**.
3. Execute as: **Me**.
4. Who has access: **Anyone**.
5. Copy URL Web App.
6. Masukkan URL itu ke file:

```text
src/config.js
```

Contoh:

```js
export const GOOGLE_SCRIPT_URL = 'https://script.google.com/macros/s/xxxxx/exec';
```

Setelah itu commit/push lagi ke GitHub. Vercel akan otomatis redeploy.
