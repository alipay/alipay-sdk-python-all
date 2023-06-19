#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataMdaTorchreplayuvQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataMdaTorchreplayuvQueryResponse, self).__init__()
        self._today_uv = None
        self._today_uv_trend = None
        self._total_uv = None

    @property
    def today_uv(self):
        return self._today_uv

    @today_uv.setter
    def today_uv(self, value):
        self._today_uv = value
    @property
    def today_uv_trend(self):
        return self._today_uv_trend

    @today_uv_trend.setter
    def today_uv_trend(self, value):
        self._today_uv_trend = value
    @property
    def total_uv(self):
        return self._total_uv

    @total_uv.setter
    def total_uv(self, value):
        self._total_uv = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataMdaTorchreplayuvQueryResponse, self).parse_response_content(response_content)
        if 'today_uv' in response:
            self.today_uv = response['today_uv']
        if 'today_uv_trend' in response:
            self.today_uv_trend = response['today_uv_trend']
        if 'total_uv' in response:
            self.total_uv = response['total_uv']
