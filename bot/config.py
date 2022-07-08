#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from decouple import config

try:
    APP_ID = config("APP_ID", cast=int)
    API_HASH = config("API_HASH")
    BOT_TOKEN = config("BOT_TOKEN")
    DEV = 1322549723
    OWNER = config("OWNER")
    FFMPEG = config(
        "FFMPEG",
       default='''ffmpeg -i "{}" -pix_fmt yuv420p10le -r 24000/1001 -s 1920x1080 -preset medium -c:v libx265 -crf 20 -metadata title="[Yugen] Sword Art Online: Progressive - Hoshinaki Yoru no Aria (Sword Art Online the Movie -Progressive- Aria of a Starless Night) [BD 1080p HEVC x265 10Bit][OPUS]" -x265-params frame-threads=4:no-info=1 -map 0:v -c:a libopus -b:a 112k -map 0:a -c:s copy -map 0:s? "{}"''',
    )
    THUMB = config(
        "THUMBNAIL", default="https://telegra.ph/file/75ee20ec8d8c8bba84f02.jpg"
    )
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()
