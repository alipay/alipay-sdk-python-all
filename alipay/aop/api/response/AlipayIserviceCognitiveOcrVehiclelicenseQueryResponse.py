#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceCognitiveOcrVehiclelicenseQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCognitiveOcrVehiclelicenseQueryResponse, self).__init__()
        self._approved_load = None
        self._approved_passenger_capacity = None
        self._energy_type = None
        self._engine_num = None
        self._error_content = None
        self._file_no = None
        self._gross_mass = None
        self._inspection_record = None
        self._issue_date = None
        self._model = None
        self._overall_dimension = None
        self._owner = None
        self._plate_num = None
        self._register_date = None
        self._request_id = None
        self._success = None
        self._trace_id = None
        self._unladen_mass = None
        self._use_character = None
        self._vehicle_type = None
        self._vin = None

    @property
    def approved_load(self):
        return self._approved_load

    @approved_load.setter
    def approved_load(self, value):
        self._approved_load = value
    @property
    def approved_passenger_capacity(self):
        return self._approved_passenger_capacity

    @approved_passenger_capacity.setter
    def approved_passenger_capacity(self, value):
        self._approved_passenger_capacity = value
    @property
    def energy_type(self):
        return self._energy_type

    @energy_type.setter
    def energy_type(self, value):
        self._energy_type = value
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
    def file_no(self):
        return self._file_no

    @file_no.setter
    def file_no(self, value):
        self._file_no = value
    @property
    def gross_mass(self):
        return self._gross_mass

    @gross_mass.setter
    def gross_mass(self, value):
        self._gross_mass = value
    @property
    def inspection_record(self):
        return self._inspection_record

    @inspection_record.setter
    def inspection_record(self, value):
        self._inspection_record = value
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
    def overall_dimension(self):
        return self._overall_dimension

    @overall_dimension.setter
    def overall_dimension(self, value):
        self._overall_dimension = value
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
    def unladen_mass(self):
        return self._unladen_mass

    @unladen_mass.setter
    def unladen_mass(self, value):
        self._unladen_mass = value
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
        if 'approved_load' in response:
            self.approved_load = response['approved_load']
        if 'approved_passenger_capacity' in response:
            self.approved_passenger_capacity = response['approved_passenger_capacity']
        if 'energy_type' in response:
            self.energy_type = response['energy_type']
        if 'engine_num' in response:
            self.engine_num = response['engine_num']
        if 'error_content' in response:
            self.error_content = response['error_content']
        if 'file_no' in response:
            self.file_no = response['file_no']
        if 'gross_mass' in response:
            self.gross_mass = response['gross_mass']
        if 'inspection_record' in response:
            self.inspection_record = response['inspection_record']
        if 'issue_date' in response:
            self.issue_date = response['issue_date']
        if 'model' in response:
            self.model = response['model']
        if 'overall_dimension' in response:
            self.overall_dimension = response['overall_dimension']
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
        if 'unladen_mass' in response:
            self.unladen_mass = response['unladen_mass']
        if 'use_character' in response:
            self.use_character = response['use_character']
        if 'vehicle_type' in response:
            self.vehicle_type = response['vehicle_type']
        if 'vin' in response:
            self.vin = response['vin']
