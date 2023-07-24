#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TipInfo(object):

    def __init__(self):
        self._info = None
        self._type = None

    @property
    def info(self):
        return self._info

    @info.setter
    def info(self, value):
        self._info = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.info:
            if hasattr(self.info, 'to_alipay_dict'):
                params['info'] = self.info.to_alipay_dict()
            else:
                params['info'] = self.info
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TipInfo()
        if 'info' in d:
            o.info = d['info']
        if 'type' in d:
            o.type = d['type']
        return o


