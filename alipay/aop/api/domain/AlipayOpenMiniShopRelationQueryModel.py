#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniShopRelationQueryModel(object):

    def __init__(self):
        self._entity_id_list = None
        self._operation = None
        self._page_num = None
        self._page_size = None

    @property
    def entity_id_list(self):
        return self._entity_id_list

    @entity_id_list.setter
    def entity_id_list(self, value):
        if isinstance(value, list):
            self._entity_id_list = list()
            for i in value:
                self._entity_id_list.append(i)
    @property
    def operation(self):
        return self._operation

    @operation.setter
    def operation(self, value):
        self._operation = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value


    def to_alipay_dict(self):
        params = dict()
        if self.entity_id_list:
            if isinstance(self.entity_id_list, list):
                for i in range(0, len(self.entity_id_list)):
                    element = self.entity_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.entity_id_list[i] = element.to_alipay_dict()
            if hasattr(self.entity_id_list, 'to_alipay_dict'):
                params['entity_id_list'] = self.entity_id_list.to_alipay_dict()
            else:
                params['entity_id_list'] = self.entity_id_list
        if self.operation:
            if hasattr(self.operation, 'to_alipay_dict'):
                params['operation'] = self.operation.to_alipay_dict()
            else:
                params['operation'] = self.operation
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniShopRelationQueryModel()
        if 'entity_id_list' in d:
            o.entity_id_list = d['entity_id_list']
        if 'operation' in d:
            o.operation = d['operation']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o


