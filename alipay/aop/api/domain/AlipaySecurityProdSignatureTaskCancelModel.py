#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdSignatureTaskCancelModel(object):

    def __init__(self):
        self._biz_id = None
        self._biz_product = None
        self._service_version = None
        self._task_id = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def biz_product(self):
        return self._biz_product

    @biz_product.setter
    def biz_product(self, value):
        self._biz_product = value
    @property
    def service_version(self):
        return self._service_version

    @service_version.setter
    def service_version(self, value):
        self._service_version = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.biz_product:
            if hasattr(self.biz_product, 'to_alipay_dict'):
                params['biz_product'] = self.biz_product.to_alipay_dict()
            else:
                params['biz_product'] = self.biz_product
        if self.service_version:
            if hasattr(self.service_version, 'to_alipay_dict'):
                params['service_version'] = self.service_version.to_alipay_dict()
            else:
                params['service_version'] = self.service_version
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdSignatureTaskCancelModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'biz_product' in d:
            o.biz_product = d['biz_product']
        if 'service_version' in d:
            o.service_version = d['service_version']
        if 'task_id' in d:
            o.task_id = d['task_id']
        return o


