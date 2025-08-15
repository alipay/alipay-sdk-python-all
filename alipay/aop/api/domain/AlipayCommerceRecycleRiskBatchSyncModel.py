#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecycleBlackList import RecycleBlackList


class AlipayCommerceRecycleRiskBatchSyncModel(object):

    def __init__(self):
        self._black_list = None
        self._black_list_type = None
        self._service_category_code = None

    @property
    def black_list(self):
        return self._black_list

    @black_list.setter
    def black_list(self, value):
        if isinstance(value, list):
            self._black_list = list()
            for i in value:
                if isinstance(i, RecycleBlackList):
                    self._black_list.append(i)
                else:
                    self._black_list.append(RecycleBlackList.from_alipay_dict(i))
    @property
    def black_list_type(self):
        return self._black_list_type

    @black_list_type.setter
    def black_list_type(self, value):
        self._black_list_type = value
    @property
    def service_category_code(self):
        return self._service_category_code

    @service_category_code.setter
    def service_category_code(self, value):
        self._service_category_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.black_list:
            if isinstance(self.black_list, list):
                for i in range(0, len(self.black_list)):
                    element = self.black_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.black_list[i] = element.to_alipay_dict()
            if hasattr(self.black_list, 'to_alipay_dict'):
                params['black_list'] = self.black_list.to_alipay_dict()
            else:
                params['black_list'] = self.black_list
        if self.black_list_type:
            if hasattr(self.black_list_type, 'to_alipay_dict'):
                params['black_list_type'] = self.black_list_type.to_alipay_dict()
            else:
                params['black_list_type'] = self.black_list_type
        if self.service_category_code:
            if hasattr(self.service_category_code, 'to_alipay_dict'):
                params['service_category_code'] = self.service_category_code.to_alipay_dict()
            else:
                params['service_category_code'] = self.service_category_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRecycleRiskBatchSyncModel()
        if 'black_list' in d:
            o.black_list = d['black_list']
        if 'black_list_type' in d:
            o.black_list_type = d['black_list_type']
        if 'service_category_code' in d:
            o.service_category_code = d['service_category_code']
        return o


