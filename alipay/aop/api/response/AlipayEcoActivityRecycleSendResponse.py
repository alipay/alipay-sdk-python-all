#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoActivityRecycleSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoActivityRecycleSendResponse, self).__init__()
        self._full_energy = None

    @property
    def full_energy(self):
        return self._full_energy

    @full_energy.setter
    def full_energy(self, value):
        self._full_energy = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoActivityRecycleSendResponse, self).parse_response_content(response_content)
        if 'full_energy' in response:
            self.full_energy = response['full_energy']
