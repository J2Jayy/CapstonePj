const openai = require('openai');
require('dotenv').config();

module.exports = async (req, res) => {
  const { surveyData } = req.body;

  openai.apiKey = process.env.OPENAI_API_KEY;

  const response = await openai.Completion.create({
    engine: 'davinci',
    prompt: `Create a fake profile based on the following survey data: ${JSON.stringify(surveyData)}`,
    max_tokens: 100,
  });

  res.status(200).json({ profile: response.choices[0].text.trim() });
};
