#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UniOpenReqItemDetailInfos(object):

    def __init__(self):
        self._default_settle_target = None
        self._default_settle_type = None
        self._merchant_type = None
        self._need_withdraw_platform_fee = None
        self._sub_merchant_order_id = None
        self._wallet_biz_product = None
        self._wallet_biz_scene = None
        self._wallet_template_id = None

    @property
    def default_settle_target(self):
        return self._default_settle_target

    @default_settle_target.setter
    def default_settle_target(self, value):
        self._default_settle_target = value
    @property
    def default_settle_type(self):
        return self._default_settle_type

    @default_settle_type.setter
    def default_settle_type(self, value):
        self._default_settle_type = value
    @property
    def merchant_type(self):
        return self._merchant_type

    @merchant_type.setter
    def merchant_type(self, value):
        self._merchant_type = value
    @property
    def need_withdraw_platform_fee(self):
        return self._need_withdraw_platform_fee

    @need_withdraw_platform_fee.setter
    def need_withdraw_platform_fee(self, value):
        self._need_withdraw_platform_fee = value
    @property
    def sub_merchant_order_id(self):
        return self._sub_merchant_order_id

    @sub_merchant_order_id.setter
    def sub_merchant_order_id(self, value):
        self._sub_merchant_order_id = value
    @property
    def wallet_biz_product(self):
        return self._wallet_biz_product

    @wallet_biz_product.setter
    def wallet_biz_product(self, value):
        self._wallet_biz_product = value
    @property
    def wallet_biz_scene(self):
        return self._wallet_biz_scene

    @wallet_biz_scene.setter
    def wallet_biz_scene(self, value):
        self._wallet_biz_scene = value
    @property
    def wallet_template_id(self):
        return self._wallet_template_id

    @wallet_template_id.setter
    def wallet_template_id(self, value):
        self._wallet_template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.default_settle_target:
            if hasattr(self.default_settle_target, 'to_alipay_dict'):
                params['default_settle_target'] = self.default_settle_target.to_alipay_dict()
            else:
                params['default_settle_target'] = self.default_settle_target
        if self.default_settle_type:
            if hasattr(self.default_settle_type, 'to_alipay_dict'):
                params['default_settle_type'] = self.default_settle_type.to_alipay_dict()
            else:
                params['default_settle_type'] = self.default_settle_type
        if self.merchant_type:
            if hasattr(self.merchant_type, 'to_alipay_dict'):
                params['merchant_type'] = self.merchant_type.to_alipay_dict()
            else:
                params['merchant_type'] = self.merchant_type
        if self.need_withdraw_platform_fee:
            if hasattr(self.need_withdraw_platform_fee, 'to_alipay_dict'):
                params['need_withdraw_platform_fee'] = self.need_withdraw_platform_fee.to_alipay_dict()
            else:
                params['need_withdraw_platform_fee'] = self.need_withdraw_platform_fee
        if self.sub_merchant_order_id:
            if hasattr(self.sub_merchant_order_id, 'to_alipay_dict'):
                params['sub_merchant_order_id'] = self.sub_merchant_order_id.to_alipay_dict()
            else:
                params['sub_merchant_order_id'] = self.sub_merchant_order_id
        if self.wallet_biz_product:
            if hasattr(self.wallet_biz_product, 'to_alipay_dict'):
                params['wallet_biz_product'] = self.wallet_biz_product.to_alipay_dict()
            else:
                params['wallet_biz_product'] = self.wallet_biz_product
        if self.wallet_biz_scene:
            if hasattr(self.wallet_biz_scene, 'to_alipay_dict'):
                params['wallet_biz_scene'] = self.wallet_biz_scene.to_alipay_dict()
            else:
                params['wallet_biz_scene'] = self.wallet_biz_scene
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
        o = UniOpenReqItemDetailInfos()
        if 'default_settle_target' in d:
            o.default_settle_target = d['default_settle_target']
        if 'default_settle_type' in d:
            o.default_settle_type = d['default_settle_type']
        if 'merchant_type' in d:
            o.merchant_type = d['merchant_type']
        if 'need_withdraw_platform_fee' in d:
            o.need_withdraw_platform_fee = d['need_withdraw_platform_fee']
        if 'sub_merchant_order_id' in d:
            o.sub_merchant_order_id = d['sub_merchant_order_id']
        if 'wallet_biz_product' in d:
            o.wallet_biz_product = d['wallet_biz_product']
        if 'wallet_biz_scene' in d:
            o.wallet_biz_scene = d['wallet_biz_scene']
        if 'wallet_template_id' in d:
            o.wallet_template_id = d['wallet_template_id']
        return o


