#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDigitalmgmtScenetypeQueryModel(object):

    def __init__(self):
        self._only_pass = None
        self._operator = None
        self._query_all = None
        self._tnt_inst_id = None

    @property
    def only_pass(self):
        return self._only_pass

    @only_pass.setter
    def only_pass(self, value):
        self._only_pass = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def query_all(self):
        return self._query_all

    @query_all.setter
    def query_all(self, value):
        self._query_all = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.only_pass:
            if hasattr(self.only_pass, 'to_alipay_dict'):
                params['only_pass'] = self.only_pass.to_alipay_dict()
            else:
                params['only_pass'] = self.only_pass
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.query_all:
            if hasattr(self.query_all, 'to_alipay_dict'):
                params['query_all'] = self.query_all.to_alipay_dict()
            else:
                params['query_all'] = self.query_all
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalmgmtScenetypeQueryModel()
        if 'only_pass' in d:
            o.only_pass = d['only_pass']
        if 'operator' in d:
            o.operator = d['operator']
        if 'query_all' in d:
            o.query_all = d['query_all']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o


