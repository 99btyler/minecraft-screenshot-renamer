import os
from PIL import Image


source_folder = "screenshots"
new_folder = "screenshots_renamed"

for file in os.listdir(source_folder):
	if file.endswith(".png"):

		screenshot = Image.open(f"{source_folder}/{file}")
		s_name, s_extension = os.path.splitext(file)

		s_namesplit = s_name.split("_")

		date = s_namesplit[0]
		datesplit = date.split("-")
		d_year = datesplit[0]
		d_month = datesplit[1]
		d_day = datesplit[2]
		better_date = f"{d_month}.{d_day}.{d_year}"

		time = s_namesplit[1]
		timesplit = time.split(".")
		t_hour = timesplit[0]
		t_minute = timesplit[1]
		t_second = timesplit[2]
		t_hourconverted = t_hour if (int(t_hour) > 0 and int(t_hour) <= 12) else abs(int(t_hour) - 12)
		t_period = "AM" if int(t_hour) < 12 else "PM"
		better_time = f"{t_hour}.{t_minute}.{t_second} ({t_hourconverted}.{t_minute} {t_period})"

		s_name_2 = f"{better_date} @ {better_time}"

		screenshot.save(f"{new_folder}/{s_name_2}{s_extension}")
		print(f"Renamed {s_name} to {s_name_2}")

