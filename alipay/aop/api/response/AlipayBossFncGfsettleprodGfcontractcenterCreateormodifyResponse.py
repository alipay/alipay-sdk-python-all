#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ContractSyncResponse import ContractSyncResponse


class AlipayBossFncGfsettleprodGfcontractcenterCreateormodifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossFncGfsettleprodGfcontractcenterCreateormodifyResponse, self).__init__()
        self._contract_sync_response = None

    @property
    def contract_sync_response(self):
        return self._contract_sync_response

    @contract_sync_response.setter
    def contract_sync_response(self, value):
        if isinstance(value, ContractSyncResponse):
            self._contract_sync_response = value
        else:
            self._contract_sync_response = ContractSyncResponse.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayBossFncGfsettleprodGfcontractcenterCreateormodifyResponse, self).parse_response_content(response_content)
        if 'contract_sync_response' in response:
            self.contract_sync_response = response['contract_sync_response']
