#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.WeatherShortTermRainDTO import WeatherShortTermRainDTO


class DatadigitalAnttechWeatherShorttermQueryResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalAnttechWeatherShorttermQueryResponse, self).__init__()
        self._short_term_rains = None

    @property
    def short_term_rains(self):
        return self._short_term_rains

    @short_term_rains.setter
    def short_term_rains(self, value):
        if isinstance(value, list):
            self._short_term_rains = list()
            for i in value:
                if isinstance(i, WeatherShortTermRainDTO):
                    self._short_term_rains.append(i)
                else:
                    self._short_term_rains.append(WeatherShortTermRainDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(DatadigitalAnttechWeatherShorttermQueryResponse, self).parse_response_content(response_content)
        if 'short_term_rains' in response:
            self.short_term_rains = response['short_term_rains']
