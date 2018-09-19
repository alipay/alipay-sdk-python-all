#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InputFieldModel import InputFieldModel


class AlipayEbppConfigProductSearchResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppConfigProductSearchResponse, self).__init__()
        self._charge_inst = None
        self._chargeoff_inst = None
        self._error_code = None
        self._error_message = None
        self._input_field_list = None
        self._is_success = None

    @property
    def charge_inst(self):
        return self._charge_inst

    @charge_inst.setter
    def charge_inst(self, value):
        self._charge_inst = value
    @property
    def chargeoff_inst(self):
        return self._chargeoff_inst

    @chargeoff_inst.setter
    def chargeoff_inst(self, value):
        self._chargeoff_inst = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_message(self):
        return self._error_message

    @error_message.setter
    def error_message(self, value):
        self._error_message = value
    @property
    def input_field_list(self):
        return self._input_field_list

    @input_field_list.setter
    def input_field_list(self, value):
        if isinstance(value, list):
            self._input_field_list = list()
            for i in value:
                if isinstance(i, InputFieldModel):
                    self._input_field_list.append(i)
                else:
                    self._input_field_list.append(InputFieldModel.from_alipay_dict(i))
    @property
    def is_success(self):
        return self._is_success

    @is_success.setter
    def is_success(self, value):
        self._is_success = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppConfigProductSearchResponse, self).parse_response_content(response_content)
        if 'charge_inst' in response:
            self.charge_inst = response['charge_inst']
        if 'chargeoff_inst' in response:
            self.chargeoff_inst = response['chargeoff_inst']
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'error_message' in response:
            self.error_message = response['error_message']
        if 'input_field_list' in response:
            self.input_field_list = response['input_field_list']
        if 'is_success' in response:
            self.is_success = response['is_success']
