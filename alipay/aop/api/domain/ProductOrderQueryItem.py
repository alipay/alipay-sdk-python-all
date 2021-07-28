#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ProductOrderQueryItem(object):

    def __init__(self):
        self._need_activity = None
        self._ordered_channel = None
        self._ps_code = None

    @property
    def need_activity(self):
        return self._need_activity

    @need_activity.setter
    def need_activity(self, value):
        self._need_activity = value
    @property
    def ordered_channel(self):
        return self._ordered_channel

    @ordered_channel.setter
    def ordered_channel(self, value):
        self._ordered_channel = value
    @property
    def ps_code(self):
        return self._ps_code

    @ps_code.setter
    def ps_code(self, value):
        self._ps_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.need_activity:
            if hasattr(self.need_activity, 'to_alipay_dict'):
                params['need_activity'] = self.need_activity.to_alipay_dict()
            else:
                params['need_activity'] = self.need_activity
        if self.ordered_channel:
            if hasattr(self.ordered_channel, 'to_alipay_dict'):
                params['ordered_channel'] = self.ordered_channel.to_alipay_dict()
            else:
                params['ordered_channel'] = self.ordered_channel
        if self.ps_code:
            if hasattr(self.ps_code, 'to_alipay_dict'):
                params['ps_code'] = self.ps_code.to_alipay_dict()
            else:
                params['ps_code'] = self.ps_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ProductOrderQueryItem()
        if 'need_activity' in d:
            o.need_activity = d['need_activity']
        if 'ordered_channel' in d:
            o.ordered_channel = d['ordered_channel']
        if 'ps_code' in d:
            o.ps_code = d['ps_code']
        return o


