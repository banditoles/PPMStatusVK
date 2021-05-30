#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time;
import requests;
import datetime;

ACCESS_TOKEN = "access_token";
API_VERSION = "5.700";

STATUS_TEXT = "{} | 2021 год прошел на {}‰";
UPDATE_PERIOD = 60;  # Минимум 60 секунд, дальше капча
SCRIPT_URL = "https://api.vk.com/method/status.set?access_token={}&v={}&text={{}}";
DATE = '2021-1-1 00:00:00';

song_text = '''
вышел заяц на крыльцо
почесать свое яйцо
раз
два
три'''.split('\n')

class Song:
    def __init__(self, song_text):

        self.song_text =  song_text
        self.current_line_number = None
        self.current_line = None
        self.iterator = iter(self.__iter__())

    def __iter__(self):

        self.current_line_number = 0
        return self

    def __next__(self):

        try:
            self.current_line = self.song_text[self.current_line_number]
            self.current_line_number += 1
            return self.current_line

        except IndexError:
            self.current_line_number = 0
            return self.__next__()

    def get_song_line(self):
            return(next(self.iterator))

song = Song(song_text)


def status_set(text):
    response = requests.Session().post(SCRIPT_URL
                                       .format(ACCESS_TOKEN, API_VERSION)
                                       .format(text));

    if response.json().get("error"):
        console(f"status.set failed: {response.json()['error']}");

    else:
        console(f"status.set: {text}");


def console(text):
    print(f'[{time.asctime()}] {text}');


while True:
    status_set(STATUS_TEXT.format(song.get_song_line(), get_2020_ppm()));
    time.sleep(UPDATE_PERIOD);
