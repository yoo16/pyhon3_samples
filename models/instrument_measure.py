import pandas as pd
import matplotlib as mpl
#background : mpl.use('Agg')
mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
#import cStringIO
import matplotlib.dates as mdates
import math
import numpy as np
import datetime as dt
import seaborn as sns
import pgsql

class InstrumentMeasure(pgsql.Pgsql):
    host = 'shamen-test.telepath'
    dbname = 'shamen3_data'
    table_name = 'instrument_measures'
    mark_size = 1
    line_width = 0.5
    style = 'bmh'

    @classmethod
    def draw(self, file_name):
        plt.style.use('ggplot')
        plt.figure(figsize = (13, 5))
        plt.title('Instrument Graph', fontsize = 12)
        plt.xlabel('dateime')
        plt.ylabel('measure')
        plt.style.use(self.style) 

        graph_count = 2
        datetimes = self.graph_values['datetimes']

        ax = plt.subplot(graph_count, 1, 1)
        ax.set_ylim([-50, 50])
        ax.set_xlim([self.date.from_datetime, self.date.to_datetime])
        plt.plot(datetimes, self.graph_values['value_x'], linewidth = self.line_width)

        ax = plt.subplot(graph_count, 1, 2)
        ax.set_ylim([-50, 50])
        ax.set_xlim([self.date.from_datetime, self.date.to_datetime])
        plt.plot(datetimes, self.graph_values['value_y'], linewidth = self.line_width)

        #plt.show()
        plt.savefig(file_name)
        return

    @classmethod
    def setDate(self, date):
        self.date = date

    @classmethod
    def setInstrumentType(self, instrument_type):
        self.instrument_type = instrument_type

    @classmethod
    def setSpot(self, spot):
        self.spot = spot

    @classmethod
    def setInstrument(self, instrument):
        self.instrument = instrument
        self.instrument_type = instrument.value['instrument_type']

    @classmethod
    def fetchValues(self):
        table_name = self.instrument_type + '_measures_' + self.spot.value['code']

        self.setTableName(table_name)
        self.where('datetime', self.date.from_datetime, '>=')
        self.where('datetime', self.date.to_datetime, '<')
        self.where('instrument_id', self.instrument.value['id'])
        self.order('datetime')
        self.all()

        self.values = self.values
        return

    @classmethod
    def graphValues(self):
        if self.values is None:
           return
        
        datetimes = []
        value_x = []
        value_y = []
        value_z = []

        for row in self.values:
            for column in ['value_x', 'value_y', 'value_z']:
                if row[column] is None:
                   row[column] = np.nan

            datetimes.append(row['datetime'])
            value_x.append(row['value_x'])
            value_y.append(row['value_y'])
            value_z.append(row['value_z'])

        self.graph_values = {
                'datetimes' : datetimes,
                'value_x' : value_x,
                'value_y' : value_y,
                'value_z' : value_z,
        }
        return