#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataMdaTorchrelayofflineQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataMdaTorchrelayofflineQueryResponse, self).__init__()
        self._top_5_country = None
        self._total_pv = None
        self._total_uv = None

    @property
    def top_5_country(self):
        return self._top_5_country

    @top_5_country.setter
    def top_5_country(self, value):
        self._top_5_country = value
    @property
    def total_pv(self):
        return self._total_pv

    @total_pv.setter
    def total_pv(self, value):
        self._total_pv = value
    @property
    def total_uv(self):
        return self._total_uv

    @total_uv.setter
    def total_uv(self, value):
        self._total_uv = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataMdaTorchrelayofflineQueryResponse, self).parse_response_content(response_content)
        if 'top_5_country' in response:
            self.top_5_country = response['top_5_country']
        if 'total_pv' in response:
            self.total_pv = response['total_pv']
        if 'total_uv' in response:
            self.total_uv = response['total_uv']
