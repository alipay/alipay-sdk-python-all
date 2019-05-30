#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundTransGroupfundsFundbillsQueryModel(object):

    def __init__(self):
        self._batch_no = None
        self._current_user_id = None
        self._ext_param = None
        self._query_type = None
        self._source = None

    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def current_user_id(self):
        return self._current_user_id

    @current_user_id.setter
    def current_user_id(self, value):
        self._current_user_id = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def query_type(self):
        return self._query_type

    @query_type.setter
    def query_type(self, value):
        self._query_type = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.current_user_id:
            if hasattr(self.current_user_id, 'to_alipay_dict'):
                params['current_user_id'] = self.current_user_id.to_alipay_dict()
            else:
                params['current_user_id'] = self.current_user_id
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.query_type:
            if hasattr(self.query_type, 'to_alipay_dict'):
                params['query_type'] = self.query_type.to_alipay_dict()
            else:
                params['query_type'] = self.query_type
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
        o = AlipayFundTransGroupfundsFundbillsQueryModel()
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'current_user_id' in d:
            o.current_user_id = d['current_user_id']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'query_type' in d:
            o.query_type = d['query_type']
        if 'source' in d:
            o.source = d['source']
        return o


