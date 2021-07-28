#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceKidsRelationQueryModel(object):

    def __init__(self):
        self._parent_uid = None
        self._product_code = None
        self._scene_code = None

    @property
    def parent_uid(self):
        return self._parent_uid

    @parent_uid.setter
    def parent_uid(self, value):
        self._parent_uid = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.parent_uid:
            if hasattr(self.parent_uid, 'to_alipay_dict'):
                params['parent_uid'] = self.parent_uid.to_alipay_dict()
            else:
                params['parent_uid'] = self.parent_uid
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceKidsRelationQueryModel()
        if 'parent_uid' in d:
            o.parent_uid = d['parent_uid']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


