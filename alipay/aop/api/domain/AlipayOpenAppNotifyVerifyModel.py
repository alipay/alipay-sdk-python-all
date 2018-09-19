#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppNotifyVerifyModel(object):

    def __init__(self):
        self._notify_id = None

    @property
    def notify_id(self):
        return self._notify_id

    @notify_id.setter
    def notify_id(self, value):
        self._notify_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.notify_id:
            if hasattr(self.notify_id, 'to_alipay_dict'):
                params['notify_id'] = self.notify_id.to_alipay_dict()
            else:
                params['notify_id'] = self.notify_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppNotifyVerifyModel()
        if 'notify_id' in d:
            o.notify_id = d['notify_id']
        return o


