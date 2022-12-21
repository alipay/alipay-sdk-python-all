#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundWalletSceneSignModel(object):

    def __init__(self):
        self._biz_scene = None
        self._out_biz_no = None
        self._principal_open_id = None
        self._product_code = None
        self._user_id = None
        self._wallet_template_id = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def principal_open_id(self):
        return self._principal_open_id

    @principal_open_id.setter
    def principal_open_id(self, value):
        self._principal_open_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def wallet_template_id(self):
        return self._wallet_template_id

    @wallet_template_id.setter
    def wallet_template_id(self, value):
        self._wallet_template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.principal_open_id:
            if hasattr(self.principal_open_id, 'to_alipay_dict'):
                params['principal_open_id'] = self.principal_open_id.to_alipay_dict()
            else:
                params['principal_open_id'] = self.principal_open_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.wallet_template_id:
            if hasattr(self.wallet_template_id, 'to_alipay_dict'):
                params['wallet_template_id'] = self.wallet_template_id.to_alipay_dict()
            else:
                params['wallet_template_id'] = self.wallet_template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundWalletSceneSignModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'principal_open_id' in d:
            o.principal_open_id = d['principal_open_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'wallet_template_id' in d:
            o.wallet_template_id = d['wallet_template_id']
        return o


