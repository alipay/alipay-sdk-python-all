#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiItemExtitemExistedQueryModel(object):

    def __init__(self):
        self._code_list = None

    @property
    def code_list(self):
        return self._code_list

    @code_list.setter
    def code_list(self, value):
        if isinstance(value, list):
            self._code_list = list()
            for i in value:
                self._code_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.code_list:
            if isinstance(self.code_list, list):
                for i in range(0, len(self.code_list)):
                    element = self.code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.code_list[i] = element.to_alipay_dict()
            if hasattr(self.code_list, 'to_alipay_dict'):
                params['code_list'] = self.code_list.to_alipay_dict()
            else:
                params['code_list'] = self.code_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiItemExtitemExistedQueryModel()
        if 'code_list' in d:
            o.code_list = d['code_list']
        return o


