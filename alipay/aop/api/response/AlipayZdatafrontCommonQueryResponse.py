#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayZdatafrontCommonQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayZdatafrontCommonQueryResponse, self).__init__()
        self._cache_timestamp = None
        self._values = None

    @property
    def cache_timestamp(self):
        return self._cache_timestamp

    @cache_timestamp.setter
    def cache_timestamp(self, value):
        self._cache_timestamp = value
    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, value):
        self._values = value

    def parse_response_content(self, response_content):
        response = super(AlipayZdatafrontCommonQueryResponse, self).parse_response_content(response_content)
        if 'cache_timestamp' in response:
            self.cache_timestamp = response['cache_timestamp']
        if 'values' in response:
            self.values = response['values']
