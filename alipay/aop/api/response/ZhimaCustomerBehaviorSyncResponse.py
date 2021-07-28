#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCustomerBehaviorSyncResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCustomerBehaviorSyncResponse, self).__init__()
        self._contract_no = None
        self._contract_nos = None

    @property
    def contract_no(self):
        return self._contract_no

    @contract_no.setter
    def contract_no(self, value):
        self._contract_no = value
    @property
    def contract_nos(self):
        return self._contract_nos

    @contract_nos.setter
    def contract_nos(self, value):
        if isinstance(value, list):
            self._contract_nos = list()
            for i in value:
                self._contract_nos.append(i)

    def parse_response_content(self, response_content):
        response = super(ZhimaCustomerBehaviorSyncResponse, self).parse_response_content(response_content)
        if 'contract_no' in response:
            self.contract_no = response['contract_no']
        if 'contract_nos' in response:
            self.contract_nos = response['contract_nos']
