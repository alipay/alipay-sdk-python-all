#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FinanceBillInfo import FinanceBillInfo


class AlipayTradeFinanceOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeFinanceOrderQueryResponse, self).__init__()
        self._finance_bill_list = None
        self._out_order_no = None
        self._settlement_no = None

    @property
    def finance_bill_list(self):
        return self._finance_bill_list

    @finance_bill_list.setter
    def finance_bill_list(self, value):
        if isinstance(value, list):
            self._finance_bill_list = list()
            for i in value:
                if isinstance(i, FinanceBillInfo):
                    self._finance_bill_list.append(i)
                else:
                    self._finance_bill_list.append(FinanceBillInfo.from_alipay_dict(i))
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def settlement_no(self):
        return self._settlement_no

    @settlement_no.setter
    def settlement_no(self, value):
        self._settlement_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeFinanceOrderQueryResponse, self).parse_response_content(response_content)
        if 'finance_bill_list' in response:
            self.finance_bill_list = response['finance_bill_list']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'settlement_no' in response:
            self.settlement_no = response['settlement_no']
