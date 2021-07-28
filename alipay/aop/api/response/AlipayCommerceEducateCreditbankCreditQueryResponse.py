#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CreditBankCredit import CreditBankCredit


class AlipayCommerceEducateCreditbankCreditQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateCreditbankCreditQueryResponse, self).__init__()
        self._credit = None

    @property
    def credit(self):
        return self._credit

    @credit.setter
    def credit(self, value):
        if isinstance(value, list):
            self._credit = list()
            for i in value:
                if isinstance(i, CreditBankCredit):
                    self._credit.append(i)
                else:
                    self._credit.append(CreditBankCredit.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateCreditbankCreditQueryResponse, self).parse_response_content(response_content)
        if 'credit' in response:
            self.credit = response['credit']
