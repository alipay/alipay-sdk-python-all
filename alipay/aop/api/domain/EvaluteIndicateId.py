#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EvaluteIndicateId(object):

    def __init__(self):
        self._isv_indicate_id = None

    @property
    def isv_indicate_id(self):
        return self._isv_indicate_id

    @isv_indicate_id.setter
    def isv_indicate_id(self, value):
        self._isv_indicate_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.isv_indicate_id:
            if hasattr(self.isv_indicate_id, 'to_alipay_dict'):
                params['isv_indicate_id'] = self.isv_indicate_id.to_alipay_dict()
            else:
                params['isv_indicate_id'] = self.isv_indicate_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EvaluteIndicateId()
        if 'isv_indicate_id' in d:
            o.isv_indicate_id = d['isv_indicate_id']
        return o


