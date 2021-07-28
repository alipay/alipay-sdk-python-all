#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPayAppTradeArrearSyncModel(object):

    def __init__(self):
        self._biz_scene = None
        self._goods_digest = None
        self._merchant_name = None
        self._trade_no = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def goods_digest(self):
        return self._goods_digest

    @goods_digest.setter
    def goods_digest(self, value):
        self._goods_digest = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.goods_digest:
            if hasattr(self.goods_digest, 'to_alipay_dict'):
                params['goods_digest'] = self.goods_digest.to_alipay_dict()
            else:
                params['goods_digest'] = self.goods_digest
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPayAppTradeArrearSyncModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'goods_digest' in d:
            o.goods_digest = d['goods_digest']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


