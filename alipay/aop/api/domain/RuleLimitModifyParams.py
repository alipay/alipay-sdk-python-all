#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RuleLimitContent import RuleLimitContent


class RuleLimitModifyParams(object):

    def __init__(self):
        self._limit_list = None
        self._limit_modify_type = None

    @property
    def limit_list(self):
        return self._limit_list

    @limit_list.setter
    def limit_list(self, value):
        if isinstance(value, list):
            self._limit_list = list()
            for i in value:
                if isinstance(i, RuleLimitContent):
                    self._limit_list.append(i)
                else:
                    self._limit_list.append(RuleLimitContent.from_alipay_dict(i))
    @property
    def limit_modify_type(self):
        return self._limit_modify_type

    @limit_modify_type.setter
    def limit_modify_type(self, value):
        self._limit_modify_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.limit_list:
            if isinstance(self.limit_list, list):
                for i in range(0, len(self.limit_list)):
                    element = self.limit_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.limit_list[i] = element.to_alipay_dict()
            if hasattr(self.limit_list, 'to_alipay_dict'):
                params['limit_list'] = self.limit_list.to_alipay_dict()
            else:
                params['limit_list'] = self.limit_list
        if self.limit_modify_type:
            if hasattr(self.limit_modify_type, 'to_alipay_dict'):
                params['limit_modify_type'] = self.limit_modify_type.to_alipay_dict()
            else:
                params['limit_modify_type'] = self.limit_modify_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RuleLimitModifyParams()
        if 'limit_list' in d:
            o.limit_list = d['limit_list']
        if 'limit_modify_type' in d:
            o.limit_modify_type = d['limit_modify_type']
        return o


