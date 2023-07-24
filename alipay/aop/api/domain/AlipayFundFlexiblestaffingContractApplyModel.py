#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SignPrincipalDTO import SignPrincipalDTO


class AlipayFundFlexiblestaffingContractApplyModel(object):

    def __init__(self):
        self._apply_link_type = None
        self._biz_scene = None
        self._channel = None
        self._contract_template_fields = None
        self._expire_time = None
        self._out_biz_no = None
        self._product_code = None
        self._sign_principal = None
        self._solution_code = None

    @property
    def apply_link_type(self):
        return self._apply_link_type

    @apply_link_type.setter
    def apply_link_type(self, value):
        self._apply_link_type = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def contract_template_fields(self):
        return self._contract_template_fields

    @contract_template_fields.setter
    def contract_template_fields(self, value):
        self._contract_template_fields = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def sign_principal(self):
        return self._sign_principal

    @sign_principal.setter
    def sign_principal(self, value):
        if isinstance(value, SignPrincipalDTO):
            self._sign_principal = value
        else:
            self._sign_principal = SignPrincipalDTO.from_alipay_dict(value)
    @property
    def solution_code(self):
        return self._solution_code

    @solution_code.setter
    def solution_code(self, value):
        self._solution_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_link_type:
            if hasattr(self.apply_link_type, 'to_alipay_dict'):
                params['apply_link_type'] = self.apply_link_type.to_alipay_dict()
            else:
                params['apply_link_type'] = self.apply_link_type
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.contract_template_fields:
            if hasattr(self.contract_template_fields, 'to_alipay_dict'):
                params['contract_template_fields'] = self.contract_template_fields.to_alipay_dict()
            else:
                params['contract_template_fields'] = self.contract_template_fields
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.sign_principal:
            if hasattr(self.sign_principal, 'to_alipay_dict'):
                params['sign_principal'] = self.sign_principal.to_alipay_dict()
            else:
                params['sign_principal'] = self.sign_principal
        if self.solution_code:
            if hasattr(self.solution_code, 'to_alipay_dict'):
                params['solution_code'] = self.solution_code.to_alipay_dict()
            else:
                params['solution_code'] = self.solution_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundFlexiblestaffingContractApplyModel()
        if 'apply_link_type' in d:
            o.apply_link_type = d['apply_link_type']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'channel' in d:
            o.channel = d['channel']
        if 'contract_template_fields' in d:
            o.contract_template_fields = d['contract_template_fields']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'sign_principal' in d:
            o.sign_principal = d['sign_principal']
        if 'solution_code' in d:
            o.solution_code = d['solution_code']
        return o


