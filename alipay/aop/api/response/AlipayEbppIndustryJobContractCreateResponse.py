#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ContractSignRsp import ContractSignRsp


class AlipayEbppIndustryJobContractCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryJobContractCreateResponse, self).__init__()
        self._sign_rsp_list = None
        self._success = None

    @property
    def sign_rsp_list(self):
        return self._sign_rsp_list

    @sign_rsp_list.setter
    def sign_rsp_list(self, value):
        if isinstance(value, list):
            self._sign_rsp_list = list()
            for i in value:
                if isinstance(i, ContractSignRsp):
                    self._sign_rsp_list.append(i)
                else:
                    self._sign_rsp_list.append(ContractSignRsp.from_alipay_dict(i))
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryJobContractCreateResponse, self).parse_response_content(response_content)
        if 'sign_rsp_list' in response:
            self.sign_rsp_list = response['sign_rsp_list']
        if 'success' in response:
            self.success = response['success']
