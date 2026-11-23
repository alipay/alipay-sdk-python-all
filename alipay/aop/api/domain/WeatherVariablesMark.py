#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WeatherVariablesMark(object):

    def __init__(self):
        self._apparent_temperature = None
        self._cloud_cover = None
        self._cloud_cover_high = None
        self._cloud_cover_low = None
        self._cloud_cover_mid = None
        self._dew_point_2m = None
        self._diffuse_radiation = None
        self._diffuse_radiation_instant = None
        self._diffuse_radiation_mean = None
        self._direct_normal_irradiance = None
        self._direct_normal_irradiance_instant = None
        self._direct_radiation = None
        self._direct_radiation_instant = None
        self._direct_radiation_mean = None
        self._precipitation = None
        self._precipitation_probability = None
        self._pressure_msl = None
        self._rain = None
        self._relative_humidity_2m = None
        self._short_term_rain = None
        self._shortwave_radiation = None
        self._shortwave_radiation_instant = None
        self._shortwave_radiation_mean = None
        self._snowfall = None
        self._soil_moisture_0_to_10 = None
        self._soil_moisture_0_to_5 = None
        self._soil_moisture_100_to_200 = None
        self._soil_moisture_10_to_40 = None
        self._soil_moisture_40_to_100 = None
        self._soil_temperature_10 = None
        self._soil_temperature_100 = None
        self._soil_temperature_200 = None
        self._soil_temperature_40 = None
        self._soil_temperature_5 = None
        self._surface_pressure = None
        self._temperature_2m = None
        self._u_wind_100m = None
        self._u_wind_10m = None
        self._u_wind_120m = None
        self._u_wind_180m = None
        self._u_wind_80m = None
        self._v_wind_100m = None
        self._v_wind_10m = None
        self._v_wind_120m = None
        self._v_wind_180m = None
        self._v_wind_80m = None
        self._weather_code = None
        self._weather_type_code = None
        self._wind_direction_100m = None
        self._wind_direction_10m = None
        self._wind_direction_120m = None
        self._wind_direction_180m = None
        self._wind_direction_80m = None
        self._wind_gusts_10m = None
        self._wind_speed_100m = None
        self._wind_speed_10m = None
        self._wind_speed_120m = None
        self._wind_speed_180m = None
        self._wind_speed_80m = None

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
    def diffuse_radiation_instant(self):
        return self._diffuse_radiation_instant

    @diffuse_radiation_instant.setter
    def diffuse_radiation_instant(self, value):
        self._diffuse_radiation_instant = value
    @property
    def diffuse_radiation_mean(self):
        return self._diffuse_radiation_mean

    @diffuse_radiation_mean.setter
    def diffuse_radiation_mean(self, value):
        self._diffuse_radiation_mean = value
    @property
    def direct_normal_irradiance(self):
        return self._direct_normal_irradiance

    @direct_normal_irradiance.setter
    def direct_normal_irradiance(self, value):
        self._direct_normal_irradiance = value
    @property
    def direct_normal_irradiance_instant(self):
        return self._direct_normal_irradiance_instant

    @direct_normal_irradiance_instant.setter
    def direct_normal_irradiance_instant(self, value):
        self._direct_normal_irradiance_instant = value
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
    def direct_radiation_mean(self):
        return self._direct_radiation_mean

    @direct_radiation_mean.setter
    def direct_radiation_mean(self, value):
        self._direct_radiation_mean = value
    @property
    def precipitation(self):
        return self._precipitation

    @precipitation.setter
    def precipitation(self, value):
        self._precipitation = value
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
    def rain(self):
        return self._rain

    @rain.setter
    def rain(self, value):
        self._rain = value
    @property
    def relative_humidity_2m(self):
        return self._relative_humidity_2m

    @relative_humidity_2m.setter
    def relative_humidity_2m(self, value):
        self._relative_humidity_2m = value
    @property
    def short_term_rain(self):
        return self._short_term_rain

    @short_term_rain.setter
    def short_term_rain(self, value):
        self._short_term_rain = value
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
    def shortwave_radiation_mean(self):
        return self._shortwave_radiation_mean

    @shortwave_radiation_mean.setter
    def shortwave_radiation_mean(self, value):
        self._shortwave_radiation_mean = value
    @property
    def snowfall(self):
        return self._snowfall

    @snowfall.setter
    def snowfall(self, value):
        self._snowfall = value
    @property
    def soil_moisture_0_to_10(self):
        return self._soil_moisture_0_to_10

    @soil_moisture_0_to_10.setter
    def soil_moisture_0_to_10(self, value):
        self._soil_moisture_0_to_10 = value
    @property
    def soil_moisture_0_to_5(self):
        return self._soil_moisture_0_to_5

    @soil_moisture_0_to_5.setter
    def soil_moisture_0_to_5(self, value):
        self._soil_moisture_0_to_5 = value
    @property
    def soil_moisture_100_to_200(self):
        return self._soil_moisture_100_to_200

    @soil_moisture_100_to_200.setter
    def soil_moisture_100_to_200(self, value):
        self._soil_moisture_100_to_200 = value
    @property
    def soil_moisture_10_to_40(self):
        return self._soil_moisture_10_to_40

    @soil_moisture_10_to_40.setter
    def soil_moisture_10_to_40(self, value):
        self._soil_moisture_10_to_40 = value
    @property
    def soil_moisture_40_to_100(self):
        return self._soil_moisture_40_to_100

    @soil_moisture_40_to_100.setter
    def soil_moisture_40_to_100(self, value):
        self._soil_moisture_40_to_100 = value
    @property
    def soil_temperature_10(self):
        return self._soil_temperature_10

    @soil_temperature_10.setter
    def soil_temperature_10(self, value):
        self._soil_temperature_10 = value
    @property
    def soil_temperature_100(self):
        return self._soil_temperature_100

    @soil_temperature_100.setter
    def soil_temperature_100(self, value):
        self._soil_temperature_100 = value
    @property
    def soil_temperature_200(self):
        return self._soil_temperature_200

    @soil_temperature_200.setter
    def soil_temperature_200(self, value):
        self._soil_temperature_200 = value
    @property
    def soil_temperature_40(self):
        return self._soil_temperature_40

    @soil_temperature_40.setter
    def soil_temperature_40(self, value):
        self._soil_temperature_40 = value
    @property
    def soil_temperature_5(self):
        return self._soil_temperature_5

    @soil_temperature_5.setter
    def soil_temperature_5(self, value):
        self._soil_temperature_5 = value
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
    def u_wind_100m(self):
        return self._u_wind_100m

    @u_wind_100m.setter
    def u_wind_100m(self, value):
        self._u_wind_100m = value
    @property
    def u_wind_10m(self):
        return self._u_wind_10m

    @u_wind_10m.setter
    def u_wind_10m(self, value):
        self._u_wind_10m = value
    @property
    def u_wind_120m(self):
        return self._u_wind_120m

    @u_wind_120m.setter
    def u_wind_120m(self, value):
        self._u_wind_120m = value
    @property
    def u_wind_180m(self):
        return self._u_wind_180m

    @u_wind_180m.setter
    def u_wind_180m(self, value):
        self._u_wind_180m = value
    @property
    def u_wind_80m(self):
        return self._u_wind_80m

    @u_wind_80m.setter
    def u_wind_80m(self, value):
        self._u_wind_80m = value
    @property
    def v_wind_100m(self):
        return self._v_wind_100m

    @v_wind_100m.setter
    def v_wind_100m(self, value):
        self._v_wind_100m = value
    @property
    def v_wind_10m(self):
        return self._v_wind_10m

    @v_wind_10m.setter
    def v_wind_10m(self, value):
        self._v_wind_10m = value
    @property
    def v_wind_120m(self):
        return self._v_wind_120m

    @v_wind_120m.setter
    def v_wind_120m(self, value):
        self._v_wind_120m = value
    @property
    def v_wind_180m(self):
        return self._v_wind_180m

    @v_wind_180m.setter
    def v_wind_180m(self, value):
        self._v_wind_180m = value
    @property
    def v_wind_80m(self):
        return self._v_wind_80m

    @v_wind_80m.setter
    def v_wind_80m(self, value):
        self._v_wind_80m = value
    @property
    def weather_code(self):
        return self._weather_code

    @weather_code.setter
    def weather_code(self, value):
        self._weather_code = value
    @property
    def weather_type_code(self):
        return self._weather_type_code

    @weather_type_code.setter
    def weather_type_code(self, value):
        self._weather_type_code = value
    @property
    def wind_direction_100m(self):
        return self._wind_direction_100m

    @wind_direction_100m.setter
    def wind_direction_100m(self, value):
        self._wind_direction_100m = value
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
    def wind_direction_180m(self):
        return self._wind_direction_180m

    @wind_direction_180m.setter
    def wind_direction_180m(self, value):
        self._wind_direction_180m = value
    @property
    def wind_direction_80m(self):
        return self._wind_direction_80m

    @wind_direction_80m.setter
    def wind_direction_80m(self, value):
        self._wind_direction_80m = value
    @property
    def wind_gusts_10m(self):
        return self._wind_gusts_10m

    @wind_gusts_10m.setter
    def wind_gusts_10m(self, value):
        self._wind_gusts_10m = value
    @property
    def wind_speed_100m(self):
        return self._wind_speed_100m

    @wind_speed_100m.setter
    def wind_speed_100m(self, value):
        self._wind_speed_100m = value
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
    def wind_speed_180m(self):
        return self._wind_speed_180m

    @wind_speed_180m.setter
    def wind_speed_180m(self, value):
        self._wind_speed_180m = value
    @property
    def wind_speed_80m(self):
        return self._wind_speed_80m

    @wind_speed_80m.setter
    def wind_speed_80m(self, value):
        self._wind_speed_80m = value


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
        if self.diffuse_radiation_instant:
            if hasattr(self.diffuse_radiation_instant, 'to_alipay_dict'):
                params['diffuse_radiation_instant'] = self.diffuse_radiation_instant.to_alipay_dict()
            else:
                params['diffuse_radiation_instant'] = self.diffuse_radiation_instant
        if self.diffuse_radiation_mean:
            if hasattr(self.diffuse_radiation_mean, 'to_alipay_dict'):
                params['diffuse_radiation_mean'] = self.diffuse_radiation_mean.to_alipay_dict()
            else:
                params['diffuse_radiation_mean'] = self.diffuse_radiation_mean
        if self.direct_normal_irradiance:
            if hasattr(self.direct_normal_irradiance, 'to_alipay_dict'):
                params['direct_normal_irradiance'] = self.direct_normal_irradiance.to_alipay_dict()
            else:
                params['direct_normal_irradiance'] = self.direct_normal_irradiance
        if self.direct_normal_irradiance_instant:
            if hasattr(self.direct_normal_irradiance_instant, 'to_alipay_dict'):
                params['direct_normal_irradiance_instant'] = self.direct_normal_irradiance_instant.to_alipay_dict()
            else:
                params['direct_normal_irradiance_instant'] = self.direct_normal_irradiance_instant
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
        if self.direct_radiation_mean:
            if hasattr(self.direct_radiation_mean, 'to_alipay_dict'):
                params['direct_radiation_mean'] = self.direct_radiation_mean.to_alipay_dict()
            else:
                params['direct_radiation_mean'] = self.direct_radiation_mean
        if self.precipitation:
            if hasattr(self.precipitation, 'to_alipay_dict'):
                params['precipitation'] = self.precipitation.to_alipay_dict()
            else:
                params['precipitation'] = self.precipitation
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
        if self.rain:
            if hasattr(self.rain, 'to_alipay_dict'):
                params['rain'] = self.rain.to_alipay_dict()
            else:
                params['rain'] = self.rain
        if self.relative_humidity_2m:
            if hasattr(self.relative_humidity_2m, 'to_alipay_dict'):
                params['relative_humidity_2m'] = self.relative_humidity_2m.to_alipay_dict()
            else:
                params['relative_humidity_2m'] = self.relative_humidity_2m
        if self.short_term_rain:
            if hasattr(self.short_term_rain, 'to_alipay_dict'):
                params['short_term_rain'] = self.short_term_rain.to_alipay_dict()
            else:
                params['short_term_rain'] = self.short_term_rain
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
        if self.shortwave_radiation_mean:
            if hasattr(self.shortwave_radiation_mean, 'to_alipay_dict'):
                params['shortwave_radiation_mean'] = self.shortwave_radiation_mean.to_alipay_dict()
            else:
                params['shortwave_radiation_mean'] = self.shortwave_radiation_mean
        if self.snowfall:
            if hasattr(self.snowfall, 'to_alipay_dict'):
                params['snowfall'] = self.snowfall.to_alipay_dict()
            else:
                params['snowfall'] = self.snowfall
        if self.soil_moisture_0_to_10:
            if hasattr(self.soil_moisture_0_to_10, 'to_alipay_dict'):
                params['soil_moisture_0_to_10'] = self.soil_moisture_0_to_10.to_alipay_dict()
            else:
                params['soil_moisture_0_to_10'] = self.soil_moisture_0_to_10
        if self.soil_moisture_0_to_5:
            if hasattr(self.soil_moisture_0_to_5, 'to_alipay_dict'):
                params['soil_moisture_0_to_5'] = self.soil_moisture_0_to_5.to_alipay_dict()
            else:
                params['soil_moisture_0_to_5'] = self.soil_moisture_0_to_5
        if self.soil_moisture_100_to_200:
            if hasattr(self.soil_moisture_100_to_200, 'to_alipay_dict'):
                params['soil_moisture_100_to_200'] = self.soil_moisture_100_to_200.to_alipay_dict()
            else:
                params['soil_moisture_100_to_200'] = self.soil_moisture_100_to_200
        if self.soil_moisture_10_to_40:
            if hasattr(self.soil_moisture_10_to_40, 'to_alipay_dict'):
                params['soil_moisture_10_to_40'] = self.soil_moisture_10_to_40.to_alipay_dict()
            else:
                params['soil_moisture_10_to_40'] = self.soil_moisture_10_to_40
        if self.soil_moisture_40_to_100:
            if hasattr(self.soil_moisture_40_to_100, 'to_alipay_dict'):
                params['soil_moisture_40_to_100'] = self.soil_moisture_40_to_100.to_alipay_dict()
            else:
                params['soil_moisture_40_to_100'] = self.soil_moisture_40_to_100
        if self.soil_temperature_10:
            if hasattr(self.soil_temperature_10, 'to_alipay_dict'):
                params['soil_temperature_10'] = self.soil_temperature_10.to_alipay_dict()
            else:
                params['soil_temperature_10'] = self.soil_temperature_10
        if self.soil_temperature_100:
            if hasattr(self.soil_temperature_100, 'to_alipay_dict'):
                params['soil_temperature_100'] = self.soil_temperature_100.to_alipay_dict()
            else:
                params['soil_temperature_100'] = self.soil_temperature_100
        if self.soil_temperature_200:
            if hasattr(self.soil_temperature_200, 'to_alipay_dict'):
                params['soil_temperature_200'] = self.soil_temperature_200.to_alipay_dict()
            else:
                params['soil_temperature_200'] = self.soil_temperature_200
        if self.soil_temperature_40:
            if hasattr(self.soil_temperature_40, 'to_alipay_dict'):
                params['soil_temperature_40'] = self.soil_temperature_40.to_alipay_dict()
            else:
                params['soil_temperature_40'] = self.soil_temperature_40
        if self.soil_temperature_5:
            if hasattr(self.soil_temperature_5, 'to_alipay_dict'):
                params['soil_temperature_5'] = self.soil_temperature_5.to_alipay_dict()
            else:
                params['soil_temperature_5'] = self.soil_temperature_5
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
        if self.u_wind_100m:
            if hasattr(self.u_wind_100m, 'to_alipay_dict'):
                params['u_wind_100m'] = self.u_wind_100m.to_alipay_dict()
            else:
                params['u_wind_100m'] = self.u_wind_100m
        if self.u_wind_10m:
            if hasattr(self.u_wind_10m, 'to_alipay_dict'):
                params['u_wind_10m'] = self.u_wind_10m.to_alipay_dict()
            else:
                params['u_wind_10m'] = self.u_wind_10m
        if self.u_wind_120m:
            if hasattr(self.u_wind_120m, 'to_alipay_dict'):
                params['u_wind_120m'] = self.u_wind_120m.to_alipay_dict()
            else:
                params['u_wind_120m'] = self.u_wind_120m
        if self.u_wind_180m:
            if hasattr(self.u_wind_180m, 'to_alipay_dict'):
                params['u_wind_180m'] = self.u_wind_180m.to_alipay_dict()
            else:
                params['u_wind_180m'] = self.u_wind_180m
        if self.u_wind_80m:
            if hasattr(self.u_wind_80m, 'to_alipay_dict'):
                params['u_wind_80m'] = self.u_wind_80m.to_alipay_dict()
            else:
                params['u_wind_80m'] = self.u_wind_80m
        if self.v_wind_100m:
            if hasattr(self.v_wind_100m, 'to_alipay_dict'):
                params['v_wind_100m'] = self.v_wind_100m.to_alipay_dict()
            else:
                params['v_wind_100m'] = self.v_wind_100m
        if self.v_wind_10m:
            if hasattr(self.v_wind_10m, 'to_alipay_dict'):
                params['v_wind_10m'] = self.v_wind_10m.to_alipay_dict()
            else:
                params['v_wind_10m'] = self.v_wind_10m
        if self.v_wind_120m:
            if hasattr(self.v_wind_120m, 'to_alipay_dict'):
                params['v_wind_120m'] = self.v_wind_120m.to_alipay_dict()
            else:
                params['v_wind_120m'] = self.v_wind_120m
        if self.v_wind_180m:
            if hasattr(self.v_wind_180m, 'to_alipay_dict'):
                params['v_wind_180m'] = self.v_wind_180m.to_alipay_dict()
            else:
                params['v_wind_180m'] = self.v_wind_180m
        if self.v_wind_80m:
            if hasattr(self.v_wind_80m, 'to_alipay_dict'):
                params['v_wind_80m'] = self.v_wind_80m.to_alipay_dict()
            else:
                params['v_wind_80m'] = self.v_wind_80m
        if self.weather_code:
            if hasattr(self.weather_code, 'to_alipay_dict'):
                params['weather_code'] = self.weather_code.to_alipay_dict()
            else:
                params['weather_code'] = self.weather_code
        if self.weather_type_code:
            if hasattr(self.weather_type_code, 'to_alipay_dict'):
                params['weather_type_code'] = self.weather_type_code.to_alipay_dict()
            else:
                params['weather_type_code'] = self.weather_type_code
        if self.wind_direction_100m:
            if hasattr(self.wind_direction_100m, 'to_alipay_dict'):
                params['wind_direction_100m'] = self.wind_direction_100m.to_alipay_dict()
            else:
                params['wind_direction_100m'] = self.wind_direction_100m
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
        if self.wind_direction_180m:
            if hasattr(self.wind_direction_180m, 'to_alipay_dict'):
                params['wind_direction_180m'] = self.wind_direction_180m.to_alipay_dict()
            else:
                params['wind_direction_180m'] = self.wind_direction_180m
        if self.wind_direction_80m:
            if hasattr(self.wind_direction_80m, 'to_alipay_dict'):
                params['wind_direction_80m'] = self.wind_direction_80m.to_alipay_dict()
            else:
                params['wind_direction_80m'] = self.wind_direction_80m
        if self.wind_gusts_10m:
            if hasattr(self.wind_gusts_10m, 'to_alipay_dict'):
                params['wind_gusts_10m'] = self.wind_gusts_10m.to_alipay_dict()
            else:
                params['wind_gusts_10m'] = self.wind_gusts_10m
        if self.wind_speed_100m:
            if hasattr(self.wind_speed_100m, 'to_alipay_dict'):
                params['wind_speed_100m'] = self.wind_speed_100m.to_alipay_dict()
            else:
                params['wind_speed_100m'] = self.wind_speed_100m
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
        if self.wind_speed_180m:
            if hasattr(self.wind_speed_180m, 'to_alipay_dict'):
                params['wind_speed_180m'] = self.wind_speed_180m.to_alipay_dict()
            else:
                params['wind_speed_180m'] = self.wind_speed_180m
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
        if 'apparent_temperature' in d:
            o.apparent_temperature = d['apparent_temperature']
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
        if 'diffuse_radiation_instant' in d:
            o.diffuse_radiation_instant = d['diffuse_radiation_instant']
        if 'diffuse_radiation_mean' in d:
            o.diffuse_radiation_mean = d['diffuse_radiation_mean']
        if 'direct_normal_irradiance' in d:
            o.direct_normal_irradiance = d['direct_normal_irradiance']
        if 'direct_normal_irradiance_instant' in d:
            o.direct_normal_irradiance_instant = d['direct_normal_irradiance_instant']
        if 'direct_radiation' in d:
            o.direct_radiation = d['direct_radiation']
        if 'direct_radiation_instant' in d:
            o.direct_radiation_instant = d['direct_radiation_instant']
        if 'direct_radiation_mean' in d:
            o.direct_radiation_mean = d['direct_radiation_mean']
        if 'precipitation' in d:
            o.precipitation = d['precipitation']
        if 'precipitation_probability' in d:
            o.precipitation_probability = d['precipitation_probability']
        if 'pressure_msl' in d:
            o.pressure_msl = d['pressure_msl']
        if 'rain' in d:
            o.rain = d['rain']
        if 'relative_humidity_2m' in d:
            o.relative_humidity_2m = d['relative_humidity_2m']
        if 'short_term_rain' in d:
            o.short_term_rain = d['short_term_rain']
        if 'shortwave_radiation' in d:
            o.shortwave_radiation = d['shortwave_radiation']
        if 'shortwave_radiation_instant' in d:
            o.shortwave_radiation_instant = d['shortwave_radiation_instant']
        if 'shortwave_radiation_mean' in d:
            o.shortwave_radiation_mean = d['shortwave_radiation_mean']
        if 'snowfall' in d:
            o.snowfall = d['snowfall']
        if 'soil_moisture_0_to_10' in d:
            o.soil_moisture_0_to_10 = d['soil_moisture_0_to_10']
        if 'soil_moisture_0_to_5' in d:
            o.soil_moisture_0_to_5 = d['soil_moisture_0_to_5']
        if 'soil_moisture_100_to_200' in d:
            o.soil_moisture_100_to_200 = d['soil_moisture_100_to_200']
        if 'soil_moisture_10_to_40' in d:
            o.soil_moisture_10_to_40 = d['soil_moisture_10_to_40']
        if 'soil_moisture_40_to_100' in d:
            o.soil_moisture_40_to_100 = d['soil_moisture_40_to_100']
        if 'soil_temperature_10' in d:
            o.soil_temperature_10 = d['soil_temperature_10']
        if 'soil_temperature_100' in d:
            o.soil_temperature_100 = d['soil_temperature_100']
        if 'soil_temperature_200' in d:
            o.soil_temperature_200 = d['soil_temperature_200']
        if 'soil_temperature_40' in d:
            o.soil_temperature_40 = d['soil_temperature_40']
        if 'soil_temperature_5' in d:
            o.soil_temperature_5 = d['soil_temperature_5']
        if 'surface_pressure' in d:
            o.surface_pressure = d['surface_pressure']
        if 'temperature_2m' in d:
            o.temperature_2m = d['temperature_2m']
        if 'u_wind_100m' in d:
            o.u_wind_100m = d['u_wind_100m']
        if 'u_wind_10m' in d:
            o.u_wind_10m = d['u_wind_10m']
        if 'u_wind_120m' in d:
            o.u_wind_120m = d['u_wind_120m']
        if 'u_wind_180m' in d:
            o.u_wind_180m = d['u_wind_180m']
        if 'u_wind_80m' in d:
            o.u_wind_80m = d['u_wind_80m']
        if 'v_wind_100m' in d:
            o.v_wind_100m = d['v_wind_100m']
        if 'v_wind_10m' in d:
            o.v_wind_10m = d['v_wind_10m']
        if 'v_wind_120m' in d:
            o.v_wind_120m = d['v_wind_120m']
        if 'v_wind_180m' in d:
            o.v_wind_180m = d['v_wind_180m']
        if 'v_wind_80m' in d:
            o.v_wind_80m = d['v_wind_80m']
        if 'weather_code' in d:
            o.weather_code = d['weather_code']
        if 'weather_type_code' in d:
            o.weather_type_code = d['weather_type_code']
        if 'wind_direction_100m' in d:
            o.wind_direction_100m = d['wind_direction_100m']
        if 'wind_direction_10m' in d:
            o.wind_direction_10m = d['wind_direction_10m']
        if 'wind_direction_120m' in d:
            o.wind_direction_120m = d['wind_direction_120m']
        if 'wind_direction_180m' in d:
            o.wind_direction_180m = d['wind_direction_180m']
        if 'wind_direction_80m' in d:
            o.wind_direction_80m = d['wind_direction_80m']
        if 'wind_gusts_10m' in d:
            o.wind_gusts_10m = d['wind_gusts_10m']
        if 'wind_speed_100m' in d:
            o.wind_speed_100m = d['wind_speed_100m']
        if 'wind_speed_10m' in d:
            o.wind_speed_10m = d['wind_speed_10m']
        if 'wind_speed_120m' in d:
            o.wind_speed_120m = d['wind_speed_120m']
        if 'wind_speed_180m' in d:
            o.wind_speed_180m = d['wind_speed_180m']
        if 'wind_speed_80m' in d:
            o.wind_speed_80m = d['wind_speed_80m']
        return o


