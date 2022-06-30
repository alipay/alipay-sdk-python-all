#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EnergyQueryRsp import EnergyQueryRsp


class AlipayEcoActivityRecycleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoActivityRecycleQueryResponse, self).__init__()
        self._energy_list = None

    @property
    def energy_list(self):
        return self._energy_list

    @energy_list.setter
    def energy_list(self, value):
        if isinstance(value, list):
            self._energy_list = list()
            for i in value:
                if isinstance(i, EnergyQueryRsp):
                    self._energy_list.append(i)
                else:
                    self._energy_list.append(EnergyQueryRsp.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEcoActivityRecycleQueryResponse, self).parse_response_content(response_content)
        if 'energy_list' in response:
            self.energy_list = response['energy_list']
