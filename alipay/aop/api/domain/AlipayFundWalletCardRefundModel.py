#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundWalletCardRefundModel(object):

    def __init__(self):
        self._asset_id_lists = None
        self._biz_scene = None
        self._merchant_id = None
        self._out_biz_no = None
        self._product_code = None

    @property
    def asset_id_lists(self):
        return self._asset_id_lists

    @asset_id_lists.setter
    def asset_id_lists(self, value):
        if isinstance(value, list):
            self._asset_id_lists = list()
            for i in value:
                self._asset_id_lists.append(i)
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.asset_id_lists:
            if isinstance(self.asset_id_lists, list):
                for i in range(0, len(self.asset_id_lists)):
                    element = self.asset_id_lists[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.asset_id_lists[i] = element.to_alipay_dict()
            if hasattr(self.asset_id_lists, 'to_alipay_dict'):
                params['asset_id_lists'] = self.asset_id_lists.to_alipay_dict()
            else:
                params['asset_id_lists'] = self.asset_id_lists
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
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
        o = AlipayFundWalletCardRefundModel()
        if 'asset_id_lists' in d:
            o.asset_id_lists = d['asset_id_lists']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


