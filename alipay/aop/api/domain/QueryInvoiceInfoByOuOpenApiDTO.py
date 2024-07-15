#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QueryInvoiceInfoByOuOpenApiDTO(object):

    def __init__(self):
        self._ou_code_list = None

    @property
    def ou_code_list(self):
        return self._ou_code_list

    @ou_code_list.setter
    def ou_code_list(self, value):
        if isinstance(value, list):
            self._ou_code_list = list()
            for i in value:
                self._ou_code_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.ou_code_list:
            if isinstance(self.ou_code_list, list):
                for i in range(0, len(self.ou_code_list)):
                    element = self.ou_code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ou_code_list[i] = element.to_alipay_dict()
            if hasattr(self.ou_code_list, 'to_alipay_dict'):
                params['ou_code_list'] = self.ou_code_list.to_alipay_dict()
            else:
                params['ou_code_list'] = self.ou_code_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QueryInvoiceInfoByOuOpenApiDTO()
        if 'ou_code_list' in d:
            o.ou_code_list = d['ou_code_list']
        return o


