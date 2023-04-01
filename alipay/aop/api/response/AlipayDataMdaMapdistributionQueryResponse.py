#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataMdaMapdistributionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataMdaMapdistributionQueryResponse, self).__init__()
        self._city_uv = None
        self._country_uv = None

    @property
    def city_uv(self):
        return self._city_uv

    @city_uv.setter
    def city_uv(self, value):
        self._city_uv = value
    @property
    def country_uv(self):
        return self._country_uv

    @country_uv.setter
    def country_uv(self, value):
        self._country_uv = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataMdaMapdistributionQueryResponse, self).parse_response_content(response_content)
        if 'city_uv' in response:
            self.city_uv = response['city_uv']
        if 'country_uv' in response:
            self.country_uv = response['country_uv']
