#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataMdaWelfareagrealtimeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataMdaWelfareagrealtimeQueryResponse, self).__init__()
        self._total_donate = None
        self._total_obtain = None

    @property
    def total_donate(self):
        return self._total_donate

    @total_donate.setter
    def total_donate(self, value):
        self._total_donate = value
    @property
    def total_obtain(self):
        return self._total_obtain

    @total_obtain.setter
    def total_obtain(self, value):
        self._total_obtain = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataMdaWelfareagrealtimeQueryResponse, self).parse_response_content(response_content)
        if 'total_donate' in response:
            self.total_donate = response['total_donate']
        if 'total_obtain' in response:
            self.total_obtain = response['total_obtain']
