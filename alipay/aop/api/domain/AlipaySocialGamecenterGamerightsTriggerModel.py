#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialGamecenterGamerightsTriggerModel(object):

    def __init__(self):
        self._open_id = None
        self._trigger_right_num = None
        self._trigger_right_type = None
        self._user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def trigger_right_num(self):
        return self._trigger_right_num

    @trigger_right_num.setter
    def trigger_right_num(self, value):
        self._trigger_right_num = value
    @property
    def trigger_right_type(self):
        return self._trigger_right_type

    @trigger_right_type.setter
    def trigger_right_type(self, value):
        self._trigger_right_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.trigger_right_num:
            if hasattr(self.trigger_right_num, 'to_alipay_dict'):
                params['trigger_right_num'] = self.trigger_right_num.to_alipay_dict()
            else:
                params['trigger_right_num'] = self.trigger_right_num
        if self.trigger_right_type:
            if hasattr(self.trigger_right_type, 'to_alipay_dict'):
                params['trigger_right_type'] = self.trigger_right_type.to_alipay_dict()
            else:
                params['trigger_right_type'] = self.trigger_right_type
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
        o = AlipaySocialGamecenterGamerightsTriggerModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'trigger_right_num' in d:
            o.trigger_right_num = d['trigger_right_num']
        if 'trigger_right_type' in d:
            o.trigger_right_type = d['trigger_right_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


