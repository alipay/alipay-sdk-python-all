#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ScenePayToken import ScenePayToken


class AlipayTradeScenepayTokenExchangeModel(object):

    def __init__(self):
        self._biz_scene = None
        self._product_code = None
        self._scene_pay_token = None
        self._seller_partner_id = None
        self._seller_secondary_merchant_id = None
        self._sub_biz_scene = None
        self._tiny_app_id = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def scene_pay_token(self):
        return self._scene_pay_token

    @scene_pay_token.setter
    def scene_pay_token(self, value):
        if isinstance(value, ScenePayToken):
            self._scene_pay_token = value
        else:
            self._scene_pay_token = ScenePayToken.from_alipay_dict(value)
    @property
    def seller_partner_id(self):
        return self._seller_partner_id

    @seller_partner_id.setter
    def seller_partner_id(self, value):
        self._seller_partner_id = value
    @property
    def seller_secondary_merchant_id(self):
        return self._seller_secondary_merchant_id

    @seller_secondary_merchant_id.setter
    def seller_secondary_merchant_id(self, value):
        self._seller_secondary_merchant_id = value
    @property
    def sub_biz_scene(self):
        return self._sub_biz_scene

    @sub_biz_scene.setter
    def sub_biz_scene(self, value):
        self._sub_biz_scene = value
    @property
    def tiny_app_id(self):
        return self._tiny_app_id

    @tiny_app_id.setter
    def tiny_app_id(self, value):
        self._tiny_app_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.scene_pay_token:
            if hasattr(self.scene_pay_token, 'to_alipay_dict'):
                params['scene_pay_token'] = self.scene_pay_token.to_alipay_dict()
            else:
                params['scene_pay_token'] = self.scene_pay_token
        if self.seller_partner_id:
            if hasattr(self.seller_partner_id, 'to_alipay_dict'):
                params['seller_partner_id'] = self.seller_partner_id.to_alipay_dict()
            else:
                params['seller_partner_id'] = self.seller_partner_id
        if self.seller_secondary_merchant_id:
            if hasattr(self.seller_secondary_merchant_id, 'to_alipay_dict'):
                params['seller_secondary_merchant_id'] = self.seller_secondary_merchant_id.to_alipay_dict()
            else:
                params['seller_secondary_merchant_id'] = self.seller_secondary_merchant_id
        if self.sub_biz_scene:
            if hasattr(self.sub_biz_scene, 'to_alipay_dict'):
                params['sub_biz_scene'] = self.sub_biz_scene.to_alipay_dict()
            else:
                params['sub_biz_scene'] = self.sub_biz_scene
        if self.tiny_app_id:
            if hasattr(self.tiny_app_id, 'to_alipay_dict'):
                params['tiny_app_id'] = self.tiny_app_id.to_alipay_dict()
            else:
                params['tiny_app_id'] = self.tiny_app_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeScenepayTokenExchangeModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'scene_pay_token' in d:
            o.scene_pay_token = d['scene_pay_token']
        if 'seller_partner_id' in d:
            o.seller_partner_id = d['seller_partner_id']
        if 'seller_secondary_merchant_id' in d:
            o.seller_secondary_merchant_id = d['seller_secondary_merchant_id']
        if 'sub_biz_scene' in d:
            o.sub_biz_scene = d['sub_biz_scene']
        if 'tiny_app_id' in d:
            o.tiny_app_id = d['tiny_app_id']
        return o


