#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SignDataInfo import SignDataInfo
from alipay.aop.api.domain.SignTask import SignTask


class AlipaySecurityProdSignatureTaskApplyModel(object):

    def __init__(self):
        self._biz_app = None
        self._biz_id = None
        self._biz_info = None
        self._biz_product = None
        self._order_type = None
        self._service_version = None
        self._sign_data_list = None
        self._sign_task_list = None
        self._sign_task_type = None

    @property
    def biz_app(self):
        return self._biz_app

    @biz_app.setter
    def biz_app(self, value):
        self._biz_app = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def biz_info(self):
        return self._biz_info

    @biz_info.setter
    def biz_info(self, value):
        self._biz_info = value
    @property
    def biz_product(self):
        return self._biz_product

    @biz_product.setter
    def biz_product(self, value):
        self._biz_product = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def service_version(self):
        return self._service_version

    @service_version.setter
    def service_version(self, value):
        self._service_version = value
    @property
    def sign_data_list(self):
        return self._sign_data_list

    @sign_data_list.setter
    def sign_data_list(self, value):
        if isinstance(value, list):
            self._sign_data_list = list()
            for i in value:
                if isinstance(i, SignDataInfo):
                    self._sign_data_list.append(i)
                else:
                    self._sign_data_list.append(SignDataInfo.from_alipay_dict(i))
    @property
    def sign_task_list(self):
        return self._sign_task_list

    @sign_task_list.setter
    def sign_task_list(self, value):
        if isinstance(value, list):
            self._sign_task_list = list()
            for i in value:
                if isinstance(i, SignTask):
                    self._sign_task_list.append(i)
                else:
                    self._sign_task_list.append(SignTask.from_alipay_dict(i))
    @property
    def sign_task_type(self):
        return self._sign_task_type

    @sign_task_type.setter
    def sign_task_type(self, value):
        self._sign_task_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_app:
            if hasattr(self.biz_app, 'to_alipay_dict'):
                params['biz_app'] = self.biz_app.to_alipay_dict()
            else:
                params['biz_app'] = self.biz_app
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.biz_info:
            if hasattr(self.biz_info, 'to_alipay_dict'):
                params['biz_info'] = self.biz_info.to_alipay_dict()
            else:
                params['biz_info'] = self.biz_info
        if self.biz_product:
            if hasattr(self.biz_product, 'to_alipay_dict'):
                params['biz_product'] = self.biz_product.to_alipay_dict()
            else:
                params['biz_product'] = self.biz_product
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.service_version:
            if hasattr(self.service_version, 'to_alipay_dict'):
                params['service_version'] = self.service_version.to_alipay_dict()
            else:
                params['service_version'] = self.service_version
        if self.sign_data_list:
            if isinstance(self.sign_data_list, list):
                for i in range(0, len(self.sign_data_list)):
                    element = self.sign_data_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sign_data_list[i] = element.to_alipay_dict()
            if hasattr(self.sign_data_list, 'to_alipay_dict'):
                params['sign_data_list'] = self.sign_data_list.to_alipay_dict()
            else:
                params['sign_data_list'] = self.sign_data_list
        if self.sign_task_list:
            if isinstance(self.sign_task_list, list):
                for i in range(0, len(self.sign_task_list)):
                    element = self.sign_task_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sign_task_list[i] = element.to_alipay_dict()
            if hasattr(self.sign_task_list, 'to_alipay_dict'):
                params['sign_task_list'] = self.sign_task_list.to_alipay_dict()
            else:
                params['sign_task_list'] = self.sign_task_list
        if self.sign_task_type:
            if hasattr(self.sign_task_type, 'to_alipay_dict'):
                params['sign_task_type'] = self.sign_task_type.to_alipay_dict()
            else:
                params['sign_task_type'] = self.sign_task_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdSignatureTaskApplyModel()
        if 'biz_app' in d:
            o.biz_app = d['biz_app']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'biz_info' in d:
            o.biz_info = d['biz_info']
        if 'biz_product' in d:
            o.biz_product = d['biz_product']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'service_version' in d:
            o.service_version = d['service_version']
        if 'sign_data_list' in d:
            o.sign_data_list = d['sign_data_list']
        if 'sign_task_list' in d:
            o.sign_task_list = d['sign_task_list']
        if 'sign_task_type' in d:
            o.sign_task_type = d['sign_task_type']
        return o


