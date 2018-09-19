#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditSupplychainTradePayableQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSupplychainTradePayableQueryResponse, self).__init__()
        self._debt_amt = None
        self._expire_date = None
        self._if_enough = None
        self._if_need_budget = None
        self._overdue_amt = None
        self._paid_amt = None
        self._total_amt = None

    @property
    def debt_amt(self):
        return self._debt_amt

    @debt_amt.setter
    def debt_amt(self, value):
        self._debt_amt = value
    @property
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value
    @property
    def if_enough(self):
        return self._if_enough

    @if_enough.setter
    def if_enough(self, value):
        self._if_enough = value
    @property
    def if_need_budget(self):
        return self._if_need_budget

    @if_need_budget.setter
    def if_need_budget(self, value):
        self._if_need_budget = value
    @property
    def overdue_amt(self):
        return self._overdue_amt

    @overdue_amt.setter
    def overdue_amt(self, value):
        self._overdue_amt = value
    @property
    def paid_amt(self):
        return self._paid_amt

    @paid_amt.setter
    def paid_amt(self, value):
        self._paid_amt = value
    @property
    def total_amt(self):
        return self._total_amt

    @total_amt.setter
    def total_amt(self, value):
        self._total_amt = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditSupplychainTradePayableQueryResponse, self).parse_response_content(response_content)
        if 'debt_amt' in response:
            self.debt_amt = response['debt_amt']
        if 'expire_date' in response:
            self.expire_date = response['expire_date']
        if 'if_enough' in response:
            self.if_enough = response['if_enough']
        if 'if_need_budget' in response:
            self.if_need_budget = response['if_need_budget']
        if 'overdue_amt' in response:
            self.overdue_amt = response['overdue_amt']
        if 'paid_amt' in response:
            self.paid_amt = response['paid_amt']
        if 'total_amt' in response:
            self.total_amt = response['total_amt']
