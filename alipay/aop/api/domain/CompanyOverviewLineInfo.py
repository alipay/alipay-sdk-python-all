#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CompanyOverviewHighLight import CompanyOverviewHighLight


class CompanyOverviewLineInfo(object):

    def __init__(self):
        self._content = None
        self._high_light_model_list = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def high_light_model_list(self):
        return self._high_light_model_list

    @high_light_model_list.setter
    def high_light_model_list(self, value):
        if isinstance(value, list):
            self._high_light_model_list = list()
            for i in value:
                if isinstance(i, CompanyOverviewHighLight):
                    self._high_light_model_list.append(i)
                else:
                    self._high_light_model_list.append(CompanyOverviewHighLight.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.high_light_model_list:
            if isinstance(self.high_light_model_list, list):
                for i in range(0, len(self.high_light_model_list)):
                    element = self.high_light_model_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.high_light_model_list[i] = element.to_alipay_dict()
            if hasattr(self.high_light_model_list, 'to_alipay_dict'):
                params['high_light_model_list'] = self.high_light_model_list.to_alipay_dict()
            else:
                params['high_light_model_list'] = self.high_light_model_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CompanyOverviewLineInfo()
        if 'content' in d:
            o.content = d['content']
        if 'high_light_model_list' in d:
            o.high_light_model_list = d['high_light_model_list']
        return o


