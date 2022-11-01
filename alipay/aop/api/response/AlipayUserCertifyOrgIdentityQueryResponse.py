#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserCertifyOrgIdentityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserCertifyOrgIdentityQueryResponse, self).__init__()
        self._address = None
        self._business_scope = None
        self._cert_name = None
        self._cert_no = None
        self._cert_type = None
        self._city = None
        self._expiry_date = None
        self._legal_person_real_name = None
        self._province = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def business_scope(self):
        return self._business_scope

    @business_scope.setter
    def business_scope(self, value):
        self._business_scope = value
    @property
    def cert_name(self):
        return self._cert_name

    @cert_name.setter
    def cert_name(self, value):
        self._cert_name = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def expiry_date(self):
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, value):
        self._expiry_date = value
    @property
    def legal_person_real_name(self):
        return self._legal_person_real_name

    @legal_person_real_name.setter
    def legal_person_real_name(self, value):
        self._legal_person_real_name = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserCertifyOrgIdentityQueryResponse, self).parse_response_content(response_content)
        if 'address' in response:
            self.address = response['address']
        if 'business_scope' in response:
            self.business_scope = response['business_scope']
        if 'cert_name' in response:
            self.cert_name = response['cert_name']
        if 'cert_no' in response:
            self.cert_no = response['cert_no']
        if 'cert_type' in response:
            self.cert_type = response['cert_type']
        if 'city' in response:
            self.city = response['city']
        if 'expiry_date' in response:
            self.expiry_date = response['expiry_date']
        if 'legal_person_real_name' in response:
            self.legal_person_real_name = response['legal_person_real_name']
        if 'province' in response:
            self.province = response['province']
