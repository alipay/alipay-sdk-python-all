#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceHousingApartmentRentalQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceHousingApartmentRentalQueryResponse, self).__init__()
        self._apartment_house_id = None
        self._apartment_id = None
        self._check_in_time = None
        self._deposit = None
        self._doorplate_number = None
        self._external_id = None
        self._has_private_bathroom = None
        self._internal_area = None
        self._name = None
        self._orientation = None
        self._payment_method = None
        self._rent = None
        self._rent_unit = None
        self._status = None
        self._verification_code = None

    @property
    def apartment_house_id(self):
        return self._apartment_house_id

    @apartment_house_id.setter
    def apartment_house_id(self, value):
        self._apartment_house_id = value
    @property
    def apartment_id(self):
        return self._apartment_id

    @apartment_id.setter
    def apartment_id(self, value):
        self._apartment_id = value
    @property
    def check_in_time(self):
        return self._check_in_time

    @check_in_time.setter
    def check_in_time(self, value):
        self._check_in_time = value
    @property
    def deposit(self):
        return self._deposit

    @deposit.setter
    def deposit(self, value):
        self._deposit = value
    @property
    def doorplate_number(self):
        return self._doorplate_number

    @doorplate_number.setter
    def doorplate_number(self, value):
        self._doorplate_number = value
    @property
    def external_id(self):
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        self._external_id = value
    @property
    def has_private_bathroom(self):
        return self._has_private_bathroom

    @has_private_bathroom.setter
    def has_private_bathroom(self, value):
        self._has_private_bathroom = value
    @property
    def internal_area(self):
        return self._internal_area

    @internal_area.setter
    def internal_area(self, value):
        self._internal_area = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def orientation(self):
        return self._orientation

    @orientation.setter
    def orientation(self, value):
        self._orientation = value
    @property
    def payment_method(self):
        return self._payment_method

    @payment_method.setter
    def payment_method(self, value):
        self._payment_method = value
    @property
    def rent(self):
        return self._rent

    @rent.setter
    def rent(self, value):
        self._rent = value
    @property
    def rent_unit(self):
        return self._rent_unit

    @rent_unit.setter
    def rent_unit(self, value):
        self._rent_unit = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def verification_code(self):
        return self._verification_code

    @verification_code.setter
    def verification_code(self, value):
        self._verification_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceHousingApartmentRentalQueryResponse, self).parse_response_content(response_content)
        if 'apartment_house_id' in response:
            self.apartment_house_id = response['apartment_house_id']
        if 'apartment_id' in response:
            self.apartment_id = response['apartment_id']
        if 'check_in_time' in response:
            self.check_in_time = response['check_in_time']
        if 'deposit' in response:
            self.deposit = response['deposit']
        if 'doorplate_number' in response:
            self.doorplate_number = response['doorplate_number']
        if 'external_id' in response:
            self.external_id = response['external_id']
        if 'has_private_bathroom' in response:
            self.has_private_bathroom = response['has_private_bathroom']
        if 'internal_area' in response:
            self.internal_area = response['internal_area']
        if 'name' in response:
            self.name = response['name']
        if 'orientation' in response:
            self.orientation = response['orientation']
        if 'payment_method' in response:
            self.payment_method = response['payment_method']
        if 'rent' in response:
            self.rent = response['rent']
        if 'rent_unit' in response:
            self.rent_unit = response['rent_unit']
        if 'status' in response:
            self.status = response['status']
        if 'verification_code' in response:
            self.verification_code = response['verification_code']
