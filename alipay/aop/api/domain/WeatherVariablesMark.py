#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WeatherVariablesMark(object):

    def __init__(self):
        self._cloud_cover = None
        self._cloud_cover_high = None
        self._cloud_cover_low = None
        self._cloud_cover_mid = None
        self._dew_point_2m = None
        self._diffuse_radiation = None
        self._direct_normal_irradiance = None
        self._direct_radiation = None
        self._precipitation_probability = None
        self._pressure_msl = None
        self._relative_humidity_2m = None
        self._shortwave_radiation = None
        self._surface_pressure = None
        self._temperature_2m = None
        self._wind_direction_10m = None
        self._wind_direction_120m = None
        self._wind_direction_80m = None
        self._wind_speed_10m = None
        self._wind_speed_120m = None
        self._wind_speed_80m = None

    @property
    def cloud_cover(self):
        return self._cloud_cover

    @cloud_cover.setter
    def cloud_cover(self, value):
        self._cloud_cover = value
    @property
    def cloud_cover_high(self):
        return self._cloud_cover_high

    @cloud_cover_high.setter
    def cloud_cover_high(self, value):
        self._cloud_cover_high = value
    @property
    def cloud_cover_low(self):
        return self._cloud_cover_low

    @cloud_cover_low.setter
    def cloud_cover_low(self, value):
        self._cloud_cover_low = value
    @property
    def cloud_cover_mid(self):
        return self._cloud_cover_mid

    @cloud_cover_mid.setter
    def cloud_cover_mid(self, value):
        self._cloud_cover_mid = value
    @property
    def dew_point_2m(self):
        return self._dew_point_2m

    @dew_point_2m.setter
    def dew_point_2m(self, value):
        self._dew_point_2m = value
    @property
    def diffuse_radiation(self):
        return self._diffuse_radiation

    @diffuse_radiation.setter
    def diffuse_radiation(self, value):
        self._diffuse_radiation = value
    @property
    def direct_normal_irradiance(self):
        return self._direct_normal_irradiance

    @direct_normal_irradiance.setter
    def direct_normal_irradiance(self, value):
        self._direct_normal_irradiance = value
    @property
    def direct_radiation(self):
        return self._direct_radiation

    @direct_radiation.setter
    def direct_radiation(self, value):
        self._direct_radiation = value
    @property
    def precipitation_probability(self):
        return self._precipitation_probability

    @precipitation_probability.setter
    def precipitation_probability(self, value):
        self._precipitation_probability = value
    @property
    def pressure_msl(self):
        return self._pressure_msl

    @pressure_msl.setter
    def pressure_msl(self, value):
        self._pressure_msl = value
    @property
    def relative_humidity_2m(self):
        return self._relative_humidity_2m

    @relative_humidity_2m.setter
    def relative_humidity_2m(self, value):
        self._relative_humidity_2m = value
    @property
    def shortwave_radiation(self):
        return self._shortwave_radiation

    @shortwave_radiation.setter
    def shortwave_radiation(self, value):
        self._shortwave_radiation = value
    @property
    def surface_pressure(self):
        return self._surface_pressure

    @surface_pressure.setter
    def surface_pressure(self, value):
        self._surface_pressure = value
    @property
    def temperature_2m(self):
        return self._temperature_2m

    @temperature_2m.setter
    def temperature_2m(self, value):
        self._temperature_2m = value
    @property
    def wind_direction_10m(self):
        return self._wind_direction_10m

    @wind_direction_10m.setter
    def wind_direction_10m(self, value):
        self._wind_direction_10m = value
    @property
    def wind_direction_120m(self):
        return self._wind_direction_120m

    @wind_direction_120m.setter
    def wind_direction_120m(self, value):
        self._wind_direction_120m = value
    @property
    def wind_direction_80m(self):
        return self._wind_direction_80m

    @wind_direction_80m.setter
    def wind_direction_80m(self, value):
        self._wind_direction_80m = value
    @property
    def wind_speed_10m(self):
        return self._wind_speed_10m

    @wind_speed_10m.setter
    def wind_speed_10m(self, value):
        self._wind_speed_10m = value
    @property
    def wind_speed_120m(self):
        return self._wind_speed_120m

    @wind_speed_120m.setter
    def wind_speed_120m(self, value):
        self._wind_speed_120m = value
    @property
    def wind_speed_80m(self):
        return self._wind_speed_80m

    @wind_speed_80m.setter
    def wind_speed_80m(self, value):
        self._wind_speed_80m = value


    def to_alipay_dict(self):
        params = dict()
        if self.cloud_cover:
            if hasattr(self.cloud_cover, 'to_alipay_dict'):
                params['cloud_cover'] = self.cloud_cover.to_alipay_dict()
            else:
                params['cloud_cover'] = self.cloud_cover
        if self.cloud_cover_high:
            if hasattr(self.cloud_cover_high, 'to_alipay_dict'):
                params['cloud_cover_high'] = self.cloud_cover_high.to_alipay_dict()
            else:
                params['cloud_cover_high'] = self.cloud_cover_high
        if self.cloud_cover_low:
            if hasattr(self.cloud_cover_low, 'to_alipay_dict'):
                params['cloud_cover_low'] = self.cloud_cover_low.to_alipay_dict()
            else:
                params['cloud_cover_low'] = self.cloud_cover_low
        if self.cloud_cover_mid:
            if hasattr(self.cloud_cover_mid, 'to_alipay_dict'):
                params['cloud_cover_mid'] = self.cloud_cover_mid.to_alipay_dict()
            else:
                params['cloud_cover_mid'] = self.cloud_cover_mid
        if self.dew_point_2m:
            if hasattr(self.dew_point_2m, 'to_alipay_dict'):
                params['dew_point_2m'] = self.dew_point_2m.to_alipay_dict()
            else:
                params['dew_point_2m'] = self.dew_point_2m
        if self.diffuse_radiation:
            if hasattr(self.diffuse_radiation, 'to_alipay_dict'):
                params['diffuse_radiation'] = self.diffuse_radiation.to_alipay_dict()
            else:
                params['diffuse_radiation'] = self.diffuse_radiation
        if self.direct_normal_irradiance:
            if hasattr(self.direct_normal_irradiance, 'to_alipay_dict'):
                params['direct_normal_irradiance'] = self.direct_normal_irradiance.to_alipay_dict()
            else:
                params['direct_normal_irradiance'] = self.direct_normal_irradiance
        if self.direct_radiation:
            if hasattr(self.direct_radiation, 'to_alipay_dict'):
                params['direct_radiation'] = self.direct_radiation.to_alipay_dict()
            else:
                params['direct_radiation'] = self.direct_radiation
        if self.precipitation_probability:
            if hasattr(self.precipitation_probability, 'to_alipay_dict'):
                params['precipitation_probability'] = self.precipitation_probability.to_alipay_dict()
            else:
                params['precipitation_probability'] = self.precipitation_probability
        if self.pressure_msl:
            if hasattr(self.pressure_msl, 'to_alipay_dict'):
                params['pressure_msl'] = self.pressure_msl.to_alipay_dict()
            else:
                params['pressure_msl'] = self.pressure_msl
        if self.relative_humidity_2m:
            if hasattr(self.relative_humidity_2m, 'to_alipay_dict'):
                params['relative_humidity_2m'] = self.relative_humidity_2m.to_alipay_dict()
            else:
                params['relative_humidity_2m'] = self.relative_humidity_2m
        if self.shortwave_radiation:
            if hasattr(self.shortwave_radiation, 'to_alipay_dict'):
                params['shortwave_radiation'] = self.shortwave_radiation.to_alipay_dict()
            else:
                params['shortwave_radiation'] = self.shortwave_radiation
        if self.surface_pressure:
            if hasattr(self.surface_pressure, 'to_alipay_dict'):
                params['surface_pressure'] = self.surface_pressure.to_alipay_dict()
            else:
                params['surface_pressure'] = self.surface_pressure
        if self.temperature_2m:
            if hasattr(self.temperature_2m, 'to_alipay_dict'):
                params['temperature_2m'] = self.temperature_2m.to_alipay_dict()
            else:
                params['temperature_2m'] = self.temperature_2m
        if self.wind_direction_10m:
            if hasattr(self.wind_direction_10m, 'to_alipay_dict'):
                params['wind_direction_10m'] = self.wind_direction_10m.to_alipay_dict()
            else:
                params['wind_direction_10m'] = self.wind_direction_10m
        if self.wind_direction_120m:
            if hasattr(self.wind_direction_120m, 'to_alipay_dict'):
                params['wind_direction_120m'] = self.wind_direction_120m.to_alipay_dict()
            else:
                params['wind_direction_120m'] = self.wind_direction_120m
        if self.wind_direction_80m:
            if hasattr(self.wind_direction_80m, 'to_alipay_dict'):
                params['wind_direction_80m'] = self.wind_direction_80m.to_alipay_dict()
            else:
                params['wind_direction_80m'] = self.wind_direction_80m
        if self.wind_speed_10m:
            if hasattr(self.wind_speed_10m, 'to_alipay_dict'):
                params['wind_speed_10m'] = self.wind_speed_10m.to_alipay_dict()
            else:
                params['wind_speed_10m'] = self.wind_speed_10m
        if self.wind_speed_120m:
            if hasattr(self.wind_speed_120m, 'to_alipay_dict'):
                params['wind_speed_120m'] = self.wind_speed_120m.to_alipay_dict()
            else:
                params['wind_speed_120m'] = self.wind_speed_120m
        if self.wind_speed_80m:
            if hasattr(self.wind_speed_80m, 'to_alipay_dict'):
                params['wind_speed_80m'] = self.wind_speed_80m.to_alipay_dict()
            else:
                params['wind_speed_80m'] = self.wind_speed_80m
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WeatherVariablesMark()
        if 'cloud_cover' in d:
            o.cloud_cover = d['cloud_cover']
        if 'cloud_cover_high' in d:
            o.cloud_cover_high = d['cloud_cover_high']
        if 'cloud_cover_low' in d:
            o.cloud_cover_low = d['cloud_cover_low']
        if 'cloud_cover_mid' in d:
            o.cloud_cover_mid = d['cloud_cover_mid']
        if 'dew_point_2m' in d:
            o.dew_point_2m = d['dew_point_2m']
        if 'diffuse_radiation' in d:
            o.diffuse_radiation = d['diffuse_radiation']
        if 'direct_normal_irradiance' in d:
            o.direct_normal_irradiance = d['direct_normal_irradiance']
        if 'direct_radiation' in d:
            o.direct_radiation = d['direct_radiation']
        if 'precipitation_probability' in d:
            o.precipitation_probability = d['precipitation_probability']
        if 'pressure_msl' in d:
            o.pressure_msl = d['pressure_msl']
        if 'relative_humidity_2m' in d:
            o.relative_humidity_2m = d['relative_humidity_2m']
        if 'shortwave_radiation' in d:
            o.shortwave_radiation = d['shortwave_radiation']
        if 'surface_pressure' in d:
            o.surface_pressure = d['surface_pressure']
        if 'temperature_2m' in d:
            o.temperature_2m = d['temperature_2m']
        if 'wind_direction_10m' in d:
            o.wind_direction_10m = d['wind_direction_10m']
        if 'wind_direction_120m' in d:
            o.wind_direction_120m = d['wind_direction_120m']
        if 'wind_direction_80m' in d:
            o.wind_direction_80m = d['wind_direction_80m']
        if 'wind_speed_10m' in d:
            o.wind_speed_10m = d['wind_speed_10m']
        if 'wind_speed_120m' in d:
            o.wind_speed_120m = d['wind_speed_120m']
        if 'wind_speed_80m' in d:
            o.wind_speed_80m = d['wind_speed_80m']
        return o


