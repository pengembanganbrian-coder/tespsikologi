// TEMPLATE TES PSIKOLOGI BERBASIS KONFIGURASI
// ----------------------------------------------------
// File ini sengaja tidak berisi item atau kunci resmi tes berlisensi/proprietary.
// Jika Anda memiliki izin/lisensi penggunaan alat tes tertentu, masukkan item,
// kunci skoring, bobot, dan tabel konversinya di bagian ini.

export const testInfo = {
  title: 'Tes Psikologi',
  subtitle: 'Skoring otomatis berbasis Sesuai / Tidak Sesuai',
  instruction: `Baca setiap pernyataan dengan saksama, lalu pilih jawaban yang paling menggambarkan kondisi Anda. Tidak ada jawaban benar atau salah. Jawablah secara jujur dan sesuai keadaan diri.`,
  disclaimer: `Hasil tes ini bersifat administratif/screening dan tidak dapat digunakan sebagai diagnosis. Interpretasi profesional tetap perlu dilakukan oleh psikolog/tenaga berwenang.`
};

export const identityFields = [
  { key: 'nama', label: 'Nama', required: true },
  { key: 'nip', label: 'NIP', required: true },
  { key: 'unit', label: 'Unit Kerja', required: true },
  { key: 'jabatan', label: 'Jabatan', required: false }
];

export const choices = [
  { value: 'true', label: 'Sesuai' },
  { value: 'false', label: 'Tidak Sesuai' }
];

// Ganti teks item di bawah dengan item yang Anda miliki hak pakainya.
// Jumlah dibuat 175 sebagai placeholder karena banyak alat klinis memakai ratusan item.
export const items = Array.from({ length: 175 }, (_, index) => ({
  id: index + 1,
  text: `Pernyataan ${index + 1} — ganti dengan item resmi/berlisensi Anda.`
}));

// Contoh skala. Silakan ganti sesuai kebutuhan.
export const scales = [
  { key: 'A', name: 'Skala A' },
  { key: 'B', name: 'Skala B' },
  { key: 'C', name: 'Skala C' },
  { key: 'V', name: 'Validitas' }
];

// Aturan skoring:
// item = nomor item
// scale = kode skala
// answer = jawaban yang diberi skor: 'true' untuk Sesuai, 'false' untuk Tidak Sesuai
// weight = bobot skor
//
// Catatan: satu item boleh masuk ke beberapa skala. Tambahkan baris baru saja.
export const scoringRules = [
  { item: 1, scale: 'A', answer: 'true', weight: 2 },
  { item: 2, scale: 'A', answer: 'false', weight: 1 },
  { item: 3, scale: 'B', answer: 'true', weight: 2 },
  { item: 4, scale: 'B', answer: 'false', weight: 1 },
  { item: 5, scale: 'C', answer: 'true', weight: 2 },
  { item: 6, scale: 'V', answer: 'true', weight: 1 }
];

// Tabel konversi Base Rate / skor standar.
// Kosongkan jika hanya ingin raw score.
// Contoh format:
// { scale: 'A', rawMin: 0, rawMax: 0, score: 0 }
// { scale: 'A', rawMin: 1, rawMax: 2, score: 35 }
export const conversionTable = [
  { scale: 'A', rawMin: 0, rawMax: 0, score: 0 },
  { scale: 'A', rawMin: 1, rawMax: 1, score: 35 },
  { scale: 'A', rawMin: 2, rawMax: 3, score: 60 },
  { scale: 'B', rawMin: 0, rawMax: 0, score: 0 },
  { scale: 'B', rawMin: 1, rawMax: 1, score: 35 },
  { scale: 'B', rawMin: 2, rawMax: 3, score: 60 },
  { scale: 'C', rawMin: 0, rawMax: 0, score: 0 },
  { scale: 'C', rawMin: 1, rawMax: 2, score: 50 },
  { scale: 'V', rawMin: 0, rawMax: 0, score: 0 },
  { scale: 'V', rawMin: 1, rawMax: 99, score: 1 }
];
