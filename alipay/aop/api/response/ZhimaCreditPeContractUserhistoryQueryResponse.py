#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ContractBasicInfo import ContractBasicInfo


class ZhimaCreditPeContractUserhistoryQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPeContractUserhistoryQueryResponse, self).__init__()
        self._contract_history = None

    @property
    def contract_history(self):
        return self._contract_history

    @contract_history.setter
    def contract_history(self, value):
        if isinstance(value, list):
            self._contract_history = list()
            for i in value:
                if isinstance(i, ContractBasicInfo):
                    self._contract_history.append(i)
                else:
                    self._contract_history.append(ContractBasicInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPeContractUserhistoryQueryResponse, self).parse_response_content(response_content)
        if 'contract_history' in response:
            self.contract_history = response['contract_history']
