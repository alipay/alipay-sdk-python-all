#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserRegisterDiscountInfo(object):

    def __init__(self):
        self._register_time = None
        self._user_remaining_discount_count = None
        self._user_total_discount_count = None
        self._user_total_use_discount_amount = None

    @property
    def register_time(self):
        return self._register_time

    @register_time.setter
    def register_time(self, value):
        self._register_time = value
    @property
    def user_remaining_discount_count(self):
        return self._user_remaining_discount_count

    @user_remaining_discount_count.setter
    def user_remaining_discount_count(self, value):
        self._user_remaining_discount_count = value
    @property
    def user_total_discount_count(self):
        return self._user_total_discount_count

    @user_total_discount_count.setter
    def user_total_discount_count(self, value):
        self._user_total_discount_count = value
    @property
    def user_total_use_discount_amount(self):
        return self._user_total_use_discount_amount

    @user_total_use_discount_amount.setter
    def user_total_use_discount_amount(self, value):
        self._user_total_use_discount_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.register_time:
            if hasattr(self.register_time, 'to_alipay_dict'):
                params['register_time'] = self.register_time.to_alipay_dict()
            else:
                params['register_time'] = self.register_time
        if self.user_remaining_discount_count:
            if hasattr(self.user_remaining_discount_count, 'to_alipay_dict'):
                params['user_remaining_discount_count'] = self.user_remaining_discount_count.to_alipay_dict()
            else:
                params['user_remaining_discount_count'] = self.user_remaining_discount_count
        if self.user_total_discount_count:
            if hasattr(self.user_total_discount_count, 'to_alipay_dict'):
                params['user_total_discount_count'] = self.user_total_discount_count.to_alipay_dict()
            else:
                params['user_total_discount_count'] = self.user_total_discount_count
        if self.user_total_use_discount_amount:
            if hasattr(self.user_total_use_discount_amount, 'to_alipay_dict'):
                params['user_total_use_discount_amount'] = self.user_total_use_discount_amount.to_alipay_dict()
            else:
                params['user_total_use_discount_amount'] = self.user_total_use_discount_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserRegisterDiscountInfo()
        if 'register_time' in d:
            o.register_time = d['register_time']
        if 'user_remaining_discount_count' in d:
            o.user_remaining_discount_count = d['user_remaining_discount_count']
        if 'user_total_discount_count' in d:
            o.user_total_discount_count = d['user_total_discount_count']
        if 'user_total_use_discount_amount' in d:
            o.user_total_use_discount_amount = d['user_total_use_discount_amount']
        return o


