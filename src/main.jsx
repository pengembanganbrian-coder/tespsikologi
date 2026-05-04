import React, { useMemo, useState } from 'react';
import { createRoot } from 'react-dom/client';
import { CheckCircle2, ClipboardList, Download, Printer, Send, ShieldAlert } from 'lucide-react';
import './styles.css';
import { GOOGLE_SCRIPT_URL, ITEMS_PER_PAGE } from './config';
import {
  choices,
  conversionTable,
  identityFields,
  items,
  scales,
  scoringRules,
  testInfo
} from './data/testConfig';

function App() {
  const [step, setStep] = useState('identity');
  const [identity, setIdentity] = useState({});
  const [answers, setAnswers] = useState({});
  const [page, setPage] = useState(0);
  const [submissionStatus, setSubmissionStatus] = useState('');

  const totalPages = Math.ceil(items.length / ITEMS_PER_PAGE);
  const visibleItems = items.slice(page * ITEMS_PER_PAGE, (page + 1) * ITEMS_PER_PAGE);
  const answeredCount = Object.keys(answers).length;
  const progress = Math.round((answeredCount / items.length) * 100);

  const result = useMemo(() => scoreTest(answers), [answers]);

  const identityComplete = identityFields
    .filter(field => field.required)
    .every(field => String(identity[field.key] || '').trim() !== '');

  const currentPageComplete = visibleItems.every(item => answers[item.id]);
  const allAnswersComplete = items.every(item => answers[item.id]);

  function updateIdentity(key, value) {
    setIdentity(prev => ({ ...prev, [key]: value }));
  }

  function updateAnswer(itemId, value) {
    setAnswers(prev => ({ ...prev, [itemId]: value }));
  }

  function nextPage() {
    if (page < totalPages - 1) {
      setPage(page + 1);
      window.scrollTo({ top: 0, behavior: 'smooth' });
    } else {
      setStep('result');
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  }

  function prevPage() {
    if (page > 0) {
      setPage(page - 1);
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  }

  async function submitToGoogleSheet() {
    if (!GOOGLE_SCRIPT_URL) {
      setSubmissionStatus('URL Google Apps Script belum diisi di src/config.js.');
      return;
    }

    setSubmissionStatus('Mengirim hasil...');

    const payload = {
      submittedAt: new Date().toISOString(),
      identity,
      answers,
      result
    };

    try {
      await fetch(GOOGLE_SCRIPT_URL, {
        method: 'POST',
        mode: 'no-cors',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });

      setSubmissionStatus('Hasil sudah dikirim. Cek Google Sheet tujuan.');
    } catch (error) {
      setSubmissionStatus(`Gagal mengirim hasil: ${error.message}`);
    }
  }

  function downloadJson() {
    const payload = {
      submittedAt: new Date().toISOString(),
      identity,
      answers,
      result
    };

    const blob = new Blob([JSON.stringify(payload, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `hasil-tes-${identity.nama || 'peserta'}.json`;
    link.click();
    URL.revokeObjectURL(url);
  }

  return (
    <main className="app-shell">
      <section className="hero-card">
        <div>
          <div className="eyebrow"><ClipboardList size={18} /> Aplikasi Tes Psikologi</div>
          <h1>{testInfo.title}</h1>
          <p>{testInfo.subtitle}</p>
        </div>
        <div className="hero-badge">{items.length} item</div>
      </section>

      {step === 'identity' && (
        <section className="card">
          <h2>Data Peserta</h2>
          <p className="muted">Isi data peserta sebelum mulai mengerjakan tes.</p>

          <div className="form-grid">
            {identityFields.map(field => (
              <label key={field.key} className="field">
                <span>{field.label}{field.required ? ' *' : ''}</span>
                <input
                  value={identity[field.key] || ''}
                  onChange={event => updateIdentity(field.key, event.target.value)}
                  placeholder={`Masukkan ${field.label.toLowerCase()}`}
                />
              </label>
            ))}
          </div>

          <div className="notice">
            <ShieldAlert size={18} />
            <span>{testInfo.disclaimer}</span>
          </div>

          <div className="actions right">
            <button className="primary" disabled={!identityComplete} onClick={() => setStep('test')}>
              Mulai Tes
            </button>
          </div>
        </section>
      )}

      {step === 'test' && (
        <section className="card">
          <div className="test-header">
            <div>
              <h2>Instruksi</h2>
              <p className="muted">{testInfo.instruction}</p>
            </div>
            <div className="page-chip">Halaman {page + 1} / {totalPages}</div>
          </div>

          <div className="progress-wrap">
            <div className="progress-text">
              <span>{answeredCount} dari {items.length} item terisi</span>
              <strong>{progress}%</strong>
            </div>
            <div className="progress-bar">
              <div style={{ width: `${progress}%` }} />
            </div>
          </div>

          <div className="items-list">
            {visibleItems.map(item => (
              <div key={item.id} className="item-card">
                <div className="item-number">{item.id}</div>
                <div className="item-content">
                  <p>{item.text}</p>
                  <div className="choice-row">
                    {choices.map(choice => (
                      <label
                        key={choice.value}
                        className={`choice ${answers[item.id] === choice.value ? 'selected' : ''}`}
                      >
                        <input
                          type="radio"
                          name={`item-${item.id}`}
                          value={choice.value}
                          checked={answers[item.id] === choice.value}
                          onChange={() => updateAnswer(item.id, choice.value)}
                        />
                        {choice.label}
                      </label>
                    ))}
                  </div>
                </div>
              </div>
            ))}
          </div>

          <div className="actions spread">
            <button className="secondary" disabled={page === 0} onClick={prevPage}>Sebelumnya</button>
            <button className="primary" disabled={!currentPageComplete} onClick={nextPage}>
              {page === totalPages - 1 ? 'Lihat Hasil' : 'Selanjutnya'}
            </button>
          </div>
        </section>
      )}

      {step === 'result' && (
        <section className="card result-card">
          <div className="result-heading">
            <div>
              <div className="eyebrow success"><CheckCircle2 size={18} /> Tes selesai</div>
              <h2>Hasil Skoring</h2>
              <p className="muted">Raw score dan skor konversi dihitung berdasarkan konfigurasi pada file testConfig.js.</p>
            </div>
            <div className="actions compact">
              <button className="secondary" onClick={() => window.print()}><Printer size={16} /> Cetak</button>
              <button className="secondary" onClick={downloadJson}><Download size={16} /> JSON</button>
              <button className="primary" onClick={submitToGoogleSheet}><Send size={16} /> Kirim</button>
            </div>
          </div>

          <div className="summary-grid">
            {identityFields.map(field => (
              <div key={field.key} className="summary-box">
                <span>{field.label}</span>
                <strong>{identity[field.key] || '-'}</strong>
              </div>
            ))}
          </div>

          <div className="table-wrap">
            <table>
              <thead>
                <tr>
                  <th>Skala</th>
                  <th>Nama Skala</th>
                  <th>Raw Score</th>
                  <th>Skor Konversi</th>
                  <th>Keterangan Umum</th>
                </tr>
              </thead>
              <tbody>
                {scales.map(scale => {
                  const raw = result.rawScores[scale.key] || 0;
                  const converted = result.convertedScores[scale.key];
                  return (
                    <tr key={scale.key}>
                      <td>{scale.key}</td>
                      <td>{scale.name}</td>
                      <td>{raw}</td>
                      <td>{converted ?? '-'}</td>
                      <td>{describeScore(converted)}</td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>

          <div className="notice warning">
            <ShieldAlert size={18} />
            <span>Hasil ini tidak boleh digunakan sebagai diagnosis otomatis. Gunakan sebagai bahan awal dan lakukan interpretasi oleh pihak yang kompeten.</span>
          </div>

          {submissionStatus && <p className="status-text">{submissionStatus}</p>}

          <div className="actions spread">
            <button className="secondary" onClick={() => setStep('test')}>Kembali ke Tes</button>
            <button className="primary" disabled={!allAnswersComplete} onClick={submitToGoogleSheet}>Kirim ke Google Sheet</button>
          </div>
        </section>
      )}
    </main>
  );
}

function scoreTest(answers) {
  const rawScores = {};
  const convertedScores = {};

  scales.forEach(scale => {
    rawScores[scale.key] = 0;
  });

  scoringRules.forEach(rule => {
    const answer = answers[rule.item];
    if (answer === rule.answer) {
      rawScores[rule.scale] = (rawScores[rule.scale] || 0) + Number(rule.weight || 1);
    }
  });

  scales.forEach(scale => {
    convertedScores[scale.key] = convertScore(scale.key, rawScores[scale.key]);
  });

  return { rawScores, convertedScores };
}

function convertScore(scale, rawScore) {
  const row = conversionTable.find(item =>
    item.scale === scale && rawScore >= item.rawMin && rawScore <= item.rawMax
  );
  return row ? row.score : null;
}

function describeScore(score) {
  if (score === null || score === undefined) return 'Belum ada tabel konversi';
  if (score >= 85) return 'Sangat tinggi / perlu telaah profesional';
  if (score >= 75) return 'Tinggi / perlu perhatian';
  if (score >= 60) return 'Sedang';
  if (score > 0) return 'Rendah';
  return 'Tidak menonjol';
}

createRoot(document.getElementById('root')).render(<App />);
