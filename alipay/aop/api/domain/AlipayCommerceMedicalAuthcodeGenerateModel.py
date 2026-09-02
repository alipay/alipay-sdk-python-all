#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalAuthcodeGenerateModel(object):

    def __init__(self):
        self._biz_id = None
        self._biz_time = None
        self._channel_type = None
        self._customer_id = None
        self._merchant_app_id = None
        self._open_id = None
        self._phone = None
        self._user_id = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def channel_type(self):
        return self._channel_type

    @channel_type.setter
    def channel_type(self, value):
        self._channel_type = value
    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
    @property
    def merchant_app_id(self):
        return self._merchant_app_id

    @merchant_app_id.setter
    def merchant_app_id(self, value):
        self._merchant_app_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.channel_type:
            if hasattr(self.channel_type, 'to_alipay_dict'):
                params['channel_type'] = self.channel_type.to_alipay_dict()
            else:
                params['channel_type'] = self.channel_type
        if self.customer_id:
            if hasattr(self.customer_id, 'to_alipay_dict'):
                params['customer_id'] = self.customer_id.to_alipay_dict()
            else:
                params['customer_id'] = self.customer_id
        if self.merchant_app_id:
            if hasattr(self.merchant_app_id, 'to_alipay_dict'):
                params['merchant_app_id'] = self.merchant_app_id.to_alipay_dict()
            else:
                params['merchant_app_id'] = self.merchant_app_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
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
        o = AlipayCommerceMedicalAuthcodeGenerateModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'channel_type' in d:
            o.channel_type = d['channel_type']
        if 'customer_id' in d:
            o.customer_id = d['customer_id']
        if 'merchant_app_id' in d:
            o.merchant_app_id = d['merchant_app_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'phone' in d:
            o.phone = d['phone']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


