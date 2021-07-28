#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LogisticsAccountStatusDTO import LogisticsAccountStatusDTO


class AlipayOpenInstantdeliveryAccountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenInstantdeliveryAccountQueryResponse, self).__init__()
        self._balance = None
        self._business_license = None
        self._business_scope = None
        self._credit_code = None
        self._email = None
        self._enterprise_address = None
        self._enterprise_city = None
        self._enterprise_district = None
        self._enterprise_name = None
        self._enterprise_province = None
        self._enterprise_type = None
        self._logistics_account_status = None
        self._phone = None

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
    @property
    def business_license(self):
        return self._business_license

    @business_license.setter
    def business_license(self, value):
        self._business_license = value
    @property
    def business_scope(self):
        return self._business_scope

    @business_scope.setter
    def business_scope(self, value):
        self._business_scope = value
    @property
    def credit_code(self):
        return self._credit_code

    @credit_code.setter
    def credit_code(self, value):
        self._credit_code = value
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def enterprise_address(self):
        return self._enterprise_address

    @enterprise_address.setter
    def enterprise_address(self, value):
        self._enterprise_address = value
    @property
    def enterprise_city(self):
        return self._enterprise_city

    @enterprise_city.setter
    def enterprise_city(self, value):
        self._enterprise_city = value
    @property
    def enterprise_district(self):
        return self._enterprise_district

    @enterprise_district.setter
    def enterprise_district(self, value):
        self._enterprise_district = value
    @property
    def enterprise_name(self):
        return self._enterprise_name

    @enterprise_name.setter
    def enterprise_name(self, value):
        self._enterprise_name = value
    @property
    def enterprise_province(self):
        return self._enterprise_province

    @enterprise_province.setter
    def enterprise_province(self, value):
        self._enterprise_province = value
    @property
    def enterprise_type(self):
        return self._enterprise_type

    @enterprise_type.setter
    def enterprise_type(self, value):
        self._enterprise_type = value
    @property
    def logistics_account_status(self):
        return self._logistics_account_status

    @logistics_account_status.setter
    def logistics_account_status(self, value):
        if isinstance(value, list):
            self._logistics_account_status = list()
            for i in value:
                if isinstance(i, LogisticsAccountStatusDTO):
                    self._logistics_account_status.append(i)
                else:
                    self._logistics_account_status.append(LogisticsAccountStatusDTO.from_alipay_dict(i))
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenInstantdeliveryAccountQueryResponse, self).parse_response_content(response_content)
        if 'balance' in response:
            self.balance = response['balance']
        if 'business_license' in response:
            self.business_license = response['business_license']
        if 'business_scope' in response:
            self.business_scope = response['business_scope']
        if 'credit_code' in response:
            self.credit_code = response['credit_code']
        if 'email' in response:
            self.email = response['email']
        if 'enterprise_address' in response:
            self.enterprise_address = response['enterprise_address']
        if 'enterprise_city' in response:
            self.enterprise_city = response['enterprise_city']
        if 'enterprise_district' in response:
            self.enterprise_district = response['enterprise_district']
        if 'enterprise_name' in response:
            self.enterprise_name = response['enterprise_name']
        if 'enterprise_province' in response:
            self.enterprise_province = response['enterprise_province']
        if 'enterprise_type' in response:
            self.enterprise_type = response['enterprise_type']
        if 'logistics_account_status' in response:
            self.logistics_account_status = response['logistics_account_status']
        if 'phone' in response:
            self.phone = response['phone']
