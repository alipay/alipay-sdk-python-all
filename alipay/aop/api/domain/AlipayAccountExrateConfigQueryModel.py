#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayAccountExrateConfigQueryModel(object):

    def __init__(self):
        self._scheduler_code = None

    @property
    def scheduler_code(self):
        return self._scheduler_code

    @scheduler_code.setter
    def scheduler_code(self, value):
        self._scheduler_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.scheduler_code:
            if hasattr(self.scheduler_code, 'to_alipay_dict'):
                params['scheduler_code'] = self.scheduler_code.to_alipay_dict()
            else:
                params['scheduler_code'] = self.scheduler_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAccountExrateConfigQueryModel()
        if 'scheduler_code' in d:
            o.scheduler_code = d['scheduler_code']
        return o


