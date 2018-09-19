#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceCognitiveOcrVehiclelicenseQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCognitiveOcrVehiclelicenseQueryResponse, self).__init__()
        self._engine_num = None
        self._error_content = None
        self._issue_date = None
        self._model = None
        self._owner = None
        self._plate_num = None
        self._register_date = None
        self._request_id = None
        self._success = None
        self._trace_id = None
        self._use_character = None
        self._vehicle_type = None
        self._vin = None

    @property
    def engine_num(self):
        return self._engine_num

    @engine_num.setter
    def engine_num(self, value):
        self._engine_num = value
    @property
    def error_content(self):
        return self._error_content

    @error_content.setter
    def error_content(self, value):
        self._error_content = value
    @property
    def issue_date(self):
        return self._issue_date

    @issue_date.setter
    def issue_date(self, value):
        self._issue_date = value
    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value
    @property
    def plate_num(self):
        return self._plate_num

    @plate_num.setter
    def plate_num(self, value):
        self._plate_num = value
    @property
    def register_date(self):
        return self._register_date

    @register_date.setter
    def register_date(self, value):
        self._register_date = value
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
    def use_character(self):
        return self._use_character

    @use_character.setter
    def use_character(self, value):
        self._use_character = value
    @property
    def vehicle_type(self):
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, value):
        self._vehicle_type = value
    @property
    def vin(self):
        return self._vin

    @vin.setter
    def vin(self, value):
        self._vin = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCognitiveOcrVehiclelicenseQueryResponse, self).parse_response_content(response_content)
        if 'engine_num' in response:
            self.engine_num = response['engine_num']
        if 'error_content' in response:
            self.error_content = response['error_content']
        if 'issue_date' in response:
            self.issue_date = response['issue_date']
        if 'model' in response:
            self.model = response['model']
        if 'owner' in response:
            self.owner = response['owner']
        if 'plate_num' in response:
            self.plate_num = response['plate_num']
        if 'register_date' in response:
            self.register_date = response['register_date']
        if 'request_id' in response:
            self.request_id = response['request_id']
        if 'success' in response:
            self.success = response['success']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']
        if 'use_character' in response:
            self.use_character = response['use_character']
        if 'vehicle_type' in response:
            self.vehicle_type = response['vehicle_type']
        if 'vin' in response:
            self.vin = response['vin']
