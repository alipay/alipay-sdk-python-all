#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CreditPayBillDetailVO import CreditPayBillDetailVO


class MybankCreditLoantradePayerBillrepayConsultResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoantradePayerBillrepayConsultResponse, self).__init__()
        self._bill_details = None
        self._exist_bill = None
        self._repay_url = None

    @property
    def bill_details(self):
        return self._bill_details

    @bill_details.setter
    def bill_details(self, value):
        if isinstance(value, list):
            self._bill_details = list()
            for i in value:
                if isinstance(i, CreditPayBillDetailVO):
                    self._bill_details.append(i)
                else:
                    self._bill_details.append(CreditPayBillDetailVO.from_alipay_dict(i))
    @property
    def exist_bill(self):
        return self._exist_bill

    @exist_bill.setter
    def exist_bill(self, value):
        self._exist_bill = value
    @property
    def repay_url(self):
        return self._repay_url

    @repay_url.setter
    def repay_url(self, value):
        self._repay_url = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoantradePayerBillrepayConsultResponse, self).parse_response_content(response_content)
        if 'bill_details' in response:
            self.bill_details = response['bill_details']
        if 'exist_bill' in response:
            self.exist_bill = response['exist_bill']
        if 'repay_url' in response:
            self.repay_url = response['repay_url']
