#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialAntforestEnergyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialAntforestEnergyQueryResponse, self).__init__()
        self._current_energy = None
        self._total_energy = None

    @property
    def current_energy(self):
        return self._current_energy

    @current_energy.setter
    def current_energy(self, value):
        self._current_energy = value
    @property
    def total_energy(self):
        return self._total_energy

    @total_energy.setter
    def total_energy(self, value):
        self._total_energy = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialAntforestEnergyQueryResponse, self).parse_response_content(response_content)
        if 'current_energy' in response:
            self.current_energy = response['current_energy']
        if 'total_energy' in response:
            self.total_energy = response['total_energy']
