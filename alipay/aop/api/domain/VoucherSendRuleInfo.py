#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherSendRuleInfo(object):

    def __init__(self):
        self._max_quantity_by_day = None
        self._natural_person_limit = None
        self._phone_number_limit = None
        self._phone_number_need_input_limit = None
        self._publish_end_time = None
        self._publish_start_time = None
        self._quantity = None
        self._quantity_limit_per_user = None
        self._quantity_limit_per_user_period_type = None
        self._real_name_limit = None

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
    def phone_number_need_input_limit(self):
        return self._phone_number_need_input_limit

    @phone_number_need_input_limit.setter
    def phone_number_need_input_limit(self, value):
        self._phone_number_need_input_limit = value
    @property
    def publish_end_time(self):
        return self._publish_end_time

    @publish_end_time.setter
    def publish_end_time(self, value):
        self._publish_end_time = value
    @property
    def publish_start_time(self):
        return self._publish_start_time

    @publish_start_time.setter
    def publish_start_time(self, value):
        self._publish_start_time = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def quantity_limit_per_user(self):
        return self._quantity_limit_per_user

    @quantity_limit_per_user.setter
    def quantity_limit_per_user(self, value):
        self._quantity_limit_per_user = value
    @property
    def quantity_limit_per_user_period_type(self):
        return self._quantity_limit_per_user_period_type

    @quantity_limit_per_user_period_type.setter
    def quantity_limit_per_user_period_type(self, value):
        self._quantity_limit_per_user_period_type = value
    @property
    def real_name_limit(self):
        return self._real_name_limit

    @real_name_limit.setter
    def real_name_limit(self, value):
        self._real_name_limit = value


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
        if self.phone_number_need_input_limit:
            if hasattr(self.phone_number_need_input_limit, 'to_alipay_dict'):
                params['phone_number_need_input_limit'] = self.phone_number_need_input_limit.to_alipay_dict()
            else:
                params['phone_number_need_input_limit'] = self.phone_number_need_input_limit
        if self.publish_end_time:
            if hasattr(self.publish_end_time, 'to_alipay_dict'):
                params['publish_end_time'] = self.publish_end_time.to_alipay_dict()
            else:
                params['publish_end_time'] = self.publish_end_time
        if self.publish_start_time:
            if hasattr(self.publish_start_time, 'to_alipay_dict'):
                params['publish_start_time'] = self.publish_start_time.to_alipay_dict()
            else:
                params['publish_start_time'] = self.publish_start_time
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.quantity_limit_per_user:
            if hasattr(self.quantity_limit_per_user, 'to_alipay_dict'):
                params['quantity_limit_per_user'] = self.quantity_limit_per_user.to_alipay_dict()
            else:
                params['quantity_limit_per_user'] = self.quantity_limit_per_user
        if self.quantity_limit_per_user_period_type:
            if hasattr(self.quantity_limit_per_user_period_type, 'to_alipay_dict'):
                params['quantity_limit_per_user_period_type'] = self.quantity_limit_per_user_period_type.to_alipay_dict()
            else:
                params['quantity_limit_per_user_period_type'] = self.quantity_limit_per_user_period_type
        if self.real_name_limit:
            if hasattr(self.real_name_limit, 'to_alipay_dict'):
                params['real_name_limit'] = self.real_name_limit.to_alipay_dict()
            else:
                params['real_name_limit'] = self.real_name_limit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherSendRuleInfo()
        if 'max_quantity_by_day' in d:
            o.max_quantity_by_day = d['max_quantity_by_day']
        if 'natural_person_limit' in d:
            o.natural_person_limit = d['natural_person_limit']
        if 'phone_number_limit' in d:
            o.phone_number_limit = d['phone_number_limit']
        if 'phone_number_need_input_limit' in d:
            o.phone_number_need_input_limit = d['phone_number_need_input_limit']
        if 'publish_end_time' in d:
            o.publish_end_time = d['publish_end_time']
        if 'publish_start_time' in d:
            o.publish_start_time = d['publish_start_time']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'quantity_limit_per_user' in d:
            o.quantity_limit_per_user = d['quantity_limit_per_user']
        if 'quantity_limit_per_user_period_type' in d:
            o.quantity_limit_per_user_period_type = d['quantity_limit_per_user_period_type']
        if 'real_name_limit' in d:
            o.real_name_limit = d['real_name_limit']
        return o


