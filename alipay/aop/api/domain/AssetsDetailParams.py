#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AssetsDetailParams(object):

    def __init__(self):
        self._admit = None
        self._int_free_info = None

    @property
    def admit(self):
        return self._admit

    @admit.setter
    def admit(self, value):
        self._admit = value
    @property
    def int_free_info(self):
        return self._int_free_info

    @int_free_info.setter
    def int_free_info(self, value):
        self._int_free_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.admit:
            if hasattr(self.admit, 'to_alipay_dict'):
                params['admit'] = self.admit.to_alipay_dict()
            else:
                params['admit'] = self.admit
        if self.int_free_info:
            if hasattr(self.int_free_info, 'to_alipay_dict'):
                params['int_free_info'] = self.int_free_info.to_alipay_dict()
            else:
                params['int_free_info'] = self.int_free_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssetsDetailParams()
        if 'admit' in d:
            o.admit = d['admit']
        if 'int_free_info' in d:
            o.int_free_info = d['int_free_info']
        return o


