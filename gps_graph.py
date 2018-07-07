import sys
import os
lib_path = os.path.dirname(os.path.abspath(__file__)) + '/lib/'
sys.path.append(lib_path)

lib_path = os.path.dirname(os.path.abspath(__file__)) + '/models/'
sys.path.append(lib_path)

import date_manager
import spot as m_spot
import sensor as m_sensor
import sensor_measure as m_sm

args = sys.argv
spot_code = args[1]
sensor_id = args[2]
from_number = args[3]
to_number = args[4]

spot = m_spot.Spot()
spot.where('code', spot_code)
spot.one()

sensor = m_sensor.Sensor()
sensor.fetch(sensor_id)

date = date_manager.DateManager()
date.setNumberForInterval(from_number, to_number)

file_name = "gps_%s_%s.png" % (spot_code, sensor_id)
print("spot code:", spot.value['code'])
print("spot name:", spot.value['name'])
print("sensor_id:", sensor_id)
print("from_datetime:", date.from_datetime)
print("to_datetime:", date.to_datetime)
print("file_name:", file_name)

sensor_measure = m_sm.SensorMeasure()
sensor_measure.setDate(date)
sensor_measure.setSpot(spot)
sensor_measure.setSensor(sensor)
sensor_measure.fetchValues()
sensor_measure.graphValues()
sensor_measure.draw(file_name)

# with TempImage(img_name) as img:
#         img.create_png()
#         return send_file(img_name, mimetype='image/png')