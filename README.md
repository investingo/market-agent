
# Market Watcher Agent

Agent, který každých 10 minut:
1. Přihlásí se na https://io-fund.com
2. Navštíví sekci Market Signals
3. Zkontroluje, zda byl zveřejněn nový příspěvek
4. Pokud ano, odešle notifikaci přes WhatsApp pomocí Twilio

## Spuštění lokálně

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.template .env  # doplň své údaje
python agent.py
```

## Nasazení na Render.com

1. Nahrát na GitHub
2. V Render.com vytvořit nový **Background Worker**
3. Build command:
```bash
pip install -r requirements.txt
```
4. Start command:
```bash
python agent.py
```
5. Environment variables zadat přes GUI
