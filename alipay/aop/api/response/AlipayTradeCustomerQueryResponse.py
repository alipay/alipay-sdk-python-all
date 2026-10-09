#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CorporationInfo import CorporationInfo


class AlipayTradeCustomerQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeCustomerQueryResponse, self).__init__()
        self._corporation_info = None
        self._description = None
        self._email = None
        self._merchant_request_no = None
        self._name = None
        self._phone = None
        self._type = None

    @property
    def corporation_info(self):
        return self._corporation_info

    @corporation_info.setter
    def corporation_info(self, value):
        if isinstance(value, CorporationInfo):
            self._corporation_info = value
        else:
            self._corporation_info = CorporationInfo.from_alipay_dict(value)
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def merchant_request_no(self):
        return self._merchant_request_no

    @merchant_request_no.setter
    def merchant_request_no(self, value):
        self._merchant_request_no = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeCustomerQueryResponse, self).parse_response_content(response_content)
        if 'corporation_info' in response:
            self.corporation_info = response['corporation_info']
        if 'description' in response:
            self.description = response['description']
        if 'email' in response:
            self.email = response['email']
        if 'merchant_request_no' in response:
            self.merchant_request_no = response['merchant_request_no']
        if 'name' in response:
            self.name = response['name']
        if 'phone' in response:
            self.phone = response['phone']
        if 'type' in response:
            self.type = response['type']
