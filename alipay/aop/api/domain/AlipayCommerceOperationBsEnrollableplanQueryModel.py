#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceOperationBsEnrollableplanQueryModel(object):

    def __init__(self):
        self._channel = None
        self._merchant_benefit_types = None
        self._page_index = None
        self._page_size = None
        self._plan_name = None
        self._solution_code = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def merchant_benefit_types(self):
        return self._merchant_benefit_types

    @merchant_benefit_types.setter
    def merchant_benefit_types(self, value):
        if isinstance(value, list):
            self._merchant_benefit_types = list()
            for i in value:
                self._merchant_benefit_types.append(i)
    @property
    def page_index(self):
        return self._page_index

    @page_index.setter
    def page_index(self, value):
        self._page_index = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def plan_name(self):
        return self._plan_name

    @plan_name.setter
    def plan_name(self, value):
        self._plan_name = value
    @property
    def solution_code(self):
        return self._solution_code

    @solution_code.setter
    def solution_code(self, value):
        self._solution_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.merchant_benefit_types:
            if isinstance(self.merchant_benefit_types, list):
                for i in range(0, len(self.merchant_benefit_types)):
                    element = self.merchant_benefit_types[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.merchant_benefit_types[i] = element.to_alipay_dict()
            if hasattr(self.merchant_benefit_types, 'to_alipay_dict'):
                params['merchant_benefit_types'] = self.merchant_benefit_types.to_alipay_dict()
            else:
                params['merchant_benefit_types'] = self.merchant_benefit_types
        if self.page_index:
            if hasattr(self.page_index, 'to_alipay_dict'):
                params['page_index'] = self.page_index.to_alipay_dict()
            else:
                params['page_index'] = self.page_index
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.plan_name:
            if hasattr(self.plan_name, 'to_alipay_dict'):
                params['plan_name'] = self.plan_name.to_alipay_dict()
            else:
                params['plan_name'] = self.plan_name
        if self.solution_code:
            if hasattr(self.solution_code, 'to_alipay_dict'):
                params['solution_code'] = self.solution_code.to_alipay_dict()
            else:
                params['solution_code'] = self.solution_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationBsEnrollableplanQueryModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'merchant_benefit_types' in d:
            o.merchant_benefit_types = d['merchant_benefit_types']
        if 'page_index' in d:
            o.page_index = d['page_index']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'plan_name' in d:
            o.plan_name = d['plan_name']
        if 'solution_code' in d:
            o.solution_code = d['solution_code']
        return o


