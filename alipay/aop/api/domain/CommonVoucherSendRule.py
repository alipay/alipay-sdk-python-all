#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CommonVoucherSendRule(object):

    def __init__(self):
        self._max_quantity_by_day = None
        self._natural_person_limit = None
        self._phone_number_limit = None
        self._real_name_limit = None
        self._voucher_quantity = None
        self._voucher_quantity_limit_per_user = None
        self._voucher_quantity_limit_per_user_period_type = None

    @property
    def max_quantity_by_day(self):
        return self._max_quantity_by_day

    @max_quantity_by_day.setter
    def max_quantity_by_day(self, value):
        self._max_quantity_by_day = value
    @property
    def natural_person_limit(self):
        return self._natural_person_limit

    @natural_person_limit.setter
    def natural_person_limit(self, value):
        self._natural_person_limit = value
    @property
    def phone_number_limit(self):
        return self._phone_number_limit

    @phone_number_limit.setter
    def phone_number_limit(self, value):
        self._phone_number_limit = value
    @property
    def real_name_limit(self):
        return self._real_name_limit

    @real_name_limit.setter
    def real_name_limit(self, value):
        self._real_name_limit = value
    @property
    def voucher_quantity(self):
        return self._voucher_quantity

    @voucher_quantity.setter
    def voucher_quantity(self, value):
        self._voucher_quantity = value
    @property
    def voucher_quantity_limit_per_user(self):
        return self._voucher_quantity_limit_per_user

    @voucher_quantity_limit_per_user.setter
    def voucher_quantity_limit_per_user(self, value):
        self._voucher_quantity_limit_per_user = value
    @property
    def voucher_quantity_limit_per_user_period_type(self):
        return self._voucher_quantity_limit_per_user_period_type

    @voucher_quantity_limit_per_user_period_type.setter
    def voucher_quantity_limit_per_user_period_type(self, value):
        self._voucher_quantity_limit_per_user_period_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.max_quantity_by_day:
            if hasattr(self.max_quantity_by_day, 'to_alipay_dict'):
                params['max_quantity_by_day'] = self.max_quantity_by_day.to_alipay_dict()
            else:
                params['max_quantity_by_day'] = self.max_quantity_by_day
        if self.natural_person_limit:
            if hasattr(self.natural_person_limit, 'to_alipay_dict'):
                params['natural_person_limit'] = self.natural_person_limit.to_alipay_dict()
            else:
                params['natural_person_limit'] = self.natural_person_limit
        if self.phone_number_limit:
            if hasattr(self.phone_number_limit, 'to_alipay_dict'):
                params['phone_number_limit'] = self.phone_number_limit.to_alipay_dict()
            else:
                params['phone_number_limit'] = self.phone_number_limit
        if self.real_name_limit:
            if hasattr(self.real_name_limit, 'to_alipay_dict'):
                params['real_name_limit'] = self.real_name_limit.to_alipay_dict()
            else:
                params['real_name_limit'] = self.real_name_limit
        if self.voucher_quantity:
            if hasattr(self.voucher_quantity, 'to_alipay_dict'):
                params['voucher_quantity'] = self.voucher_quantity.to_alipay_dict()
            else:
                params['voucher_quantity'] = self.voucher_quantity
        if self.voucher_quantity_limit_per_user:
            if hasattr(self.voucher_quantity_limit_per_user, 'to_alipay_dict'):
                params['voucher_quantity_limit_per_user'] = self.voucher_quantity_limit_per_user.to_alipay_dict()
            else:
                params['voucher_quantity_limit_per_user'] = self.voucher_quantity_limit_per_user
        if self.voucher_quantity_limit_per_user_period_type:
            if hasattr(self.voucher_quantity_limit_per_user_period_type, 'to_alipay_dict'):
                params['voucher_quantity_limit_per_user_period_type'] = self.voucher_quantity_limit_per_user_period_type.to_alipay_dict()
            else:
                params['voucher_quantity_limit_per_user_period_type'] = self.voucher_quantity_limit_per_user_period_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CommonVoucherSendRule()
        if 'max_quantity_by_day' in d:
            o.max_quantity_by_day = d['max_quantity_by_day']
        if 'natural_person_limit' in d:
            o.natural_person_limit = d['natural_person_limit']
        if 'phone_number_limit' in d:
            o.phone_number_limit = d['phone_number_limit']
        if 'real_name_limit' in d:
            o.real_name_limit = d['real_name_limit']
        if 'voucher_quantity' in d:
            o.voucher_quantity = d['voucher_quantity']
        if 'voucher_quantity_limit_per_user' in d:
            o.voucher_quantity_limit_per_user = d['voucher_quantity_limit_per_user']
        if 'voucher_quantity_limit_per_user_period_type' in d:
            o.voucher_quantity_limit_per_user_period_type = d['voucher_quantity_limit_per_user_period_type']
        return o


