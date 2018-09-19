#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CreditResult import CreditResult


class AlipayEcapiprodCreditGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcapiprodCreditGetResponse, self).__init__()
        self._credit_result = None
        self._request_id = None

    @property
    def credit_result(self):
        return self._credit_result

    @credit_result.setter
    def credit_result(self, value):
        if isinstance(value, CreditResult):
            self._credit_result = value
        else:
            self._credit_result = CreditResult.from_alipay_dict(value)
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcapiprodCreditGetResponse, self).parse_response_content(response_content)
        if 'credit_result' in response:
            self.credit_result = response['credit_result']
        if 'request_id' in response:
            self.request_id = response['request_id']
