#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossFncWallstreetCompareflowTransferModel(object):

    def __init__(self):
        self._compare_method_name = None
        self._compare_method_param_tp = None
        self._compare_service = None
        self._parameter_map = None
        self._vpc_result = None

    @property
    def compare_method_name(self):
        return self._compare_method_name

    @compare_method_name.setter
    def compare_method_name(self, value):
        self._compare_method_name = value
    @property
    def compare_method_param_tp(self):
        return self._compare_method_param_tp

    @compare_method_param_tp.setter
    def compare_method_param_tp(self, value):
        if isinstance(value, list):
            self._compare_method_param_tp = list()
            for i in value:
                self._compare_method_param_tp.append(i)
    @property
    def compare_service(self):
        return self._compare_service

    @compare_service.setter
    def compare_service(self, value):
        self._compare_service = value
    @property
    def parameter_map(self):
        return self._parameter_map

    @parameter_map.setter
    def parameter_map(self, value):
        self._parameter_map = value
    @property
    def vpc_result(self):
        return self._vpc_result

    @vpc_result.setter
    def vpc_result(self, value):
        self._vpc_result = value


    def to_alipay_dict(self):
        params = dict()
        if self.compare_method_name:
            if hasattr(self.compare_method_name, 'to_alipay_dict'):
                params['compare_method_name'] = self.compare_method_name.to_alipay_dict()
            else:
                params['compare_method_name'] = self.compare_method_name
        if self.compare_method_param_tp:
            if isinstance(self.compare_method_param_tp, list):
                for i in range(0, len(self.compare_method_param_tp)):
                    element = self.compare_method_param_tp[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.compare_method_param_tp[i] = element.to_alipay_dict()
            if hasattr(self.compare_method_param_tp, 'to_alipay_dict'):
                params['compare_method_param_tp'] = self.compare_method_param_tp.to_alipay_dict()
            else:
                params['compare_method_param_tp'] = self.compare_method_param_tp
        if self.compare_service:
            if hasattr(self.compare_service, 'to_alipay_dict'):
                params['compare_service'] = self.compare_service.to_alipay_dict()
            else:
                params['compare_service'] = self.compare_service
        if self.parameter_map:
            if hasattr(self.parameter_map, 'to_alipay_dict'):
                params['parameter_map'] = self.parameter_map.to_alipay_dict()
            else:
                params['parameter_map'] = self.parameter_map
        if self.vpc_result:
            if hasattr(self.vpc_result, 'to_alipay_dict'):
                params['vpc_result'] = self.vpc_result.to_alipay_dict()
            else:
                params['vpc_result'] = self.vpc_result
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncWallstreetCompareflowTransferModel()
        if 'compare_method_name' in d:
            o.compare_method_name = d['compare_method_name']
        if 'compare_method_param_tp' in d:
            o.compare_method_param_tp = d['compare_method_param_tp']
        if 'compare_service' in d:
            o.compare_service = d['compare_service']
        if 'parameter_map' in d:
            o.parameter_map = d['parameter_map']
        if 'vpc_result' in d:
            o.vpc_result = d['vpc_result']
        return o


