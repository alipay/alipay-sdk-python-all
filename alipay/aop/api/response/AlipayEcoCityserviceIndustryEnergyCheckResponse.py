#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoCityserviceIndustryEnergyCheckResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoCityserviceIndustryEnergyCheckResponse, self).__init__()
        self._limited = None

    @property
    def limited(self):
        return self._limited

    @limited.setter
    def limited(self, value):
        self._limited = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoCityserviceIndustryEnergyCheckResponse, self).parse_response_content(response_content)
        if 'limited' in response:
            self.limited = response['limited']
