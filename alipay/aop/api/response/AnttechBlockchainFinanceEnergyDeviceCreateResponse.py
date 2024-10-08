#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainFinanceEnergyDeviceCreateResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinanceEnergyDeviceCreateResponse, self).__init__()
        self._entity_id = None
        self._entity_status = None

    @property
    def entity_id(self):
        return self._entity_id

    @entity_id.setter
    def entity_id(self, value):
        self._entity_id = value
    @property
    def entity_status(self):
        return self._entity_status

    @entity_status.setter
    def entity_status(self, value):
        self._entity_status = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinanceEnergyDeviceCreateResponse, self).parse_response_content(response_content)
        if 'entity_id' in response:
            self.entity_id = response['entity_id']
        if 'entity_status' in response:
            self.entity_status = response['entity_status']
