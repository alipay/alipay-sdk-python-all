#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMsaasMediarecogAftscvpayTransactionInitializeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMsaasMediarecogAftscvpayTransactionInitializeResponse, self).__init__()
        self._result = None
        self._transaction_id = None

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def transaction_id(self):
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        self._transaction_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMsaasMediarecogAftscvpayTransactionInitializeResponse, self).parse_response_content(response_content)
        if 'result' in response:
            self.result = response['result']
        if 'transaction_id' in response:
            self.transaction_id = response['transaction_id']
