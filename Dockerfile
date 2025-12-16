
FROM python:3.12

WORKDIR /home/juicy/Documents/dev/python/vergil-bot

RUN pip install discord.py
RUN pip install discord.py[voice]
RUN pip install PyNaCl
RUN apt update
RUN apt install -y ffmpeg

COPY . .

CMD ["python3", "vergil_bot.py"]
