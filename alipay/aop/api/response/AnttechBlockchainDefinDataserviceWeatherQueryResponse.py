#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainDefinDataserviceWeatherQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainDefinDataserviceWeatherQueryResponse, self).__init__()
        self._forecast_date = None
        self._humidity = None
        self._precipitation = None
        self._temperature = None
        self._weather_desc = None
        self._wind_speed = None

    @property
    def forecast_date(self):
        return self._forecast_date

    @forecast_date.setter
    def forecast_date(self, value):
        self._forecast_date = value
    @property
    def humidity(self):
        return self._humidity

    @humidity.setter
    def humidity(self, value):
        self._humidity = value
    @property
    def precipitation(self):
        return self._precipitation

    @precipitation.setter
    def precipitation(self, value):
        self._precipitation = value
    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value
    @property
    def weather_desc(self):
        return self._weather_desc

    @weather_desc.setter
    def weather_desc(self, value):
        self._weather_desc = value
    @property
    def wind_speed(self):
        return self._wind_speed

    @wind_speed.setter
    def wind_speed(self, value):
        self._wind_speed = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainDefinDataserviceWeatherQueryResponse, self).parse_response_content(response_content)
        if 'forecast_date' in response:
            self.forecast_date = response['forecast_date']
        if 'humidity' in response:
            self.humidity = response['humidity']
        if 'precipitation' in response:
            self.precipitation = response['precipitation']
        if 'temperature' in response:
            self.temperature = response['temperature']
        if 'weather_desc' in response:
            self.weather_desc = response['weather_desc']
        if 'wind_speed' in response:
            self.wind_speed = response['wind_speed']
