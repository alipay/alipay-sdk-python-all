#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DynamicRentBillingRuleDTO import DynamicRentBillingRuleDTO
from alipay.aop.api.domain.FixedRentBillingRuleDTO import FixedRentBillingRuleDTO
from alipay.aop.api.domain.PeriodPayBillingRuleDTO import PeriodPayBillingRuleDTO


class AlipayMerchantSolcreditserviceprodProductCreateormodifyModel(object):

    def __init__(self):
        self._credit_service_type = None
        self._deposit_amount = None
        self._description = None
        self._dynamic_rent_billing_rule = None
        self._fixed_rent_billing_rule = None
        self._out_product_no = None
        self._period_pay_billing_rule = None
        self._post_payment_name = None
        self._product_cover_pic_url = None
        self._product_name = None
        self._product_no = None
        self._purchase_note = None
        self._scene_category_code = None
        self._smid = None

    @property
    def credit_service_type(self):
        return self._credit_service_type

    @credit_service_type.setter
    def credit_service_type(self, value):
        self._credit_service_type = value
    @property
    def deposit_amount(self):
        return self._deposit_amount

    @deposit_amount.setter
    def deposit_amount(self, value):
        self._deposit_amount = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def dynamic_rent_billing_rule(self):
        return self._dynamic_rent_billing_rule

    @dynamic_rent_billing_rule.setter
    def dynamic_rent_billing_rule(self, value):
        if isinstance(value, DynamicRentBillingRuleDTO):
            self._dynamic_rent_billing_rule = value
        else:
            self._dynamic_rent_billing_rule = DynamicRentBillingRuleDTO.from_alipay_dict(value)
    @property
    def fixed_rent_billing_rule(self):
        return self._fixed_rent_billing_rule

    @fixed_rent_billing_rule.setter
    def fixed_rent_billing_rule(self, value):
        if isinstance(value, FixedRentBillingRuleDTO):
            self._fixed_rent_billing_rule = value
        else:
            self._fixed_rent_billing_rule = FixedRentBillingRuleDTO.from_alipay_dict(value)
    @property
    def out_product_no(self):
        return self._out_product_no

    @out_product_no.setter
    def out_product_no(self, value):
        self._out_product_no = value
    @property
    def period_pay_billing_rule(self):
        return self._period_pay_billing_rule

    @period_pay_billing_rule.setter
    def period_pay_billing_rule(self, value):
        if isinstance(value, PeriodPayBillingRuleDTO):
            self._period_pay_billing_rule = value
        else:
            self._period_pay_billing_rule = PeriodPayBillingRuleDTO.from_alipay_dict(value)
    @property
    def post_payment_name(self):
        return self._post_payment_name

    @post_payment_name.setter
    def post_payment_name(self, value):
        self._post_payment_name = value
    @property
    def product_cover_pic_url(self):
        return self._product_cover_pic_url

    @product_cover_pic_url.setter
    def product_cover_pic_url(self, value):
        self._product_cover_pic_url = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def product_no(self):
        return self._product_no

    @product_no.setter
    def product_no(self, value):
        self._product_no = value
    @property
    def purchase_note(self):
        return self._purchase_note

    @purchase_note.setter
    def purchase_note(self, value):
        self._purchase_note = value
    @property
    def scene_category_code(self):
        return self._scene_category_code

    @scene_category_code.setter
    def scene_category_code(self, value):
        self._scene_category_code = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value


    def to_alipay_dict(self):
        params = dict()
        if self.credit_service_type:
            if hasattr(self.credit_service_type, 'to_alipay_dict'):
                params['credit_service_type'] = self.credit_service_type.to_alipay_dict()
            else:
                params['credit_service_type'] = self.credit_service_type
        if self.deposit_amount:
            if hasattr(self.deposit_amount, 'to_alipay_dict'):
                params['deposit_amount'] = self.deposit_amount.to_alipay_dict()
            else:
                params['deposit_amount'] = self.deposit_amount
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.dynamic_rent_billing_rule:
            if hasattr(self.dynamic_rent_billing_rule, 'to_alipay_dict'):
                params['dynamic_rent_billing_rule'] = self.dynamic_rent_billing_rule.to_alipay_dict()
            else:
                params['dynamic_rent_billing_rule'] = self.dynamic_rent_billing_rule
        if self.fixed_rent_billing_rule:
            if hasattr(self.fixed_rent_billing_rule, 'to_alipay_dict'):
                params['fixed_rent_billing_rule'] = self.fixed_rent_billing_rule.to_alipay_dict()
            else:
                params['fixed_rent_billing_rule'] = self.fixed_rent_billing_rule
        if self.out_product_no:
            if hasattr(self.out_product_no, 'to_alipay_dict'):
                params['out_product_no'] = self.out_product_no.to_alipay_dict()
            else:
                params['out_product_no'] = self.out_product_no
        if self.period_pay_billing_rule:
            if hasattr(self.period_pay_billing_rule, 'to_alipay_dict'):
                params['period_pay_billing_rule'] = self.period_pay_billing_rule.to_alipay_dict()
            else:
                params['period_pay_billing_rule'] = self.period_pay_billing_rule
        if self.post_payment_name:
            if hasattr(self.post_payment_name, 'to_alipay_dict'):
                params['post_payment_name'] = self.post_payment_name.to_alipay_dict()
            else:
                params['post_payment_name'] = self.post_payment_name
        if self.product_cover_pic_url:
            if hasattr(self.product_cover_pic_url, 'to_alipay_dict'):
                params['product_cover_pic_url'] = self.product_cover_pic_url.to_alipay_dict()
            else:
                params['product_cover_pic_url'] = self.product_cover_pic_url
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.product_no:
            if hasattr(self.product_no, 'to_alipay_dict'):
                params['product_no'] = self.product_no.to_alipay_dict()
            else:
                params['product_no'] = self.product_no
        if self.purchase_note:
            if hasattr(self.purchase_note, 'to_alipay_dict'):
                params['purchase_note'] = self.purchase_note.to_alipay_dict()
            else:
                params['purchase_note'] = self.purchase_note
        if self.scene_category_code:
            if hasattr(self.scene_category_code, 'to_alipay_dict'):
                params['scene_category_code'] = self.scene_category_code.to_alipay_dict()
            else:
                params['scene_category_code'] = self.scene_category_code
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantSolcreditserviceprodProductCreateormodifyModel()
        if 'credit_service_type' in d:
            o.credit_service_type = d['credit_service_type']
        if 'deposit_amount' in d:
            o.deposit_amount = d['deposit_amount']
        if 'description' in d:
            o.description = d['description']
        if 'dynamic_rent_billing_rule' in d:
            o.dynamic_rent_billing_rule = d['dynamic_rent_billing_rule']
        if 'fixed_rent_billing_rule' in d:
            o.fixed_rent_billing_rule = d['fixed_rent_billing_rule']
        if 'out_product_no' in d:
            o.out_product_no = d['out_product_no']
        if 'period_pay_billing_rule' in d:
            o.period_pay_billing_rule = d['period_pay_billing_rule']
        if 'post_payment_name' in d:
            o.post_payment_name = d['post_payment_name']
        if 'product_cover_pic_url' in d:
            o.product_cover_pic_url = d['product_cover_pic_url']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'product_no' in d:
            o.product_no = d['product_no']
        if 'purchase_note' in d:
            o.purchase_note = d['purchase_note']
        if 'scene_category_code' in d:
            o.scene_category_code = d['scene_category_code']
        if 'smid' in d:
            o.smid = d['smid']
        return o


