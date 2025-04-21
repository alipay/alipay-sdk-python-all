#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbaseEntityroleHuaweimpBatchqueryModel(object):

    def __init__(self):
        self._passport_id_list = None

    @property
    def passport_id_list(self):
        return self._passport_id_list

    @passport_id_list.setter
    def passport_id_list(self, value):
        if isinstance(value, list):
            self._passport_id_list = list()
            for i in value:
                self._passport_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.passport_id_list:
            if isinstance(self.passport_id_list, list):
                for i in range(0, len(self.passport_id_list)):
                    element = self.passport_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.passport_id_list[i] = element.to_alipay_dict()
            if hasattr(self.passport_id_list, 'to_alipay_dict'):
                params['passport_id_list'] = self.passport_id_list.to_alipay_dict()
            else:
                params['passport_id_list'] = self.passport_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseEntityroleHuaweimpBatchqueryModel()
        if 'passport_id_list' in d:
            o.passport_id_list = d['passport_id_list']
        return o


