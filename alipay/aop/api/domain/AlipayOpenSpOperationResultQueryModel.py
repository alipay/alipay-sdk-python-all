#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpOperationResultQueryModel(object):

    def __init__(self):
        self._access_product_code = None
        self._alipay_account = None
        self._batch_no = None
        self._isv_scene_permissions = None
        self._merchant_no = None
        self._operate_type = None

    @property
    def access_product_code(self):
        return self._access_product_code

    @access_product_code.setter
    def access_product_code(self, value):
        self._access_product_code = value
    @property
    def alipay_account(self):
        return self._alipay_account

    @alipay_account.setter
    def alipay_account(self, value):
        self._alipay_account = value
    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def isv_scene_permissions(self):
        return self._isv_scene_permissions

    @isv_scene_permissions.setter
    def isv_scene_permissions(self, value):
        self._isv_scene_permissions = value
    @property
    def merchant_no(self):
        return self._merchant_no

    @merchant_no.setter
    def merchant_no(self, value):
        self._merchant_no = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_product_code:
            if hasattr(self.access_product_code, 'to_alipay_dict'):
                params['access_product_code'] = self.access_product_code.to_alipay_dict()
            else:
                params['access_product_code'] = self.access_product_code
        if self.alipay_account:
            if hasattr(self.alipay_account, 'to_alipay_dict'):
                params['alipay_account'] = self.alipay_account.to_alipay_dict()
            else:
                params['alipay_account'] = self.alipay_account
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.isv_scene_permissions:
            if hasattr(self.isv_scene_permissions, 'to_alipay_dict'):
                params['isv_scene_permissions'] = self.isv_scene_permissions.to_alipay_dict()
            else:
                params['isv_scene_permissions'] = self.isv_scene_permissions
        if self.merchant_no:
            if hasattr(self.merchant_no, 'to_alipay_dict'):
                params['merchant_no'] = self.merchant_no.to_alipay_dict()
            else:
                params['merchant_no'] = self.merchant_no
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpOperationResultQueryModel()
        if 'access_product_code' in d:
            o.access_product_code = d['access_product_code']
        if 'alipay_account' in d:
            o.alipay_account = d['alipay_account']
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'isv_scene_permissions' in d:
            o.isv_scene_permissions = d['isv_scene_permissions']
        if 'merchant_no' in d:
            o.merchant_no = d['merchant_no']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        return o


