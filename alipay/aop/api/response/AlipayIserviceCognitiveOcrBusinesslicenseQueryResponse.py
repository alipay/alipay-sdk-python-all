#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceCognitiveOcrBusinesslicenseQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCognitiveOcrBusinesslicenseQueryResponse, self).__init__()
        self._address = None
        self._business = None
        self._captial = None
        self._error_content = None
        self._establish_date = None
        self._name = None
        self._person = None
        self._reg_num = None
        self._request_id = None
        self._success = None
        self._trace_id = None
        self._valid_period = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def business(self):
        return self._business

    @business.setter
    def business(self, value):
        self._business = value
    @property
    def captial(self):
        return self._captial

    @captial.setter
    def captial(self, value):
        self._captial = value
    @property
    def error_content(self):
        return self._error_content

    @error_content.setter
    def error_content(self, value):
        self._error_content = value
    @property
    def establish_date(self):
        return self._establish_date

    @establish_date.setter
    def establish_date(self, value):
        self._establish_date = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def person(self):
        return self._person

    @person.setter
    def person(self, value):
        self._person = value
    @property
    def reg_num(self):
        return self._reg_num

    @reg_num.setter
    def reg_num(self, value):
        self._reg_num = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value
    @property
    def valid_period(self):
        return self._valid_period

    @valid_period.setter
    def valid_period(self, value):
        self._valid_period = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCognitiveOcrBusinesslicenseQueryResponse, self).parse_response_content(response_content)
        if 'address' in response:
            self.address = response['address']
        if 'business' in response:
            self.business = response['business']
        if 'captial' in response:
            self.captial = response['captial']
        if 'error_content' in response:
            self.error_content = response['error_content']
        if 'establish_date' in response:
            self.establish_date = response['establish_date']
        if 'name' in response:
            self.name = response['name']
        if 'person' in response:
            self.person = response['person']
        if 'reg_num' in response:
            self.reg_num = response['reg_num']
        if 'request_id' in response:
            self.request_id = response['request_id']
        if 'success' in response:
            self.success = response['success']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']
        if 'valid_period' in response:
            self.valid_period = response['valid_period']
