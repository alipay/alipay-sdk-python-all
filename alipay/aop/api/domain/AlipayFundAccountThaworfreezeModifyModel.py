#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundAccountThaworfreezeModifyModel(object):

    def __init__(self):
        self._biz_scene = None
        self._business_lice = None
        self._open_id = None
        self._operate_type = None
        self._product_code = None
        self._taobao_agreement_id = None
        self._taobao_sign_time = None
        self._taobao_user_id = None
        self._taobao_user_type = None
        self._user_id = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def business_lice(self):
        return self._business_lice

    @business_lice.setter
    def business_lice(self, value):
        self._business_lice = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def taobao_agreement_id(self):
        return self._taobao_agreement_id

    @taobao_agreement_id.setter
    def taobao_agreement_id(self, value):
        self._taobao_agreement_id = value
    @property
    def taobao_sign_time(self):
        return self._taobao_sign_time

    @taobao_sign_time.setter
    def taobao_sign_time(self, value):
        self._taobao_sign_time = value
    @property
    def taobao_user_id(self):
        return self._taobao_user_id

    @taobao_user_id.setter
    def taobao_user_id(self, value):
        self._taobao_user_id = value
    @property
    def taobao_user_type(self):
        return self._taobao_user_type

    @taobao_user_type.setter
    def taobao_user_type(self, value):
        self._taobao_user_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.business_lice:
            if hasattr(self.business_lice, 'to_alipay_dict'):
                params['business_lice'] = self.business_lice.to_alipay_dict()
            else:
                params['business_lice'] = self.business_lice
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.taobao_agreement_id:
            if hasattr(self.taobao_agreement_id, 'to_alipay_dict'):
                params['taobao_agreement_id'] = self.taobao_agreement_id.to_alipay_dict()
            else:
                params['taobao_agreement_id'] = self.taobao_agreement_id
        if self.taobao_sign_time:
            if hasattr(self.taobao_sign_time, 'to_alipay_dict'):
                params['taobao_sign_time'] = self.taobao_sign_time.to_alipay_dict()
            else:
                params['taobao_sign_time'] = self.taobao_sign_time
        if self.taobao_user_id:
            if hasattr(self.taobao_user_id, 'to_alipay_dict'):
                params['taobao_user_id'] = self.taobao_user_id.to_alipay_dict()
            else:
                params['taobao_user_id'] = self.taobao_user_id
        if self.taobao_user_type:
            if hasattr(self.taobao_user_type, 'to_alipay_dict'):
                params['taobao_user_type'] = self.taobao_user_type.to_alipay_dict()
            else:
                params['taobao_user_type'] = self.taobao_user_type
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundAccountThaworfreezeModifyModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'business_lice' in d:
            o.business_lice = d['business_lice']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'taobao_agreement_id' in d:
            o.taobao_agreement_id = d['taobao_agreement_id']
        if 'taobao_sign_time' in d:
            o.taobao_sign_time = d['taobao_sign_time']
        if 'taobao_user_id' in d:
            o.taobao_user_id = d['taobao_user_id']
        if 'taobao_user_type' in d:
            o.taobao_user_type = d['taobao_user_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


