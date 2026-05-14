#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeCreditOrderPayModel(object):

    def __init__(self):
        self._biz_scene = None
        self._credit_biz_order_id = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def credit_biz_order_id(self):
        return self._credit_biz_order_id

    @credit_biz_order_id.setter
    def credit_biz_order_id(self, value):
        self._credit_biz_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.credit_biz_order_id:
            if hasattr(self.credit_biz_order_id, 'to_alipay_dict'):
                params['credit_biz_order_id'] = self.credit_biz_order_id.to_alipay_dict()
            else:
                params['credit_biz_order_id'] = self.credit_biz_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeCreditOrderPayModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'credit_biz_order_id' in d:
            o.credit_biz_order_id = d['credit_biz_order_id']
        return o


