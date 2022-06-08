#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundEnterprisepaySignModel(object):

    def __init__(self):
        self._account_name = None
        self._biz_scene = None
        self._identity = None
        self._identity_name = None
        self._identity_type = None
        self._out_biz_no = None
        self._out_entity_id = None
        self._out_source = None
        self._product_code = None

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def identity(self):
        return self._identity

    @identity.setter
    def identity(self, value):
        self._identity = value
    @property
    def identity_name(self):
        return self._identity_name

    @identity_name.setter
    def identity_name(self, value):
        self._identity_name = value
    @property
    def identity_type(self):
        return self._identity_type

    @identity_type.setter
    def identity_type(self, value):
        self._identity_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_entity_id(self):
        return self._out_entity_id

    @out_entity_id.setter
    def out_entity_id(self, value):
        self._out_entity_id = value
    @property
    def out_source(self):
        return self._out_source

    @out_source.setter
    def out_source(self, value):
        self._out_source = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_name:
            if hasattr(self.account_name, 'to_alipay_dict'):
                params['account_name'] = self.account_name.to_alipay_dict()
            else:
                params['account_name'] = self.account_name
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.identity:
            if hasattr(self.identity, 'to_alipay_dict'):
                params['identity'] = self.identity.to_alipay_dict()
            else:
                params['identity'] = self.identity
        if self.identity_name:
            if hasattr(self.identity_name, 'to_alipay_dict'):
                params['identity_name'] = self.identity_name.to_alipay_dict()
            else:
                params['identity_name'] = self.identity_name
        if self.identity_type:
            if hasattr(self.identity_type, 'to_alipay_dict'):
                params['identity_type'] = self.identity_type.to_alipay_dict()
            else:
                params['identity_type'] = self.identity_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_entity_id:
            if hasattr(self.out_entity_id, 'to_alipay_dict'):
                params['out_entity_id'] = self.out_entity_id.to_alipay_dict()
            else:
                params['out_entity_id'] = self.out_entity_id
        if self.out_source:
            if hasattr(self.out_source, 'to_alipay_dict'):
                params['out_source'] = self.out_source.to_alipay_dict()
            else:
                params['out_source'] = self.out_source
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
        o = AlipayFundEnterprisepaySignModel()
        if 'account_name' in d:
            o.account_name = d['account_name']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'identity' in d:
            o.identity = d['identity']
        if 'identity_name' in d:
            o.identity_name = d['identity_name']
        if 'identity_type' in d:
            o.identity_type = d['identity_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_entity_id' in d:
            o.out_entity_id = d['out_entity_id']
        if 'out_source' in d:
            o.out_source = d['out_source']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


