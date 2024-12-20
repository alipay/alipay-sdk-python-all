#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HeXiQueryVo import HeXiQueryVo


class AlipayOpenAppHexidemoModifyModel(object):

    def __init__(self):
        self._model = None
        self._query = None

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if isinstance(value, HeXiQueryVo):
            self._model = value
        else:
            self._model = HeXiQueryVo.from_alipay_dict(value)
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value


    def to_alipay_dict(self):
        params = dict()
        if self.model:
            if hasattr(self.model, 'to_alipay_dict'):
                params['model'] = self.model.to_alipay_dict()
            else:
                params['model'] = self.model
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppHexidemoModifyModel()
        if 'model' in d:
            o.model = d['model']
        if 'query' in d:
            o.query = d['query']
        return o


