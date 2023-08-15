#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossSWsstestAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossSWsstestAddResponse, self).__init__()
        self._ss = None

    @property
    def ss(self):
        return self._ss

    @ss.setter
    def ss(self, value):
        self._ss = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossSWsstestAddResponse, self).parse_response_content(response_content)
        if 'ss' in response:
            self.ss = response['ss']
