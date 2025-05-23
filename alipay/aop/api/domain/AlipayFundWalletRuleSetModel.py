#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.WalletUseRule import WalletUseRule


class AlipayFundWalletRuleSetModel(object):

    def __init__(self):
        self._biz_scene = None
        self._out_biz_no = None
        self._product_code = None
        self._type = None
        self._wallet_template_id = None
        self._wallet_use_rule = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
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
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def wallet_template_id(self):
        return self._wallet_template_id

    @wallet_template_id.setter
    def wallet_template_id(self, value):
        self._wallet_template_id = value
    @property
    def wallet_use_rule(self):
        return self._wallet_use_rule

    @wallet_use_rule.setter
    def wallet_use_rule(self, value):
        if isinstance(value, WalletUseRule):
            self._wallet_use_rule = value
        else:
            self._wallet_use_rule = WalletUseRule.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
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
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.wallet_template_id:
            if hasattr(self.wallet_template_id, 'to_alipay_dict'):
                params['wallet_template_id'] = self.wallet_template_id.to_alipay_dict()
            else:
                params['wallet_template_id'] = self.wallet_template_id
        if self.wallet_use_rule:
            if hasattr(self.wallet_use_rule, 'to_alipay_dict'):
                params['wallet_use_rule'] = self.wallet_use_rule.to_alipay_dict()
            else:
                params['wallet_use_rule'] = self.wallet_use_rule
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundWalletRuleSetModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'type' in d:
            o.type = d['type']
        if 'wallet_template_id' in d:
            o.wallet_template_id = d['wallet_template_id']
        if 'wallet_use_rule' in d:
            o.wallet_use_rule = d['wallet_use_rule']
        return o


