#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OutOfConfigGoodsResult(object):

    def __init__(self):
        self._algorithm_id = None

    @property
    def algorithm_id(self):
        return self._algorithm_id

    @algorithm_id.setter
    def algorithm_id(self, value):
        self._algorithm_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.algorithm_id:
            if hasattr(self.algorithm_id, 'to_alipay_dict'):
                params['algorithm_id'] = self.algorithm_id.to_alipay_dict()
            else:
                params['algorithm_id'] = self.algorithm_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OutOfConfigGoodsResult()
        if 'algorithm_id' in d:
            o.algorithm_id = d['algorithm_id']
        return o


