#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SearchOrderCreateRequest import SearchOrderCreateRequest


class AlipayOpenSearchServiceorderModifyModel(object):

    def __init__(self):
        self._biz_data = None
        self._biz_type = None
        self._opt_type = None

    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        if isinstance(value, SearchOrderCreateRequest):
            self._biz_data = value
        else:
            self._biz_data = SearchOrderCreateRequest.from_alipay_dict(value)
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def opt_type(self):
        return self._opt_type

    @opt_type.setter
    def opt_type(self, value):
        self._opt_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.opt_type:
            if hasattr(self.opt_type, 'to_alipay_dict'):
                params['opt_type'] = self.opt_type.to_alipay_dict()
            else:
                params['opt_type'] = self.opt_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSearchServiceorderModifyModel()
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'opt_type' in d:
            o.opt_type = d['opt_type']
        return o


