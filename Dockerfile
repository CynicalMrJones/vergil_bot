
FROM python:3.12

WORKDIR /home/juicy/Documents/dev/python/vergil-bot

RUN pip install discord.py

COPY . .

CMD ["python3", "vergil_bot.py"]
