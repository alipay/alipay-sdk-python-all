#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ComplextMockModel import ComplextMockModel


class ListListComplexMockModel(object):

    def __init__(self):
        self._cm_list = None

    @property
    def cm_list(self):
        return self._cm_list

    @cm_list.setter
    def cm_list(self, value):
        if isinstance(value, list):
            self._cm_list = list()
            for i in value:
                if isinstance(i, ComplextMockModel):
                    self._cm_list.append(i)
                else:
                    self._cm_list.append(ComplextMockModel.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.cm_list:
            if isinstance(self.cm_list, list):
                for i in range(0, len(self.cm_list)):
                    element = self.cm_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.cm_list[i] = element.to_alipay_dict()
            if hasattr(self.cm_list, 'to_alipay_dict'):
                params['cm_list'] = self.cm_list.to_alipay_dict()
            else:
                params['cm_list'] = self.cm_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ListListComplexMockModel()
        if 'cm_list' in d:
            o.cm_list = d['cm_list']
        return o


