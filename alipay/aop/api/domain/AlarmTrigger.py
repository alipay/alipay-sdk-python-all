#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AlarmCompareRule import AlarmCompareRule
from alipay.aop.api.domain.AlarmFunctionFilter import AlarmFunctionFilter


class AlarmTrigger(object):

    def __init__(self):
        self._aggregator = None
        self._aggregator_range = None
        self._compare_rules = None
        self._condition_type = None
        self._function_filters = None
        self._metric = None
        self._product = None
        self._product_operate = None
        self._step_num = None
        self._zero_fill = None

    @property
    def aggregator(self):
        return self._aggregator

    @aggregator.setter
    def aggregator(self, value):
        self._aggregator = value
    @property
    def aggregator_range(self):
        return self._aggregator_range

    @aggregator_range.setter
    def aggregator_range(self, value):
        self._aggregator_range = value
    @property
    def compare_rules(self):
        return self._compare_rules

    @compare_rules.setter
    def compare_rules(self, value):
        if isinstance(value, list):
            self._compare_rules = list()
            for i in value:
                if isinstance(i, AlarmCompareRule):
                    self._compare_rules.append(i)
                else:
                    self._compare_rules.append(AlarmCompareRule.from_alipay_dict(i))
    @property
    def condition_type(self):
        return self._condition_type

    @condition_type.setter
    def condition_type(self, value):
        self._condition_type = value
    @property
    def function_filters(self):
        return self._function_filters

    @function_filters.setter
    def function_filters(self, value):
        if isinstance(value, list):
            self._function_filters = list()
            for i in value:
                if isinstance(i, AlarmFunctionFilter):
                    self._function_filters.append(i)
                else:
                    self._function_filters.append(AlarmFunctionFilter.from_alipay_dict(i))
    @property
    def metric(self):
        return self._metric

    @metric.setter
    def metric(self, value):
        self._metric = value
    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        self._product = value
    @property
    def product_operate(self):
        return self._product_operate

    @product_operate.setter
    def product_operate(self, value):
        self._product_operate = value
    @property
    def step_num(self):
        return self._step_num

    @step_num.setter
    def step_num(self, value):
        self._step_num = value
    @property
    def zero_fill(self):
        return self._zero_fill

    @zero_fill.setter
    def zero_fill(self, value):
        self._zero_fill = value


    def to_alipay_dict(self):
        params = dict()
        if self.aggregator:
            if hasattr(self.aggregator, 'to_alipay_dict'):
                params['aggregator'] = self.aggregator.to_alipay_dict()
            else:
                params['aggregator'] = self.aggregator
        if self.aggregator_range:
            if hasattr(self.aggregator_range, 'to_alipay_dict'):
                params['aggregator_range'] = self.aggregator_range.to_alipay_dict()
            else:
                params['aggregator_range'] = self.aggregator_range
        if self.compare_rules:
            if isinstance(self.compare_rules, list):
                for i in range(0, len(self.compare_rules)):
                    element = self.compare_rules[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.compare_rules[i] = element.to_alipay_dict()
            if hasattr(self.compare_rules, 'to_alipay_dict'):
                params['compare_rules'] = self.compare_rules.to_alipay_dict()
            else:
                params['compare_rules'] = self.compare_rules
        if self.condition_type:
            if hasattr(self.condition_type, 'to_alipay_dict'):
                params['condition_type'] = self.condition_type.to_alipay_dict()
            else:
                params['condition_type'] = self.condition_type
        if self.function_filters:
            if isinstance(self.function_filters, list):
                for i in range(0, len(self.function_filters)):
                    element = self.function_filters[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.function_filters[i] = element.to_alipay_dict()
            if hasattr(self.function_filters, 'to_alipay_dict'):
                params['function_filters'] = self.function_filters.to_alipay_dict()
            else:
                params['function_filters'] = self.function_filters
        if self.metric:
            if hasattr(self.metric, 'to_alipay_dict'):
                params['metric'] = self.metric.to_alipay_dict()
            else:
                params['metric'] = self.metric
        if self.product:
            if hasattr(self.product, 'to_alipay_dict'):
                params['product'] = self.product.to_alipay_dict()
            else:
                params['product'] = self.product
        if self.product_operate:
            if hasattr(self.product_operate, 'to_alipay_dict'):
                params['product_operate'] = self.product_operate.to_alipay_dict()
            else:
                params['product_operate'] = self.product_operate
        if self.step_num:
            if hasattr(self.step_num, 'to_alipay_dict'):
                params['step_num'] = self.step_num.to_alipay_dict()
            else:
                params['step_num'] = self.step_num
        if self.zero_fill:
            if hasattr(self.zero_fill, 'to_alipay_dict'):
                params['zero_fill'] = self.zero_fill.to_alipay_dict()
            else:
                params['zero_fill'] = self.zero_fill
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlarmTrigger()
        if 'aggregator' in d:
            o.aggregator = d['aggregator']
        if 'aggregator_range' in d:
            o.aggregator_range = d['aggregator_range']
        if 'compare_rules' in d:
            o.compare_rules = d['compare_rules']
        if 'condition_type' in d:
            o.condition_type = d['condition_type']
        if 'function_filters' in d:
            o.function_filters = d['function_filters']
        if 'metric' in d:
            o.metric = d['metric']
        if 'product' in d:
            o.product = d['product']
        if 'product_operate' in d:
            o.product_operate = d['product_operate']
        if 'step_num' in d:
            o.step_num = d['step_num']
        if 'zero_fill' in d:
            o.zero_fill = d['zero_fill']
        return o


