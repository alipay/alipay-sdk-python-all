#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CreditPayMoneyVO import CreditPayMoneyVO
from alipay.aop.api.domain.CreditPayChargePricingVO import CreditPayChargePricingVO
from alipay.aop.api.domain.CreditPayIntPricingVO import CreditPayIntPricingVO
from alipay.aop.api.domain.CreditPayMoneyVO import CreditPayMoneyVO


class MybankCreditLoantradePayeeReceivableQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoantradePayeeReceivableQueryResponse, self).__init__()
        self._factoring_amt = None
        self._factoring_fee_pricing = None
        self._factoring_int_pricing = None
        self._receivable_cnt = None
        self._receivable_manage_url = None
        self._remit_date = None
        self._total_rcv_amt = None

    @property
    def factoring_amt(self):
        return self._factoring_amt

    @factoring_amt.setter
    def factoring_amt(self, value):
        if isinstance(value, CreditPayMoneyVO):
            self._factoring_amt = value
        else:
            self._factoring_amt = CreditPayMoneyVO.from_alipay_dict(value)
    @property
    def factoring_fee_pricing(self):
        return self._factoring_fee_pricing

    @factoring_fee_pricing.setter
    def factoring_fee_pricing(self, value):
        if isinstance(value, list):
            self._factoring_fee_pricing = list()
            for i in value:
                if isinstance(i, CreditPayChargePricingVO):
                    self._factoring_fee_pricing.append(i)
                else:
                    self._factoring_fee_pricing.append(CreditPayChargePricingVO.from_alipay_dict(i))
    @property
    def factoring_int_pricing(self):
        return self._factoring_int_pricing

    @factoring_int_pricing.setter
    def factoring_int_pricing(self, value):
        if isinstance(value, CreditPayIntPricingVO):
            self._factoring_int_pricing = value
        else:
            self._factoring_int_pricing = CreditPayIntPricingVO.from_alipay_dict(value)
    @property
    def receivable_cnt(self):
        return self._receivable_cnt

    @receivable_cnt.setter
    def receivable_cnt(self, value):
        self._receivable_cnt = value
    @property
    def receivable_manage_url(self):
        return self._receivable_manage_url

    @receivable_manage_url.setter
    def receivable_manage_url(self, value):
        self._receivable_manage_url = value
    @property
    def remit_date(self):
        return self._remit_date

    @remit_date.setter
    def remit_date(self, value):
        self._remit_date = value
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
        response = super(MybankCreditLoantradePayeeReceivableQueryResponse, self).parse_response_content(response_content)
        if 'factoring_amt' in response:
            self.factoring_amt = response['factoring_amt']
        if 'factoring_fee_pricing' in response:
            self.factoring_fee_pricing = response['factoring_fee_pricing']
        if 'factoring_int_pricing' in response:
            self.factoring_int_pricing = response['factoring_int_pricing']
        if 'receivable_cnt' in response:
            self.receivable_cnt = response['receivable_cnt']
        if 'receivable_manage_url' in response:
            self.receivable_manage_url = response['receivable_manage_url']
        if 'remit_date' in response:
            self.remit_date = response['remit_date']
        if 'total_rcv_amt' in response:
            self.total_rcv_amt = response['total_rcv_amt']
