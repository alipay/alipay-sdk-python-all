#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MerchantCardMsgInfo(object):

    def __init__(self):
        self._changed_point = None

    @property
    def changed_point(self):
        return self._changed_point

    @changed_point.setter
    def changed_point(self, value):
        self._changed_point = value


    def to_alipay_dict(self):
        params = dict()
        if self.changed_point:
            if hasattr(self.changed_point, 'to_alipay_dict'):
                params['changed_point'] = self.changed_point.to_alipay_dict()
            else:
                params['changed_point'] = self.changed_point
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantCardMsgInfo()
        if 'changed_point' in d:
            o.changed_point = d['changed_point']
        return o


