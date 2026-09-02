#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LongRangeWeatherVariables(object):

    def __init__(self):
        self._apparent_temperature = None
        self._cloud_cover = None
        self._dew_point_2_m = None
        self._diffuse_radiation = None
        self._diffuse_radiation_instant = None
        self._direct_radiation = None
        self._direct_radiation_instant = None
        self._precipitation = None
        self._pressure_msl = None
        self._relative_humidity_2_m = None
        self._shortwave_radiation = None
        self._shortwave_radiation_instant = None
        self._surface_pressure = None
        self._temperature_2_m = None
        self._temperature_max_2_m = None
        self._temperature_min_2_m = None
        self._variable_date = None
        self._weather_code = None
        self._wind_direction_100_m = None
        self._wind_direction_10_m = None
        self._wind_direction_200_m = None
        self._wind_gusts_10_m = None
        self._wind_speed_100_m = None
        self._wind_speed_10_m = None
        self._wind_speed_200_m = None

    @property
    def apparent_temperature(self):
        return self._apparent_temperature

    @apparent_temperature.setter
    def apparent_temperature(self, value):
        self._apparent_temperature = value
    @property
    def cloud_cover(self):
        return self._cloud_cover

    @cloud_cover.setter
    def cloud_cover(self, value):
        self._cloud_cover = value
    @property
    def dew_point_2_m(self):
        return self._dew_point_2_m

    @dew_point_2_m.setter
    def dew_point_2_m(self, value):
        self._dew_point_2_m = value
    @property
    def diffuse_radiation(self):
        return self._diffuse_radiation

    @diffuse_radiation.setter
    def diffuse_radiation(self, value):
        self._diffuse_radiation = value
    @property
    def diffuse_radiation_instant(self):
        return self._diffuse_radiation_instant

    @diffuse_radiation_instant.setter
    def diffuse_radiation_instant(self, value):
        self._diffuse_radiation_instant = value
    @property
    def direct_radiation(self):
        return self._direct_radiation

    @direct_radiation.setter
    def direct_radiation(self, value):
        self._direct_radiation = value
    @property
    def direct_radiation_instant(self):
        return self._direct_radiation_instant

    @direct_radiation_instant.setter
    def direct_radiation_instant(self, value):
        self._direct_radiation_instant = value
    @property
    def precipitation(self):
        return self._precipitation

    @precipitation.setter
    def precipitation(self, value):
        self._precipitation = value
    @property
    def pressure_msl(self):
        return self._pressure_msl

    @pressure_msl.setter
    def pressure_msl(self, value):
        self._pressure_msl = value
    @property
    def relative_humidity_2_m(self):
        return self._relative_humidity_2_m

    @relative_humidity_2_m.setter
    def relative_humidity_2_m(self, value):
        self._relative_humidity_2_m = value
    @property
    def shortwave_radiation(self):
        return self._shortwave_radiation

    @shortwave_radiation.setter
    def shortwave_radiation(self, value):
        self._shortwave_radiation = value
    @property
    def shortwave_radiation_instant(self):
        return self._shortwave_radiation_instant

    @shortwave_radiation_instant.setter
    def shortwave_radiation_instant(self, value):
        self._shortwave_radiation_instant = value
    @property
    def surface_pressure(self):
        return self._surface_pressure

    @surface_pressure.setter
    def surface_pressure(self, value):
        self._surface_pressure = value
    @property
    def temperature_2_m(self):
        return self._temperature_2_m

    @temperature_2_m.setter
    def temperature_2_m(self, value):
        self._temperature_2_m = value
    @property
    def temperature_max_2_m(self):
        return self._temperature_max_2_m

    @temperature_max_2_m.setter
    def temperature_max_2_m(self, value):
        self._temperature_max_2_m = value
    @property
    def temperature_min_2_m(self):
        return self._temperature_min_2_m

    @temperature_min_2_m.setter
    def temperature_min_2_m(self, value):
        self._temperature_min_2_m = value
    @property
    def variable_date(self):
        return self._variable_date

    @variable_date.setter
    def variable_date(self, value):
        self._variable_date = value
    @property
    def weather_code(self):
        return self._weather_code

    @weather_code.setter
    def weather_code(self, value):
        self._weather_code = value
    @property
    def wind_direction_100_m(self):
        return self._wind_direction_100_m

    @wind_direction_100_m.setter
    def wind_direction_100_m(self, value):
        self._wind_direction_100_m = value
    @property
    def wind_direction_10_m(self):
        return self._wind_direction_10_m

    @wind_direction_10_m.setter
    def wind_direction_10_m(self, value):
        self._wind_direction_10_m = value
    @property
    def wind_direction_200_m(self):
        return self._wind_direction_200_m

    @wind_direction_200_m.setter
    def wind_direction_200_m(self, value):
        self._wind_direction_200_m = value
    @property
    def wind_gusts_10_m(self):
        return self._wind_gusts_10_m

    @wind_gusts_10_m.setter
    def wind_gusts_10_m(self, value):
        self._wind_gusts_10_m = value
    @property
    def wind_speed_100_m(self):
        return self._wind_speed_100_m

    @wind_speed_100_m.setter
    def wind_speed_100_m(self, value):
        self._wind_speed_100_m = value
    @property
    def wind_speed_10_m(self):
        return self._wind_speed_10_m

    @wind_speed_10_m.setter
    def wind_speed_10_m(self, value):
        self._wind_speed_10_m = value
    @property
    def wind_speed_200_m(self):
        return self._wind_speed_200_m

    @wind_speed_200_m.setter
    def wind_speed_200_m(self, value):
        self._wind_speed_200_m = value


    def to_alipay_dict(self):
        params = dict()
        if self.apparent_temperature:
            if hasattr(self.apparent_temperature, 'to_alipay_dict'):
                params['apparent_temperature'] = self.apparent_temperature.to_alipay_dict()
            else:
                params['apparent_temperature'] = self.apparent_temperature
        if self.cloud_cover:
            if hasattr(self.cloud_cover, 'to_alipay_dict'):
                params['cloud_cover'] = self.cloud_cover.to_alipay_dict()
            else:
                params['cloud_cover'] = self.cloud_cover
        if self.dew_point_2_m:
            if hasattr(self.dew_point_2_m, 'to_alipay_dict'):
                params['dew_point_2_m'] = self.dew_point_2_m.to_alipay_dict()
            else:
                params['dew_point_2_m'] = self.dew_point_2_m
        if self.diffuse_radiation:
            if hasattr(self.diffuse_radiation, 'to_alipay_dict'):
                params['diffuse_radiation'] = self.diffuse_radiation.to_alipay_dict()
            else:
                params['diffuse_radiation'] = self.diffuse_radiation
        if self.diffuse_radiation_instant:
            if hasattr(self.diffuse_radiation_instant, 'to_alipay_dict'):
                params['diffuse_radiation_instant'] = self.diffuse_radiation_instant.to_alipay_dict()
            else:
                params['diffuse_radiation_instant'] = self.diffuse_radiation_instant
        if self.direct_radiation:
            if hasattr(self.direct_radiation, 'to_alipay_dict'):
                params['direct_radiation'] = self.direct_radiation.to_alipay_dict()
            else:
                params['direct_radiation'] = self.direct_radiation
        if self.direct_radiation_instant:
            if hasattr(self.direct_radiation_instant, 'to_alipay_dict'):
                params['direct_radiation_instant'] = self.direct_radiation_instant.to_alipay_dict()
            else:
                params['direct_radiation_instant'] = self.direct_radiation_instant
        if self.precipitation:
            if hasattr(self.precipitation, 'to_alipay_dict'):
                params['precipitation'] = self.precipitation.to_alipay_dict()
            else:
                params['precipitation'] = self.precipitation
        if self.pressure_msl:
            if hasattr(self.pressure_msl, 'to_alipay_dict'):
                params['pressure_msl'] = self.pressure_msl.to_alipay_dict()
            else:
                params['pressure_msl'] = self.pressure_msl
        if self.relative_humidity_2_m:
            if hasattr(self.relative_humidity_2_m, 'to_alipay_dict'):
                params['relative_humidity_2_m'] = self.relative_humidity_2_m.to_alipay_dict()
            else:
                params['relative_humidity_2_m'] = self.relative_humidity_2_m
        if self.shortwave_radiation:
            if hasattr(self.shortwave_radiation, 'to_alipay_dict'):
                params['shortwave_radiation'] = self.shortwave_radiation.to_alipay_dict()
            else:
                params['shortwave_radiation'] = self.shortwave_radiation
        if self.shortwave_radiation_instant:
            if hasattr(self.shortwave_radiation_instant, 'to_alipay_dict'):
                params['shortwave_radiation_instant'] = self.shortwave_radiation_instant.to_alipay_dict()
            else:
                params['shortwave_radiation_instant'] = self.shortwave_radiation_instant
        if self.surface_pressure:
            if hasattr(self.surface_pressure, 'to_alipay_dict'):
                params['surface_pressure'] = self.surface_pressure.to_alipay_dict()
            else:
                params['surface_pressure'] = self.surface_pressure
        if self.temperature_2_m:
            if hasattr(self.temperature_2_m, 'to_alipay_dict'):
                params['temperature_2_m'] = self.temperature_2_m.to_alipay_dict()
            else:
                params['temperature_2_m'] = self.temperature_2_m
        if self.temperature_max_2_m:
            if hasattr(self.temperature_max_2_m, 'to_alipay_dict'):
                params['temperature_max_2_m'] = self.temperature_max_2_m.to_alipay_dict()
            else:
                params['temperature_max_2_m'] = self.temperature_max_2_m
        if self.temperature_min_2_m:
            if hasattr(self.temperature_min_2_m, 'to_alipay_dict'):
                params['temperature_min_2_m'] = self.temperature_min_2_m.to_alipay_dict()
            else:
                params['temperature_min_2_m'] = self.temperature_min_2_m
        if self.variable_date:
            if hasattr(self.variable_date, 'to_alipay_dict'):
                params['variable_date'] = self.variable_date.to_alipay_dict()
            else:
                params['variable_date'] = self.variable_date
        if self.weather_code:
            if hasattr(self.weather_code, 'to_alipay_dict'):
                params['weather_code'] = self.weather_code.to_alipay_dict()
            else:
                params['weather_code'] = self.weather_code
        if self.wind_direction_100_m:
            if hasattr(self.wind_direction_100_m, 'to_alipay_dict'):
                params['wind_direction_100_m'] = self.wind_direction_100_m.to_alipay_dict()
            else:
                params['wind_direction_100_m'] = self.wind_direction_100_m
        if self.wind_direction_10_m:
            if hasattr(self.wind_direction_10_m, 'to_alipay_dict'):
                params['wind_direction_10_m'] = self.wind_direction_10_m.to_alipay_dict()
            else:
                params['wind_direction_10_m'] = self.wind_direction_10_m
        if self.wind_direction_200_m:
            if hasattr(self.wind_direction_200_m, 'to_alipay_dict'):
                params['wind_direction_200_m'] = self.wind_direction_200_m.to_alipay_dict()
            else:
                params['wind_direction_200_m'] = self.wind_direction_200_m
        if self.wind_gusts_10_m:
            if hasattr(self.wind_gusts_10_m, 'to_alipay_dict'):
                params['wind_gusts_10_m'] = self.wind_gusts_10_m.to_alipay_dict()
            else:
                params['wind_gusts_10_m'] = self.wind_gusts_10_m
        if self.wind_speed_100_m:
            if hasattr(self.wind_speed_100_m, 'to_alipay_dict'):
                params['wind_speed_100_m'] = self.wind_speed_100_m.to_alipay_dict()
            else:
                params['wind_speed_100_m'] = self.wind_speed_100_m
        if self.wind_speed_10_m:
            if hasattr(self.wind_speed_10_m, 'to_alipay_dict'):
                params['wind_speed_10_m'] = self.wind_speed_10_m.to_alipay_dict()
            else:
                params['wind_speed_10_m'] = self.wind_speed_10_m
        if self.wind_speed_200_m:
            if hasattr(self.wind_speed_200_m, 'to_alipay_dict'):
                params['wind_speed_200_m'] = self.wind_speed_200_m.to_alipay_dict()
            else:
                params['wind_speed_200_m'] = self.wind_speed_200_m
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LongRangeWeatherVariables()
        if 'apparent_temperature' in d:
            o.apparent_temperature = d['apparent_temperature']
        if 'cloud_cover' in d:
            o.cloud_cover = d['cloud_cover']
        if 'dew_point_2_m' in d:
            o.dew_point_2_m = d['dew_point_2_m']
        if 'diffuse_radiation' in d:
            o.diffuse_radiation = d['diffuse_radiation']
        if 'diffuse_radiation_instant' in d:
            o.diffuse_radiation_instant = d['diffuse_radiation_instant']
        if 'direct_radiation' in d:
            o.direct_radiation = d['direct_radiation']
        if 'direct_radiation_instant' in d:
            o.direct_radiation_instant = d['direct_radiation_instant']
        if 'precipitation' in d:
            o.precipitation = d['precipitation']
        if 'pressure_msl' in d:
            o.pressure_msl = d['pressure_msl']
        if 'relative_humidity_2_m' in d:
            o.relative_humidity_2_m = d['relative_humidity_2_m']
        if 'shortwave_radiation' in d:
            o.shortwave_radiation = d['shortwave_radiation']
        if 'shortwave_radiation_instant' in d:
            o.shortwave_radiation_instant = d['shortwave_radiation_instant']
        if 'surface_pressure' in d:
            o.surface_pressure = d['surface_pressure']
        if 'temperature_2_m' in d:
            o.temperature_2_m = d['temperature_2_m']
        if 'temperature_max_2_m' in d:
            o.temperature_max_2_m = d['temperature_max_2_m']
        if 'temperature_min_2_m' in d:
            o.temperature_min_2_m = d['temperature_min_2_m']
        if 'variable_date' in d:
            o.variable_date = d['variable_date']
        if 'weather_code' in d:
            o.weather_code = d['weather_code']
        if 'wind_direction_100_m' in d:
            o.wind_direction_100_m = d['wind_direction_100_m']
        if 'wind_direction_10_m' in d:
            o.wind_direction_10_m = d['wind_direction_10_m']
        if 'wind_direction_200_m' in d:
            o.wind_direction_200_m = d['wind_direction_200_m']
        if 'wind_gusts_10_m' in d:
            o.wind_gusts_10_m = d['wind_gusts_10_m']
        if 'wind_speed_100_m' in d:
            o.wind_speed_100_m = d['wind_speed_100_m']
        if 'wind_speed_10_m' in d:
            o.wind_speed_10_m = d['wind_speed_10_m']
        if 'wind_speed_200_m' in d:
            o.wind_speed_200_m = d['wind_speed_200_m']
        return o


