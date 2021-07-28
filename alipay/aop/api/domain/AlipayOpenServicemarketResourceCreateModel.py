#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AbilityResourceConsume import AbilityResourceConsume


class AlipayOpenServicemarketResourceCreateModel(object):

    def __init__(self):
        self._ability_resource_consume = None
        self._execution_time_end = None
        self._execution_time_start = None
        self._outer_code = None
        self._record_id = None
        self._record_unit = None
        self._uid = None

    @property
    def ability_resource_consume(self):
        return self._ability_resource_consume

    @ability_resource_consume.setter
    def ability_resource_consume(self, value):
        if isinstance(value, list):
            self._ability_resource_consume = list()
            for i in value:
                if isinstance(i, AbilityResourceConsume):
                    self._ability_resource_consume.append(i)
                else:
                    self._ability_resource_consume.append(AbilityResourceConsume.from_alipay_dict(i))
    @property
    def execution_time_end(self):
        return self._execution_time_end

    @execution_time_end.setter
    def execution_time_end(self, value):
        self._execution_time_end = value
    @property
    def execution_time_start(self):
        return self._execution_time_start

    @execution_time_start.setter
    def execution_time_start(self, value):
        self._execution_time_start = value
    @property
    def outer_code(self):
        return self._outer_code

    @outer_code.setter
    def outer_code(self, value):
        self._outer_code = value
    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value
    @property
    def record_unit(self):
        return self._record_unit

    @record_unit.setter
    def record_unit(self, value):
        self._record_unit = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.ability_resource_consume:
            if isinstance(self.ability_resource_consume, list):
                for i in range(0, len(self.ability_resource_consume)):
                    element = self.ability_resource_consume[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ability_resource_consume[i] = element.to_alipay_dict()
            if hasattr(self.ability_resource_consume, 'to_alipay_dict'):
                params['ability_resource_consume'] = self.ability_resource_consume.to_alipay_dict()
            else:
                params['ability_resource_consume'] = self.ability_resource_consume
        if self.execution_time_end:
            if hasattr(self.execution_time_end, 'to_alipay_dict'):
                params['execution_time_end'] = self.execution_time_end.to_alipay_dict()
            else:
                params['execution_time_end'] = self.execution_time_end
        if self.execution_time_start:
            if hasattr(self.execution_time_start, 'to_alipay_dict'):
                params['execution_time_start'] = self.execution_time_start.to_alipay_dict()
            else:
                params['execution_time_start'] = self.execution_time_start
        if self.outer_code:
            if hasattr(self.outer_code, 'to_alipay_dict'):
                params['outer_code'] = self.outer_code.to_alipay_dict()
            else:
                params['outer_code'] = self.outer_code
        if self.record_id:
            if hasattr(self.record_id, 'to_alipay_dict'):
                params['record_id'] = self.record_id.to_alipay_dict()
            else:
                params['record_id'] = self.record_id
        if self.record_unit:
            if hasattr(self.record_unit, 'to_alipay_dict'):
                params['record_unit'] = self.record_unit.to_alipay_dict()
            else:
                params['record_unit'] = self.record_unit
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenServicemarketResourceCreateModel()
        if 'ability_resource_consume' in d:
            o.ability_resource_consume = d['ability_resource_consume']
        if 'execution_time_end' in d:
            o.execution_time_end = d['execution_time_end']
        if 'execution_time_start' in d:
            o.execution_time_start = d['execution_time_start']
        if 'outer_code' in d:
            o.outer_code = d['outer_code']
        if 'record_id' in d:
            o.record_id = d['record_id']
        if 'record_unit' in d:
            o.record_unit = d['record_unit']
        if 'uid' in d:
            o.uid = d['uid']
        return o


