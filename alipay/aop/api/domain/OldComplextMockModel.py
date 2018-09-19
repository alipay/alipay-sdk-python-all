#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SimpleMockModel import SimpleMockModel


class OldComplextMockModel(object):

    def __init__(self):
        self._biz_num = None
        self._biz_type = None
        self._simple_mock_model = None

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
    @property
    def simple_mock_model(self):
        return self._simple_mock_model

    @simple_mock_model.setter
    def simple_mock_model(self, value):
        if isinstance(value, SimpleMockModel):
            self._simple_mock_model = value
        else:
            self._simple_mock_model = SimpleMockModel.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
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
        if self.simple_mock_model:
            if hasattr(self.simple_mock_model, 'to_alipay_dict'):
                params['simple_mock_model'] = self.simple_mock_model.to_alipay_dict()
            else:
                params['simple_mock_model'] = self.simple_mock_model
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OldComplextMockModel()
        if 'biz_num' in d:
            o.biz_num = d['biz_num']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'simple_mock_model' in d:
            o.simple_mock_model = d['simple_mock_model']
        return o


