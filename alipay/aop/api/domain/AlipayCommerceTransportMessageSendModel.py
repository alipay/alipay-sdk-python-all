#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportMessageSendModel(object):

    def __init__(self):
        self._card_type = None
        self._merchant_biz_time = None
        self._notify_data = None
        self._notify_time = None
        self._notify_type = None
        self._user_ids = None

    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def merchant_biz_time(self):
        return self._merchant_biz_time

    @merchant_biz_time.setter
    def merchant_biz_time(self, value):
        self._merchant_biz_time = value
    @property
    def notify_data(self):
        return self._notify_data

    @notify_data.setter
    def notify_data(self, value):
        self._notify_data = value
    @property
    def notify_time(self):
        return self._notify_time

    @notify_time.setter
    def notify_time(self, value):
        self._notify_time = value
    @property
    def notify_type(self):
        return self._notify_type

    @notify_type.setter
    def notify_type(self, value):
        self._notify_type = value
    @property
    def user_ids(self):
        return self._user_ids

    @user_ids.setter
    def user_ids(self, value):
        if isinstance(value, list):
            self._user_ids = list()
            for i in value:
                self._user_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.merchant_biz_time:
            if hasattr(self.merchant_biz_time, 'to_alipay_dict'):
                params['merchant_biz_time'] = self.merchant_biz_time.to_alipay_dict()
            else:
                params['merchant_biz_time'] = self.merchant_biz_time
        if self.notify_data:
            if hasattr(self.notify_data, 'to_alipay_dict'):
                params['notify_data'] = self.notify_data.to_alipay_dict()
            else:
                params['notify_data'] = self.notify_data
        if self.notify_time:
            if hasattr(self.notify_time, 'to_alipay_dict'):
                params['notify_time'] = self.notify_time.to_alipay_dict()
            else:
                params['notify_time'] = self.notify_time
        if self.notify_type:
            if hasattr(self.notify_type, 'to_alipay_dict'):
                params['notify_type'] = self.notify_type.to_alipay_dict()
            else:
                params['notify_type'] = self.notify_type
        if self.user_ids:
            if isinstance(self.user_ids, list):
                for i in range(0, len(self.user_ids)):
                    element = self.user_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user_ids[i] = element.to_alipay_dict()
            if hasattr(self.user_ids, 'to_alipay_dict'):
                params['user_ids'] = self.user_ids.to_alipay_dict()
            else:
                params['user_ids'] = self.user_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportMessageSendModel()
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'merchant_biz_time' in d:
            o.merchant_biz_time = d['merchant_biz_time']
        if 'notify_data' in d:
            o.notify_data = d['notify_data']
        if 'notify_time' in d:
            o.notify_time = d['notify_time']
        if 'notify_type' in d:
            o.notify_type = d['notify_type']
        if 'user_ids' in d:
            o.user_ids = d['user_ids']
        return o


