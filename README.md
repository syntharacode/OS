<p align="center">
  <img src="./img/logo.png">
</p>

# Synthara OS

Synthara OS is a modular LLM Operating System focused on autonomous learning in the crypto and technology space. It includes training pipelines, inference API, a full web frontend, CLI tools, a database layer, analytics, and agent support.

## Table of Contents

- Features
- Tech Stack
- Directory Structure
- Installation
- Usage
- API
- Environment Configuration
- Testing
- License

## Features

- Continual learning with user feedback and auto-training
- Prompt optimization and semantic similarity
- Full backend with FastAPI, PostgreSQL and SQLAlchemy
- Web frontend with React, Tailwind and Vite
- Live logs, metrics and vectorization
- Integrated CLI tooling
- Agent architecture for feedback, optimization and auto training

## Tech Stack

Backend: FastAPI, SQLAlchemy, PostgreSQL, Transformers, SentenceTransformers  
Frontend: React, Vite, Tailwind CSS  
Infrastructure: Uvicorn, Gunicorn, dotenv, Bash scripts

## Directory Structure

```
synthara/
├── backend/
│   ├── api/            # FastAPI routes and middleware
│   ├── core/           # Config, engine, lifecycle, registry
│   ├── models/         # LLM loading, training, inference, adapter
│   ├── data/           # Dataset, tokenizer, parser, vectorizer
│   ├── agents/         # AutoTrainer, Optimizer, Feedback loop
│   ├── services/       # Training, user, memory, analytics
│   ├── db/             # Schema, models, queries, connection
│   ├── utils/          # Benchmarks, crypto, eval metrics
│   ├── tests/          # All test cases
│   ├── gunicorn.conf.py
│   └── requirements.txt
│
├── web/
│   ├── public/         # index.html
│   ├── src/            # API clients, components, hooks, pages
│   ├── tailwind.config.js
│   ├── vite.config.js
│   └── package.json
│
├── database/
│   ├── migrations/     # SQL migration files
│   ├── seed/           # Seed data for users, prompts
│   └── db_init.py
│
├── scripts/            # Shell + Python utility scripts
├── .env.example
├── README.md
├── LICENSE
├── setup.py
└── requirements.txt
```

## Installation

```bash
# Backend
cd backend
pip install -r requirements.txt

# Frontend
cd ../web
npm install
```

## Usage

Start the backend server:
```bash
bash scripts/run_server.sh
```

Start the frontend:
```bash
cd web
npm run dev
```

Initialize database:
```bash
python database/db_init.py
```

## API

| Method | Endpoint         | Description                |
|--------|------------------|----------------------------|
| POST   | /api/llm/query   | Query the model            |
| POST   | /api/llm/train   | Train with user input      |
| POST   | /api/user/create | Register new user          |
| GET    | /api/system/logs | Stream live logs           |

## Environment Configuration

Create `.env` from `.env.example` and update:

```
MODEL_NAME=tiiuae/falcon-rw-1b
DATABASE_URL=postgresql://user:pass@localhost:5432/synthara
DEBUG=true
```

## Testing

```bash
pytest backend/tests
```

## License

MIT License