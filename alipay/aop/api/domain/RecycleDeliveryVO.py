#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleDeliveryVO(object):

    def __init__(self):
        self._actual_time = None
        self._delivery_status = None
        self._delivery_type = None
        self._end_time = None
        self._logistic_bill_no = None
        self._logistic_platform = None
        self._staff_phone = None
        self._start_time = None
        self._user_address = None
        self._user_phone = None

    @property
    def actual_time(self):
        return self._actual_time

    @actual_time.setter
    def actual_time(self, value):
        self._actual_time = value
    @property
    def delivery_status(self):
        return self._delivery_status

    @delivery_status.setter
    def delivery_status(self, value):
        self._delivery_status = value
    @property
    def delivery_type(self):
        return self._delivery_type

    @delivery_type.setter
    def delivery_type(self, value):
        self._delivery_type = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def logistic_bill_no(self):
        return self._logistic_bill_no

    @logistic_bill_no.setter
    def logistic_bill_no(self, value):
        self._logistic_bill_no = value
    @property
    def logistic_platform(self):
        return self._logistic_platform

    @logistic_platform.setter
    def logistic_platform(self, value):
        self._logistic_platform = value
    @property
    def staff_phone(self):
        return self._staff_phone

    @staff_phone.setter
    def staff_phone(self, value):
        self._staff_phone = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def user_address(self):
        return self._user_address

    @user_address.setter
    def user_address(self, value):
        self._user_address = value
    @property
    def user_phone(self):
        return self._user_phone

    @user_phone.setter
    def user_phone(self, value):
        self._user_phone = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_time:
            if hasattr(self.actual_time, 'to_alipay_dict'):
                params['actual_time'] = self.actual_time.to_alipay_dict()
            else:
                params['actual_time'] = self.actual_time
        if self.delivery_status:
            if hasattr(self.delivery_status, 'to_alipay_dict'):
                params['delivery_status'] = self.delivery_status.to_alipay_dict()
            else:
                params['delivery_status'] = self.delivery_status
        if self.delivery_type:
            if hasattr(self.delivery_type, 'to_alipay_dict'):
                params['delivery_type'] = self.delivery_type.to_alipay_dict()
            else:
                params['delivery_type'] = self.delivery_type
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.logistic_bill_no:
            if hasattr(self.logistic_bill_no, 'to_alipay_dict'):
                params['logistic_bill_no'] = self.logistic_bill_no.to_alipay_dict()
            else:
                params['logistic_bill_no'] = self.logistic_bill_no
        if self.logistic_platform:
            if hasattr(self.logistic_platform, 'to_alipay_dict'):
                params['logistic_platform'] = self.logistic_platform.to_alipay_dict()
            else:
                params['logistic_platform'] = self.logistic_platform
        if self.staff_phone:
            if hasattr(self.staff_phone, 'to_alipay_dict'):
                params['staff_phone'] = self.staff_phone.to_alipay_dict()
            else:
                params['staff_phone'] = self.staff_phone
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.user_address:
            if hasattr(self.user_address, 'to_alipay_dict'):
                params['user_address'] = self.user_address.to_alipay_dict()
            else:
                params['user_address'] = self.user_address
        if self.user_phone:
            if hasattr(self.user_phone, 'to_alipay_dict'):
                params['user_phone'] = self.user_phone.to_alipay_dict()
            else:
                params['user_phone'] = self.user_phone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleDeliveryVO()
        if 'actual_time' in d:
            o.actual_time = d['actual_time']
        if 'delivery_status' in d:
            o.delivery_status = d['delivery_status']
        if 'delivery_type' in d:
            o.delivery_type = d['delivery_type']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'logistic_bill_no' in d:
            o.logistic_bill_no = d['logistic_bill_no']
        if 'logistic_platform' in d:
            o.logistic_platform = d['logistic_platform']
        if 'staff_phone' in d:
            o.staff_phone = d['staff_phone']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'user_address' in d:
            o.user_address = d['user_address']
        if 'user_phone' in d:
            o.user_phone = d['user_phone']
        return o


