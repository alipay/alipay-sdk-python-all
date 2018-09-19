#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCognitiveImageRouteQueryModel(object):

    def __init__(self):
        self._biz_id = None
        self._ctx = None
        self._trace_id = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def ctx(self):
        return self._ctx

    @ctx.setter
    def ctx(self, value):
        if isinstance(value, list):
            self._ctx = list()
            for i in value:
                self._ctx.append(i)
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.ctx:
            if isinstance(self.ctx, list):
                for i in range(0, len(self.ctx)):
                    element = self.ctx[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ctx[i] = element.to_alipay_dict()
            if hasattr(self.ctx, 'to_alipay_dict'):
                params['ctx'] = self.ctx.to_alipay_dict()
            else:
                params['ctx'] = self.ctx
        if self.trace_id:
            if hasattr(self.trace_id, 'to_alipay_dict'):
                params['trace_id'] = self.trace_id.to_alipay_dict()
            else:
                params['trace_id'] = self.trace_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCognitiveImageRouteQueryModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'ctx' in d:
            o.ctx = d['ctx']
        if 'trace_id' in d:
            o.trace_id = d['trace_id']
        return o


