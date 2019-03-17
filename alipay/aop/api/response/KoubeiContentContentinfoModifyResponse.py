#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiContentContentinfoModifyResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiContentContentinfoModifyResponse, self).__init__()
        self._data = None
        self._trace_id = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiContentContentinfoModifyResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']
