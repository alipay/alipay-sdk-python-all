#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingToolFengdieTemplateSendModel(object):

    def __init__(self):
        self._operator = None
        self._space_ids = None
        self._template_name = None

    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def space_ids(self):
        return self._space_ids

    @space_ids.setter
    def space_ids(self, value):
        if isinstance(value, list):
            self._space_ids = list()
            for i in value:
                self._space_ids.append(i)
    @property
    def template_name(self):
        return self._template_name

    @template_name.setter
    def template_name(self, value):
        self._template_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.space_ids:
            if isinstance(self.space_ids, list):
                for i in range(0, len(self.space_ids)):
                    element = self.space_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.space_ids[i] = element.to_alipay_dict()
            if hasattr(self.space_ids, 'to_alipay_dict'):
                params['space_ids'] = self.space_ids.to_alipay_dict()
            else:
                params['space_ids'] = self.space_ids
        if self.template_name:
            if hasattr(self.template_name, 'to_alipay_dict'):
                params['template_name'] = self.template_name.to_alipay_dict()
            else:
                params['template_name'] = self.template_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingToolFengdieTemplateSendModel()
        if 'operator' in d:
            o.operator = d['operator']
        if 'space_ids' in d:
            o.space_ids = d['space_ids']
        if 'template_name' in d:
            o.template_name = d['template_name']
        return o


