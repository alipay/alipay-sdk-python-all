#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarCarmodelQueryModel(object):

    def __init__(self):
        self._model_id = None

    @property
    def model_id(self):
        return self._model_id

    @model_id.setter
    def model_id(self, value):
        self._model_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.model_id:
            if hasattr(self.model_id, 'to_alipay_dict'):
                params['model_id'] = self.model_id.to_alipay_dict()
            else:
                params['model_id'] = self.model_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarCarmodelQueryModel()
        if 'model_id' in d:
            o.model_id = d['model_id']
        return o


