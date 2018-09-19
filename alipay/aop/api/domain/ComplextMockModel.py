#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SimpleMockModel import SimpleMockModel


class ComplextMockModel(object):

    def __init__(self):
        self._biz_model = None
        self._biz_num = None
        self._biz_type = None

    @property
    def biz_model(self):
        return self._biz_model

    @biz_model.setter
    def biz_model(self, value):
        if isinstance(value, SimpleMockModel):
            self._biz_model = value
        else:
            self._biz_model = SimpleMockModel.from_alipay_dict(value)
    @property
    def biz_num(self):
        return self._biz_num

    @biz_num.setter
    def biz_num(self, value):
        self._biz_num = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_model:
            if hasattr(self.biz_model, 'to_alipay_dict'):
                params['biz_model'] = self.biz_model.to_alipay_dict()
            else:
                params['biz_model'] = self.biz_model
        if self.biz_num:
            if hasattr(self.biz_num, 'to_alipay_dict'):
                params['biz_num'] = self.biz_num.to_alipay_dict()
            else:
                params['biz_num'] = self.biz_num
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ComplextMockModel()
        if 'biz_model' in d:
            o.biz_model = d['biz_model']
        if 'biz_num' in d:
            o.biz_num = d['biz_num']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        return o


