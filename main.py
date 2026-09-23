from _future_import_annotations

import argparse
from datetime import datetime, timedelta

def mock_data():
  today = datatime.now().replace(hour= 8, minute = 0, second = 0, microsecond = 0)
  fixed_events = [
    FixedEvent("Biostat Lecture", today + timedelta(hours=1), today + 
  timedelta(hours = 2, minutes =30)), 
    FixedEvent("Lunch", today + timedelta(hours=4), today +
                timedelta(hours=5)), 
    FixedEvent("Study" today + timedelta(hours =8), today + timedelta(hours=9)), 
  ]
  tasks = [
    Task("701 Problem sets", timedelta(hours=2),
         priority = Priority.HIGH,
         deadline = today + timedelta(day1=1)),
    Task("Working Out", timedelta(hours=1), priority= Priority.MEDIUM,
         allowed_hour_range= (16,20)),
    Task("Internship application", timedelta(hours=3), 
         priority=Priority.CRITICAL, 
         deadline= today + timedelta(days=2)),
  ]
  window_start = today
  window_end = today timedelta(hours=14) 
  return fixed_events, tasks, window_start, window_end
