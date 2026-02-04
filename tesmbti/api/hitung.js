const mbtiData = {
  "ISTJ": {
    "nama": "ISTJ (Bertanggungjawab)",
    "karakteristik_umum": "Orang yang tenang yang mencari stabilitas dan kedamaian. Bekerja sendiri dan bisa diandalkan, namun nyaman dalam tim jika peran jelas. Sangat menghormati fakta, realistis, dan sistematis.",
    "kekuatan": "Memiliki rasa tanggung jawab tinggi, loyal, tekun, dan memegang teguh prosedur.",
    "gaya_komunikasi": "Menggunakan logika untuk mengenali kelemahan, ingin tahu 'mengapa', dan menyukai informasi obyektif serta padat.",
    "pemimpin_pengikut": "Sebagai pemimpin, menjunjung tinggi standar dan kompetensi. Sebagai pengikut, sangat loyal jika pemimpinnya kompeten.",
    "perilaku_stres": "Menjadi kaku, kritis, dan sulit mendelegasikan. Saat depresi bisa terjebak 'Catastrophizing' atau membayangkan hal negatif.",
    "saran": "Belajarlah memahami perasaan orang lain, kurangi keinginan mengontrol, dan lebih terbuka terhadap perubahan perspektif."
  },
  "ISFJ": {
    "nama": "ISFJ (Setia)",
    "karakteristik_umum": "Penuh pertimbangan, hati-hati, teliti, dan akurat. Ramah, perhatian pada perasaan orang lain, dan pendengar yang baik.",
    "kekuatan": "Sangat bertanggung jawab, kooperatif, dan memiliki kemampuan mengorganisasi yang detail.",
    "gaya_komunikasi": "Menghindari konflik, lebih suka mendukung secara personal, dan sangat menjaga keharmonisan hubungan.",
    "perilaku_stres": "Cenderung menyalahkan diri sendiri dan merasa terbebani oleh kebutuhan semua orang di sekitarnya.",
    "saran": "Belajarlah mengatakan 'tidak' agar tidak dianggap plin-plan, dan jangan takut mencoba hal baru di luar zona nyaman."
  },
  "INFJ": {
    "nama": "INFJ (Reflektif)",
    "karakteristik_umum": "Idealis, perfeksionis, visioner, dan penuh ide kreatif. Biasanya diikuti karena kejelasan visi dan dedikasi pada hal baik.",
    "kekuatan": "Empati tinggi, sensitif, original, dan memiliki keinginan kuat memberikan yang terbaik dalam pekerjaan.",
    "gaya_komunikasi": "Menginspirasi, suka merenung, dan menunjukkan perhatian mendalam melalui tindakan dan visi.",
    "saran": "Seimbangkan cara pandang, jangan hanya melihat risiko negatif. Belajarlah untuk rileks dan jangan menyalahkan diri sendiri."
  },
  "INTJ": {
    "nama": "INTJ (Independen)",
    "karakteristik_umum": "Mandiri, percaya diri, dan memiliki dorongan kuat untuk mencapai ide-ide original. Mampu menyederhanakan hal rumit menjadi praktis.",
    "kekuatan": "Analisa yang tajam, visioner, dan tidak terganggu oleh kritik atau konflik dalam mencapai tujuan.",
    "saran": "Belajarlah mengungkapkan emosi, lebih terbuka pada dunia luar (bergaul), dan hindari perdebatan yang tidak penting."
  },
  "ISTP": {
    "nama": "ISTP (Pragmatis)",
    "karakteristik_umum": "Tenang, pendiam, namun sangat percaya diri dan tegas. Mampu menghadapi perubahan mendadak dengan tenang.",
    "kekuatan": "Problem solver teknis yang handal, logis, rasional, dan mampu mendelegasikan tugas secara efektif.",
    "saran": "Belajarlah mengenali dan mengekspresikan perasaan. Jangan menyimpan informasi yang seharusnya dibagi kepada tim."
  },
  "ISFP": {
    "nama": "ISFP (Artistik)",
    "karakteristik_umum": "Rendah hati, fleksibel, sensitif, dan menghindari konflik. Lebih banyak bertindak daripada bicara.",
    "kekuatan": "Sangat menikmati momen saat ini, ramah, dan menjadi pelaksana yang setia terhadap nilai-nilai yang mereka yakini.",
    "saran": "Jangan takut pada penolakan atau konflik. Pikirkan dampak jangka panjang dari keputusan kecil hari ini."
  },
  "INFP": {
    "nama": "INFP (Idealis)",
    "karakteristik_umum": "Sangat peka dengan perasaan orang lain, penuh antusiasme, dan setia kepada orang yang dekat dengannya.",
    "kekuatan": "Optimis dalam melihat potensi orang lain, berpikir win-win solution, dan sangat idealis.",
    "saran": "Belajarlah menghadapi kritik tanpa menyalahkan diri sendiri. Bertindak benar lebih penting daripada sekadar bertindak baik."
  },
  "INTP": {
    "nama": "INTP (Konseptual)",
    "karakteristik_umum": "Menghargai intelektualitas, kritis, skeptis, dan menikmati hal-hal teoritis serta ilmiah.",
    "kekuatan": "Mampu memecahkan masalah dengan logika dan analisa mendalam. Sangat serius jika menemukan minat yang menarik.",
    "saran": "Belajarlah membangun hubungan sosial dan mendengar aktif. Jangan hanya berganti ide tanpa ada yang terwujud."
  },
  "ESTP": {
    "nama": "ESTP (Spontan)",
    "karakteristik_umum": "Enerjik, cekatan, dan ceplas-ceplos. Memiliki interpersonal skill yang baik dan berkarisma.",
    "kekuatan": "Pemecah masalah langsung di tempat, asertif, dan mampu menghadapi konflik tanpa rasa khawatir.",
    "saran": "Luangkan waktu untuk merenung dan merencanakan masa depan. Belajarlah memahami pemikiran orang lain sebelum bicara."
  },
  "ESFP": {
    "nama": "ESFP (Murah Hati)",
    "karakteristik_umum": "Easygoing, ceria, dan suka menjadi pusat perhatian. Menghindari konflik demi menjaga keharmonisan.",
    "kekuatan": "Sangat baik dalam ketrampilan praktis, murah hati, dan mudah mengenali perasaan orang sekelilingnya.",
    "saran": "Jangan terburu-buru mengambil keputusan. Belajarlah menghadapi kritik daripada lari dari masalah."
  },
  "ENFP": {
    "nama": "ENFP (Optimis)",
    "karakteristik_umum": "Bersemangat, inovatif, dan sangat menghargai orang lain. Secara dominan menggunakan Intuition eksternal dan Feeling internal.",
    "kekuatan": "Pandai berkomunikasi, membawa suasana positif, dan mampu beradaptasi dengan perubahan beragam.",
    "saran": "Belajarlah untuk fokus, disiplin, dan tegas. Jangan melupakan kebutuhan diri sendiri karena terlalu peduli pada orang lain."
  },
  "ENTP": {
    "nama": "ENTP (Inovatif – Kreatif)",
    "karakteristik_umum": "Gesit, cerdik, dan punya kemampuan debat yang baik tanpa merasa bersalah. Selalu ingin mengembangkan diri.",
    "kekuatan": "Fleksibel dan punya banyak cara memecahkan tantangan. Sangat logis dalam menganalisa masalah.",
    "saran": "Hindari perdebatan tidak penting. Belajarlah untuk waspada dan tidak terlalu optimis mengambil risiko yang tidak realistis."
  },
  "ESTJ": {
    "nama": "ESTJ (Konservatif – Disiplin)",
    "karakteristik_umum": "Praktis, sistematis, dan pekerja keras. Sangat patuh pada prosedur dan instruksi yang terencana.",
    "kekuatan": "Administrator yang baik, on time, dan sangat disiplin dalam menjaga standar organisasi.",
    "saran": "Kurangi keinginan memaksa orang lain. Belajarlah sabar dan luangkan waktu untuk introspeksi diri serta mengontrol amarah."
  },
  "ESFJ": {
    "nama": "ESFJ (Harmonis)",
    "karakteristik_umum": "Populer, suportif, dan dilahirkan untuk bekerja sama. Menciptakan harmoni dalam kelompok adalah prioritasnya.",
    "kekuatan": "Teliti, rajin merawat apa yang dimiliki, dan selalu melakukan hal manis untuk orang lain.",
    "saran": "Jangan mengukur harga diri hanya dari pujian orang. Belajarlah menghadapi konflik secara dewasa dan tegas."
  },
  "ENFJ": {
    "nama": "ENFJ (Meyakinkan)",
    "karakteristik_umum": "Responsif terhadap pujian dan kritik. Pandai bergaul, simpatik, dan meyakinkan orang lain dengan mudah.",
    "kekuatan": "Loyal, kreatif, dan sangat peduli pada keinginan atau perasaan orang di sekitarnya.",
    "saran": "Jangan mengorbankan diri hanya untuk menyenangkan orang lain. Belajarlah untuk tidak mudah kecewa jika orang tidak sesuai harapan."
  },
  "ENTJ": {
    "nama": "ENTJ (Pemimpin Alami)",
    "karakteristik_umum": "Tangguh, disiplin, dan sangat menghargai komitmen. Cenderung menutupi kelemahan dan perasaan.",
    "kekuatan": "Berkarisma, obyektif, jujur terus terang, dan berbakat menjadi pemimpin yang mampu menggerakkan orang.",
    "saran": "Belajarlah untuk rileks dan tidak selalu kompetitif. Menyatakan perasaan bukanlah sebuah kelemahan."
  }
};

