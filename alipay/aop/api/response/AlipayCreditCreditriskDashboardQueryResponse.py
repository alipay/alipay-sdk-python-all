#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCreditCreditriskDashboardQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCreditCreditriskDashboardQueryResponse, self).__init__()
        self._credit_loan = None
        self._sale_refund = None
        self._service_charge = None
        self._total_income = None
        self._total_payout = None
        self._tqsk_loan = None
        self._ylb_profit = None

    @property
    def credit_loan(self):
        return self._credit_loan

    @credit_loan.setter
    def credit_loan(self, value):
        self._credit_loan = value
    @property
    def sale_refund(self):
        return self._sale_refund

    @sale_refund.setter
    def sale_refund(self, value):
        self._sale_refund = value
    @property
    def service_charge(self):
        return self._service_charge

    @service_charge.setter
    def service_charge(self, value):
        self._service_charge = value
    @property
    def total_income(self):
        return self._total_income

    @total_income.setter
    def total_income(self, value):
        self._total_income = value
    @property
    def total_payout(self):
        return self._total_payout

    @total_payout.setter
    def total_payout(self, value):
        self._total_payout = value
    @property
    def tqsk_loan(self):
        return self._tqsk_loan

    @tqsk_loan.setter
    def tqsk_loan(self, value):
        self._tqsk_loan = value
    @property
    def ylb_profit(self):
        return self._ylb_profit

    @ylb_profit.setter
    def ylb_profit(self, value):
        self._ylb_profit = value

    def parse_response_content(self, response_content):
        response = super(AlipayCreditCreditriskDashboardQueryResponse, self).parse_response_content(response_content)
        if 'credit_loan' in response:
            self.credit_loan = response['credit_loan']
        if 'sale_refund' in response:
            self.sale_refund = response['sale_refund']
        if 'service_charge' in response:
            self.service_charge = response['service_charge']
        if 'total_income' in response:
            self.total_income = response['total_income']
        if 'total_payout' in response:
            self.total_payout = response['total_payout']
        if 'tqsk_loan' in response:
            self.tqsk_loan = response['tqsk_loan']
        if 'ylb_profit' in response:
            self.ylb_profit = response['ylb_profit']
