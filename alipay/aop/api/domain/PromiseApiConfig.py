#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PromiseApiConfig(object):

    def __init__(self):
        self._fulfillment_days = None
        self._merchant_service_phone = None
        self._merchant_service_url = None
        self._promise_operation_type = None
        self._promise_operation_value = None

    @property
    def fulfillment_days(self):
        return self._fulfillment_days

    @fulfillment_days.setter
    def fulfillment_days(self, value):
        self._fulfillment_days = value
    @property
    def merchant_service_phone(self):
        return self._merchant_service_phone

    @merchant_service_phone.setter
    def merchant_service_phone(self, value):
        self._merchant_service_phone = value
    @property
    def merchant_service_url(self):
        return self._merchant_service_url

    @merchant_service_url.setter
    def merchant_service_url(self, value):
        self._merchant_service_url = value
    @property
    def promise_operation_type(self):
        return self._promise_operation_type

    @promise_operation_type.setter
    def promise_operation_type(self, value):
        self._promise_operation_type = value
    @property
    def promise_operation_value(self):
        return self._promise_operation_value

    @promise_operation_value.setter
    def promise_operation_value(self, value):
        self._promise_operation_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.fulfillment_days:
            if hasattr(self.fulfillment_days, 'to_alipay_dict'):
                params['fulfillment_days'] = self.fulfillment_days.to_alipay_dict()
            else:
                params['fulfillment_days'] = self.fulfillment_days
        if self.merchant_service_phone:
            if hasattr(self.merchant_service_phone, 'to_alipay_dict'):
                params['merchant_service_phone'] = self.merchant_service_phone.to_alipay_dict()
            else:
                params['merchant_service_phone'] = self.merchant_service_phone
        if self.merchant_service_url:
            if hasattr(self.merchant_service_url, 'to_alipay_dict'):
                params['merchant_service_url'] = self.merchant_service_url.to_alipay_dict()
            else:
                params['merchant_service_url'] = self.merchant_service_url
        if self.promise_operation_type:
            if hasattr(self.promise_operation_type, 'to_alipay_dict'):
                params['promise_operation_type'] = self.promise_operation_type.to_alipay_dict()
            else:
                params['promise_operation_type'] = self.promise_operation_type
        if self.promise_operation_value:
            if hasattr(self.promise_operation_value, 'to_alipay_dict'):
                params['promise_operation_value'] = self.promise_operation_value.to_alipay_dict()
            else:
                params['promise_operation_value'] = self.promise_operation_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PromiseApiConfig()
        if 'fulfillment_days' in d:
            o.fulfillment_days = d['fulfillment_days']
        if 'merchant_service_phone' in d:
            o.merchant_service_phone = d['merchant_service_phone']
        if 'merchant_service_url' in d:
            o.merchant_service_url = d['merchant_service_url']
        if 'promise_operation_type' in d:
            o.promise_operation_type = d['promise_operation_type']
        if 'promise_operation_value' in d:
            o.promise_operation_value = d['promise_operation_value']
        return o


