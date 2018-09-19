#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AlipayContract import AlipayContract


class AlipayUserContractGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserContractGetResponse, self).__init__()
        self._alipay_contract = None

    @property
    def alipay_contract(self):
        return self._alipay_contract

    @alipay_contract.setter
    def alipay_contract(self, value):
        if isinstance(value, AlipayContract):
            self._alipay_contract = value
        else:
            self._alipay_contract = AlipayContract.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayUserContractGetResponse, self).parse_response_content(response_content)
        if 'alipay_contract' in response:
            self.alipay_contract = response['alipay_contract']
