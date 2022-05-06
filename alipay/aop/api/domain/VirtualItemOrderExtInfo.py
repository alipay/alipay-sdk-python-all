#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VirtualItemOrderExtInfo(object):

    def __init__(self):
        self._notify_app_id = None

    @property
    def notify_app_id(self):
        return self._notify_app_id

    @notify_app_id.setter
    def notify_app_id(self, value):
        self._notify_app_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.notify_app_id:
            if hasattr(self.notify_app_id, 'to_alipay_dict'):
                params['notify_app_id'] = self.notify_app_id.to_alipay_dict()
            else:
                params['notify_app_id'] = self.notify_app_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VirtualItemOrderExtInfo()
        if 'notify_app_id' in d:
            o.notify_app_id = d['notify_app_id']
        return o


