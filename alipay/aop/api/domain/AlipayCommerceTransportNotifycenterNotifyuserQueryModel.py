#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportNotifycenterNotifyuserQueryModel(object):

    def __init__(self):
        self._notify_id = None
        self._notify_object = None
        self._user_id = None

    @property
    def notify_id(self):
        return self._notify_id

    @notify_id.setter
    def notify_id(self, value):
        self._notify_id = value
    @property
    def notify_object(self):
        return self._notify_object

    @notify_object.setter
    def notify_object(self, value):
        self._notify_object = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.notify_id:
            if hasattr(self.notify_id, 'to_alipay_dict'):
                params['notify_id'] = self.notify_id.to_alipay_dict()
            else:
                params['notify_id'] = self.notify_id
        if self.notify_object:
            if hasattr(self.notify_object, 'to_alipay_dict'):
                params['notify_object'] = self.notify_object.to_alipay_dict()
            else:
                params['notify_object'] = self.notify_object
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
        o = AlipayCommerceTransportNotifycenterNotifyuserQueryModel()
        if 'notify_id' in d:
            o.notify_id = d['notify_id']
        if 'notify_object' in d:
            o.notify_object = d['notify_object']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


