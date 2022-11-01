#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IotEmergencyLogIndexSaveOpenMqRequest import IotEmergencyLogIndexSaveOpenMqRequest


class AlipayOpenIoteopLogSendModel(object):

    def __init__(self):
        self._code = None
        self._cost_time = None
        self._index_list = None
        self._sequence_diagram_id = None
        self._success = None
        self._trace_id = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def cost_time(self):
        return self._cost_time

    @cost_time.setter
    def cost_time(self, value):
        self._cost_time = value
    @property
    def index_list(self):
        return self._index_list

    @index_list.setter
    def index_list(self, value):
        if isinstance(value, list):
            self._index_list = list()
            for i in value:
                if isinstance(i, IotEmergencyLogIndexSaveOpenMqRequest):
                    self._index_list.append(i)
                else:
                    self._index_list.append(IotEmergencyLogIndexSaveOpenMqRequest.from_alipay_dict(i))
    @property
    def sequence_diagram_id(self):
        return self._sequence_diagram_id

    @sequence_diagram_id.setter
    def sequence_diagram_id(self, value):
        self._sequence_diagram_id = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.cost_time:
            if hasattr(self.cost_time, 'to_alipay_dict'):
                params['cost_time'] = self.cost_time.to_alipay_dict()
            else:
                params['cost_time'] = self.cost_time
        if self.index_list:
            if isinstance(self.index_list, list):
                for i in range(0, len(self.index_list)):
                    element = self.index_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.index_list[i] = element.to_alipay_dict()
            if hasattr(self.index_list, 'to_alipay_dict'):
                params['index_list'] = self.index_list.to_alipay_dict()
            else:
                params['index_list'] = self.index_list
        if self.sequence_diagram_id:
            if hasattr(self.sequence_diagram_id, 'to_alipay_dict'):
                params['sequence_diagram_id'] = self.sequence_diagram_id.to_alipay_dict()
            else:
                params['sequence_diagram_id'] = self.sequence_diagram_id
        if self.success:
            if hasattr(self.success, 'to_alipay_dict'):
                params['success'] = self.success.to_alipay_dict()
            else:
                params['success'] = self.success
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
        o = AlipayOpenIoteopLogSendModel()
        if 'code' in d:
            o.code = d['code']
        if 'cost_time' in d:
            o.cost_time = d['cost_time']
        if 'index_list' in d:
            o.index_list = d['index_list']
        if 'sequence_diagram_id' in d:
            o.sequence_diagram_id = d['sequence_diagram_id']
        if 'success' in d:
            o.success = d['success']
        if 'trace_id' in d:
            o.trace_id = d['trace_id']
        return o


