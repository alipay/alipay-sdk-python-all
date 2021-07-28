#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DiscountDetailInfo import DiscountDetailInfo


class KoubeiTradeOrderAggregateConsultResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiTradeOrderAggregateConsultResponse, self).__init__()
        self._buyer_id = None
        self._buyer_id_type = None
        self._buyer_pay_amount = None
        self._create_time = None
        self._discount_detail_list = None
        self._gmt_payment_time = None
        self._merchant_discount_amount = None
        self._order_no = None
        self._order_status = None
        self._out_order_no = None
        self._pay_channel = None
        self._platform_discount_amount = None
        self._receipt_amount = None
        self._total_amount = None
        self._trade_no = None

    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def buyer_id_type(self):
        return self._buyer_id_type

    @buyer_id_type.setter
    def buyer_id_type(self, value):
        self._buyer_id_type = value
    @property
    def buyer_pay_amount(self):
        return self._buyer_pay_amount

    @buyer_pay_amount.setter
    def buyer_pay_amount(self, value):
        self._buyer_pay_amount = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def discount_detail_list(self):
        return self._discount_detail_list

    @discount_detail_list.setter
    def discount_detail_list(self, value):
        if isinstance(value, DiscountDetailInfo):
            self._discount_detail_list = value
        else:
            self._discount_detail_list = DiscountDetailInfo.from_alipay_dict(value)
    @property
    def gmt_payment_time(self):
        return self._gmt_payment_time

    @gmt_payment_time.setter
    def gmt_payment_time(self, value):
        self._gmt_payment_time = value
    @property
    def merchant_discount_amount(self):
        return self._merchant_discount_amount

    @merchant_discount_amount.setter
    def merchant_discount_amount(self, value):
        self._merchant_discount_amount = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def pay_channel(self):
        return self._pay_channel

    @pay_channel.setter
    def pay_channel(self, value):
        self._pay_channel = value
    @property
    def platform_discount_amount(self):
        return self._platform_discount_amount

    @platform_discount_amount.setter
    def platform_discount_amount(self, value):
        self._platform_discount_amount = value
    @property
    def receipt_amount(self):
        return self._receipt_amount

    @receipt_amount.setter
    def receipt_amount(self, value):
        self._receipt_amount = value
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

    def parse_response_content(self, response_content):
        response = super(KoubeiTradeOrderAggregateConsultResponse, self).parse_response_content(response_content)
        if 'buyer_id' in response:
            self.buyer_id = response['buyer_id']
        if 'buyer_id_type' in response:
            self.buyer_id_type = response['buyer_id_type']
        if 'buyer_pay_amount' in response:
            self.buyer_pay_amount = response['buyer_pay_amount']
        if 'create_time' in response:
            self.create_time = response['create_time']
        if 'discount_detail_list' in response:
            self.discount_detail_list = response['discount_detail_list']
        if 'gmt_payment_time' in response:
            self.gmt_payment_time = response['gmt_payment_time']
        if 'merchant_discount_amount' in response:
            self.merchant_discount_amount = response['merchant_discount_amount']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'pay_channel' in response:
            self.pay_channel = response['pay_channel']
        if 'platform_discount_amount' in response:
            self.platform_discount_amount = response['platform_discount_amount']
        if 'receipt_amount' in response:
            self.receipt_amount = response['receipt_amount']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
