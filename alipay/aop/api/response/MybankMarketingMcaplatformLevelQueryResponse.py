#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankMarketingMcaplatformLevelQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankMarketingMcaplatformLevelQueryResponse, self).__init__()
        self._green_level = None
        self._growth_value = None

    @property
    def green_level(self):
        return self._green_level

    @green_level.setter
    def green_level(self, value):
        self._green_level = value
    @property
    def growth_value(self):
        return self._growth_value

    @growth_value.setter
    def growth_value(self, value):
        self._growth_value = value

    def parse_response_content(self, response_content):
        response = super(MybankMarketingMcaplatformLevelQueryResponse, self).parse_response_content(response_content)
        if 'green_level' in response:
            self.green_level = response['green_level']
        if 'growth_value' in response:
            self.growth_value = response['growth_value']
