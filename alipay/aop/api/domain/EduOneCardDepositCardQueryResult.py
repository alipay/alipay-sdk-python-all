#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EduOneCardDepositCardQueryResult(object):

    def __init__(self):
        self._agent_code = None
        self._agent_name = None
        self._balance = None
        self._card_name = None
        self._card_no = None
        self._last_update_time = None
        self._pound_amount = None

    @property
    def agent_code(self):
        return self._agent_code

    @agent_code.setter
    def agent_code(self, value):
        self._agent_code = value
    @property
    def agent_name(self):
        return self._agent_name

    @agent_name.setter
    def agent_name(self, value):
        self._agent_name = value
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
    @property
    def card_name(self):
        return self._card_name

    @card_name.setter
    def card_name(self, value):
        self._card_name = value
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def last_update_time(self):
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, value):
        self._last_update_time = value
    @property
    def pound_amount(self):
        return self._pound_amount

    @pound_amount.setter
    def pound_amount(self, value):
        self._pound_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_code:
            if hasattr(self.agent_code, 'to_alipay_dict'):
                params['agent_code'] = self.agent_code.to_alipay_dict()
            else:
                params['agent_code'] = self.agent_code
        if self.agent_name:
            if hasattr(self.agent_name, 'to_alipay_dict'):
                params['agent_name'] = self.agent_name.to_alipay_dict()
            else:
                params['agent_name'] = self.agent_name
        if self.balance:
            if hasattr(self.balance, 'to_alipay_dict'):
                params['balance'] = self.balance.to_alipay_dict()
            else:
                params['balance'] = self.balance
        if self.card_name:
            if hasattr(self.card_name, 'to_alipay_dict'):
                params['card_name'] = self.card_name.to_alipay_dict()
            else:
                params['card_name'] = self.card_name
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.last_update_time:
            if hasattr(self.last_update_time, 'to_alipay_dict'):
                params['last_update_time'] = self.last_update_time.to_alipay_dict()
            else:
                params['last_update_time'] = self.last_update_time
        if self.pound_amount:
            if hasattr(self.pound_amount, 'to_alipay_dict'):
                params['pound_amount'] = self.pound_amount.to_alipay_dict()
            else:
                params['pound_amount'] = self.pound_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EduOneCardDepositCardQueryResult()
        if 'agent_code' in d:
            o.agent_code = d['agent_code']
        if 'agent_name' in d:
            o.agent_name = d['agent_name']
        if 'balance' in d:
            o.balance = d['balance']
        if 'card_name' in d:
            o.card_name = d['card_name']
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'last_update_time' in d:
            o.last_update_time = d['last_update_time']
        if 'pound_amount' in d:
            o.pound_amount = d['pound_amount']
        return o


