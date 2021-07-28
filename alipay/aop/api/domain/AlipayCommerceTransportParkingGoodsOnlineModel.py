#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportParkingGoodsOnlineModel(object):

    def __init__(self):
        self._goods_id = None
        self._op_type = None
        self._out_id = None
        self._parking_id = None

    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value
    @property
    def op_type(self):
        return self._op_type

    @op_type.setter
    def op_type(self, value):
        self._op_type = value
    @property
    def out_id(self):
        return self._out_id

    @out_id.setter
    def out_id(self, value):
        self._out_id = value
    @property
    def parking_id(self):
        return self._parking_id

    @parking_id.setter
    def parking_id(self, value):
        self._parking_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.goods_id:
            if hasattr(self.goods_id, 'to_alipay_dict'):
                params['goods_id'] = self.goods_id.to_alipay_dict()
            else:
                params['goods_id'] = self.goods_id
        if self.op_type:
            if hasattr(self.op_type, 'to_alipay_dict'):
                params['op_type'] = self.op_type.to_alipay_dict()
            else:
                params['op_type'] = self.op_type
        if self.out_id:
            if hasattr(self.out_id, 'to_alipay_dict'):
                params['out_id'] = self.out_id.to_alipay_dict()
            else:
                params['out_id'] = self.out_id
        if self.parking_id:
            if hasattr(self.parking_id, 'to_alipay_dict'):
                params['parking_id'] = self.parking_id.to_alipay_dict()
            else:
                params['parking_id'] = self.parking_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportParkingGoodsOnlineModel()
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'op_type' in d:
            o.op_type = d['op_type']
        if 'out_id' in d:
            o.out_id = d['out_id']
        if 'parking_id' in d:
            o.parking_id = d['parking_id']
        return o


