#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcApprovalConfigQueryModel(object):

    def __init__(self):
        self._enterprise_id = None
        self._payment_type = None
        self._scene = None
        self._scene_sub_category = None

    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def payment_type(self):
        return self._payment_type

    @payment_type.setter
    def payment_type(self, value):
        self._payment_type = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def scene_sub_category(self):
        return self._scene_sub_category

    @scene_sub_category.setter
    def scene_sub_category(self, value):
        self._scene_sub_category = value


    def to_alipay_dict(self):
        params = dict()
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.payment_type:
            if hasattr(self.payment_type, 'to_alipay_dict'):
                params['payment_type'] = self.payment_type.to_alipay_dict()
            else:
                params['payment_type'] = self.payment_type
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.scene_sub_category:
            if hasattr(self.scene_sub_category, 'to_alipay_dict'):
                params['scene_sub_category'] = self.scene_sub_category.to_alipay_dict()
            else:
                params['scene_sub_category'] = self.scene_sub_category
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcApprovalConfigQueryModel()
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'payment_type' in d:
            o.payment_type = d['payment_type']
        if 'scene' in d:
            o.scene = d['scene']
        if 'scene_sub_category' in d:
            o.scene_sub_category = d['scene_sub_category']
        return o


