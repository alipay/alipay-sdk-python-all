#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAddressQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAddressQueryResponse, self).__init__()
        self._address = None
        self._address_code = None
        self._area = None
        self._city = None
        self._coordinate = None
        self._default_user_address = None
        self._fullname = None
        self._mobile = None
        self._prov = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def address_code(self):
        return self._address_code

    @address_code.setter
    def address_code(self, value):
        self._address_code = value
    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def coordinate(self):
        return self._coordinate

    @coordinate.setter
    def coordinate(self, value):
        self._coordinate = value
    @property
    def default_user_address(self):
        return self._default_user_address

    @default_user_address.setter
    def default_user_address(self, value):
        self._default_user_address = value
    @property
    def fullname(self):
        return self._fullname

    @fullname.setter
    def fullname(self, value):
        self._fullname = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def prov(self):
        return self._prov

    @prov.setter
    def prov(self, value):
        self._prov = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAddressQueryResponse, self).parse_response_content(response_content)
        if 'address' in response:
            self.address = response['address']
        if 'address_code' in response:
            self.address_code = response['address_code']
        if 'area' in response:
            self.area = response['area']
        if 'city' in response:
            self.city = response['city']
        if 'coordinate' in response:
            self.coordinate = response['coordinate']
        if 'default_user_address' in response:
            self.default_user_address = response['default_user_address']
        if 'fullname' in response:
            self.fullname = response['fullname']
        if 'mobile' in response:
            self.mobile = response['mobile']
        if 'prov' in response:
            self.prov = response['prov']
