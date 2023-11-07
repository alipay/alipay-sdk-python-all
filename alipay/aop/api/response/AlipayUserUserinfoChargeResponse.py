#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserUserinfoChargeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserUserinfoChargeResponse, self).__init__()
        self._sd = None

    @property
    def sd(self):
        return self._sd

    @sd.setter
    def sd(self, value):
        self._sd = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserUserinfoChargeResponse, self).parse_response_content(response_content)
        if 'sd' in response:
            self.sd = response['sd']
