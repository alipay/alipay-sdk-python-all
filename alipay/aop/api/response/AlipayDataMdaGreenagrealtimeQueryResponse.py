#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataMdaGreenagrealtimeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataMdaGreenagrealtimeQueryResponse, self).__init__()
        self._completed = None
        self._dau = None

    @property
    def completed(self):
        return self._completed

    @completed.setter
    def completed(self, value):
        self._completed = value
    @property
    def dau(self):
        return self._dau

    @dau.setter
    def dau(self, value):
        self._dau = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataMdaGreenagrealtimeQueryResponse, self).parse_response_content(response_content)
        if 'completed' in response:
            self.completed = response['completed']
        if 'dau' in response:
            self.dau = response['dau']
