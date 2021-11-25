#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpOperationApplyModel(object):

    def __init__(self):
        self._access_product_code = None
        self._alipay_account = None
        self._isv_scene_permissions = None
        self._merchant_no = None
        self._operate_type = None
        self._out_biz_no = None

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
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


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
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpOperationApplyModel()
        if 'access_product_code' in d:
            o.access_product_code = d['access_product_code']
        if 'alipay_account' in d:
            o.alipay_account = d['alipay_account']
        if 'isv_scene_permissions' in d:
            o.isv_scene_permissions = d['isv_scene_permissions']
        if 'merchant_no' in d:
            o.merchant_no = d['merchant_no']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


