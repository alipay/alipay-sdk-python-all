#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasTravelGoodsSyncresultQueryModel(object):

    def __init__(self):
        self._out_goods_id = None
        self._out_shop_id = None

    @property
    def out_goods_id(self):
        return self._out_goods_id

    @out_goods_id.setter
    def out_goods_id(self, value):
        self._out_goods_id = value
    @property
    def out_shop_id(self):
        return self._out_shop_id

    @out_shop_id.setter
    def out_shop_id(self, value):
        self._out_shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_goods_id:
            if hasattr(self.out_goods_id, 'to_alipay_dict'):
                params['out_goods_id'] = self.out_goods_id.to_alipay_dict()
            else:
                params['out_goods_id'] = self.out_goods_id
        if self.out_shop_id:
            if hasattr(self.out_shop_id, 'to_alipay_dict'):
                params['out_shop_id'] = self.out_shop_id.to_alipay_dict()
            else:
                params['out_shop_id'] = self.out_shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasTravelGoodsSyncresultQueryModel()
        if 'out_goods_id' in d:
            o.out_goods_id = d['out_goods_id']
        if 'out_shop_id' in d:
            o.out_shop_id = d['out_shop_id']
        return o


