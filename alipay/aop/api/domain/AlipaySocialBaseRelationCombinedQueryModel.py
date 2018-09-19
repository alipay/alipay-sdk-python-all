#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialBaseRelationCombinedQueryModel(object):

    def __init__(self):
        self._limit = None
        self._scene_code = None

    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, value):
        self._limit = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.limit:
            if hasattr(self.limit, 'to_alipay_dict'):
                params['limit'] = self.limit.to_alipay_dict()
            else:
                params['limit'] = self.limit
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialBaseRelationCombinedQueryModel()
        if 'limit' in d:
            o.limit = d['limit']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


