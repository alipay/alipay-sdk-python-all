#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayAipayNowpaydirectChargeQueryModel(object):

    def __init__(self):
        self._out_product_id = None

    @property
    def out_product_id(self):
        return self._out_product_id

    @out_product_id.setter
    def out_product_id(self, value):
        self._out_product_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_product_id:
            if hasattr(self.out_product_id, 'to_alipay_dict'):
                params['out_product_id'] = self.out_product_id.to_alipay_dict()
            else:
                params['out_product_id'] = self.out_product_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAipayNowpaydirectChargeQueryModel()
        if 'out_product_id' in d:
            o.out_product_id = d['out_product_id']
        return o


