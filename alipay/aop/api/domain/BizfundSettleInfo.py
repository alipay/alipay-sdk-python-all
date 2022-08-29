#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BizfundSettleInfo(object):

    def __init__(self):
        self._settle_mode = None
        self._settle_target_type = None

    @property
    def settle_mode(self):
        return self._settle_mode

    @settle_mode.setter
    def settle_mode(self, value):
        self._settle_mode = value
    @property
    def settle_target_type(self):
        return self._settle_target_type

    @settle_target_type.setter
    def settle_target_type(self, value):
        self._settle_target_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.settle_mode:
            if hasattr(self.settle_mode, 'to_alipay_dict'):
                params['settle_mode'] = self.settle_mode.to_alipay_dict()
            else:
                params['settle_mode'] = self.settle_mode
        if self.settle_target_type:
            if hasattr(self.settle_target_type, 'to_alipay_dict'):
                params['settle_target_type'] = self.settle_target_type.to_alipay_dict()
            else:
                params['settle_target_type'] = self.settle_target_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BizfundSettleInfo()
        if 'settle_mode' in d:
            o.settle_mode = d['settle_mode']
        if 'settle_target_type' in d:
            o.settle_target_type = d['settle_target_type']
        return o


