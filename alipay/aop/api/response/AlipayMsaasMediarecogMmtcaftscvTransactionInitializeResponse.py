#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMsaasMediarecogMmtcaftscvTransactionInitializeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMsaasMediarecogMmtcaftscvTransactionInitializeResponse, self).__init__()
        self._algorithm_config = None
        self._result = None
        self._transaction_id = None

    @property
    def algorithm_config(self):
        return self._algorithm_config

    @algorithm_config.setter
    def algorithm_config(self, value):
        self._algorithm_config = value
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
        response = super(AlipayMsaasMediarecogMmtcaftscvTransactionInitializeResponse, self).parse_response_content(response_content)
        if 'algorithm_config' in response:
            self.algorithm_config = response['algorithm_config']
        if 'result' in response:
            self.result = response['result']
        if 'transaction_id' in response:
            self.transaction_id = response['transaction_id']
