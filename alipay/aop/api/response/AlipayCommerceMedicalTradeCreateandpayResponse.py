#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalTradeCreateandpayResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalTradeCreateandpayResponse, self).__init__()
        self._alipay_trade_no = None
        self._bank_id = None
        self._bank_name = None
        self._bank_order_id = None
        self._chrg_bch_no = None
        self._med_org_ord = None
        self._order_type = None
        self._out_trade_no = None
        self._pay_order_id = None
        self._pay_url = None
        self._rels_pay_flag = None
        self._rels_pay_user_name = None
        self._trade_no = None

    @property
    def alipay_trade_no(self):
        return self._alipay_trade_no

    @alipay_trade_no.setter
    def alipay_trade_no(self, value):
        self._alipay_trade_no = value
    @property
    def bank_id(self):
        return self._bank_id

    @bank_id.setter
    def bank_id(self, value):
        self._bank_id = value
    @property
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, value):
        self._bank_name = value
    @property
    def bank_order_id(self):
        return self._bank_order_id

    @bank_order_id.setter
    def bank_order_id(self, value):
        self._bank_order_id = value
    @property
    def chrg_bch_no(self):
        return self._chrg_bch_no

    @chrg_bch_no.setter
    def chrg_bch_no(self, value):
        self._chrg_bch_no = value
    @property
    def med_org_ord(self):
        return self._med_org_ord

    @med_org_ord.setter
    def med_org_ord(self, value):
        self._med_org_ord = value
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
    def pay_order_id(self):
        return self._pay_order_id

    @pay_order_id.setter
    def pay_order_id(self, value):
        self._pay_order_id = value
    @property
    def pay_url(self):
        return self._pay_url

    @pay_url.setter
    def pay_url(self, value):
        self._pay_url = value
    @property
    def rels_pay_flag(self):
        return self._rels_pay_flag

    @rels_pay_flag.setter
    def rels_pay_flag(self, value):
        self._rels_pay_flag = value
    @property
    def rels_pay_user_name(self):
        return self._rels_pay_user_name

    @rels_pay_user_name.setter
    def rels_pay_user_name(self, value):
        self._rels_pay_user_name = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalTradeCreateandpayResponse, self).parse_response_content(response_content)
        if 'alipay_trade_no' in response:
            self.alipay_trade_no = response['alipay_trade_no']
        if 'bank_id' in response:
            self.bank_id = response['bank_id']
        if 'bank_name' in response:
            self.bank_name = response['bank_name']
        if 'bank_order_id' in response:
            self.bank_order_id = response['bank_order_id']
        if 'chrg_bch_no' in response:
            self.chrg_bch_no = response['chrg_bch_no']
        if 'med_org_ord' in response:
            self.med_org_ord = response['med_org_ord']
        if 'order_type' in response:
            self.order_type = response['order_type']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'pay_order_id' in response:
            self.pay_order_id = response['pay_order_id']
        if 'pay_url' in response:
            self.pay_url = response['pay_url']
        if 'rels_pay_flag' in response:
            self.rels_pay_flag = response['rels_pay_flag']
        if 'rels_pay_user_name' in response:
            self.rels_pay_user_name = response['rels_pay_user_name']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
