#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CreditPayReceivableVO import CreditPayReceivableVO
from alipay.aop.api.domain.CreditPayMoneyVO import CreditPayMoneyVO


class MybankCreditLoantradePayeeReceivableBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoantradePayeeReceivableBatchqueryResponse, self).__init__()
        self._receivable_list = None
        self._total_rcv_amt = None

    @property
    def receivable_list(self):
        return self._receivable_list

    @receivable_list.setter
    def receivable_list(self, value):
        if isinstance(value, list):
            self._receivable_list = list()
            for i in value:
                if isinstance(i, CreditPayReceivableVO):
                    self._receivable_list.append(i)
                else:
                    self._receivable_list.append(CreditPayReceivableVO.from_alipay_dict(i))
    @property
    def total_rcv_amt(self):
        return self._total_rcv_amt

    @total_rcv_amt.setter
    def total_rcv_amt(self, value):
        if isinstance(value, CreditPayMoneyVO):
            self._total_rcv_amt = value
        else:
            self._total_rcv_amt = CreditPayMoneyVO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoantradePayeeReceivableBatchqueryResponse, self).parse_response_content(response_content)
        if 'receivable_list' in response:
            self.receivable_list = response['receivable_list']
        if 'total_rcv_amt' in response:
            self.total_rcv_amt = response['total_rcv_amt']
