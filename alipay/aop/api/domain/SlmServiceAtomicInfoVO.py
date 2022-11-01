#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Operator import Operator
from alipay.aop.api.domain.SlmMethodInfo import SlmMethodInfo


class SlmServiceAtomicInfoVO(object):

    def __init__(self):
        self._operate = None
        self._operate_desc = None
        self._operator = None
        self._slm_service_atomic_info_list = None
        self._type = None

    @property
    def operate(self):
        return self._operate

    @operate.setter
    def operate(self, value):
        self._operate = value
    @property
    def operate_desc(self):
        return self._operate_desc

    @operate_desc.setter
    def operate_desc(self, value):
        self._operate_desc = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        if isinstance(value, Operator):
            self._operator = value
        else:
            self._operator = Operator.from_alipay_dict(value)
    @property
    def slm_service_atomic_info_list(self):
        return self._slm_service_atomic_info_list

    @slm_service_atomic_info_list.setter
    def slm_service_atomic_info_list(self, value):
        if isinstance(value, SlmMethodInfo):
            self._slm_service_atomic_info_list = value
        else:
            self._slm_service_atomic_info_list = SlmMethodInfo.from_alipay_dict(value)
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.operate:
            if hasattr(self.operate, 'to_alipay_dict'):
                params['operate'] = self.operate.to_alipay_dict()
            else:
                params['operate'] = self.operate
        if self.operate_desc:
            if hasattr(self.operate_desc, 'to_alipay_dict'):
                params['operate_desc'] = self.operate_desc.to_alipay_dict()
            else:
                params['operate_desc'] = self.operate_desc
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.slm_service_atomic_info_list:
            if hasattr(self.slm_service_atomic_info_list, 'to_alipay_dict'):
                params['slm_service_atomic_info_list'] = self.slm_service_atomic_info_list.to_alipay_dict()
            else:
                params['slm_service_atomic_info_list'] = self.slm_service_atomic_info_list
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SlmServiceAtomicInfoVO()
        if 'operate' in d:
            o.operate = d['operate']
        if 'operate_desc' in d:
            o.operate_desc = d['operate_desc']
        if 'operator' in d:
            o.operator = d['operator']
        if 'slm_service_atomic_info_list' in d:
            o.slm_service_atomic_info_list = d['slm_service_atomic_info_list']
        if 'type' in d:
            o.type = d['type']
        return o


