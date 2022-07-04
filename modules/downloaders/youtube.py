from os import path

from yt_dlp import YoutubeDL

from modules.config import DURATION_LIMIT
from modules.helpers.errors import DurationLimitError

ydl_opts = {
    "format": "bestaudio/best",
    "geo-bypass": True,
    "nocheckcertificate": True,
    "outtmpl": "downloads/%(id)s.%(ext)s",
}
ydl = YoutubeDL(ydl_opts)


def download(url: str) -> str:
    info = ydl.extract_info(url, False)
    duration = round(info["duration"] / 60)
    if duration > DURATION_LIMIT:
        raise DurationLimitError(
            f"Your Video is Longer Than {DURATION_LIMIT} Minute's Are not Allowed, The Provided is {duration} Minute(s)",
        )
    try:
        ydl.download([url])
    except:
        raise DurationLimitError(
            f"Your Video is Longer Than {DURATION_LIMIT} Minute's Are not Allowed, The Provided is {duration} Minute(s)",
        )
    return path.join("downloads", f"{info['id']}.{info['ext']}")
