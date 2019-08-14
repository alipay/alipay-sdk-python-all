#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CustScpBillAmtVO import CustScpBillAmtVO
from alipay.aop.api.domain.CustScpInstallmentBudgetVO import CustScpInstallmentBudgetVO


class MybankCreditSupplychainTradeBillrepaybudgetQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSupplychainTradeBillrepaybudgetQueryResponse, self).__init__()
        self._bill_amt_detail = None
        self._can_repay = None
        self._exempt_amt = None
        self._install_budget_detail_list = None
        self._out_order = None
        self._status = None
        self._total_amt = None

    @property
    def bill_amt_detail(self):
        return self._bill_amt_detail

    @bill_amt_detail.setter
    def bill_amt_detail(self, value):
        if isinstance(value, CustScpBillAmtVO):
            self._bill_amt_detail = value
        else:
            self._bill_amt_detail = CustScpBillAmtVO.from_alipay_dict(value)
    @property
    def can_repay(self):
        return self._can_repay

    @can_repay.setter
    def can_repay(self, value):
        self._can_repay = value
    @property
    def exempt_amt(self):
        return self._exempt_amt

    @exempt_amt.setter
    def exempt_amt(self, value):
        self._exempt_amt = value
    @property
    def install_budget_detail_list(self):
        return self._install_budget_detail_list

    @install_budget_detail_list.setter
    def install_budget_detail_list(self, value):
        if isinstance(value, list):
            self._install_budget_detail_list = list()
            for i in value:
                if isinstance(i, CustScpInstallmentBudgetVO):
                    self._install_budget_detail_list.append(i)
                else:
                    self._install_budget_detail_list.append(CustScpInstallmentBudgetVO.from_alipay_dict(i))
    @property
    def out_order(self):
        return self._out_order

    @out_order.setter
    def out_order(self, value):
        self._out_order = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def total_amt(self):
        return self._total_amt

    @total_amt.setter
    def total_amt(self, value):
        self._total_amt = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditSupplychainTradeBillrepaybudgetQueryResponse, self).parse_response_content(response_content)
        if 'bill_amt_detail' in response:
            self.bill_amt_detail = response['bill_amt_detail']
        if 'can_repay' in response:
            self.can_repay = response['can_repay']
        if 'exempt_amt' in response:
            self.exempt_amt = response['exempt_amt']
        if 'install_budget_detail_list' in response:
            self.install_budget_detail_list = response['install_budget_detail_list']
        if 'out_order' in response:
            self.out_order = response['out_order']
        if 'status' in response:
            self.status = response['status']
        if 'total_amt' in response:
            self.total_amt = response['total_amt']
