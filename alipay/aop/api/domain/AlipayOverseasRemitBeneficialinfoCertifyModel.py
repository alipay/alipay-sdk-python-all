#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasRemitBeneficialinfoCertifyModel(object):

    def __init__(self):
        self._chinese_full_name = None
        self._first_name = None
        self._last_name = None
        self._logon_id = None
        self._middle_name = None
        self._order_amount = None
        self._order_currency = None
        self._receiver_mid = None
        self._sender_mid = None

    @property
    def chinese_full_name(self):
        return self._chinese_full_name

    @chinese_full_name.setter
    def chinese_full_name(self, value):
        self._chinese_full_name = value
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value
    @property
    def logon_id(self):
        return self._logon_id

    @logon_id.setter
    def logon_id(self, value):
        self._logon_id = value
    @property
    def middle_name(self):
        return self._middle_name

    @middle_name.setter
    def middle_name(self, value):
        self._middle_name = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def order_currency(self):
        return self._order_currency

    @order_currency.setter
    def order_currency(self, value):
        self._order_currency = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.chinese_full_name:
            if hasattr(self.chinese_full_name, 'to_alipay_dict'):
                params['chinese_full_name'] = self.chinese_full_name.to_alipay_dict()
            else:
                params['chinese_full_name'] = self.chinese_full_name
        if self.first_name:
            if hasattr(self.first_name, 'to_alipay_dict'):
                params['first_name'] = self.first_name.to_alipay_dict()
            else:
                params['first_name'] = self.first_name
        if self.last_name:
            if hasattr(self.last_name, 'to_alipay_dict'):
                params['last_name'] = self.last_name.to_alipay_dict()
            else:
                params['last_name'] = self.last_name
        if self.logon_id:
            if hasattr(self.logon_id, 'to_alipay_dict'):
                params['logon_id'] = self.logon_id.to_alipay_dict()
            else:
                params['logon_id'] = self.logon_id
        if self.middle_name:
            if hasattr(self.middle_name, 'to_alipay_dict'):
                params['middle_name'] = self.middle_name.to_alipay_dict()
            else:
                params['middle_name'] = self.middle_name
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.order_currency:
            if hasattr(self.order_currency, 'to_alipay_dict'):
                params['order_currency'] = self.order_currency.to_alipay_dict()
            else:
                params['order_currency'] = self.order_currency
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasRemitBeneficialinfoCertifyModel()
        if 'chinese_full_name' in d:
            o.chinese_full_name = d['chinese_full_name']
        if 'first_name' in d:
            o.first_name = d['first_name']
        if 'last_name' in d:
            o.last_name = d['last_name']
        if 'logon_id' in d:
            o.logon_id = d['logon_id']
        if 'middle_name' in d:
            o.middle_name = d['middle_name']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'order_currency' in d:
            o.order_currency = d['order_currency']
        if 'receiver_mid' in d:
            o.receiver_mid = d['receiver_mid']
        if 'sender_mid' in d:
            o.sender_mid = d['sender_mid']
        return o


