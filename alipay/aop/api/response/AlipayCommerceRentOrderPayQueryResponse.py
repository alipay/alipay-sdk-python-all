#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RentTradeFundBillVO import RentTradeFundBillVO


class AlipayCommerceRentOrderPayQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRentOrderPayQueryResponse, self).__init__()
        self._additional_status = None
        self._buyer_pay_amount = None
        self._buyer_user_id = None
        self._discount_amount = None
        self._fund_bill_list = None
        self._mdiscount_amount = None
        self._out_trade_no = None
        self._receipt_amount = None
        self._send_pay_date = None
        self._total_amount = None
        self._trade_no = None
        self._trade_status = None

    @property
    def additional_status(self):
        return self._additional_status

    @additional_status.setter
    def additional_status(self, value):
        self._additional_status = value
    @property
    def buyer_pay_amount(self):
        return self._buyer_pay_amount

    @buyer_pay_amount.setter
    def buyer_pay_amount(self, value):
        self._buyer_pay_amount = value
    @property
    def buyer_user_id(self):
        return self._buyer_user_id

    @buyer_user_id.setter
    def buyer_user_id(self, value):
        self._buyer_user_id = value
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def fund_bill_list(self):
        return self._fund_bill_list

    @fund_bill_list.setter
    def fund_bill_list(self, value):
        if isinstance(value, list):
            self._fund_bill_list = list()
            for i in value:
                if isinstance(i, RentTradeFundBillVO):
                    self._fund_bill_list.append(i)
                else:
                    self._fund_bill_list.append(RentTradeFundBillVO.from_alipay_dict(i))
    @property
    def mdiscount_amount(self):
        return self._mdiscount_amount

    @mdiscount_amount.setter
    def mdiscount_amount(self, value):
        self._mdiscount_amount = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def receipt_amount(self):
        return self._receipt_amount

    @receipt_amount.setter
    def receipt_amount(self, value):
        self._receipt_amount = value
    @property
    def send_pay_date(self):
        return self._send_pay_date

    @send_pay_date.setter
    def send_pay_date(self, value):
        self._send_pay_date = value
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
    def trade_status(self):
        return self._trade_status

    @trade_status.setter
    def trade_status(self, value):
        self._trade_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRentOrderPayQueryResponse, self).parse_response_content(response_content)
        if 'additional_status' in response:
            self.additional_status = response['additional_status']
        if 'buyer_pay_amount' in response:
            self.buyer_pay_amount = response['buyer_pay_amount']
        if 'buyer_user_id' in response:
            self.buyer_user_id = response['buyer_user_id']
        if 'discount_amount' in response:
            self.discount_amount = response['discount_amount']
        if 'fund_bill_list' in response:
            self.fund_bill_list = response['fund_bill_list']
        if 'mdiscount_amount' in response:
            self.mdiscount_amount = response['mdiscount_amount']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'receipt_amount' in response:
            self.receipt_amount = response['receipt_amount']
        if 'send_pay_date' in response:
            self.send_pay_date = response['send_pay_date']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
        if 'trade_status' in response:
            self.trade_status = response['trade_status']
