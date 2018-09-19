#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoMycarDialogonlineVehicleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarDialogonlineVehicleQueryResponse, self).__init__()
        self._factory_date = None
        self._lib_id = None
        self._manufacturer = None
        self._resident_city = None
        self._vi_brand = None
        self._vi_cc = None
        self._vi_id = None
        self._vi_mileage = None
        self._vi_model = None
        self._vi_series = None
        self._vi_time = None

    @property
    def factory_date(self):
        return self._factory_date

    @factory_date.setter
    def factory_date(self, value):
        self._factory_date = value
    @property
    def lib_id(self):
        return self._lib_id

    @lib_id.setter
    def lib_id(self, value):
        self._lib_id = value
    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        self._manufacturer = value
    @property
    def resident_city(self):
        return self._resident_city

    @resident_city.setter
    def resident_city(self, value):
        self._resident_city = value
    @property
    def vi_brand(self):
        return self._vi_brand

    @vi_brand.setter
    def vi_brand(self, value):
        self._vi_brand = value
    @property
    def vi_cc(self):
        return self._vi_cc

    @vi_cc.setter
    def vi_cc(self, value):
        self._vi_cc = value
    @property
    def vi_id(self):
        return self._vi_id

    @vi_id.setter
    def vi_id(self, value):
        self._vi_id = value
    @property
    def vi_mileage(self):
        return self._vi_mileage

    @vi_mileage.setter
    def vi_mileage(self, value):
        self._vi_mileage = value
    @property
    def vi_model(self):
        return self._vi_model

    @vi_model.setter
    def vi_model(self, value):
        self._vi_model = value
    @property
    def vi_series(self):
        return self._vi_series

    @vi_series.setter
    def vi_series(self, value):
        self._vi_series = value
    @property
    def vi_time(self):
        return self._vi_time

    @vi_time.setter
    def vi_time(self, value):
        self._vi_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarDialogonlineVehicleQueryResponse, self).parse_response_content(response_content)
        if 'factory_date' in response:
            self.factory_date = response['factory_date']
        if 'lib_id' in response:
            self.lib_id = response['lib_id']
        if 'manufacturer' in response:
            self.manufacturer = response['manufacturer']
        if 'resident_city' in response:
            self.resident_city = response['resident_city']
        if 'vi_brand' in response:
            self.vi_brand = response['vi_brand']
        if 'vi_cc' in response:
            self.vi_cc = response['vi_cc']
        if 'vi_id' in response:
            self.vi_id = response['vi_id']
        if 'vi_mileage' in response:
            self.vi_mileage = response['vi_mileage']
        if 'vi_model' in response:
            self.vi_model = response['vi_model']
        if 'vi_series' in response:
            self.vi_series = response['vi_series']
        if 'vi_time' in response:
            self.vi_time = response['vi_time']
