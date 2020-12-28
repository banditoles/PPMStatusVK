#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time;
import requests;


ACCESS_TOKEN = "";
API_VERSION  = "5.700";

STATUS_TEXT = "Хочу бдсм | 2020 год прошел на {}‰";
UPDATE_PERIOD = 60; #минимум 60 секунд, дальше капча
SCRIPT_URL   = "https://api.vk.com/method/status.set?access_token={}&v={}&text={{}}".format(ACCESS_TOKEN, API_VERSION);

def get_2020_ppm():
    return 1000 / (366 * 86400) * (time.time() - time.mktime((2020, 1, 1, 0, 0, 0, 0, 0, 0)));

def status_set(text):
    response = requests.Session().post(SCRIPT_URL.format(text));

    if response.json().get("error"):
        console(f"status.set failed: {response.json()['error']}");

    else:
        console(f"status.set: {text}");


def console(text):
    print(f'[{time.asctime()}] {text}');
    # print(f'{time.ctime(time.time())}');

while True:
    status_set(STATUS_TEXT.format(get_2020_ppm()));
    time.sleep(UPDATE_PERIOD);
