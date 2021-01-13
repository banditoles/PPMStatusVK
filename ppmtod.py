#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime


def ppmtod(ppm):
    year = int(datetime.datetime.now().year)
    return ppm * ((366 if year % 400 == 0 or year % 4 == 0 and year % 100 != 0 else 365)) * 86400 / 1000 + datetime.datetime.strptime(f"{year}-1-1 00:00:00", '%Y-%m-%d %H:%M:%S').timestamp()


while True:
    try:
        date = int(input())
    except ValueError:
        print('Invalid number.\n')
        continue
    print(datetime.datetime.fromtimestamp(ppmtod(date)).strftime('%d.%m.%Y %H:%M:%S'))
