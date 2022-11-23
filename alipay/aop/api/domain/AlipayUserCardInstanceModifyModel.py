#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserCardInstanceModifyModel(object):

    def __init__(self):
        self._active_date = None
        self._balance = None
        self._before_level = None
        self._card_no = None
        self._changed_balance = None
        self._changed_point = None
        self._expiry_date = None
        self._level = None
        self._open_id = None
        self._point = None
        self._user_id = None

    @property
    def active_date(self):
        return self._active_date

    @active_date.setter
    def active_date(self, value):
        self._active_date = value
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
    @property
    def before_level(self):
        return self._before_level

    @before_level.setter
    def before_level(self, value):
        self._before_level = value
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def changed_balance(self):
        return self._changed_balance

    @changed_balance.setter
    def changed_balance(self, value):
        self._changed_balance = value
    @property
    def changed_point(self):
        return self._changed_point

    @changed_point.setter
    def changed_point(self, value):
        self._changed_point = value
    @property
    def expiry_date(self):
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, value):
        self._expiry_date = value
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def point(self):
        return self._point

    @point.setter
    def point(self, value):
        self._point = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.active_date:
            if hasattr(self.active_date, 'to_alipay_dict'):
                params['active_date'] = self.active_date.to_alipay_dict()
            else:
                params['active_date'] = self.active_date
        if self.balance:
            if hasattr(self.balance, 'to_alipay_dict'):
                params['balance'] = self.balance.to_alipay_dict()
            else:
                params['balance'] = self.balance
        if self.before_level:
            if hasattr(self.before_level, 'to_alipay_dict'):
                params['before_level'] = self.before_level.to_alipay_dict()
            else:
                params['before_level'] = self.before_level
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.changed_balance:
            if hasattr(self.changed_balance, 'to_alipay_dict'):
                params['changed_balance'] = self.changed_balance.to_alipay_dict()
            else:
                params['changed_balance'] = self.changed_balance
        if self.changed_point:
            if hasattr(self.changed_point, 'to_alipay_dict'):
                params['changed_point'] = self.changed_point.to_alipay_dict()
            else:
                params['changed_point'] = self.changed_point
        if self.expiry_date:
            if hasattr(self.expiry_date, 'to_alipay_dict'):
                params['expiry_date'] = self.expiry_date.to_alipay_dict()
            else:
                params['expiry_date'] = self.expiry_date
        if self.level:
            if hasattr(self.level, 'to_alipay_dict'):
                params['level'] = self.level.to_alipay_dict()
            else:
                params['level'] = self.level
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.point:
            if hasattr(self.point, 'to_alipay_dict'):
                params['point'] = self.point.to_alipay_dict()
            else:
                params['point'] = self.point
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserCardInstanceModifyModel()
        if 'active_date' in d:
            o.active_date = d['active_date']
        if 'balance' in d:
            o.balance = d['balance']
        if 'before_level' in d:
            o.before_level = d['before_level']
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'changed_balance' in d:
            o.changed_balance = d['changed_balance']
        if 'changed_point' in d:
            o.changed_point = d['changed_point']
        if 'expiry_date' in d:
            o.expiry_date = d['expiry_date']
        if 'level' in d:
            o.level = d['level']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'point' in d:
            o.point = d['point']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


