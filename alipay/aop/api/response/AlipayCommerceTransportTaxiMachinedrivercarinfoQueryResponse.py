#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportTaxiMachinedrivercarinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportTaxiMachinedrivercarinfoQueryResponse, self).__init__()
        self._car_color = None
        self._driver_city = None
        self._driver_name = None
        self._phone = None
        self._plate_no = None
        self._result_code = None
        self._result_msg = None
        self._seats = None
        self._sex = None
        self._sign_status = None
        self._sys_driver_id = None

    @property
    def car_color(self):
        return self._car_color

    @car_color.setter
    def car_color(self, value):
        self._car_color = value
    @property
    def driver_city(self):
        return self._driver_city

    @driver_city.setter
    def driver_city(self, value):
        self._driver_city = value
    @property
    def driver_name(self):
        return self._driver_name

    @driver_name.setter
    def driver_name(self, value):
        self._driver_name = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def plate_no(self):
        return self._plate_no

    @plate_no.setter
    def plate_no(self, value):
        self._plate_no = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_msg(self):
        return self._result_msg

    @result_msg.setter
    def result_msg(self, value):
        self._result_msg = value
    @property
    def seats(self):
        return self._seats

    @seats.setter
    def seats(self, value):
        self._seats = value
    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        self._sex = value
    @property
    def sign_status(self):
        return self._sign_status

    @sign_status.setter
    def sign_status(self, value):
        self._sign_status = value
    @property
    def sys_driver_id(self):
        return self._sys_driver_id

    @sys_driver_id.setter
    def sys_driver_id(self, value):
        self._sys_driver_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportTaxiMachinedrivercarinfoQueryResponse, self).parse_response_content(response_content)
        if 'car_color' in response:
            self.car_color = response['car_color']
        if 'driver_city' in response:
            self.driver_city = response['driver_city']
        if 'driver_name' in response:
            self.driver_name = response['driver_name']
        if 'phone' in response:
            self.phone = response['phone']
        if 'plate_no' in response:
            self.plate_no = response['plate_no']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_msg' in response:
            self.result_msg = response['result_msg']
        if 'seats' in response:
            self.seats = response['seats']
        if 'sex' in response:
            self.sex = response['sex']
        if 'sign_status' in response:
            self.sign_status = response['sign_status']
        if 'sys_driver_id' in response:
            self.sys_driver_id = response['sys_driver_id']
