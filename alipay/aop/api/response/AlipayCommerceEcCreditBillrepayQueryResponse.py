#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EcCreditBillRepayment import EcCreditBillRepayment


class AlipayCommerceEcCreditBillrepayQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcCreditBillrepayQueryResponse, self).__init__()
        self._repayments = None

    @property
    def repayments(self):
        return self._repayments

    @repayments.setter
    def repayments(self, value):
        if isinstance(value, list):
            self._repayments = list()
            for i in value:
                if isinstance(i, EcCreditBillRepayment):
                    self._repayments.append(i)
                else:
                    self._repayments.append(EcCreditBillRepayment.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcCreditBillrepayQueryResponse, self).parse_response_content(response_content)
        if 'repayments' in response:
            self.repayments = response['repayments']
