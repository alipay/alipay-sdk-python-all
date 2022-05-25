#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TimeCardSimpleItemInfo import TimeCardSimpleItemInfo


class TimeCardUseLogRecordInfo(object):

    def __init__(self):
        self._amount = None
        self._card_id = None
        self._log_id = None
        self._log_time = None
        self._log_type = None
        self._time_card_info = None
        self._user_id = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value
    @property
    def log_id(self):
        return self._log_id

    @log_id.setter
    def log_id(self, value):
        self._log_id = value
    @property
    def log_time(self):
        return self._log_time

    @log_time.setter
    def log_time(self, value):
        self._log_time = value
    @property
    def log_type(self):
        return self._log_type

    @log_type.setter
    def log_type(self, value):
        self._log_type = value
    @property
    def time_card_info(self):
        return self._time_card_info

    @time_card_info.setter
    def time_card_info(self, value):
        if isinstance(value, TimeCardSimpleItemInfo):
            self._time_card_info = value
        else:
            self._time_card_info = TimeCardSimpleItemInfo.from_alipay_dict(value)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.card_id:
            if hasattr(self.card_id, 'to_alipay_dict'):
                params['card_id'] = self.card_id.to_alipay_dict()
            else:
                params['card_id'] = self.card_id
        if self.log_id:
            if hasattr(self.log_id, 'to_alipay_dict'):
                params['log_id'] = self.log_id.to_alipay_dict()
            else:
                params['log_id'] = self.log_id
        if self.log_time:
            if hasattr(self.log_time, 'to_alipay_dict'):
                params['log_time'] = self.log_time.to_alipay_dict()
            else:
                params['log_time'] = self.log_time
        if self.log_type:
            if hasattr(self.log_type, 'to_alipay_dict'):
                params['log_type'] = self.log_type.to_alipay_dict()
            else:
                params['log_type'] = self.log_type
        if self.time_card_info:
            if hasattr(self.time_card_info, 'to_alipay_dict'):
                params['time_card_info'] = self.time_card_info.to_alipay_dict()
            else:
                params['time_card_info'] = self.time_card_info
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
        o = TimeCardUseLogRecordInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'card_id' in d:
            o.card_id = d['card_id']
        if 'log_id' in d:
            o.log_id = d['log_id']
        if 'log_time' in d:
            o.log_time = d['log_time']
        if 'log_type' in d:
            o.log_type = d['log_type']
        if 'time_card_info' in d:
            o.time_card_info = d['time_card_info']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


