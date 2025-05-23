#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.WeatherVariables import WeatherVariables


class DatadigitalAnttechWeatherFutureQueryResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalAnttechWeatherFutureQueryResponse, self).__init__()
        self._quota_cost = None
        self._weather_variables_list = None

    @property
    def quota_cost(self):
        return self._quota_cost

    @quota_cost.setter
    def quota_cost(self, value):
        self._quota_cost = value
    @property
    def weather_variables_list(self):
        return self._weather_variables_list

    @weather_variables_list.setter
    def weather_variables_list(self, value):
        if isinstance(value, list):
            self._weather_variables_list = list()
            for i in value:
                if isinstance(i, WeatherVariables):
                    self._weather_variables_list.append(i)
                else:
                    self._weather_variables_list.append(WeatherVariables.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(DatadigitalAnttechWeatherFutureQueryResponse, self).parse_response_content(response_content)
        if 'quota_cost' in response:
            self.quota_cost = response['quota_cost']
        if 'weather_variables_list' in response:
            self.weather_variables_list = response['weather_variables_list']
