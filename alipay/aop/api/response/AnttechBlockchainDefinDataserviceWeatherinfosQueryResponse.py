#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.WeatherInfo import WeatherInfo


class AnttechBlockchainDefinDataserviceWeatherinfosQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainDefinDataserviceWeatherinfosQueryResponse, self).__init__()
        self._weather_infos = None

    @property
    def weather_infos(self):
        return self._weather_infos

    @weather_infos.setter
    def weather_infos(self, value):
        if isinstance(value, list):
            self._weather_infos = list()
            for i in value:
                if isinstance(i, WeatherInfo):
                    self._weather_infos.append(i)
                else:
                    self._weather_infos.append(WeatherInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainDefinDataserviceWeatherinfosQueryResponse, self).parse_response_content(response_content)
        if 'weather_infos' in response:
            self.weather_infos = response['weather_infos']
