#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Money import Money


class AlipayOverseasRemitFxtradeorderCreateModel(object):

    def __init__(self):
        self._bc_remit_id = None
        self._currency_pair = None
        self._extend_info = None
        self._fx_trade_order_id = None
        self._fx_trade_side = None
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


    def to_alipay_dict(self):
        params = dict()
        if self.bc_remit_id:
            if hasattr(self.bc_remit_id, 'to_alipay_dict'):
                params['bc_remit_id'] = self.bc_remit_id.to_alipay_dict()
            else:
                params['bc_remit_id'] = self.bc_remit_id
        if self.currency_pair:
            if hasattr(self.currency_pair, 'to_alipay_dict'):
                params['currency_pair'] = self.currency_pair.to_alipay_dict()
            else:
                params['currency_pair'] = self.currency_pair
        if self.extend_info:
            if hasattr(self.extend_info, 'to_alipay_dict'):
                params['extend_info'] = self.extend_info.to_alipay_dict()
            else:
                params['extend_info'] = self.extend_info
        if self.fx_trade_order_id:
            if hasattr(self.fx_trade_order_id, 'to_alipay_dict'):
                params['fx_trade_order_id'] = self.fx_trade_order_id.to_alipay_dict()
            else:
                params['fx_trade_order_id'] = self.fx_trade_order_id
        if self.fx_trade_side:
            if hasattr(self.fx_trade_side, 'to_alipay_dict'):
                params['fx_trade_side'] = self.fx_trade_side.to_alipay_dict()
            else:
                params['fx_trade_side'] = self.fx_trade_side
        if self.receiver_mid:
            if hasattr(self.receiver_mid, 'to_alipay_dict'):
                params['receiver_mid'] = self.receiver_mid.to_alipay_dict()
            else:
                params['receiver_mid'] = self.receiver_mid
        if self.sender_mid:
            if hasattr(self.sender_mid, 'to_alipay_dict'):
                params['sender_mid'] = self.sender_mid.to_alipay_dict()
            else:
                params['sender_mid'] = self.sender_mid
        if self.trans_amount:
            if hasattr(self.trans_amount, 'to_alipay_dict'):
                params['trans_amount'] = self.trans_amount.to_alipay_dict()
            else:
                params['trans_amount'] = self.trans_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasRemitFxtradeorderCreateModel()
        if 'bc_remit_id' in d:
            o.bc_remit_id = d['bc_remit_id']
        if 'currency_pair' in d:
            o.currency_pair = d['currency_pair']
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'fx_trade_order_id' in d:
            o.fx_trade_order_id = d['fx_trade_order_id']
        if 'fx_trade_side' in d:
            o.fx_trade_side = d['fx_trade_side']
        if 'receiver_mid' in d:
            o.receiver_mid = d['receiver_mid']
        if 'sender_mid' in d:
            o.sender_mid = d['sender_mid']
        if 'trans_amount' in d:
            o.trans_amount = d['trans_amount']
        return o


