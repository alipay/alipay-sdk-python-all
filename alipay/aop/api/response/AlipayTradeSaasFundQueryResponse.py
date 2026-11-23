#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SaasFundAccountInfo import SaasFundAccountInfo
from alipay.aop.api.domain.SaasFundAccountInfo import SaasFundAccountInfo


class AlipayTradeSaasFundQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeSaasFundQueryResponse, self).__init__()
        self._amount = None
        self._claim_amount = None
        self._currency = None
        self._customer_id = None
        self._fund_no = None
        self._fund_status = None
        self._order_no = None
        self._payee_account_info = None
        self._payer_account_info = None
        self._refund_amount = None
        self._trade_no = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def claim_amount(self):
        return self._claim_amount

    @claim_amount.setter
    def claim_amount(self, value):
        self._claim_amount = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
    @property
    def fund_no(self):
        return self._fund_no

    @fund_no.setter
    def fund_no(self, value):
        self._fund_no = value
    @property
    def fund_status(self):
        return self._fund_status

    @fund_status.setter
    def fund_status(self, value):
        self._fund_status = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def payee_account_info(self):
        return self._payee_account_info

    @payee_account_info.setter
    def payee_account_info(self, value):
        if isinstance(value, SaasFundAccountInfo):
            self._payee_account_info = value
        else:
            self._payee_account_info = SaasFundAccountInfo.from_alipay_dict(value)
    @property
    def payer_account_info(self):
        return self._payer_account_info

    @payer_account_info.setter
    def payer_account_info(self, value):
        if isinstance(value, SaasFundAccountInfo):
            self._payer_account_info = value
        else:
            self._payer_account_info = SaasFundAccountInfo.from_alipay_dict(value)
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeSaasFundQueryResponse, self).parse_response_content(response_content)
        if 'amount' in response:
            self.amount = response['amount']
        if 'claim_amount' in response:
            self.claim_amount = response['claim_amount']
        if 'currency' in response:
            self.currency = response['currency']
        if 'customer_id' in response:
            self.customer_id = response['customer_id']
        if 'fund_no' in response:
            self.fund_no = response['fund_no']
        if 'fund_status' in response:
            self.fund_status = response['fund_status']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'payee_account_info' in response:
            self.payee_account_info = response['payee_account_info']
        if 'payer_account_info' in response:
            self.payer_account_info = response['payer_account_info']
        if 'refund_amount' in response:
            self.refund_amount = response['refund_amount']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
