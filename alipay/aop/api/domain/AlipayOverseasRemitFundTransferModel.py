#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasRemitFundTransferModel(object):

    def __init__(self):
        self._base_currency = None
        self._bc_remit_id = None
        self._exchange_rate = None
        self._receiver_amount = None
        self._receiver_currency = None
        self._receiver_mid = None
        self._sender_amount = None
        self._sender_currency = None
        self._sender_mid = None

    @property
    def base_currency(self):
        return self._base_currency

    @base_currency.setter
    def base_currency(self, value):
        self._base_currency = value
    @property
    def bc_remit_id(self):
        return self._bc_remit_id

    @bc_remit_id.setter
    def bc_remit_id(self, value):
        self._bc_remit_id = value
    @property
    def exchange_rate(self):
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, value):
        self._exchange_rate = value
    @property
    def receiver_amount(self):
        return self._receiver_amount

    @receiver_amount.setter
    def receiver_amount(self, value):
        self._receiver_amount = value
    @property
    def receiver_currency(self):
        return self._receiver_currency

    @receiver_currency.setter
    def receiver_currency(self, value):
        self._receiver_currency = value
    @property
    def receiver_mid(self):
        return self._receiver_mid

    @receiver_mid.setter
    def receiver_mid(self, value):
        self._receiver_mid = value
    @property
    def sender_amount(self):
        return self._sender_amount

    @sender_amount.setter
    def sender_amount(self, value):
        self._sender_amount = value
    @property
    def sender_currency(self):
        return self._sender_currency

    @sender_currency.setter
    def sender_currency(self, value):
        self._sender_currency = value
    @property
    def sender_mid(self):
        return self._sender_mid

    @sender_mid.setter
    def sender_mid(self, value):
        self._sender_mid = value


    def to_alipay_dict(self):
        params = dict()
        if self.base_currency:
            if hasattr(self.base_currency, 'to_alipay_dict'):
                params['base_currency'] = self.base_currency.to_alipay_dict()
            else:
                params['base_currency'] = self.base_currency
        if self.bc_remit_id:
            if hasattr(self.bc_remit_id, 'to_alipay_dict'):
                params['bc_remit_id'] = self.bc_remit_id.to_alipay_dict()
            else:
                params['bc_remit_id'] = self.bc_remit_id
        if self.exchange_rate:
            if hasattr(self.exchange_rate, 'to_alipay_dict'):
                params['exchange_rate'] = self.exchange_rate.to_alipay_dict()
            else:
                params['exchange_rate'] = self.exchange_rate
        if self.receiver_amount:
            if hasattr(self.receiver_amount, 'to_alipay_dict'):
                params['receiver_amount'] = self.receiver_amount.to_alipay_dict()
            else:
                params['receiver_amount'] = self.receiver_amount
        if self.receiver_currency:
            if hasattr(self.receiver_currency, 'to_alipay_dict'):
                params['receiver_currency'] = self.receiver_currency.to_alipay_dict()
            else:
                params['receiver_currency'] = self.receiver_currency
        if self.receiver_mid:
            if hasattr(self.receiver_mid, 'to_alipay_dict'):
                params['receiver_mid'] = self.receiver_mid.to_alipay_dict()
            else:
                params['receiver_mid'] = self.receiver_mid
        if self.sender_amount:
            if hasattr(self.sender_amount, 'to_alipay_dict'):
                params['sender_amount'] = self.sender_amount.to_alipay_dict()
            else:
                params['sender_amount'] = self.sender_amount
        if self.sender_currency:
            if hasattr(self.sender_currency, 'to_alipay_dict'):
                params['sender_currency'] = self.sender_currency.to_alipay_dict()
            else:
                params['sender_currency'] = self.sender_currency
        if self.sender_mid:
            if hasattr(self.sender_mid, 'to_alipay_dict'):
                params['sender_mid'] = self.sender_mid.to_alipay_dict()
            else:
                params['sender_mid'] = self.sender_mid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasRemitFundTransferModel()
        if 'base_currency' in d:
            o.base_currency = d['base_currency']
        if 'bc_remit_id' in d:
            o.bc_remit_id = d['bc_remit_id']
        if 'exchange_rate' in d:
            o.exchange_rate = d['exchange_rate']
        if 'receiver_amount' in d:
            o.receiver_amount = d['receiver_amount']
        if 'receiver_currency' in d:
            o.receiver_currency = d['receiver_currency']
        if 'receiver_mid' in d:
            o.receiver_mid = d['receiver_mid']
        if 'sender_amount' in d:
            o.sender_amount = d['sender_amount']
        if 'sender_currency' in d:
            o.sender_currency = d['sender_currency']
        if 'sender_mid' in d:
            o.sender_mid = d['sender_mid']
        return o


