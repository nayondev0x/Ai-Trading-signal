# 📈 AI Trading Analyse — Live Dashboard

Crypto + US Stocks-এর live trading signal dashboard। **FastAPI** backend,
**Vercel**-এ deploy করার জন্য সম্পূর্ণ প্রস্তুত।

## 🗂️ Structure
```
ai-trading-analyse/
├── api/
│   └── index.py          # Vercel entry point
├── app/
│   ├── main.py           # FastAPI routes (/ = live dashboard)
│   ├── tradingview_api.py# TradingView signal (RapidAPI)
│   ├── coingecko_api.py  # CoinGecko live price + RSI (key লাগে না)
│   ├── signal_engine.py  # BUY/SELL/NEUTRAL তৈরির লজিক
│   ├── crypto_api.py, config.py, models.py, store.py
│   ├── static/
│   └── templates/        # dashboard.html, index.html
├── vercel.json
├── requirements.txt
└── .python-version
```

## 🚀 Vercel-এ Deploy (৪ ধাপ)
1. পুরো folder একটা **GitHub** repo-তে upload করুন।
2. **vercel.com → Add New → Project** → repo select করুন।
3. **Framework Preset: Other** রাখুন (Build Command / Output খালি)।
4. **Settings → Environment Variables**-এ key দিন (নিচে দেখুন) → **Deploy**।

Deploy হলে লিংক: `https://your-app.vercel.app` → সরাসরি live dashboard দেখাবে।

## 🔑 Environment Variables (Vercel dashboard-এ)
| Variable | দরকার? | কাজ |
|----------|--------|-----|
| `RAPIDAPI_KEY` | ঐচ্ছিক | TradingView signal (stocks + crypto) |
| `USE_MOCK_FALLBACK` | না | `true` রাখুন |

> 💡 **key না দিলেও dashboard চলবে** — crypto live দেখাবে (CoinGecko, free),
> আর stocks তখন demo/mock দেখাবে। key দিলে stocks-ও live হবে।

## 🔗 Endpoints
| Path | কাজ |
|------|------|
| `/` | Live dashboard (crypto + stocks) |
| `/dashboard` | একই dashboard |
| `/api/market` | JSON signal data |
| `/api/symbols` | সব symbol-এর তালিকা |
| `/docs` | Swagger API docs |

## 💻 লোকালি চালাতে
```bash
pip install -r requirements.txt uvicorn
uvicorn app.main:app --reload
```

> ⚠️ Vercel filesystem read-only — তাই in-memory data প্রতি cold-start-এ reset হয়।
> এটা signal dashboard-এর জন্য সমস্যা না (data live API থেকে আসে)।
