#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PushDTO(object):

    def __init__(self):
        self._cal_type = None
        self._inc_value = None

    @property
    def cal_type(self):
        return self._cal_type

    @cal_type.setter
    def cal_type(self, value):
        self._cal_type = value
    @property
    def inc_value(self):
        return self._inc_value

    @inc_value.setter
    def inc_value(self, value):
        self._inc_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.cal_type:
            if hasattr(self.cal_type, 'to_alipay_dict'):
                params['cal_type'] = self.cal_type.to_alipay_dict()
            else:
                params['cal_type'] = self.cal_type
        if self.inc_value:
            if hasattr(self.inc_value, 'to_alipay_dict'):
                params['inc_value'] = self.inc_value.to_alipay_dict()
            else:
                params['inc_value'] = self.inc_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PushDTO()
        if 'cal_type' in d:
            o.cal_type = d['cal_type']
        if 'inc_value' in d:
            o.inc_value = d['inc_value']
        return o


