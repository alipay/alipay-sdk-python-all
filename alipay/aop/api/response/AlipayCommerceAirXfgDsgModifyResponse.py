#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceAirXfgDsgModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAirXfgDsgModifyResponse, self).__init__()
        self._level = None

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAirXfgDsgModifyResponse, self).parse_response_content(response_content)
        if 'level' in response:
            self.level = response['level']
