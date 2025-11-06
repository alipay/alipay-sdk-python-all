#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossProdContractBusinessidQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossProdContractBusinessidQueryResponse, self).__init__()
        self._biz_status = None
        self._business_id = None
        self._contract_code = None
        self._contract_name = None

    @property
    def biz_status(self):
        return self._biz_status

    @biz_status.setter
    def biz_status(self, value):
        self._biz_status = value
    @property
    def business_id(self):
        return self._business_id

    @business_id.setter
    def business_id(self, value):
        self._business_id = value
    @property
    def contract_code(self):
        return self._contract_code

    @contract_code.setter
    def contract_code(self, value):
        self._contract_code = value
    @property
    def contract_name(self):
        return self._contract_name

    @contract_name.setter
    def contract_name(self, value):
        self._contract_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossProdContractBusinessidQueryResponse, self).parse_response_content(response_content)
        if 'biz_status' in response:
            self.biz_status = response['biz_status']
        if 'business_id' in response:
            self.business_id = response['business_id']
        if 'contract_code' in response:
            self.contract_code = response['contract_code']
        if 'contract_name' in response:
            self.contract_name = response['contract_name']
