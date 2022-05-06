#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundIdentitypayOrganizationUnsignModel(object):

    def __init__(self):
        self._biz_scene = None
        self._out_org_id = None
        self._out_org_name = None
        self._product_code = None
        self._sub_biz_scene = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def out_org_id(self):
        return self._out_org_id

    @out_org_id.setter
    def out_org_id(self, value):
        self._out_org_id = value
    @property
    def out_org_name(self):
        return self._out_org_name

    @out_org_name.setter
    def out_org_name(self, value):
        self._out_org_name = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def sub_biz_scene(self):
        return self._sub_biz_scene

    @sub_biz_scene.setter
    def sub_biz_scene(self, value):
        self._sub_biz_scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.out_org_id:
            if hasattr(self.out_org_id, 'to_alipay_dict'):
                params['out_org_id'] = self.out_org_id.to_alipay_dict()
            else:
                params['out_org_id'] = self.out_org_id
        if self.out_org_name:
            if hasattr(self.out_org_name, 'to_alipay_dict'):
                params['out_org_name'] = self.out_org_name.to_alipay_dict()
            else:
                params['out_org_name'] = self.out_org_name
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.sub_biz_scene:
            if hasattr(self.sub_biz_scene, 'to_alipay_dict'):
                params['sub_biz_scene'] = self.sub_biz_scene.to_alipay_dict()
            else:
                params['sub_biz_scene'] = self.sub_biz_scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundIdentitypayOrganizationUnsignModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'out_org_id' in d:
            o.out_org_id = d['out_org_id']
        if 'out_org_name' in d:
            o.out_org_name = d['out_org_name']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'sub_biz_scene' in d:
            o.sub_biz_scene = d['sub_biz_scene']
        return o


