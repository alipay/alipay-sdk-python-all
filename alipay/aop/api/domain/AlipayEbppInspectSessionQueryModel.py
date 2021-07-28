#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInspectSessionQueryModel(object):

    def __init__(self):
        self._log_name = None

    @property
    def log_name(self):
        return self._log_name

    @log_name.setter
    def log_name(self, value):
        self._log_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.log_name:
            if hasattr(self.log_name, 'to_alipay_dict'):
                params['log_name'] = self.log_name.to_alipay_dict()
            else:
                params['log_name'] = self.log_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInspectSessionQueryModel()
        if 'log_name' in d:
            o.log_name = d['log_name']
        return o


