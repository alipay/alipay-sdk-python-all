#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ContractBasicInfo import ContractBasicInfo


class ZhimaCreditPeContractInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPeContractInfoQueryResponse, self).__init__()
        self._contract_basic_info = None
        self._contract_status = None
        self._contract_status_desc = None

    @property
    def contract_basic_info(self):
        return self._contract_basic_info

    @contract_basic_info.setter
    def contract_basic_info(self, value):
        if isinstance(value, ContractBasicInfo):
            self._contract_basic_info = value
        else:
            self._contract_basic_info = ContractBasicInfo.from_alipay_dict(value)
    @property
    def contract_status(self):
        return self._contract_status

    @contract_status.setter
    def contract_status(self, value):
        self._contract_status = value
    @property
    def contract_status_desc(self):
        return self._contract_status_desc

    @contract_status_desc.setter
    def contract_status_desc(self, value):
        self._contract_status_desc = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPeContractInfoQueryResponse, self).parse_response_content(response_content)
        if 'contract_basic_info' in response:
            self.contract_basic_info = response['contract_basic_info']
        if 'contract_status' in response:
            self.contract_status = response['contract_status']
        if 'contract_status_desc' in response:
            self.contract_status_desc = response['contract_status_desc']
