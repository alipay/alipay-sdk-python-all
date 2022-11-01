#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CardAssetInfo import CardAssetInfo


class AlipayFundWalletCardCreateModel(object):

    def __init__(self):
        self._biz_scene = None
        self._card_asset_info = None
        self._card_template_id = None
        self._out_biz_no = None
        self._principal_id = None
        self._principal_type = None
        self._product_code = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def card_asset_info(self):
        return self._card_asset_info

    @card_asset_info.setter
    def card_asset_info(self, value):
        if isinstance(value, CardAssetInfo):
            self._card_asset_info = value
        else:
            self._card_asset_info = CardAssetInfo.from_alipay_dict(value)
    @property
    def card_template_id(self):
        return self._card_template_id

    @card_template_id.setter
    def card_template_id(self, value):
        self._card_template_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value
    @property
    def principal_type(self):
        return self._principal_type

    @principal_type.setter
    def principal_type(self, value):
        self._principal_type = value
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
        if self.card_asset_info:
            if hasattr(self.card_asset_info, 'to_alipay_dict'):
                params['card_asset_info'] = self.card_asset_info.to_alipay_dict()
            else:
                params['card_asset_info'] = self.card_asset_info
        if self.card_template_id:
            if hasattr(self.card_template_id, 'to_alipay_dict'):
                params['card_template_id'] = self.card_template_id.to_alipay_dict()
            else:
                params['card_template_id'] = self.card_template_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.principal_id:
            if hasattr(self.principal_id, 'to_alipay_dict'):
                params['principal_id'] = self.principal_id.to_alipay_dict()
            else:
                params['principal_id'] = self.principal_id
        if self.principal_type:
            if hasattr(self.principal_type, 'to_alipay_dict'):
                params['principal_type'] = self.principal_type.to_alipay_dict()
            else:
                params['principal_type'] = self.principal_type
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
        o = AlipayFundWalletCardCreateModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'card_asset_info' in d:
            o.card_asset_info = d['card_asset_info']
        if 'card_template_id' in d:
            o.card_template_id = d['card_template_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'principal_id' in d:
            o.principal_id = d['principal_id']
        if 'principal_type' in d:
            o.principal_type = d['principal_type']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


