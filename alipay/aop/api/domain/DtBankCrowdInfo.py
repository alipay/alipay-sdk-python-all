#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DtBankCrowdInfo(object):

    def __init__(self):
        self._crowd_code = None
        self._crowd_name = None

    @property
    def crowd_code(self):
        return self._crowd_code

    @crowd_code.setter
    def crowd_code(self, value):
        self._crowd_code = value
    @property
    def crowd_name(self):
        return self._crowd_name

    @crowd_name.setter
    def crowd_name(self, value):
        self._crowd_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.crowd_code:
            if hasattr(self.crowd_code, 'to_alipay_dict'):
                params['crowd_code'] = self.crowd_code.to_alipay_dict()
            else:
                params['crowd_code'] = self.crowd_code
        if self.crowd_name:
            if hasattr(self.crowd_name, 'to_alipay_dict'):
                params['crowd_name'] = self.crowd_name.to_alipay_dict()
            else:
                params['crowd_name'] = self.crowd_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DtBankCrowdInfo()
        if 'crowd_code' in d:
            o.crowd_code = d['crowd_code']
        if 'crowd_name' in d:
            o.crowd_name = d['crowd_name']
        return o


