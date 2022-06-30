#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NimitzQueryContext import NimitzQueryContext
from alipay.aop.api.domain.NimitzDimRequest import NimitzDimRequest


class AntfortuneQuotationNimitzDimQueryModel(object):

    def __init__(self):
        self._context = None
        self._ext = None
        self._nimitz_dim_request = None
        self._opt = None
        self._request_id = None

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, value):
        if isinstance(value, NimitzQueryContext):
            self._context = value
        else:
            self._context = NimitzQueryContext.from_alipay_dict(value)
    @property
    def ext(self):
        return self._ext

    @ext.setter
    def ext(self, value):
        self._ext = value
    @property
    def nimitz_dim_request(self):
        return self._nimitz_dim_request

    @nimitz_dim_request.setter
    def nimitz_dim_request(self, value):
        if isinstance(value, NimitzDimRequest):
            self._nimitz_dim_request = value
        else:
            self._nimitz_dim_request = NimitzDimRequest.from_alipay_dict(value)
    @property
    def opt(self):
        return self._opt

    @opt.setter
    def opt(self, value):
        self._opt = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.context:
            if hasattr(self.context, 'to_alipay_dict'):
                params['context'] = self.context.to_alipay_dict()
            else:
                params['context'] = self.context
        if self.ext:
            if hasattr(self.ext, 'to_alipay_dict'):
                params['ext'] = self.ext.to_alipay_dict()
            else:
                params['ext'] = self.ext
        if self.nimitz_dim_request:
            if hasattr(self.nimitz_dim_request, 'to_alipay_dict'):
                params['nimitz_dim_request'] = self.nimitz_dim_request.to_alipay_dict()
            else:
                params['nimitz_dim_request'] = self.nimitz_dim_request
        if self.opt:
            if hasattr(self.opt, 'to_alipay_dict'):
                params['opt'] = self.opt.to_alipay_dict()
            else:
                params['opt'] = self.opt
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneQuotationNimitzDimQueryModel()
        if 'context' in d:
            o.context = d['context']
        if 'ext' in d:
            o.ext = d['ext']
        if 'nimitz_dim_request' in d:
            o.nimitz_dim_request = d['nimitz_dim_request']
        if 'opt' in d:
            o.opt = d['opt']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


