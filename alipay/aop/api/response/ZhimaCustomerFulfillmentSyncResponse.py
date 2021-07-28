#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCustomerFulfillmentSyncResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCustomerFulfillmentSyncResponse, self).__init__()
        self._contract_nos = None

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
        response = super(ZhimaCustomerFulfillmentSyncResponse, self).parse_response_content(response_content)
        if 'contract_nos' in response:
            self.contract_nos = response['contract_nos']
