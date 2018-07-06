import sys
import os
lib_path = os.path.dirname(os.path.abspath(__file__)) + '/lib/'
sys.path.append(lib_path)

lib_path = os.path.dirname(os.path.abspath(__file__)) + '/models/'
sys.path.append(lib_path)

import date_manager
import spot as m_spot
import instrument as m_instrument
import instrument_measure as m_instrument_measure

args = sys.argv
spot_code = args[1]
instrument_id = args[2]
from_number = args[3]
to_number = args[4]

spot = m_spot.Spot()
spot.where('code', spot_code)
spot.one()

instrument = m_instrument.Instrument()
instrument.fetch(instrument_id)

date = date_manager.DateManager()
date.setNumberForInterval(from_number, to_number)

file_name = "instrument_%s_%s.png" % (spot_code, instrument_id)

instrument_measure = m_instrument_measure.InstrumentMeasure()
instrument_measure.setDate(date)
instrument_measure.setSpot(spot)
instrument_measure.setInstrument(instrument)
instrument_measure.fetchValues()
instrument_measure.graphValues()
instrument_measure.draw(file_name)

print("file_name:", file_name)
print("spot code:", spot.value['code'])
print("spot name:", spot.value['name'])
print("instrument_id:", instrument_id)
print("from_datetime:", date.from_datetime)
print("to_datetime:", date.to_datetime)

# with TempImage(img_name) as img:
#         img.create_png()
#         return send_file(img_name, mimetype='image/png')