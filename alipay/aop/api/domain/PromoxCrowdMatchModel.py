#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PromoxCrowdMatchModel(object):

    def __init__(self):
        self._crowd_code = None
        self._is_match = None

    @property
    def crowd_code(self):
        return self._crowd_code

    @crowd_code.setter
    def crowd_code(self, value):
        self._crowd_code = value
    @property
    def is_match(self):
        return self._is_match

    @is_match.setter
    def is_match(self, value):
        self._is_match = value


    def to_alipay_dict(self):
        params = dict()
        if self.crowd_code:
            if hasattr(self.crowd_code, 'to_alipay_dict'):
                params['crowd_code'] = self.crowd_code.to_alipay_dict()
            else:
                params['crowd_code'] = self.crowd_code
        if self.is_match:
            if hasattr(self.is_match, 'to_alipay_dict'):
                params['is_match'] = self.is_match.to_alipay_dict()
            else:
                params['is_match'] = self.is_match
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PromoxCrowdMatchModel()
        if 'crowd_code' in d:
            o.crowd_code = d['crowd_code']
        if 'is_match' in d:
            o.is_match = d['is_match']
        return o


