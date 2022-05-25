#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PrincipalPartyInfo import PrincipalPartyInfo


class AlipayFundFlexiblestaffingAuthorizeInitializeModel(object):

    def __init__(self):
        self._back_url = None
        self._biz_scene = None
        self._expire_time = None
        self._initialize_code_type = None
        self._out_biz_no = None
        self._principal_party_info = None
        self._product_code = None

    @property
    def back_url(self):
        return self._back_url

    @back_url.setter
    def back_url(self, value):
        self._back_url = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def initialize_code_type(self):
        return self._initialize_code_type

    @initialize_code_type.setter
    def initialize_code_type(self, value):
        self._initialize_code_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def principal_party_info(self):
        return self._principal_party_info

    @principal_party_info.setter
    def principal_party_info(self, value):
        if isinstance(value, PrincipalPartyInfo):
            self._principal_party_info = value
        else:
            self._principal_party_info = PrincipalPartyInfo.from_alipay_dict(value)
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.back_url:
            if hasattr(self.back_url, 'to_alipay_dict'):
                params['back_url'] = self.back_url.to_alipay_dict()
            else:
                params['back_url'] = self.back_url
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.initialize_code_type:
            if hasattr(self.initialize_code_type, 'to_alipay_dict'):
                params['initialize_code_type'] = self.initialize_code_type.to_alipay_dict()
            else:
                params['initialize_code_type'] = self.initialize_code_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.principal_party_info:
            if hasattr(self.principal_party_info, 'to_alipay_dict'):
                params['principal_party_info'] = self.principal_party_info.to_alipay_dict()
            else:
                params['principal_party_info'] = self.principal_party_info
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
        o = AlipayFundFlexiblestaffingAuthorizeInitializeModel()
        if 'back_url' in d:
            o.back_url = d['back_url']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'initialize_code_type' in d:
            o.initialize_code_type = d['initialize_code_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'principal_party_info' in d:
            o.principal_party_info = d['principal_party_info']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


