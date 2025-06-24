#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneServiceAvailableQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneServiceAvailableQueryResponse, self).__init__()
        self._available_flag = None
        self._ser_contract_no = None

    @property
    def available_flag(self):
        return self._available_flag

    @available_flag.setter
    def available_flag(self, value):
        self._available_flag = value
    @property
    def ser_contract_no(self):
        return self._ser_contract_no

    @ser_contract_no.setter
    def ser_contract_no(self, value):
        self._ser_contract_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneServiceAvailableQueryResponse, self).parse_response_content(response_content)
        if 'available_flag' in response:
            self.available_flag = response['available_flag']
        if 'ser_contract_no' in response:
            self.ser_contract_no = response['ser_contract_no']
