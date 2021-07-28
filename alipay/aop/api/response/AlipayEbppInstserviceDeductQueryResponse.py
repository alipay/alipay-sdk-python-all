#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInstserviceDeductQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInstserviceDeductQueryResponse, self).__init__()
        self._agreement_id = None
        self._current_status = None
        self._error_code = None
        self._extend_field = None

    @property
    def agreement_id(self):
        return self._agreement_id

    @agreement_id.setter
    def agreement_id(self, value):
        self._agreement_id = value
    @property
    def current_status(self):
        return self._current_status

    @current_status.setter
    def current_status(self, value):
        self._current_status = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def extend_field(self):
        return self._extend_field

    @extend_field.setter
    def extend_field(self, value):
        self._extend_field = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInstserviceDeductQueryResponse, self).parse_response_content(response_content)
        if 'agreement_id' in response:
            self.agreement_id = response['agreement_id']
        if 'current_status' in response:
            self.current_status = response['current_status']
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'extend_field' in response:
            self.extend_field = response['extend_field']
