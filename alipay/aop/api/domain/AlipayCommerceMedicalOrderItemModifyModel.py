#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TraceCodeInfo import TraceCodeInfo


class AlipayCommerceMedicalOrderItemModifyModel(object):

    def __init__(self):
        self._order_no = None
        self._trace_code_infos = None

    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def trace_code_infos(self):
        return self._trace_code_infos

    @trace_code_infos.setter
    def trace_code_infos(self, value):
        if isinstance(value, list):
            self._trace_code_infos = list()
            for i in value:
                if isinstance(i, TraceCodeInfo):
                    self._trace_code_infos.append(i)
                else:
                    self._trace_code_infos.append(TraceCodeInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.trace_code_infos:
            if isinstance(self.trace_code_infos, list):
                for i in range(0, len(self.trace_code_infos)):
                    element = self.trace_code_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.trace_code_infos[i] = element.to_alipay_dict()
            if hasattr(self.trace_code_infos, 'to_alipay_dict'):
                params['trace_code_infos'] = self.trace_code_infos.to_alipay_dict()
            else:
                params['trace_code_infos'] = self.trace_code_infos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalOrderItemModifyModel()
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'trace_code_infos' in d:
            o.trace_code_infos = d['trace_code_infos']
        return o


