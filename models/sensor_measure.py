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

class SensorMeasure(pgsql.Pgsql):
    dbname = 'sample'
    host = 'localhost'
    table_name = 'sensor_measures'
    values = []
    mark_size = 1
    line_width = 0.5
    style = 'bmh'

    @classmethod
    def draw(self, file_name):
        plt.style.use('ggplot')
        plt.figure(figsize = (13, 10))
        plt.title('Calculate Graph', fontsize = 12)
        plt.xlabel('dateime')
        plt.ylabel('measure')
        plt.style.use(self.style) 

        graph_count = 5
        datetimes = self.graph_values['datetimes']

        ax = plt.subplot(graph_count, 1, 1)
        ax.set_ylim([-50, 50])
        ax.set_xlim([self.date.from_datetime, self.date.to_datetime])
        plt.plot(datetimes, self.graph_values['rev_x'], 'o', markersize = self.mark_size)
        plt.plot(datetimes, self.graph_values['value_x'], linewidth = self.line_width)

        ax = plt.subplot(graph_count, 1, 2)
        ax.set_ylim([-50, 50])
        ax.set_xlim([self.date.from_datetime, self.date.to_datetime])
        plt.plot(datetimes, self.graph_values['rev_y'], 'o', markersize = self.mark_size)
        plt.plot(datetimes, self.graph_values['value_y'], linewidth = self.line_width)

        ax = plt.subplot(graph_count, 1, 3)
        ax.set_ylim([-50, 50])
        ax.set_xlim([self.date.from_datetime, self.date.to_datetime])
        plt.plot(datetimes, self.graph_values['rev_z'], 'o', markersize = self.mark_size)
        plt.plot(datetimes, self.graph_values['value_z'], linewidth = self.line_width)

        ax = plt.subplot(graph_count, 1, 4)
        ax.set_ylim([0, 100])
        ax.set_xlim([self.date.from_datetime, self.date.to_datetime])
        plt.plot(datetimes, self.graph_values['value_h'], linewidth = self.line_width)

        ax = plt.subplot(graph_count, 1, 5)
        ax.set_ylim([0, 100])
        ax.set_xlim([self.date.from_datetime, self.date.to_datetime])
        plt.plot(datetimes, self.graph_values['value_t'], linewidth = self.line_width)

        #plt.show()
        plt.savefig(file_name)
        return

    @classmethod
    def setDate(self, date):
        self.date = date

    @classmethod
    def setSpot(self, spot):
        self.spot = spot

    @classmethod
    def setSensor(self, sensor):
        self.sensor = sensor

    @classmethod
    def fetchValues(self):
        table_name = self.table_name + '_' + self.spot.value['code']

        self.setTableName(table_name)
        self.where('datetime', self.date.from_datetime, '>=')
        self.where('datetime', self.date.to_datetime, '<')
        self.where('sensor_id', self.sensor.value['id'])
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
        value_h = []
        value_t = []
        rev_x = []
        rev_y = []
        rev_z = []
        for row in self.values:
            for column in ['value_x', 'value_y', 'value_z', 'rev_x', 'rev_y', 'rev_z']:
                if row[column] is None:
                   row[column] = np.nan

            datetimes.append(row['datetime'])
            value_x.append(row['value_x'])
            value_y.append(row['value_y'])
            value_z.append(row['value_z'])
            rev_x.append(row['rev_x'])
            rev_y.append(row['rev_y'])
            rev_z.append(row['rev_z'])
            value_h.append(np.sqrt(row['value_x']**2 + row['value_y']**2))
            value_t.append(np.sqrt(row['value_x']**2 + row['value_y']**2 + row['value_z']**2))

        self.graph_values = {
                'datetimes' : datetimes,
                'value_x' : value_x,
                'value_y' : value_y,
                'value_z' : value_z,
                'value_h' : value_h,
                'value_t' : value_t,
                'rev_x' : rev_x,
                'rev_y' : rev_y,
                'rev_z' : rev_z
        }
        return