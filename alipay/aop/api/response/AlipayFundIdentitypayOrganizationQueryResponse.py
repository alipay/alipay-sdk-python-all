#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundIdentitypayOrganizationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundIdentitypayOrganizationQueryResponse, self).__init__()
        self._business_params = None
        self._latitude = None
        self._longitude = None
        self._member_count = None
        self._out_org_address = None
        self._out_org_area = None
        self._out_org_city = None
        self._out_org_name = None
        self._out_org_province = None
        self._out_org_street = None
        self._status = None

    @property
    def business_params(self):
        return self._business_params

    @business_params.setter
    def business_params(self, value):
        self._business_params = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def member_count(self):
        return self._member_count

    @member_count.setter
    def member_count(self, value):
        self._member_count = value
    @property
    def out_org_address(self):
        return self._out_org_address

    @out_org_address.setter
    def out_org_address(self, value):
        self._out_org_address = value
    @property
    def out_org_area(self):
        return self._out_org_area

    @out_org_area.setter
    def out_org_area(self, value):
        self._out_org_area = value
    @property
    def out_org_city(self):
        return self._out_org_city

    @out_org_city.setter
    def out_org_city(self, value):
        self._out_org_city = value
    @property
    def out_org_name(self):
        return self._out_org_name

    @out_org_name.setter
    def out_org_name(self, value):
        self._out_org_name = value
    @property
    def out_org_province(self):
        return self._out_org_province

    @out_org_province.setter
    def out_org_province(self, value):
        self._out_org_province = value
    @property
    def out_org_street(self):
        return self._out_org_street

    @out_org_street.setter
    def out_org_street(self, value):
        self._out_org_street = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundIdentitypayOrganizationQueryResponse, self).parse_response_content(response_content)
        if 'business_params' in response:
            self.business_params = response['business_params']
        if 'latitude' in response:
            self.latitude = response['latitude']
        if 'longitude' in response:
            self.longitude = response['longitude']
        if 'member_count' in response:
            self.member_count = response['member_count']
        if 'out_org_address' in response:
            self.out_org_address = response['out_org_address']
        if 'out_org_area' in response:
            self.out_org_area = response['out_org_area']
        if 'out_org_city' in response:
            self.out_org_city = response['out_org_city']
        if 'out_org_name' in response:
            self.out_org_name = response['out_org_name']
        if 'out_org_province' in response:
            self.out_org_province = response['out_org_province']
        if 'out_org_street' in response:
            self.out_org_street = response['out_org_street']
        if 'status' in response:
            self.status = response['status']
