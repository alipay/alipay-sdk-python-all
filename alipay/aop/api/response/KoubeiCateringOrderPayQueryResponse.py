#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PosDiscountDetail import PosDiscountDetail


class KoubeiCateringOrderPayQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringOrderPayQueryResponse, self).__init__()
        self._discount_details = None
        self._out_pay_no = None
        self._pay_amount = None
        self._pay_no = None
        self._pay_time = None
        self._receipt_amount = None
        self._status = None
        self._total_amount = None
        self._trade_no = None
        self._user_id = None

    @property
    def discount_details(self):
        return self._discount_details

    @discount_details.setter
    def discount_details(self, value):
        if isinstance(value, list):
            self._discount_details = list()
            for i in value:
                if isinstance(i, PosDiscountDetail):
                    self._discount_details.append(i)
                else:
                    self._discount_details.append(PosDiscountDetail.from_alipay_dict(i))
    @property
    def out_pay_no(self):
        return self._out_pay_no

    @out_pay_no.setter
    def out_pay_no(self, value):
        self._out_pay_no = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pay_no(self):
        return self._pay_no

    @pay_no.setter
    def pay_no(self, value):
        self._pay_no = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def receipt_amount(self):
        return self._receipt_amount

    @receipt_amount.setter
    def receipt_amount(self, value):
        self._receipt_amount = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringOrderPayQueryResponse, self).parse_response_content(response_content)
        if 'discount_details' in response:
            self.discount_details = response['discount_details']
        if 'out_pay_no' in response:
            self.out_pay_no = response['out_pay_no']
        if 'pay_amount' in response:
            self.pay_amount = response['pay_amount']
        if 'pay_no' in response:
            self.pay_no = response['pay_no']
        if 'pay_time' in response:
            self.pay_time = response['pay_time']
        if 'receipt_amount' in response:
            self.receipt_amount = response['receipt_amount']
        if 'status' in response:
            self.status = response['status']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
        if 'user_id' in response:
            self.user_id = response['user_id']
