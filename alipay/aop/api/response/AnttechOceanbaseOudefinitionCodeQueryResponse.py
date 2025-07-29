#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechOceanbaseOudefinitionCodeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseOudefinitionCodeQueryResponse, self).__init__()
        self._alipay_account = None
        self._alipay_virtual_id = None
        self._base_currency_value = None
        self._from_effective_date = None
        self._ou_code = None
        self._ou_name = None
        self._payment_currency_value = None
        self._region = None
        self._to_effective_date = None
        self._unified_social_credit_code = None

    @property
    def alipay_account(self):
        return self._alipay_account

    @alipay_account.setter
    def alipay_account(self, value):
        self._alipay_account = value
    @property
    def alipay_virtual_id(self):
        return self._alipay_virtual_id

    @alipay_virtual_id.setter
    def alipay_virtual_id(self, value):
        self._alipay_virtual_id = value
    @property
    def base_currency_value(self):
        return self._base_currency_value

    @base_currency_value.setter
    def base_currency_value(self, value):
        self._base_currency_value = value
    @property
    def from_effective_date(self):
        return self._from_effective_date

    @from_effective_date.setter
    def from_effective_date(self, value):
        self._from_effective_date = value
    @property
    def ou_code(self):
        return self._ou_code

    @ou_code.setter
    def ou_code(self, value):
        self._ou_code = value
    @property
    def ou_name(self):
        return self._ou_name

    @ou_name.setter
    def ou_name(self, value):
        self._ou_name = value
    @property
    def payment_currency_value(self):
        return self._payment_currency_value

    @payment_currency_value.setter
    def payment_currency_value(self, value):
        self._payment_currency_value = value
    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, value):
        self._region = value
    @property
    def to_effective_date(self):
        return self._to_effective_date

    @to_effective_date.setter
    def to_effective_date(self, value):
        self._to_effective_date = value
    @property
    def unified_social_credit_code(self):
        return self._unified_social_credit_code

    @unified_social_credit_code.setter
    def unified_social_credit_code(self, value):
        self._unified_social_credit_code = value

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseOudefinitionCodeQueryResponse, self).parse_response_content(response_content)
        if 'alipay_account' in response:
            self.alipay_account = response['alipay_account']
        if 'alipay_virtual_id' in response:
            self.alipay_virtual_id = response['alipay_virtual_id']
        if 'base_currency_value' in response:
            self.base_currency_value = response['base_currency_value']
        if 'from_effective_date' in response:
            self.from_effective_date = response['from_effective_date']
        if 'ou_code' in response:
            self.ou_code = response['ou_code']
        if 'ou_name' in response:
            self.ou_name = response['ou_name']
        if 'payment_currency_value' in response:
            self.payment_currency_value = response['payment_currency_value']
        if 'region' in response:
            self.region = response['region']
        if 'to_effective_date' in response:
            self.to_effective_date = response['to_effective_date']
        if 'unified_social_credit_code' in response:
            self.unified_social_credit_code = response['unified_social_credit_code']
