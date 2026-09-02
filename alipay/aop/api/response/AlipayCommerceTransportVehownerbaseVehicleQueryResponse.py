#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportVehownerbaseVehicleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportVehownerbaseVehicleQueryResponse, self).__init__()
        self._auth_date = None
        self._brand_id = None
        self._brand_name = None
        self._engine_no = None
        self._issue_date = None
        self._license_back_url = None
        self._license_url = None
        self._model_id = None
        self._model_name = None
        self._owner = None
        self._plate_color = None
        self._register_date = None
        self._senior_certificated = None
        self._series_id = None
        self._series_name = None
        self._trusted_from = None
        self._use_type = None
        self._vehicle_type = None
        self._vi_id = None
        self._vi_number = None
        self._vin = None
        self._vur_grade = None

    @property
    def auth_date(self):
        return self._auth_date

    @auth_date.setter
    def auth_date(self, value):
        self._auth_date = value
    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def engine_no(self):
        return self._engine_no

    @engine_no.setter
    def engine_no(self, value):
        self._engine_no = value
    @property
    def issue_date(self):
        return self._issue_date

    @issue_date.setter
    def issue_date(self, value):
        self._issue_date = value
    @property
    def license_back_url(self):
        return self._license_back_url

    @license_back_url.setter
    def license_back_url(self, value):
        self._license_back_url = value
    @property
    def license_url(self):
        return self._license_url

    @license_url.setter
    def license_url(self, value):
        self._license_url = value
    @property
    def model_id(self):
        return self._model_id

    @model_id.setter
    def model_id(self, value):
        self._model_id = value
    @property
    def model_name(self):
        return self._model_name

    @model_name.setter
    def model_name(self, value):
        self._model_name = value
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value
    @property
    def plate_color(self):
        return self._plate_color

    @plate_color.setter
    def plate_color(self, value):
        self._plate_color = value
    @property
    def register_date(self):
        return self._register_date

    @register_date.setter
    def register_date(self, value):
        self._register_date = value
    @property
    def senior_certificated(self):
        return self._senior_certificated

    @senior_certificated.setter
    def senior_certificated(self, value):
        self._senior_certificated = value
    @property
    def series_id(self):
        return self._series_id

    @series_id.setter
    def series_id(self, value):
        self._series_id = value
    @property
    def series_name(self):
        return self._series_name

    @series_name.setter
    def series_name(self, value):
        self._series_name = value
    @property
    def trusted_from(self):
        return self._trusted_from

    @trusted_from.setter
    def trusted_from(self, value):
        self._trusted_from = value
    @property
    def use_type(self):
        return self._use_type

    @use_type.setter
    def use_type(self, value):
        self._use_type = value
    @property
    def vehicle_type(self):
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, value):
        self._vehicle_type = value
    @property
    def vi_id(self):
        return self._vi_id

    @vi_id.setter
    def vi_id(self, value):
        self._vi_id = value
    @property
    def vi_number(self):
        return self._vi_number

    @vi_number.setter
    def vi_number(self, value):
        self._vi_number = value
    @property
    def vin(self):
        return self._vin

    @vin.setter
    def vin(self, value):
        self._vin = value
    @property
    def vur_grade(self):
        return self._vur_grade

    @vur_grade.setter
    def vur_grade(self, value):
        self._vur_grade = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportVehownerbaseVehicleQueryResponse, self).parse_response_content(response_content)
        if 'auth_date' in response:
            self.auth_date = response['auth_date']
        if 'brand_id' in response:
            self.brand_id = response['brand_id']
        if 'brand_name' in response:
            self.brand_name = response['brand_name']
        if 'engine_no' in response:
            self.engine_no = response['engine_no']
        if 'issue_date' in response:
            self.issue_date = response['issue_date']
        if 'license_back_url' in response:
            self.license_back_url = response['license_back_url']
        if 'license_url' in response:
            self.license_url = response['license_url']
        if 'model_id' in response:
            self.model_id = response['model_id']
        if 'model_name' in response:
            self.model_name = response['model_name']
        if 'owner' in response:
            self.owner = response['owner']
        if 'plate_color' in response:
            self.plate_color = response['plate_color']
        if 'register_date' in response:
            self.register_date = response['register_date']
        if 'senior_certificated' in response:
            self.senior_certificated = response['senior_certificated']
        if 'series_id' in response:
            self.series_id = response['series_id']
        if 'series_name' in response:
            self.series_name = response['series_name']
        if 'trusted_from' in response:
            self.trusted_from = response['trusted_from']
        if 'use_type' in response:
            self.use_type = response['use_type']
        if 'vehicle_type' in response:
            self.vehicle_type = response['vehicle_type']
        if 'vi_id' in response:
            self.vi_id = response['vi_id']
        if 'vi_number' in response:
            self.vi_number = response['vi_number']
        if 'vin' in response:
            self.vin = response['vin']
        if 'vur_grade' in response:
            self.vur_grade = response['vur_grade']
