#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCognitiveAswfDagQueryModel(object):

    def __init__(self):
        self._biz_id = None
        self._ctxs = None
        self._template_id = None
        self._trace_id = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def ctxs(self):
        return self._ctxs

    @ctxs.setter
    def ctxs(self, value):
        self._ctxs = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
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
        if self.ctxs:
            if hasattr(self.ctxs, 'to_alipay_dict'):
                params['ctxs'] = self.ctxs.to_alipay_dict()
            else:
                params['ctxs'] = self.ctxs
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
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
        o = AlipayIserviceCognitiveAswfDagQueryModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'ctxs' in d:
            o.ctxs = d['ctxs']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'trace_id' in d:
            o.trace_id = d['trace_id']
        return o


