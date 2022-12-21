#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditUserOpencoremodeltestXinghuiModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditUserOpencoremodeltestXinghuiModifyResponse, self).__init__()
        self._c = None

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, value):
        self._c = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditUserOpencoremodeltestXinghuiModifyResponse, self).parse_response_content(response_content)
        if 'c' in response:
            self.c = response['c']
