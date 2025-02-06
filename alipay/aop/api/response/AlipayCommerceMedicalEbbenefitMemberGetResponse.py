#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalEbbenefitMemberGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalEbbenefitMemberGetResponse, self).__init__()
        self._address = None
        self._binding_hdf_service = None
        self._city_code = None
        self._member_birthday = None
        self._member_cert_type = None
        self._member_gender = None
        self._member_id = None
        self._member_id_no = None
        self._member_name = None
        self._member_phone_no = None
        self._out_member_id = None
        self._rel = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def binding_hdf_service(self):
        return self._binding_hdf_service

    @binding_hdf_service.setter
    def binding_hdf_service(self, value):
        self._binding_hdf_service = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def member_birthday(self):
        return self._member_birthday

    @member_birthday.setter
    def member_birthday(self, value):
        self._member_birthday = value
    @property
    def member_cert_type(self):
        return self._member_cert_type

    @member_cert_type.setter
    def member_cert_type(self, value):
        self._member_cert_type = value
    @property
    def member_gender(self):
        return self._member_gender

    @member_gender.setter
    def member_gender(self, value):
        self._member_gender = value
    @property
    def member_id(self):
        return self._member_id

    @member_id.setter
    def member_id(self, value):
        self._member_id = value
    @property
    def member_id_no(self):
        return self._member_id_no

    @member_id_no.setter
    def member_id_no(self, value):
        self._member_id_no = value
    @property
    def member_name(self):
        return self._member_name

    @member_name.setter
    def member_name(self, value):
        self._member_name = value
    @property
    def member_phone_no(self):
        return self._member_phone_no

    @member_phone_no.setter
    def member_phone_no(self, value):
        self._member_phone_no = value
    @property
    def out_member_id(self):
        return self._out_member_id

    @out_member_id.setter
    def out_member_id(self, value):
        self._out_member_id = value
    @property
    def rel(self):
        return self._rel

    @rel.setter
    def rel(self, value):
        self._rel = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalEbbenefitMemberGetResponse, self).parse_response_content(response_content)
        if 'address' in response:
            self.address = response['address']
        if 'binding_hdf_service' in response:
            self.binding_hdf_service = response['binding_hdf_service']
        if 'city_code' in response:
            self.city_code = response['city_code']
        if 'member_birthday' in response:
            self.member_birthday = response['member_birthday']
        if 'member_cert_type' in response:
            self.member_cert_type = response['member_cert_type']
        if 'member_gender' in response:
            self.member_gender = response['member_gender']
        if 'member_id' in response:
            self.member_id = response['member_id']
        if 'member_id_no' in response:
            self.member_id_no = response['member_id_no']
        if 'member_name' in response:
            self.member_name = response['member_name']
        if 'member_phone_no' in response:
            self.member_phone_no = response['member_phone_no']
        if 'out_member_id' in response:
            self.out_member_id = response['out_member_id']
        if 'rel' in response:
            self.rel = response['rel']
