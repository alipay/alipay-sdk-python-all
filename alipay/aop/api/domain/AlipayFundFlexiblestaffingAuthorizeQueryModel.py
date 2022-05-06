#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundFlexiblestaffingAuthorizeQueryModel(object):

    def __init__(self):
        self._biz_scene = None
        self._principal_account_no = None
        self._principal_id = None
        self._product_code = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def principal_account_no(self):
        return self._principal_account_no

    @principal_account_no.setter
    def principal_account_no(self, value):
        self._principal_account_no = value
    @property
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.principal_account_no:
            if hasattr(self.principal_account_no, 'to_alipay_dict'):
                params['principal_account_no'] = self.principal_account_no.to_alipay_dict()
            else:
                params['principal_account_no'] = self.principal_account_no
        if self.principal_id:
            if hasattr(self.principal_id, 'to_alipay_dict'):
                params['principal_id'] = self.principal_id.to_alipay_dict()
            else:
                params['principal_id'] = self.principal_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundFlexiblestaffingAuthorizeQueryModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'principal_account_no' in d:
            o.principal_account_no = d['principal_account_no']
        if 'principal_id' in d:
            o.principal_id = d['principal_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


