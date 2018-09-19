#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FaceExtInfo(object):

    def __init__(self):
        self._query_type = None

    @property
    def query_type(self):
        return self._query_type

    @query_type.setter
    def query_type(self, value):
        self._query_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.query_type:
            if hasattr(self.query_type, 'to_alipay_dict'):
                params['query_type'] = self.query_type.to_alipay_dict()
            else:
                params['query_type'] = self.query_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FaceExtInfo()
        if 'query_type' in d:
            o.query_type = d['query_type']
        return o


