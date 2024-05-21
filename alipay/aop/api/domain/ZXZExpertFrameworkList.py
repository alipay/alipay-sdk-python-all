#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FinFrameworkDetail import FinFrameworkDetail


class ZXZExpertFrameworkList(object):

    def __init__(self):
        self._framework_list = None
        self._type_name = None

    @property
    def framework_list(self):
        return self._framework_list

    @framework_list.setter
    def framework_list(self, value):
        if isinstance(value, list):
            self._framework_list = list()
            for i in value:
                if isinstance(i, FinFrameworkDetail):
                    self._framework_list.append(i)
                else:
                    self._framework_list.append(FinFrameworkDetail.from_alipay_dict(i))
    @property
    def type_name(self):
        return self._type_name

    @type_name.setter
    def type_name(self, value):
        self._type_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.framework_list:
            if isinstance(self.framework_list, list):
                for i in range(0, len(self.framework_list)):
                    element = self.framework_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.framework_list[i] = element.to_alipay_dict()
            if hasattr(self.framework_list, 'to_alipay_dict'):
                params['framework_list'] = self.framework_list.to_alipay_dict()
            else:
                params['framework_list'] = self.framework_list
        if self.type_name:
            if hasattr(self.type_name, 'to_alipay_dict'):
                params['type_name'] = self.type_name.to_alipay_dict()
            else:
                params['type_name'] = self.type_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZXZExpertFrameworkList()
        if 'framework_list' in d:
            o.framework_list = d['framework_list']
        if 'type_name' in d:
            o.type_name = d['type_name']
        return o


