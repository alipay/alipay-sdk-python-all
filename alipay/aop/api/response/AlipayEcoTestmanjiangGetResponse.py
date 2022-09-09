#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoTestmanjiangGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoTestmanjiangGetResponse, self).__init__()
        self._addr = None

    @property
    def addr(self):
        return self._addr

    @addr.setter
    def addr(self, value):
        self._addr = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoTestmanjiangGetResponse, self).parse_response_content(response_content)
        if 'addr' in response:
            self.addr = response['addr']
