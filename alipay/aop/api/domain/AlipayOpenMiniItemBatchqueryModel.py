#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniItemBatchqueryModel(object):

    def __init__(self):
        self._operation = None
        self._platform_item_id_list = None

    @property
    def operation(self):
        return self._operation

    @operation.setter
    def operation(self, value):
        self._operation = value
    @property
    def platform_item_id_list(self):
        return self._platform_item_id_list

    @platform_item_id_list.setter
    def platform_item_id_list(self, value):
        if isinstance(value, list):
            self._platform_item_id_list = list()
            for i in value:
                self._platform_item_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.operation:
            if hasattr(self.operation, 'to_alipay_dict'):
                params['operation'] = self.operation.to_alipay_dict()
            else:
                params['operation'] = self.operation
        if self.platform_item_id_list:
            if isinstance(self.platform_item_id_list, list):
                for i in range(0, len(self.platform_item_id_list)):
                    element = self.platform_item_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.platform_item_id_list[i] = element.to_alipay_dict()
            if hasattr(self.platform_item_id_list, 'to_alipay_dict'):
                params['platform_item_id_list'] = self.platform_item_id_list.to_alipay_dict()
            else:
                params['platform_item_id_list'] = self.platform_item_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniItemBatchqueryModel()
        if 'operation' in d:
            o.operation = d['operation']
        if 'platform_item_id_list' in d:
            o.platform_item_id_list = d['platform_item_id_list']
        return o


