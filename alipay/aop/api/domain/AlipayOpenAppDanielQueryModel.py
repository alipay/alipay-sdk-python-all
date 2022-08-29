#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppDanielQueryModel(object):

    def __init__(self):
        self._daniel_path = None
        self._daniel_query = None

    @property
    def daniel_path(self):
        return self._daniel_path

    @daniel_path.setter
    def daniel_path(self, value):
        self._daniel_path = value
    @property
    def daniel_query(self):
        return self._daniel_query

    @daniel_query.setter
    def daniel_query(self, value):
        self._daniel_query = value


    def to_alipay_dict(self):
        params = dict()
        if self.daniel_path:
            if hasattr(self.daniel_path, 'to_alipay_dict'):
                params['daniel_path'] = self.daniel_path.to_alipay_dict()
            else:
                params['daniel_path'] = self.daniel_path
        if self.daniel_query:
            if hasattr(self.daniel_query, 'to_alipay_dict'):
                params['daniel_query'] = self.daniel_query.to_alipay_dict()
            else:
                params['daniel_query'] = self.daniel_query
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppDanielQueryModel()
        if 'daniel_path' in d:
            o.daniel_path = d['daniel_path']
        if 'daniel_query' in d:
            o.daniel_query = d['daniel_query']
        return o


