#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class YpzServiceDetailCardExt(object):

    def __init__(self):
        self._attendant_name = None

    @property
    def attendant_name(self):
        return self._attendant_name

    @attendant_name.setter
    def attendant_name(self, value):
        self._attendant_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.attendant_name:
            if hasattr(self.attendant_name, 'to_alipay_dict'):
                params['attendant_name'] = self.attendant_name.to_alipay_dict()
            else:
                params['attendant_name'] = self.attendant_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = YpzServiceDetailCardExt()
        if 'attendant_name' in d:
            o.attendant_name = d['attendant_name']
        return o


