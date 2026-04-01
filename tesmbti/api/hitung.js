export default async function handler(req, res) {
  try {
    const response = await fetch("https://script.google.com/macros/s/AKfycbzN2Li6L_ZQ_KDibPclXE-_p-Mzm2DziE8Q0HJ6M8OiVodVcs4gCcS3U5Su__eNpIdiAg/exec", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(req.body),
    });

    const result = await response.json();
    res.status(200).json(result);
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
}
