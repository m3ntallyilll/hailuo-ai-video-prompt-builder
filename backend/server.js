const express = require('express');
const bodyParser = require('body-parser');
const { Pool } = require('pg');
const fetch = require('node-fetch');
require('dotenv').config();

const app = express();
const port = process.env.PORT || 3000;

// PostgreSQL pool setup
const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
});

// Middleware
app.use(bodyParser.json());

// Endpoint for chat completions using Groq API
app.post('/api/chat/completions', async (req, res) => {
  try {
    const { model, messages, tools, tool_choice, max_completion_tokens } = req.body;

    const response = await fetch('https://api.groq.com/openai/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${process.env.GROQ_API_KEY}`,
      },
      body: JSON.stringify({
        model,
        messages,
        tools,
        tool_choice,
        max_completion_tokens,
      }),
    });

    const data = await response.json();
    res.json(data);
  } catch (error) {
    console.error('Error in chat completions:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Endpoint for audio transcription using Groq API
app.post('/api/audio/transcriptions', async (req, res) => {
  try {
    // Assuming audio file is sent as base64 or multipart form-data
    // For simplicity, this example expects JSON with audio data as base64 string
    const { model, file, prompt, response_format, temperature, language } = req.body;

    const response = await fetch('https://api.groq.com/v1/audio/transcriptions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${process.env.GROQ_API_KEY}`,
      },
      body: JSON.stringify({
        model,
        file,
        prompt,
        response_format,
        temperature,
        language,
      }),
    });

    const data = await response.json();
    res.json(data);
  } catch (error) {
    console.error('Error in audio transcription:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Example endpoint to test database connection
app.get('/api/users', async (req, res) => {
  try {
    const result = await pool.query('SELECT * FROM users LIMIT 10');
    res.json(result.rows);
  } catch (error) {
    console.error('Error querying users:', error);
    res.status(500).json({ error: 'Database query error' });
  }
});

app.listen(port, () => {
  console.log(`Backend server running on port ${port}`);
});
