#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserDtbankcustDailydiscountuserQueryModel(object):

    def __init__(self):
        self._account_no = None
        self._activity_id = None
        self._daily_discount_app_id_specify = None
        self._daily_discount_open_id_specify = None
        self._open_id = None
        self._user_id = None

    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def daily_discount_app_id_specify(self):
        return self._daily_discount_app_id_specify

    @daily_discount_app_id_specify.setter
    def daily_discount_app_id_specify(self, value):
        self._daily_discount_app_id_specify = value
    @property
    def daily_discount_open_id_specify(self):
        return self._daily_discount_open_id_specify

    @daily_discount_open_id_specify.setter
    def daily_discount_open_id_specify(self, value):
        self._daily_discount_open_id_specify = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.daily_discount_app_id_specify:
            if hasattr(self.daily_discount_app_id_specify, 'to_alipay_dict'):
                params['daily_discount_app_id_specify'] = self.daily_discount_app_id_specify.to_alipay_dict()
            else:
                params['daily_discount_app_id_specify'] = self.daily_discount_app_id_specify
        if self.daily_discount_open_id_specify:
            if hasattr(self.daily_discount_open_id_specify, 'to_alipay_dict'):
                params['daily_discount_open_id_specify'] = self.daily_discount_open_id_specify.to_alipay_dict()
            else:
                params['daily_discount_open_id_specify'] = self.daily_discount_open_id_specify
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
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
        o = AlipayUserDtbankcustDailydiscountuserQueryModel()
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'daily_discount_app_id_specify' in d:
            o.daily_discount_app_id_specify = d['daily_discount_app_id_specify']
        if 'daily_discount_open_id_specify' in d:
            o.daily_discount_open_id_specify = d['daily_discount_open_id_specify']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


