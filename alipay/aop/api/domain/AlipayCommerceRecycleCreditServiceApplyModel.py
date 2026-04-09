#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRecycleCreditServiceApplyModel(object):

    def __init__(self):
        self._binding_alipay_logon_id = None
        self._rules = None
        self._scene = None
        self._service_category = None
        self._submerchant = None

    @property
    def binding_alipay_logon_id(self):
        return self._binding_alipay_logon_id

    @binding_alipay_logon_id.setter
    def binding_alipay_logon_id(self, value):
        self._binding_alipay_logon_id = value
    @property
    def rules(self):
        return self._rules

    @rules.setter
    def rules(self, value):
        self._rules = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def service_category(self):
        return self._service_category

    @service_category.setter
    def service_category(self, value):
        self._service_category = value
    @property
    def submerchant(self):
        return self._submerchant

    @submerchant.setter
    def submerchant(self, value):
        self._submerchant = value


    def to_alipay_dict(self):
        params = dict()
        if self.binding_alipay_logon_id:
            if hasattr(self.binding_alipay_logon_id, 'to_alipay_dict'):
                params['binding_alipay_logon_id'] = self.binding_alipay_logon_id.to_alipay_dict()
            else:
                params['binding_alipay_logon_id'] = self.binding_alipay_logon_id
        if self.rules:
            if hasattr(self.rules, 'to_alipay_dict'):
                params['rules'] = self.rules.to_alipay_dict()
            else:
                params['rules'] = self.rules
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.service_category:
            if hasattr(self.service_category, 'to_alipay_dict'):
                params['service_category'] = self.service_category.to_alipay_dict()
            else:
                params['service_category'] = self.service_category
        if self.submerchant:
            if hasattr(self.submerchant, 'to_alipay_dict'):
                params['submerchant'] = self.submerchant.to_alipay_dict()
            else:
                params['submerchant'] = self.submerchant
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRecycleCreditServiceApplyModel()
        if 'binding_alipay_logon_id' in d:
            o.binding_alipay_logon_id = d['binding_alipay_logon_id']
        if 'rules' in d:
            o.rules = d['rules']
        if 'scene' in d:
            o.scene = d['scene']
        if 'service_category' in d:
            o.service_category = d['service_category']
        if 'submerchant' in d:
            o.submerchant = d['submerchant']
        return o


