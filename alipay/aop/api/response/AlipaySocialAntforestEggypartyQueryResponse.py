#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialAntforestEggypartyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialAntforestEggypartyQueryResponse, self).__init__()
        self._total_water_energy = None
        self._total_water_times = None

    @property
    def total_water_energy(self):
        return self._total_water_energy

    @total_water_energy.setter
    def total_water_energy(self, value):
        self._total_water_energy = value
    @property
    def total_water_times(self):
        return self._total_water_times

    @total_water_times.setter
    def total_water_times(self, value):
        self._total_water_times = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialAntforestEggypartyQueryResponse, self).parse_response_content(response_content)
        if 'total_water_energy' in response:
            self.total_water_energy = response['total_water_energy']
        if 'total_water_times' in response:
            self.total_water_times = response['total_water_times']
