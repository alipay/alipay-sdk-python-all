#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundBatchCloseModel(object):

    def __init__(self):
        self._batch_trans_id = None
        self._biz_scene = None
        self._product_code = None

    @property
    def batch_trans_id(self):
        return self._batch_trans_id

    @batch_trans_id.setter
    def batch_trans_id(self, value):
        self._batch_trans_id = value
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
        if isinstance(value, list):
            self._product_code = list()
            for i in value:
                self._product_code.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.batch_trans_id:
            if hasattr(self.batch_trans_id, 'to_alipay_dict'):
                params['batch_trans_id'] = self.batch_trans_id.to_alipay_dict()
            else:
                params['batch_trans_id'] = self.batch_trans_id
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.product_code:
            if isinstance(self.product_code, list):
                for i in range(0, len(self.product_code)):
                    element = self.product_code[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.product_code[i] = element.to_alipay_dict()
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundBatchCloseModel()
        if 'batch_trans_id' in d:
            o.batch_trans_id = d['batch_trans_id']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


