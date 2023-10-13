#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StoreInfoDTO(object):

    def __init__(self):
        self._mall_id = None
        self._real_store_id = None
        self._real_store_id_list = None

    @property
    def mall_id(self):
        return self._mall_id

    @mall_id.setter
    def mall_id(self, value):
        self._mall_id = value
    @property
    def real_store_id(self):
        return self._real_store_id

    @real_store_id.setter
    def real_store_id(self, value):
        self._real_store_id = value
    @property
    def real_store_id_list(self):
        return self._real_store_id_list

    @real_store_id_list.setter
    def real_store_id_list(self, value):
        if isinstance(value, list):
            self._real_store_id_list = list()
            for i in value:
                self._real_store_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.mall_id:
            if hasattr(self.mall_id, 'to_alipay_dict'):
                params['mall_id'] = self.mall_id.to_alipay_dict()
            else:
                params['mall_id'] = self.mall_id
        if self.real_store_id:
            if hasattr(self.real_store_id, 'to_alipay_dict'):
                params['real_store_id'] = self.real_store_id.to_alipay_dict()
            else:
                params['real_store_id'] = self.real_store_id
        if self.real_store_id_list:
            if isinstance(self.real_store_id_list, list):
                for i in range(0, len(self.real_store_id_list)):
                    element = self.real_store_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.real_store_id_list[i] = element.to_alipay_dict()
            if hasattr(self.real_store_id_list, 'to_alipay_dict'):
                params['real_store_id_list'] = self.real_store_id_list.to_alipay_dict()
            else:
                params['real_store_id_list'] = self.real_store_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StoreInfoDTO()
        if 'mall_id' in d:
            o.mall_id = d['mall_id']
        if 'real_store_id' in d:
            o.real_store_id = d['real_store_id']
        if 'real_store_id_list' in d:
            o.real_store_id_list = d['real_store_id_list']
        return o


