#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ConsumeExtend import ConsumeExtend
from alipay.aop.api.domain.WalletUseRule import WalletUseRule


class AlipayFundWalletTemplateCreateModel(object):

    def __init__(self):
        self._biz_identity = None
        self._biz_scene = None
        self._consume_extend = None
        self._has_large_details_scene = None
        self._out_biz_no = None
        self._product_code = None
        self._support_wallet_use_rule_define = None
        self._wallet_template_name = None
        self._wallet_use_rule = None

    @property
    def biz_identity(self):
        return self._biz_identity

    @biz_identity.setter
    def biz_identity(self, value):
        self._biz_identity = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def consume_extend(self):
        return self._consume_extend

    @consume_extend.setter
    def consume_extend(self, value):
        if isinstance(value, ConsumeExtend):
            self._consume_extend = value
        else:
            self._consume_extend = ConsumeExtend.from_alipay_dict(value)
    @property
    def has_large_details_scene(self):
        return self._has_large_details_scene

    @has_large_details_scene.setter
    def has_large_details_scene(self, value):
        self._has_large_details_scene = value
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
    def support_wallet_use_rule_define(self):
        return self._support_wallet_use_rule_define

    @support_wallet_use_rule_define.setter
    def support_wallet_use_rule_define(self, value):
        self._support_wallet_use_rule_define = value
    @property
    def wallet_template_name(self):
        return self._wallet_template_name

    @wallet_template_name.setter
    def wallet_template_name(self, value):
        self._wallet_template_name = value
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
        if self.biz_identity:
            if hasattr(self.biz_identity, 'to_alipay_dict'):
                params['biz_identity'] = self.biz_identity.to_alipay_dict()
            else:
                params['biz_identity'] = self.biz_identity
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.consume_extend:
            if hasattr(self.consume_extend, 'to_alipay_dict'):
                params['consume_extend'] = self.consume_extend.to_alipay_dict()
            else:
                params['consume_extend'] = self.consume_extend
        if self.has_large_details_scene:
            if hasattr(self.has_large_details_scene, 'to_alipay_dict'):
                params['has_large_details_scene'] = self.has_large_details_scene.to_alipay_dict()
            else:
                params['has_large_details_scene'] = self.has_large_details_scene
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
        if self.support_wallet_use_rule_define:
            if hasattr(self.support_wallet_use_rule_define, 'to_alipay_dict'):
                params['support_wallet_use_rule_define'] = self.support_wallet_use_rule_define.to_alipay_dict()
            else:
                params['support_wallet_use_rule_define'] = self.support_wallet_use_rule_define
        if self.wallet_template_name:
            if hasattr(self.wallet_template_name, 'to_alipay_dict'):
                params['wallet_template_name'] = self.wallet_template_name.to_alipay_dict()
            else:
                params['wallet_template_name'] = self.wallet_template_name
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
        o = AlipayFundWalletTemplateCreateModel()
        if 'biz_identity' in d:
            o.biz_identity = d['biz_identity']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'consume_extend' in d:
            o.consume_extend = d['consume_extend']
        if 'has_large_details_scene' in d:
            o.has_large_details_scene = d['has_large_details_scene']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'support_wallet_use_rule_define' in d:
            o.support_wallet_use_rule_define = d['support_wallet_use_rule_define']
        if 'wallet_template_name' in d:
            o.wallet_template_name = d['wallet_template_name']
        if 'wallet_use_rule' in d:
            o.wallet_use_rule = d['wallet_use_rule']
        return o


