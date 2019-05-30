#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayAccountFinriskMarkriskDatafactorQueryModel(object):

    def __init__(self):
        self._data_factor_build_req = None

    @property
    def data_factor_build_req(self):
        return self._data_factor_build_req

    @data_factor_build_req.setter
    def data_factor_build_req(self, value):
        self._data_factor_build_req = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_factor_build_req:
            if hasattr(self.data_factor_build_req, 'to_alipay_dict'):
                params['data_factor_build_req'] = self.data_factor_build_req.to_alipay_dict()
            else:
                params['data_factor_build_req'] = self.data_factor_build_req
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAccountFinriskMarkriskDatafactorQueryModel()
        if 'data_factor_build_req' in d:
            o.data_factor_build_req = d['data_factor_build_req']
        return o


