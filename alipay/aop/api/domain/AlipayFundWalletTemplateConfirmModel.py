#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ConsumeExtend import ConsumeExtend
from alipay.aop.api.domain.GiftCardTemplate import GiftCardTemplate


class AlipayFundWalletTemplateConfirmModel(object):

    def __init__(self):
        self._biz_scene = None
        self._consume_extend = None
        self._gift_card_template = None
        self._out_biz_no = None
        self._product_code = None
        self._wallet_template_name = None

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
    def gift_card_template(self):
        return self._gift_card_template

    @gift_card_template.setter
    def gift_card_template(self, value):
        if isinstance(value, GiftCardTemplate):
            self._gift_card_template = value
        else:
            self._gift_card_template = GiftCardTemplate.from_alipay_dict(value)
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
    def wallet_template_name(self):
        return self._wallet_template_name

    @wallet_template_name.setter
    def wallet_template_name(self, value):
        self._wallet_template_name = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.gift_card_template:
            if hasattr(self.gift_card_template, 'to_alipay_dict'):
                params['gift_card_template'] = self.gift_card_template.to_alipay_dict()
            else:
                params['gift_card_template'] = self.gift_card_template
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
        if self.wallet_template_name:
            if hasattr(self.wallet_template_name, 'to_alipay_dict'):
                params['wallet_template_name'] = self.wallet_template_name.to_alipay_dict()
            else:
                params['wallet_template_name'] = self.wallet_template_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundWalletTemplateConfirmModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'consume_extend' in d:
            o.consume_extend = d['consume_extend']
        if 'gift_card_template' in d:
            o.gift_card_template = d['gift_card_template']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'wallet_template_name' in d:
            o.wallet_template_name = d['wallet_template_name']
        return o


