#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportBikeEnergyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportBikeEnergyQueryResponse, self).__init__()
        self._energy_open = None

    @property
    def energy_open(self):
        return self._energy_open

    @energy_open.setter
    def energy_open(self, value):
        self._energy_open = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportBikeEnergyQueryResponse, self).parse_response_content(response_content)
        if 'energy_open' in response:
            self.energy_open = response['energy_open']
