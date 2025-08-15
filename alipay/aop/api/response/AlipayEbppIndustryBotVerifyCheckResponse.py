#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryBotVerifyCheckResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryBotVerifyCheckResponse, self).__init__()
        self._verify_status = None

    @property
    def verify_status(self):
        return self._verify_status

    @verify_status.setter
    def verify_status(self, value):
        self._verify_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryBotVerifyCheckResponse, self).parse_response_content(response_content)
        if 'verify_status' in response:
            self.verify_status = response['verify_status']
