#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LongRangeWeatherVariables import LongRangeWeatherVariables


class DatadigitalAnttechWeatherLongrangeQueryResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalAnttechWeatherLongrangeQueryResponse, self).__init__()
        self._forecast_batch_time = None
        self._weather_variables_list = None

    @property
    def forecast_batch_time(self):
        return self._forecast_batch_time

    @forecast_batch_time.setter
    def forecast_batch_time(self, value):
        self._forecast_batch_time = value
    @property
    def weather_variables_list(self):
        return self._weather_variables_list

    @weather_variables_list.setter
    def weather_variables_list(self, value):
        if isinstance(value, list):
            self._weather_variables_list = list()
            for i in value:
                if isinstance(i, LongRangeWeatherVariables):
                    self._weather_variables_list.append(i)
                else:
                    self._weather_variables_list.append(LongRangeWeatherVariables.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(DatadigitalAnttechWeatherLongrangeQueryResponse, self).parse_response_content(response_content)
        if 'forecast_batch_time' in response:
            self.forecast_batch_time = response['forecast_batch_time']
        if 'weather_variables_list' in response:
            self.weather_variables_list = response['weather_variables_list']
