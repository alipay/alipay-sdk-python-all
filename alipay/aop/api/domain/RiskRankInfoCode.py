#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RiskRankInfoCode(object):

    def __init__(self):
        self._code = None
        self._contribution_degree = None
        self._desc = None
        self._model_name = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def contribution_degree(self):
        return self._contribution_degree

    @contribution_degree.setter
    def contribution_degree(self, value):
        self._contribution_degree = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def model_name(self):
        return self._model_name

    @model_name.setter
    def model_name(self, value):
        self._model_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.contribution_degree:
            if hasattr(self.contribution_degree, 'to_alipay_dict'):
                params['contribution_degree'] = self.contribution_degree.to_alipay_dict()
            else:
                params['contribution_degree'] = self.contribution_degree
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.model_name:
            if hasattr(self.model_name, 'to_alipay_dict'):
                params['model_name'] = self.model_name.to_alipay_dict()
            else:
                params['model_name'] = self.model_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RiskRankInfoCode()
        if 'code' in d:
            o.code = d['code']
        if 'contribution_degree' in d:
            o.contribution_degree = d['contribution_degree']
        if 'desc' in d:
            o.desc = d['desc']
        if 'model_name' in d:
            o.model_name = d['model_name']
        return o


