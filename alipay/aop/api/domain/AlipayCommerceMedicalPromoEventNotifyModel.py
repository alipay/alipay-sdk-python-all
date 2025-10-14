#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalPromoEventNotifyModel(object):

    def __init__(self):
        self._event_code = None
        self._event_name = None
        self._finish_time = None
        self._merchant_name = None
        self._merchant_uscc = None
        self._open_id = None
        self._service_name = None
        self._user_id = None

    @property
    def event_code(self):
        return self._event_code

    @event_code.setter
    def event_code(self, value):
        self._event_code = value
    @property
    def event_name(self):
        return self._event_name

    @event_name.setter
    def event_name(self, value):
        self._event_name = value
    @property
    def finish_time(self):
        return self._finish_time

    @finish_time.setter
    def finish_time(self, value):
        self._finish_time = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def merchant_uscc(self):
        return self._merchant_uscc

    @merchant_uscc.setter
    def merchant_uscc(self, value):
        self._merchant_uscc = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.event_code:
            if hasattr(self.event_code, 'to_alipay_dict'):
                params['event_code'] = self.event_code.to_alipay_dict()
            else:
                params['event_code'] = self.event_code
        if self.event_name:
            if hasattr(self.event_name, 'to_alipay_dict'):
                params['event_name'] = self.event_name.to_alipay_dict()
            else:
                params['event_name'] = self.event_name
        if self.finish_time:
            if hasattr(self.finish_time, 'to_alipay_dict'):
                params['finish_time'] = self.finish_time.to_alipay_dict()
            else:
                params['finish_time'] = self.finish_time
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.merchant_uscc:
            if hasattr(self.merchant_uscc, 'to_alipay_dict'):
                params['merchant_uscc'] = self.merchant_uscc.to_alipay_dict()
            else:
                params['merchant_uscc'] = self.merchant_uscc
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.service_name:
            if hasattr(self.service_name, 'to_alipay_dict'):
                params['service_name'] = self.service_name.to_alipay_dict()
            else:
                params['service_name'] = self.service_name
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
        o = AlipayCommerceMedicalPromoEventNotifyModel()
        if 'event_code' in d:
            o.event_code = d['event_code']
        if 'event_name' in d:
            o.event_name = d['event_name']
        if 'finish_time' in d:
            o.finish_time = d['finish_time']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'merchant_uscc' in d:
            o.merchant_uscc = d['merchant_uscc']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'service_name' in d:
            o.service_name = d['service_name']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


