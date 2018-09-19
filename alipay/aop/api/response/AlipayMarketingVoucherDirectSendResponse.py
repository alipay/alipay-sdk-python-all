#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingVoucherDirectSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingVoucherDirectSendResponse, self).__init__()
        self._assets_code = None
        self._available_amount = None
        self._available_cash = None
        self._extend_info = None
        self._extend_template_info = None
        self._gmt_active = None
        self._gmt_create = None
        self._gmt_expired = None
        self._gmt_extend = None
        self._gmt_modified = None
        self._name = None
        self._product_code = None
        self._status = None
        self._template_id = None
        self._total_amount = None
        self._total_cash = None
        self._user_id = None
        self._voucher_description = None
        self._voucher_id = None

    @property
    def assets_code(self):
        return self._assets_code

    @assets_code.setter
    def assets_code(self, value):
        self._assets_code = value
    @property
    def available_amount(self):
        return self._available_amount

    @available_amount.setter
    def available_amount(self, value):
        self._available_amount = value
    @property
    def available_cash(self):
        return self._available_cash

    @available_cash.setter
    def available_cash(self, value):
        self._available_cash = value
    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value
    @property
    def extend_template_info(self):
        return self._extend_template_info

    @extend_template_info.setter
    def extend_template_info(self, value):
        self._extend_template_info = value
    @property
    def gmt_active(self):
        return self._gmt_active

    @gmt_active.setter
    def gmt_active(self, value):
        self._gmt_active = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_expired(self):
        return self._gmt_expired

    @gmt_expired.setter
    def gmt_expired(self, value):
        self._gmt_expired = value
    @property
    def gmt_extend(self):
        return self._gmt_extend

    @gmt_extend.setter
    def gmt_extend(self, value):
        self._gmt_extend = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def total_cash(self):
        return self._total_cash

    @total_cash.setter
    def total_cash(self, value):
        self._total_cash = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def voucher_description(self):
        return self._voucher_description

    @voucher_description.setter
    def voucher_description(self, value):
        self._voucher_description = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingVoucherDirectSendResponse, self).parse_response_content(response_content)
        if 'assets_code' in response:
            self.assets_code = response['assets_code']
        if 'available_amount' in response:
            self.available_amount = response['available_amount']
        if 'available_cash' in response:
            self.available_cash = response['available_cash']
        if 'extend_info' in response:
            self.extend_info = response['extend_info']
        if 'extend_template_info' in response:
            self.extend_template_info = response['extend_template_info']
        if 'gmt_active' in response:
            self.gmt_active = response['gmt_active']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'gmt_expired' in response:
            self.gmt_expired = response['gmt_expired']
        if 'gmt_extend' in response:
            self.gmt_extend = response['gmt_extend']
        if 'gmt_modified' in response:
            self.gmt_modified = response['gmt_modified']
        if 'name' in response:
            self.name = response['name']
        if 'product_code' in response:
            self.product_code = response['product_code']
        if 'status' in response:
            self.status = response['status']
        if 'template_id' in response:
            self.template_id = response['template_id']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'total_cash' in response:
            self.total_cash = response['total_cash']
        if 'user_id' in response:
            self.user_id = response['user_id']
        if 'voucher_description' in response:
            self.voucher_description = response['voucher_description']
        if 'voucher_id' in response:
            self.voucher_id = response['voucher_id']
