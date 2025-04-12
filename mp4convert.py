#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Copyright 2014 MadMax <madmaxxx@email.it>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

__author__ = 'MadMax'
__version__ = '1.0'
__license__ = 'Public Domain'

import os
import sys
import shutil
import subprocess
import tempfile
import argparse
sys.path.append(os.path.expanduser("~") + "/Scripts/Python/lib/")
import basedaemon

AVIDEMUX = "/usr/bin/avidemux3_cli"
SCRIPT = "/home/madmax/Scripts/Python/Tinypy/x264.py"
RATE = 20
BITRATE = "224k"
FFMPEG = "/usr/bin/ffmpeg"
SAMPLERATE = 48000
EXTENSIONS = (".bak", ".avi", ".mp4", ".mkv", ".srt")
AUDIO_LIBRARIES = ("libfaac", "libfdk_aac", "aac")
X264PRESETS = (
    "ultrafast",
    "superfast",
    "veryfast",
    "faster",
    "fast",
    "medium",
    "slow",
    "slower",
    "veryslow",
    "placebo")
X264LEVELS = ("1", "1b", "1.1", "1.2", "1.3", "2", "2.1", "2.2",
              "3", "3.1", "3.2", "4", "4.1", "4.2", "5", "5.1")
WIDTH = 1280


class Mp4ConvertException(Exception):
    pass


class Mp4Convert:
    def __init__(self, *args):
        self.filename = os.path.realpath(args[0])
        self.daemon = args[1]
        self.tempfile = tempfile.mkstemp(
            EXTENSIONS[1], "tmp~", tempfile.gettempdir())[-1]
        self.command = ()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if os.path.isfile(self.tempfile):
            os.remove(self.tempfile)

    def move(self):
        if self.filename.endswith(EXTENSIONS[2]):
            shutil.move(self.filename, f"{self.filename}.original")
        else:
            self.filename = f"{os.path.splitext(self.filename)[0]}{EXTENSIONS[2]}"
        shutil.move(self.tempfile, self.filename)

    def _popen(self, **kwargs):
        with subprocess.Popen(self.command, stdin=kwargs.get("stdin")) as _process:
            _process.communicate(kwargs.get("communicate"))
            return _process

    def run(self, **kwargs):
        try:
            if self.daemon:
                _process = basedaemon.BaseDaemon().start(self._popen, **kwargs)
            else:
                _process = self._popen(**kwargs)
            if _process.returncode:
                raise Mp4ConvertException
            self.move()
        except OSError as _error:
            raise Mp4ConvertException from _error


class FfmpegConvert(Mp4Convert):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.lib = kwargs.get("lib")
        self.map = kwargs.get("amap")
        self.scale = kwargs.get("scale")
        self.subtitles = kwargs.get("subtitles")
        if os.path.isfile(_filename_srt := f"{os.path.splitext(self.filename)[0]}{EXTENSIONS[4]}"):
            self.subtitles = _filename_srt

    def encode(self):
        self.command += (FFMPEG, "-nostdin", "-hide_banner",
                         "-y", "-i", self.filename)
        _subtitles = f"subtitles=filename='{self.subtitles}':force_style='Fontsize=10'"
        _scale = f"scale='min(iw, {WIDTH})':-2"
        if self.scale and self.subtitles:
            self.command += ("-vf", f"{_scale}, {_subtitles}")
        elif self.scale:
            self.command += ("-vf", f"{_scale}")
        elif self.subtitles:
            self.command += ("-vf", f"{_subtitles}")
        if self.map:
            self.command += ("-map", "0:v", "-map", f"0:a:{self.map}")
        self.command += ("-c:v",
                         "libx264",
                         "-preset:v",
                         X264PRESETS[2],
                         "-level",
                         X264LEVELS[9],
                         "-x264opts",
                         f"crf={RATE}",
                         "-c:a",
                         self.lib,
                         "-b:a",
                         BITRATE,
                         "-ar",
                         f"{SAMPLERATE}",
                         self.tempfile)
        self.run()


class AvidemuxConvert(Mp4Convert):
    def encode(self):
        self.command += (AVIDEMUX,
                         "--load",
                         self.filename,
                         "--run",
                         SCRIPT,
                         "--save",
                         self.tempfile,
                         "--quit")
        self.run(stdin=subprocess.PIPE, communicate=b"y\n\\y\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ffmpeg", action="store_true")
    parser.add_argument(
        "--lib",
        action="store",
        choices=AUDIO_LIBRARIES,
        default=AUDIO_LIBRARIES[2])
    parser.add_argument("--map", action="store", type=int, default=None)
    parser.add_argument("--no-scale", action="store_false")
    parser.add_argument("--daemon", action="store_true")
    parser.add_argument("files", nargs="+")
    args = parser.parse_args()
    for _file in args.files:
        if args.ffmpeg:
            FfmpegConvert(
                _file,
                args.daemon,
                lib=args.lib,
                amap=args.map,
                scale=args.no_scale).encode()
        else:
            AvidemuxConvert(_file, args.daemon).encode()


if __name__ == "__main__":
    main()
