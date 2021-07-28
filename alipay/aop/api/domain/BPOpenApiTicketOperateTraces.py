#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BPOpenApiTicketOperateTrace import BPOpenApiTicketOperateTrace


class BPOpenApiTicketOperateTraces(object):

    def __init__(self):
        self._operate_traces = None

    @property
    def operate_traces(self):
        return self._operate_traces

    @operate_traces.setter
    def operate_traces(self, value):
        if isinstance(value, list):
            self._operate_traces = list()
            for i in value:
                if isinstance(i, BPOpenApiTicketOperateTrace):
                    self._operate_traces.append(i)
                else:
                    self._operate_traces.append(BPOpenApiTicketOperateTrace.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.operate_traces:
            if isinstance(self.operate_traces, list):
                for i in range(0, len(self.operate_traces)):
                    element = self.operate_traces[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.operate_traces[i] = element.to_alipay_dict()
            if hasattr(self.operate_traces, 'to_alipay_dict'):
                params['operate_traces'] = self.operate_traces.to_alipay_dict()
            else:
                params['operate_traces'] = self.operate_traces
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BPOpenApiTicketOperateTraces()
        if 'operate_traces' in d:
            o.operate_traces = d['operate_traces']
        return o


