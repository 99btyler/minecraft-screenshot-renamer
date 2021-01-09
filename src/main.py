import os
from PIL import Image


input_folder = "screenshots"
output_folder = "screenshots_renamed"

for file in os.listdir(input_folder):

	# Get the current screenshot (plus its name & extension)
	screenshot = Image.open(f"{input_folder}/{file}")
	s_name, s_extension = os.path.splitext(file)

	# Separate the date and time
	s_namesplit = s_name.split("_")

	# DATE (xxxx-xx-xx)
	date = s_namesplit[0]
	datesplit = date.split("-")
	d_year = datesplit[0]
	d_month = datesplit[1].lstrip("0")
	d_day = datesplit[2].lstrip("0")
	better_date = f"{d_month}.{d_day}.{d_year}"

	# TIME (xx.xx.xx)
	time = s_namesplit[1]
	timesplit = time.split(".")
	t_hour = timesplit[0]
	t_minute = timesplit[1]
	t_second = timesplit[2]
	t_hourconverted = t_hour if (int(t_hour) > 0 and int(t_hour) <= 12) else abs(int(t_hour) - 12)
	t_period = "AM" if int(t_hour) < 12 else "PM"
	better_time = f"{t_hour}.{t_minute}.{t_second} ({t_hourconverted}.{t_minute} {t_period})"

	s_name_2 = f"{better_date} @ {better_time}"

	screenshot.save(f"{output_folder}/{s_name_2}{s_extension}")
	print(f"Renamed {s_name} to {s_name_2}")

