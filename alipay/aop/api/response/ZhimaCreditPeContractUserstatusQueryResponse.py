#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ContractBasicInfo import ContractBasicInfo


class ZhimaCreditPeContractUserstatusQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPeContractUserstatusQueryResponse, self).__init__()
        self._contract_basic_info = None
        self._user_status = None
        self._user_status_desc = None

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
    def user_status(self):
        return self._user_status

    @user_status.setter
    def user_status(self, value):
        self._user_status = value
    @property
    def user_status_desc(self):
        return self._user_status_desc

    @user_status_desc.setter
    def user_status_desc(self, value):
        self._user_status_desc = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPeContractUserstatusQueryResponse, self).parse_response_content(response_content)
        if 'contract_basic_info' in response:
            self.contract_basic_info = response['contract_basic_info']
        if 'user_status' in response:
            self.user_status = response['user_status']
        if 'user_status_desc' in response:
            self.user_status_desc = response['user_status_desc']
