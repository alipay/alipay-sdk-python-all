#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoCityserviceIndustryEnergySendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoCityserviceIndustryEnergySendResponse, self).__init__()
        self._total_energy = None

    @property
    def total_energy(self):
        return self._total_energy

    @total_energy.setter
    def total_energy(self, value):
        self._total_energy = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoCityserviceIndustryEnergySendResponse, self).parse_response_content(response_content)
        if 'total_energy' in response:
            self.total_energy = response['total_energy']
