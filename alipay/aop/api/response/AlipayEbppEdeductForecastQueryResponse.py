#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppEdeductForecastQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppEdeductForecastQueryResponse, self).__init__()
        self._forecast_expect = None

    @property
    def forecast_expect(self):
        return self._forecast_expect

    @forecast_expect.setter
    def forecast_expect(self, value):
        self._forecast_expect = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppEdeductForecastQueryResponse, self).parse_response_content(response_content)
        if 'forecast_expect' in response:
            self.forecast_expect = response['forecast_expect']
