#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ChargerOrderInfo import ChargerOrderInfo
from alipay.aop.api.domain.ChargerTradeSettleInfo import ChargerTradeSettleInfo


class AlipayCommerceTransportChargerPayQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportChargerPayQueryResponse, self).__init__()
        self._charger_order_info = None
        self._merchant_discount_amount = None
        self._merchant_pay_amount = None
        self._merchant_total_amount = None
        self._order_no = None
        self._order_time = None
        self._order_type = None
        self._out_trade_no = None
        self._trade_no = None
        self._trade_settle_info = None
        self._trade_status = None

    @property
    def charger_order_info(self):
        return self._charger_order_info

    @charger_order_info.setter
    def charger_order_info(self, value):
        if isinstance(value, ChargerOrderInfo):
            self._charger_order_info = value
        else:
            self._charger_order_info = ChargerOrderInfo.from_alipay_dict(value)
    @property
    def merchant_discount_amount(self):
        return self._merchant_discount_amount

    @merchant_discount_amount.setter
    def merchant_discount_amount(self, value):
        self._merchant_discount_amount = value
    @property
    def merchant_pay_amount(self):
        return self._merchant_pay_amount

    @merchant_pay_amount.setter
    def merchant_pay_amount(self, value):
        self._merchant_pay_amount = value
    @property
    def merchant_total_amount(self):
        return self._merchant_total_amount

    @merchant_total_amount.setter
    def merchant_total_amount(self, value):
        self._merchant_total_amount = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def order_time(self):
        return self._order_time

    @order_time.setter
    def order_time(self, value):
        self._order_time = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def trade_settle_info(self):
        return self._trade_settle_info

    @trade_settle_info.setter
    def trade_settle_info(self, value):
        if isinstance(value, ChargerTradeSettleInfo):
            self._trade_settle_info = value
        else:
            self._trade_settle_info = ChargerTradeSettleInfo.from_alipay_dict(value)
    @property
    def trade_status(self):
        return self._trade_status

    @trade_status.setter
    def trade_status(self, value):
        self._trade_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportChargerPayQueryResponse, self).parse_response_content(response_content)
        if 'charger_order_info' in response:
            self.charger_order_info = response['charger_order_info']
        if 'merchant_discount_amount' in response:
            self.merchant_discount_amount = response['merchant_discount_amount']
        if 'merchant_pay_amount' in response:
            self.merchant_pay_amount = response['merchant_pay_amount']
        if 'merchant_total_amount' in response:
            self.merchant_total_amount = response['merchant_total_amount']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'order_time' in response:
            self.order_time = response['order_time']
        if 'order_type' in response:
            self.order_type = response['order_type']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
        if 'trade_settle_info' in response:
            self.trade_settle_info = response['trade_settle_info']
        if 'trade_status' in response:
            self.trade_status = response['trade_status']
