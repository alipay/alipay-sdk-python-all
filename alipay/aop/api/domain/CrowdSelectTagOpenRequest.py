#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CrowdSelectTagValuesOpenRequest import CrowdSelectTagValuesOpenRequest


class CrowdSelectTagOpenRequest(object):

    def __init__(self):
        self._select_tag_values = None

    @property
    def select_tag_values(self):
        return self._select_tag_values

    @select_tag_values.setter
    def select_tag_values(self, value):
        if isinstance(value, list):
            self._select_tag_values = list()
            for i in value:
                if isinstance(i, CrowdSelectTagValuesOpenRequest):
                    self._select_tag_values.append(i)
                else:
                    self._select_tag_values.append(CrowdSelectTagValuesOpenRequest.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.select_tag_values:
            if isinstance(self.select_tag_values, list):
                for i in range(0, len(self.select_tag_values)):
                    element = self.select_tag_values[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.select_tag_values[i] = element.to_alipay_dict()
            if hasattr(self.select_tag_values, 'to_alipay_dict'):
                params['select_tag_values'] = self.select_tag_values.to_alipay_dict()
            else:
                params['select_tag_values'] = self.select_tag_values
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CrowdSelectTagOpenRequest()
        if 'select_tag_values' in d:
            o.select_tag_values = d['select_tag_values']
        return o


