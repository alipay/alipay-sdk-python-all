#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.WeatherAlertDTO import WeatherAlertDTO


class DatadigitalAnttechWeatherAlertQueryResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalAnttechWeatherAlertQueryResponse, self).__init__()
        self._alerts = None

    @property
    def alerts(self):
        return self._alerts

    @alerts.setter
    def alerts(self, value):
        if isinstance(value, list):
            self._alerts = list()
            for i in value:
                if isinstance(i, WeatherAlertDTO):
                    self._alerts.append(i)
                else:
                    self._alerts.append(WeatherAlertDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(DatadigitalAnttechWeatherAlertQueryResponse, self).parse_response_content(response_content)
        if 'alerts' in response:
            self.alerts = response['alerts']
