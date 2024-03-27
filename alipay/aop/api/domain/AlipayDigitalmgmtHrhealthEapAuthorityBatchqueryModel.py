#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDigitalmgmtHrhealthEapAuthorityBatchqueryModel(object):

    def __init__(self):
        self._biz_emp_id = None
        self._biz_id = None
        self._data_key = None
        self._source = None

    @property
    def biz_emp_id(self):
        return self._biz_emp_id

    @biz_emp_id.setter
    def biz_emp_id(self, value):
        self._biz_emp_id = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def data_key(self):
        return self._data_key

    @data_key.setter
    def data_key(self, value):
        self._data_key = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_emp_id:
            if hasattr(self.biz_emp_id, 'to_alipay_dict'):
                params['biz_emp_id'] = self.biz_emp_id.to_alipay_dict()
            else:
                params['biz_emp_id'] = self.biz_emp_id
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.data_key:
            if hasattr(self.data_key, 'to_alipay_dict'):
                params['data_key'] = self.data_key.to_alipay_dict()
            else:
                params['data_key'] = self.data_key
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalmgmtHrhealthEapAuthorityBatchqueryModel()
        if 'biz_emp_id' in d:
            o.biz_emp_id = d['biz_emp_id']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'data_key' in d:
            o.data_key = d['data_key']
        if 'source' in d:
            o.source = d['source']
        return o