export default function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).send('Method Not Allowed');

  const { jawaban, peserta } = req.body;
  
  // Mapping rumus persis tabel skoring
  const mapping = {
    "60B":"I","60A":"E","52B":"I","52A":"E","45A":"I","45B":"E","38A":"I","38B":"E","35B":"I","35A":"E","31A":"I","31B":"E","29A":"I","29B":"E","28B":"I","28A":"E","20A":"I","20B":"E","15A":"I","15B":"E","11A":"I","11B":"E","10A":"I","10B":"E","7B":"I","7A":"E","5B":"I","5A":"E","2A":"I","2B":"E",
    "53A":"S","53B":"N","51A":"S","51B":"N","46A":"S","46B":"N","43A":"S","43B":"N","41A":"S","41B":"N","36A":"S","36B":"N","34A":"S","34B":"N","27A":"S","27B":"N","25A":"S","25B":"N","22B":"S","22A":"N","18B":"S","18A":"N","16A":"S","16B":"N","13A":"S","13B":"N","8A":"S","8B":"N","6B":"S","6A":"N",
    "58A":"T","58B":"F","57A":"T","57B":"F","55A":"T","55B":"F","49B":"T","49A":"F","48A":"T","48B":"F","42A":"T","42B":"F","39B":"T","39A":"F","37A":"T","37B":"F","23A":"T","32A":"F","32B":"T","30B":"F","30A":"T","23B":"F","17A":"T","17B":"F","9B":"T","14B":"F","4A":"T","9A":"F","14A":"T","4B":"F",
    "59B":"J","59A":"P","56A":"J","56B":"P","54A":"J","54B":"P","50B":"J","50A":"P","47A":"J","47B":"P","44B":"J","44A":"P","40B":"J","40A":"P","33B":"J","33A":"P","26B":"J","26A":"P","24A":"J","24B":"P","21B":"J","21A":"P","19A":"J","19B":"P","12B":"J","12A":"P","3A":"J","3B":"P","1B":"J","1A":"P"
  };

  let skor = { I: 0, E: 0, S: 0, N: 0, T: 0, F: 0, J: 0, P: 0 };
  jawaban.forEach(code => {
    if (mapping[code]) skor[mapping[code]]++;
  });

  const tipe = (skor.I >= skor.E ? 'I' : 'E') + 
               (skor.S >= skor.N ? 'S' : 'N') + 
               (skor.T >= skor.F ? 'T' : 'F') + 
               (skor.J >= skor.P ? 'J' : 'P');

  res.status(200).json({
    tipe: tipe,
    detail: mbtiData[tipe],
    peserta: peserta
  });
}
