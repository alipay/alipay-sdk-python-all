#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DynamicRentBillingRuleDTO import DynamicRentBillingRuleDTO
from alipay.aop.api.domain.FixedRentBillingRuleDTO import FixedRentBillingRuleDTO
from alipay.aop.api.domain.PeriodPayBillingRuleDTO import PeriodPayBillingRuleDTO


class AlipayMerchantSolcreditserviceprodOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantSolcreditserviceprodOrderQueryResponse, self).__init__()
        self._billing_end_time = None
        self._billing_start_time = None
        self._credit_service_type = None
        self._default_amount = None
        self._deposit_amount = None
        self._dynamic_rent_billing_rule = None
        self._fixed_rent_billing_rule = None
        self._merchant_app_id = None
        self._open_id = None
        self._order_end_time = None
        self._order_no = None
        self._order_status = None
        self._out_order_no = None
        self._period_pay_billing_rule = None
        self._product_no = None
        self._smid = None
        self._u_open_id = None
        self._user_id = None
        self._zm_sign_time = None

    @property
    def billing_end_time(self):
        return self._billing_end_time

    @billing_end_time.setter
    def billing_end_time(self, value):
        self._billing_end_time = value
    @property
    def billing_start_time(self):
        return self._billing_start_time

    @billing_start_time.setter
    def billing_start_time(self, value):
        self._billing_start_time = value
    @property
    def credit_service_type(self):
        return self._credit_service_type

    @credit_service_type.setter
    def credit_service_type(self, value):
        self._credit_service_type = value
    @property
    def default_amount(self):
        return self._default_amount

    @default_amount.setter
    def default_amount(self, value):
        self._default_amount = value
    @property
    def deposit_amount(self):
        return self._deposit_amount

    @deposit_amount.setter
    def deposit_amount(self, value):
        self._deposit_amount = value
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
    def merchant_app_id(self):
        return self._merchant_app_id

    @merchant_app_id.setter
    def merchant_app_id(self, value):
        self._merchant_app_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_end_time(self):
        return self._order_end_time

    @order_end_time.setter
    def order_end_time(self, value):
        self._order_end_time = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
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
    def product_no(self):
        return self._product_no

    @product_no.setter
    def product_no(self, value):
        self._product_no = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value
    @property
    def u_open_id(self):
        return self._u_open_id

    @u_open_id.setter
    def u_open_id(self, value):
        self._u_open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def zm_sign_time(self):
        return self._zm_sign_time

    @zm_sign_time.setter
    def zm_sign_time(self, value):
        self._zm_sign_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantSolcreditserviceprodOrderQueryResponse, self).parse_response_content(response_content)
        if 'billing_end_time' in response:
            self.billing_end_time = response['billing_end_time']
        if 'billing_start_time' in response:
            self.billing_start_time = response['billing_start_time']
        if 'credit_service_type' in response:
            self.credit_service_type = response['credit_service_type']
        if 'default_amount' in response:
            self.default_amount = response['default_amount']
        if 'deposit_amount' in response:
            self.deposit_amount = response['deposit_amount']
        if 'dynamic_rent_billing_rule' in response:
            self.dynamic_rent_billing_rule = response['dynamic_rent_billing_rule']
        if 'fixed_rent_billing_rule' in response:
            self.fixed_rent_billing_rule = response['fixed_rent_billing_rule']
        if 'merchant_app_id' in response:
            self.merchant_app_id = response['merchant_app_id']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'order_end_time' in response:
            self.order_end_time = response['order_end_time']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'period_pay_billing_rule' in response:
            self.period_pay_billing_rule = response['period_pay_billing_rule']
        if 'product_no' in response:
            self.product_no = response['product_no']
        if 'smid' in response:
            self.smid = response['smid']
        if 'u_open_id' in response:
            self.u_open_id = response['u_open_id']
        if 'user_id' in response:
            self.user_id = response['user_id']
        if 'zm_sign_time' in response:
            self.zm_sign_time = response['zm_sign_time']
