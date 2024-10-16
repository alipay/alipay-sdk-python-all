#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DynamicRentBillingRuleDTO import DynamicRentBillingRuleDTO
from alipay.aop.api.domain.FixedRentBillingRuleDTO import FixedRentBillingRuleDTO
from alipay.aop.api.domain.PeriodPayBillingRuleDTO import PeriodPayBillingRuleDTO


class AlipayMerchantSolcreditserviceprodProductQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantSolcreditserviceprodProductQueryResponse, self).__init__()
        self._credit_service_type = None
        self._deposit_amount = None
        self._description = None
        self._dynamic_rent_billing_rule = None
        self._fixed_rent_billing_rule = None
        self._gmt_create = None
        self._out_product_no = None
        self._period_pay_billing_rule = None
        self._post_payment_name = None
        self._product_cover_pic_url = None
        self._product_name = None
        self._product_no = None
        self._product_status = None
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
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
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
    def product_status(self):
        return self._product_status

    @product_status.setter
    def product_status(self, value):
        self._product_status = value
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

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantSolcreditserviceprodProductQueryResponse, self).parse_response_content(response_content)
        if 'credit_service_type' in response:
            self.credit_service_type = response['credit_service_type']
        if 'deposit_amount' in response:
            self.deposit_amount = response['deposit_amount']
        if 'description' in response:
            self.description = response['description']
        if 'dynamic_rent_billing_rule' in response:
            self.dynamic_rent_billing_rule = response['dynamic_rent_billing_rule']
        if 'fixed_rent_billing_rule' in response:
            self.fixed_rent_billing_rule = response['fixed_rent_billing_rule']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'out_product_no' in response:
            self.out_product_no = response['out_product_no']
        if 'period_pay_billing_rule' in response:
            self.period_pay_billing_rule = response['period_pay_billing_rule']
        if 'post_payment_name' in response:
            self.post_payment_name = response['post_payment_name']
        if 'product_cover_pic_url' in response:
            self.product_cover_pic_url = response['product_cover_pic_url']
        if 'product_name' in response:
            self.product_name = response['product_name']
        if 'product_no' in response:
            self.product_no = response['product_no']
        if 'product_status' in response:
            self.product_status = response['product_status']
        if 'purchase_note' in response:
            self.purchase_note = response['purchase_note']
        if 'scene_category_code' in response:
            self.scene_category_code = response['scene_category_code']
        if 'smid' in response:
            self.smid = response['smid']
