#!/usr/bin/env python
import os
import csv
from live_schedule.models import Schedule

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

reader = csv.reader(open("kaijyu-1.csv"))

for r in reader:
    print r
    h = Heya()
    h.tanako = r[0].decode('cp932').encode('utf-8')
    h.bango = r[1]
    h.hirosa = r[2]
    h.yachin = r[3]
    h.save()
