#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TradeFundBill import TradeFundBill
from alipay.aop.api.domain.PresetPayToolInfo import PresetPayToolInfo


class AlipayTradeRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeRefundResponse, self).__init__()
        self._buyer_logon_id = None
        self._buyer_user_id = None
        self._fund_change = None
        self._gmt_refund_pay = None
        self._open_id = None
        self._out_trade_no = None
        self._present_refund_buyer_amount = None
        self._present_refund_discount_amount = None
        self._present_refund_mdiscount_amount = None
        self._refund_charge_amount = None
        self._refund_currency = None
        self._refund_detail_item_list = None
        self._refund_fee = None
        self._refund_preset_paytool_list = None
        self._refund_settlement_id = None
        self._send_back_fee = None
        self._store_name = None
        self._trade_no = None

    @property
    def buyer_logon_id(self):
        return self._buyer_logon_id

    @buyer_logon_id.setter
    def buyer_logon_id(self, value):
        self._buyer_logon_id = value
    @property
    def buyer_user_id(self):
        return self._buyer_user_id

    @buyer_user_id.setter
    def buyer_user_id(self, value):
        self._buyer_user_id = value
    @property
    def fund_change(self):
        return self._fund_change

    @fund_change.setter
    def fund_change(self, value):
        self._fund_change = value
    @property
    def gmt_refund_pay(self):
        return self._gmt_refund_pay

    @gmt_refund_pay.setter
    def gmt_refund_pay(self, value):
        self._gmt_refund_pay = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def present_refund_buyer_amount(self):
        return self._present_refund_buyer_amount

    @present_refund_buyer_amount.setter
    def present_refund_buyer_amount(self, value):
        self._present_refund_buyer_amount = value
    @property
    def present_refund_discount_amount(self):
        return self._present_refund_discount_amount

    @present_refund_discount_amount.setter
    def present_refund_discount_amount(self, value):
        self._present_refund_discount_amount = value
    @property
    def present_refund_mdiscount_amount(self):
        return self._present_refund_mdiscount_amount

    @present_refund_mdiscount_amount.setter
    def present_refund_mdiscount_amount(self, value):
        self._present_refund_mdiscount_amount = value
    @property
    def refund_charge_amount(self):
        return self._refund_charge_amount

    @refund_charge_amount.setter
    def refund_charge_amount(self, value):
        self._refund_charge_amount = value
    @property
    def refund_currency(self):
        return self._refund_currency

    @refund_currency.setter
    def refund_currency(self, value):
        self._refund_currency = value
    @property
    def refund_detail_item_list(self):
        return self._refund_detail_item_list

    @refund_detail_item_list.setter
    def refund_detail_item_list(self, value):
        if isinstance(value, list):
            self._refund_detail_item_list = list()
            for i in value:
                if isinstance(i, TradeFundBill):
                    self._refund_detail_item_list.append(i)
                else:
                    self._refund_detail_item_list.append(TradeFundBill.from_alipay_dict(i))
    @property
    def refund_fee(self):
        return self._refund_fee

    @refund_fee.setter
    def refund_fee(self, value):
        self._refund_fee = value
    @property
    def refund_preset_paytool_list(self):
        return self._refund_preset_paytool_list

    @refund_preset_paytool_list.setter
    def refund_preset_paytool_list(self, value):
        if isinstance(value, PresetPayToolInfo):
            self._refund_preset_paytool_list = value
        else:
            self._refund_preset_paytool_list = PresetPayToolInfo.from_alipay_dict(value)
    @property
    def refund_settlement_id(self):
        return self._refund_settlement_id

    @refund_settlement_id.setter
    def refund_settlement_id(self, value):
        self._refund_settlement_id = value
    @property
    def send_back_fee(self):
        return self._send_back_fee

    @send_back_fee.setter
    def send_back_fee(self, value):
        self._send_back_fee = value
    @property
    def store_name(self):
        return self._store_name

    @store_name.setter
    def store_name(self, value):
        self._store_name = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeRefundResponse, self).parse_response_content(response_content)
        if 'buyer_logon_id' in response:
            self.buyer_logon_id = response['buyer_logon_id']
        if 'buyer_user_id' in response:
            self.buyer_user_id = response['buyer_user_id']
        if 'fund_change' in response:
            self.fund_change = response['fund_change']
        if 'gmt_refund_pay' in response:
            self.gmt_refund_pay = response['gmt_refund_pay']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'present_refund_buyer_amount' in response:
            self.present_refund_buyer_amount = response['present_refund_buyer_amount']
        if 'present_refund_discount_amount' in response:
            self.present_refund_discount_amount = response['present_refund_discount_amount']
        if 'present_refund_mdiscount_amount' in response:
            self.present_refund_mdiscount_amount = response['present_refund_mdiscount_amount']
        if 'refund_charge_amount' in response:
            self.refund_charge_amount = response['refund_charge_amount']
        if 'refund_currency' in response:
            self.refund_currency = response['refund_currency']
        if 'refund_detail_item_list' in response:
            self.refund_detail_item_list = response['refund_detail_item_list']
        if 'refund_fee' in response:
            self.refund_fee = response['refund_fee']
        if 'refund_preset_paytool_list' in response:
            self.refund_preset_paytool_list = response['refund_preset_paytool_list']
        if 'refund_settlement_id' in response:
            self.refund_settlement_id = response['refund_settlement_id']
        if 'send_back_fee' in response:
            self.send_back_fee = response['send_back_fee']
        if 'store_name' in response:
            self.store_name = response['store_name']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
