#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderBusinessInfo(object):

    def __init__(self):
        self._card_balance = None
        self._card_name = None
        self._cardid = None
        self._consumption_amount = None
        self._consumption_project = None
        self._details = None
        self._recharge_amount = None
        self._recharge_time = None
        self._refund_amount = None
        self._reminder = None

    @property
    def card_balance(self):
        return self._card_balance

    @card_balance.setter
    def card_balance(self, value):
        self._card_balance = value
    @property
    def card_name(self):
        return self._card_name

    @card_name.setter
    def card_name(self, value):
        self._card_name = value
    @property
    def cardid(self):
        return self._cardid

    @cardid.setter
    def cardid(self, value):
        self._cardid = value
    @property
    def consumption_amount(self):
        return self._consumption_amount

    @consumption_amount.setter
    def consumption_amount(self, value):
        self._consumption_amount = value
    @property
    def consumption_project(self):
        return self._consumption_project

    @consumption_project.setter
    def consumption_project(self, value):
        self._consumption_project = value
    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, value):
        self._details = value
    @property
    def recharge_amount(self):
        return self._recharge_amount

    @recharge_amount.setter
    def recharge_amount(self, value):
        self._recharge_amount = value
    @property
    def recharge_time(self):
        return self._recharge_time

    @recharge_time.setter
    def recharge_time(self, value):
        self._recharge_time = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def reminder(self):
        return self._reminder

    @reminder.setter
    def reminder(self, value):
        self._reminder = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_balance:
            if hasattr(self.card_balance, 'to_alipay_dict'):
                params['card_balance'] = self.card_balance.to_alipay_dict()
            else:
                params['card_balance'] = self.card_balance
        if self.card_name:
            if hasattr(self.card_name, 'to_alipay_dict'):
                params['card_name'] = self.card_name.to_alipay_dict()
            else:
                params['card_name'] = self.card_name
        if self.cardid:
            if hasattr(self.cardid, 'to_alipay_dict'):
                params['cardid'] = self.cardid.to_alipay_dict()
            else:
                params['cardid'] = self.cardid
        if self.consumption_amount:
            if hasattr(self.consumption_amount, 'to_alipay_dict'):
                params['consumption_amount'] = self.consumption_amount.to_alipay_dict()
            else:
                params['consumption_amount'] = self.consumption_amount
        if self.consumption_project:
            if hasattr(self.consumption_project, 'to_alipay_dict'):
                params['consumption_project'] = self.consumption_project.to_alipay_dict()
            else:
                params['consumption_project'] = self.consumption_project
        if self.details:
            if hasattr(self.details, 'to_alipay_dict'):
                params['details'] = self.details.to_alipay_dict()
            else:
                params['details'] = self.details
        if self.recharge_amount:
            if hasattr(self.recharge_amount, 'to_alipay_dict'):
                params['recharge_amount'] = self.recharge_amount.to_alipay_dict()
            else:
                params['recharge_amount'] = self.recharge_amount
        if self.recharge_time:
            if hasattr(self.recharge_time, 'to_alipay_dict'):
                params['recharge_time'] = self.recharge_time.to_alipay_dict()
            else:
                params['recharge_time'] = self.recharge_time
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.reminder:
            if hasattr(self.reminder, 'to_alipay_dict'):
                params['reminder'] = self.reminder.to_alipay_dict()
            else:
                params['reminder'] = self.reminder
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderBusinessInfo()
        if 'card_balance' in d:
            o.card_balance = d['card_balance']
        if 'card_name' in d:
            o.card_name = d['card_name']
        if 'cardid' in d:
            o.cardid = d['cardid']
        if 'consumption_amount' in d:
            o.consumption_amount = d['consumption_amount']
        if 'consumption_project' in d:
            o.consumption_project = d['consumption_project']
        if 'details' in d:
            o.details = d['details']
        if 'recharge_amount' in d:
            o.recharge_amount = d['recharge_amount']
        if 'recharge_time' in d:
            o.recharge_time = d['recharge_time']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'reminder' in d:
            o.reminder = d['reminder']
        return o


