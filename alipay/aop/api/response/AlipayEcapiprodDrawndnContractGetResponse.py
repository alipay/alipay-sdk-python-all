#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcapiprodDrawndnContractGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcapiprodDrawndnContractGetResponse, self).__init__()
        self._contract_content = None
        self._contract_no = None
        self._request_id = None

    @property
    def contract_content(self):
        return self._contract_content

    @contract_content.setter
    def contract_content(self, value):
        self._contract_content = value
    @property
    def contract_no(self):
        return self._contract_no

    @contract_no.setter
    def contract_no(self, value):
        self._contract_no = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcapiprodDrawndnContractGetResponse, self).parse_response_content(response_content)
        if 'contract_content' in response:
            self.contract_content = response['contract_content']
        if 'contract_no' in response:
            self.contract_no = response['contract_no']
        if 'request_id' in response:
            self.request_id = response['request_id']
