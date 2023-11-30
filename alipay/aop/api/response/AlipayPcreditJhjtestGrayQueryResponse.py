#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditJhjtestGrayQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditJhjtestGrayQueryResponse, self).__init__()
        self._out_a = None

    @property
    def out_a(self):
        return self._out_a

    @out_a.setter
    def out_a(self, value):
        self._out_a = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditJhjtestGrayQueryResponse, self).parse_response_content(response_content)
        if 'out_a' in response:
            self.out_a = response['out_a']
