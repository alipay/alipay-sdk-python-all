#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.Money import Money
from alipay.aop.api.domain.ReceiptQuoteInfo import ReceiptQuoteInfo
from alipay.aop.api.domain.Money import Money


class AlipayOverseasRemitFxtradeorderCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasRemitFxtradeorderCreateResponse, self).__init__()
        self._bc_remit_id = None
        self._contra_amount = None
        self._currency_pair = None
        self._extend_info = None
        self._fx_order_time = None
        self._fx_trade_order_id = None
        self._fx_trade_side = None
        self._quote_info = None
        self._receiver_mid = None
        self._sender_mid = None
        self._trans_amount = None

    @property
    def bc_remit_id(self):
        return self._bc_remit_id

    @bc_remit_id.setter
    def bc_remit_id(self, value):
        self._bc_remit_id = value
    @property
    def contra_amount(self):
        return self._contra_amount

    @contra_amount.setter
    def contra_amount(self, value):
        if isinstance(value, Money):
            self._contra_amount = value
        else:
            self._contra_amount = Money.from_alipay_dict(value)
    @property
    def currency_pair(self):
        return self._currency_pair

    @currency_pair.setter
    def currency_pair(self, value):
        self._currency_pair = value
    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value
    @property
    def fx_order_time(self):
        return self._fx_order_time

    @fx_order_time.setter
    def fx_order_time(self, value):
        self._fx_order_time = value
    @property
    def fx_trade_order_id(self):
        return self._fx_trade_order_id

    @fx_trade_order_id.setter
    def fx_trade_order_id(self, value):
        self._fx_trade_order_id = value
    @property
    def fx_trade_side(self):
        return self._fx_trade_side

    @fx_trade_side.setter
    def fx_trade_side(self, value):
        self._fx_trade_side = value
    @property
    def quote_info(self):
        return self._quote_info

    @quote_info.setter
    def quote_info(self, value):
        if isinstance(value, ReceiptQuoteInfo):
            self._quote_info = value
        else:
            self._quote_info = ReceiptQuoteInfo.from_alipay_dict(value)
    @property
    def receiver_mid(self):
        return self._receiver_mid

    @receiver_mid.setter
    def receiver_mid(self, value):
        self._receiver_mid = value
    @property
    def sender_mid(self):
        return self._sender_mid

    @sender_mid.setter
    def sender_mid(self, value):
        self._sender_mid = value
    @property
    def trans_amount(self):
        return self._trans_amount

    @trans_amount.setter
    def trans_amount(self, value):
        if isinstance(value, Money):
            self._trans_amount = value
        else:
            self._trans_amount = Money.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasRemitFxtradeorderCreateResponse, self).parse_response_content(response_content)
        if 'bc_remit_id' in response:
            self.bc_remit_id = response['bc_remit_id']
        if 'contra_amount' in response:
            self.contra_amount = response['contra_amount']
        if 'currency_pair' in response:
            self.currency_pair = response['currency_pair']
        if 'extend_info' in response:
            self.extend_info = response['extend_info']
        if 'fx_order_time' in response:
            self.fx_order_time = response['fx_order_time']
        if 'fx_trade_order_id' in response:
            self.fx_trade_order_id = response['fx_trade_order_id']
        if 'fx_trade_side' in response:
            self.fx_trade_side = response['fx_trade_side']
        if 'quote_info' in response:
            self.quote_info = response['quote_info']
        if 'receiver_mid' in response:
            self.receiver_mid = response['receiver_mid']
        if 'sender_mid' in response:
            self.sender_mid = response['sender_mid']
        if 'trans_amount' in response:
            self.trans_amount = response['trans_amount']
