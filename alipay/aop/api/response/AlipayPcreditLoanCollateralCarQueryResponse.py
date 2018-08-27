#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditLoanCollateralCarQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanCollateralCarQueryResponse, self).__init__()
        self._address = None
        self._apply_no = None
        self._car_brand_id = None
        self._car_color = None
        self._car_engine_no = None
        self._car_mileage = None
        self._car_model_id = None
        self._car_reg_date = None
        self._car_series_id = None
        self._car_vin = None
        self._cert_no = None
        self._cert_type = None
        self._created_time = None
        self._lic_plate_address = None
        self._lic_plate_no = None
        self._name = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def car_brand_id(self):
        return self._car_brand_id

    @car_brand_id.setter
    def car_brand_id(self, value):
        self._car_brand_id = value
    @property
    def car_color(self):
        return self._car_color

    @car_color.setter
    def car_color(self, value):
        self._car_color = value
    @property
    def car_engine_no(self):
        return self._car_engine_no

    @car_engine_no.setter
    def car_engine_no(self, value):
        self._car_engine_no = value
    @property
    def car_mileage(self):
        return self._car_mileage

    @car_mileage.setter
    def car_mileage(self, value):
        self._car_mileage = value
    @property
    def car_model_id(self):
        return self._car_model_id

    @car_model_id.setter
    def car_model_id(self, value):
        self._car_model_id = value
    @property
    def car_reg_date(self):
        return self._car_reg_date

    @car_reg_date.setter
    def car_reg_date(self, value):
        self._car_reg_date = value
    @property
    def car_series_id(self):
        return self._car_series_id

    @car_series_id.setter
    def car_series_id(self, value):
        self._car_series_id = value
    @property
    def car_vin(self):
        return self._car_vin

    @car_vin.setter
    def car_vin(self, value):
        self._car_vin = value
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
    def created_time(self):
        return self._created_time

    @created_time.setter
    def created_time(self, value):
        self._created_time = value
    @property
    def lic_plate_address(self):
        return self._lic_plate_address

    @lic_plate_address.setter
    def lic_plate_address(self, value):
        self._lic_plate_address = value
    @property
    def lic_plate_no(self):
        return self._lic_plate_no

    @lic_plate_no.setter
    def lic_plate_no(self, value):
        self._lic_plate_no = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanCollateralCarQueryResponse, self).parse_response_content(response_content)
        if 'address' in response:
            self.address = response['address']
        if 'apply_no' in response:
            self.apply_no = response['apply_no']
        if 'car_brand_id' in response:
            self.car_brand_id = response['car_brand_id']
        if 'car_color' in response:
            self.car_color = response['car_color']
        if 'car_engine_no' in response:
            self.car_engine_no = response['car_engine_no']
        if 'car_mileage' in response:
            self.car_mileage = response['car_mileage']
        if 'car_model_id' in response:
            self.car_model_id = response['car_model_id']
        if 'car_reg_date' in response:
            self.car_reg_date = response['car_reg_date']
        if 'car_series_id' in response:
            self.car_series_id = response['car_series_id']
        if 'car_vin' in response:
            self.car_vin = response['car_vin']
        if 'cert_no' in response:
            self.cert_no = response['cert_no']
        if 'cert_type' in response:
            self.cert_type = response['cert_type']
        if 'created_time' in response:
            self.created_time = response['created_time']
        if 'lic_plate_address' in response:
            self.lic_plate_address = response['lic_plate_address']
        if 'lic_plate_no' in response:
            self.lic_plate_no = response['lic_plate_no']
        if 'name' in response:
            self.name = response['name']
