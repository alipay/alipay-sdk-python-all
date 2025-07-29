#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GroupControlActionVO(object):

    def __init__(self):
        self._action_type = None
        self._warn_msg = None

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def warn_msg(self):
        return self._warn_msg

    @warn_msg.setter
    def warn_msg(self, value):
        self._warn_msg = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.warn_msg:
            if hasattr(self.warn_msg, 'to_alipay_dict'):
                params['warn_msg'] = self.warn_msg.to_alipay_dict()
            else:
                params['warn_msg'] = self.warn_msg
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupControlActionVO()
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'warn_msg' in d:
            o.warn_msg = d['warn_msg']
        return o


