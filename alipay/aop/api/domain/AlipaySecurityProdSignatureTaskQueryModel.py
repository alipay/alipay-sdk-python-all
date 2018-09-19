#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdSignatureTaskQueryModel(object):

    def __init__(self):
        self._biz_product = None
        self._order_id = None
        self._service_version = None
        self._task_id_list = None

    @property
    def biz_product(self):
        return self._biz_product

    @biz_product.setter
    def biz_product(self, value):
        self._biz_product = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def service_version(self):
        return self._service_version

    @service_version.setter
    def service_version(self, value):
        self._service_version = value
    @property
    def task_id_list(self):
        return self._task_id_list

    @task_id_list.setter
    def task_id_list(self, value):
        if isinstance(value, list):
            self._task_id_list = list()
            for i in value:
                self._task_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.biz_product:
            if hasattr(self.biz_product, 'to_alipay_dict'):
                params['biz_product'] = self.biz_product.to_alipay_dict()
            else:
                params['biz_product'] = self.biz_product
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.service_version:
            if hasattr(self.service_version, 'to_alipay_dict'):
                params['service_version'] = self.service_version.to_alipay_dict()
            else:
                params['service_version'] = self.service_version
        if self.task_id_list:
            if isinstance(self.task_id_list, list):
                for i in range(0, len(self.task_id_list)):
                    element = self.task_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.task_id_list[i] = element.to_alipay_dict()
            if hasattr(self.task_id_list, 'to_alipay_dict'):
                params['task_id_list'] = self.task_id_list.to_alipay_dict()
            else:
                params['task_id_list'] = self.task_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdSignatureTaskQueryModel()
        if 'biz_product' in d:
            o.biz_product = d['biz_product']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'service_version' in d:
            o.service_version = d['service_version']
        if 'task_id_list' in d:
            o.task_id_list = d['task_id_list']
        return o


