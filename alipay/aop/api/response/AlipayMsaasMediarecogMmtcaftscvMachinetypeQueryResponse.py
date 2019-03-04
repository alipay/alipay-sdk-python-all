#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MachineType import MachineType


class AlipayMsaasMediarecogMmtcaftscvMachinetypeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMsaasMediarecogMmtcaftscvMachinetypeQueryResponse, self).__init__()
        self._machine_types = None

    @property
    def machine_types(self):
        return self._machine_types

    @machine_types.setter
    def machine_types(self, value):
        if isinstance(value, list):
            self._machine_types = list()
            for i in value:
                if isinstance(i, MachineType):
                    self._machine_types.append(i)
                else:
                    self._machine_types.append(MachineType.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMsaasMediarecogMmtcaftscvMachinetypeQueryResponse, self).parse_response_content(response_content)
        if 'machine_types' in response:
            self.machine_types = response['machine_types']
