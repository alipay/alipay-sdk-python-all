#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceNfcmarketingCashbackQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceNfcmarketingCashbackQueryResponse, self).__init__()
        self._available_date = None
        self._business_time = None
        self._calculated_cashback_amount = None
        self._calculated_cashback_amount_reason = None
        self._campaign_code = None
        self._campaign_config_version = None
        self._cashback_id = None
        self._cashback_status = None
        self._cashback_time = None
        self._expect_expire_time = None
        self._ext_info = None
        self._invalid_cashback_amount = None
        self._invalid_cashback_amount_reason = None
        self._open_id = None
        self._order_business = None
        self._order_id = None
        self._order_paid_time = None
        self._partner = None
        self._product_id = None
        self._product_type = None
        self._user_id = None
        self._user_jump_time = None

    @property
    def available_date(self):
        return self._available_date

    @available_date.setter
    def available_date(self, value):
        self._available_date = value
    @property
    def business_time(self):
        return self._business_time

    @business_time.setter
    def business_time(self, value):
        self._business_time = value
    @property
    def calculated_cashback_amount(self):
        return self._calculated_cashback_amount

    @calculated_cashback_amount.setter
    def calculated_cashback_amount(self, value):
        self._calculated_cashback_amount = value
    @property
    def calculated_cashback_amount_reason(self):
        return self._calculated_cashback_amount_reason

    @calculated_cashback_amount_reason.setter
    def calculated_cashback_amount_reason(self, value):
        self._calculated_cashback_amount_reason = value
    @property
    def campaign_code(self):
        return self._campaign_code

    @campaign_code.setter
    def campaign_code(self, value):
        self._campaign_code = value
    @property
    def campaign_config_version(self):
        return self._campaign_config_version

    @campaign_config_version.setter
    def campaign_config_version(self, value):
        self._campaign_config_version = value
    @property
    def cashback_id(self):
        return self._cashback_id

    @cashback_id.setter
    def cashback_id(self, value):
        self._cashback_id = value
    @property
    def cashback_status(self):
        return self._cashback_status

    @cashback_status.setter
    def cashback_status(self, value):
        self._cashback_status = value
    @property
    def cashback_time(self):
        return self._cashback_time

    @cashback_time.setter
    def cashback_time(self, value):
        self._cashback_time = value
    @property
    def expect_expire_time(self):
        return self._expect_expire_time

    @expect_expire_time.setter
    def expect_expire_time(self, value):
        self._expect_expire_time = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def invalid_cashback_amount(self):
        return self._invalid_cashback_amount

    @invalid_cashback_amount.setter
    def invalid_cashback_amount(self, value):
        self._invalid_cashback_amount = value
    @property
    def invalid_cashback_amount_reason(self):
        return self._invalid_cashback_amount_reason

    @invalid_cashback_amount_reason.setter
    def invalid_cashback_amount_reason(self, value):
        self._invalid_cashback_amount_reason = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_business(self):
        return self._order_business

    @order_business.setter
    def order_business(self, value):
        self._order_business = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_paid_time(self):
        return self._order_paid_time

    @order_paid_time.setter
    def order_paid_time(self, value):
        self._order_paid_time = value
    @property
    def partner(self):
        return self._partner

    @partner.setter
    def partner(self, value):
        self._partner = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def product_type(self):
        return self._product_type

    @product_type.setter
    def product_type(self, value):
        self._product_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_jump_time(self):
        return self._user_jump_time

    @user_jump_time.setter
    def user_jump_time(self, value):
        self._user_jump_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceNfcmarketingCashbackQueryResponse, self).parse_response_content(response_content)
        if 'available_date' in response:
            self.available_date = response['available_date']
        if 'business_time' in response:
            self.business_time = response['business_time']
        if 'calculated_cashback_amount' in response:
            self.calculated_cashback_amount = response['calculated_cashback_amount']
        if 'calculated_cashback_amount_reason' in response:
            self.calculated_cashback_amount_reason = response['calculated_cashback_amount_reason']
        if 'campaign_code' in response:
            self.campaign_code = response['campaign_code']
        if 'campaign_config_version' in response:
            self.campaign_config_version = response['campaign_config_version']
        if 'cashback_id' in response:
            self.cashback_id = response['cashback_id']
        if 'cashback_status' in response:
            self.cashback_status = response['cashback_status']
        if 'cashback_time' in response:
            self.cashback_time = response['cashback_time']
        if 'expect_expire_time' in response:
            self.expect_expire_time = response['expect_expire_time']
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'invalid_cashback_amount' in response:
            self.invalid_cashback_amount = response['invalid_cashback_amount']
        if 'invalid_cashback_amount_reason' in response:
            self.invalid_cashback_amount_reason = response['invalid_cashback_amount_reason']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'order_business' in response:
            self.order_business = response['order_business']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'order_paid_time' in response:
            self.order_paid_time = response['order_paid_time']
        if 'partner' in response:
            self.partner = response['partner']
        if 'product_id' in response:
            self.product_id = response['product_id']
        if 'product_type' in response:
            self.product_type = response['product_type']
        if 'user_id' in response:
            self.user_id = response['user_id']
        if 'user_jump_time' in response:
            self.user_jump_time = response['user_jump_time']
