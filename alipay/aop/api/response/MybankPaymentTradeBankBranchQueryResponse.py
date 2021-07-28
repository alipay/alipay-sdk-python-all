#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.Institution import Institution


class MybankPaymentTradeBankBranchQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankPaymentTradeBankBranchQueryResponse, self).__init__()
        self._bank_details = None

    @property
    def bank_details(self):
        return self._bank_details

    @bank_details.setter
    def bank_details(self, value):
        if isinstance(value, list):
            self._bank_details = list()
            for i in value:
                if isinstance(i, Institution):
                    self._bank_details.append(i)
                else:
                    self._bank_details.append(Institution.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(MybankPaymentTradeBankBranchQueryResponse, self).parse_response_content(response_content)
        if 'bank_details' in response:
            self.bank_details = response['bank_details']
