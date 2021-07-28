#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TargetInfo(object):

    def __init__(self):
        self._target_id = None
        self._target_type = None

    @property
    def target_id(self):
        return self._target_id

    @target_id.setter
    def target_id(self, value):
        self._target_id = value
    @property
    def target_type(self):
        return self._target_type

    @target_type.setter
    def target_type(self, value):
        self._target_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.target_id:
            if hasattr(self.target_id, 'to_alipay_dict'):
                params['target_id'] = self.target_id.to_alipay_dict()
            else:
                params['target_id'] = self.target_id
        if self.target_type:
            if hasattr(self.target_type, 'to_alipay_dict'):
                params['target_type'] = self.target_type.to_alipay_dict()
            else:
                params['target_type'] = self.target_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TargetInfo()
        if 'target_id' in d:
            o.target_id = d['target_id']
        if 'target_type' in d:
            o.target_type = d['target_type']
        return o


