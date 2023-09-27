#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantInfoShareResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantInfoShareResponse, self).__init__()
        self._address = None
        self._area = None
        self._business_scope = None
        self._cert_no = None
        self._cert_pic_exist = None
        self._cert_type = None
        self._city = None
        self._expire_date = None
        self._is_certified = None
        self._legal_person_real_name = None
        self._name = None
        self._partner_id = None
        self._partner_type = None
        self._province = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value
    @property
    def business_scope(self):
        return self._business_scope

    @business_scope.setter
    def business_scope(self, value):
        self._business_scope = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_pic_exist(self):
        return self._cert_pic_exist

    @cert_pic_exist.setter
    def cert_pic_exist(self, value):
        self._cert_pic_exist = value
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
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value
    @property
    def is_certified(self):
        return self._is_certified

    @is_certified.setter
    def is_certified(self, value):
        self._is_certified = value
    @property
    def legal_person_real_name(self):
        return self._legal_person_real_name

    @legal_person_real_name.setter
    def legal_person_real_name(self, value):
        self._legal_person_real_name = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def partner_type(self):
        return self._partner_type

    @partner_type.setter
    def partner_type(self, value):
        self._partner_type = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantInfoShareResponse, self).parse_response_content(response_content)
        if 'address' in response:
            self.address = response['address']
        if 'area' in response:
            self.area = response['area']
        if 'business_scope' in response:
            self.business_scope = response['business_scope']
        if 'cert_no' in response:
            self.cert_no = response['cert_no']
        if 'cert_pic_exist' in response:
            self.cert_pic_exist = response['cert_pic_exist']
        if 'cert_type' in response:
            self.cert_type = response['cert_type']
        if 'city' in response:
            self.city = response['city']
        if 'expire_date' in response:
            self.expire_date = response['expire_date']
        if 'is_certified' in response:
            self.is_certified = response['is_certified']
        if 'legal_person_real_name' in response:
            self.legal_person_real_name = response['legal_person_real_name']
        if 'name' in response:
            self.name = response['name']
        if 'partner_id' in response:
            self.partner_id = response['partner_id']
        if 'partner_type' in response:
            self.partner_type = response['partner_type']
        if 'province' in response:
            self.province = response['province']
