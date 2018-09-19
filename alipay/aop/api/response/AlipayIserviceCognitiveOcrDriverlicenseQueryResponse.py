#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceCognitiveOcrDriverlicenseQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCognitiveOcrDriverlicenseQueryResponse, self).__init__()
        self._addr = None
        self._end_date = None
        self._error_content = None
        self._name = None
        self._num = None
        self._request_id = None
        self._sex = None
        self._start_date = None
        self._success = None
        self._trace_id = None
        self._vehicle_type = None

    @property
    def addr(self):
        return self._addr

    @addr.setter
    def addr(self, value):
        self._addr = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def error_content(self):
        return self._error_content

    @error_content.setter
    def error_content(self, value):
        self._error_content = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, value):
        self._num = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        self._sex = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
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
    def vehicle_type(self):
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, value):
        self._vehicle_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCognitiveOcrDriverlicenseQueryResponse, self).parse_response_content(response_content)
        if 'addr' in response:
            self.addr = response['addr']
        if 'end_date' in response:
            self.end_date = response['end_date']
        if 'error_content' in response:
            self.error_content = response['error_content']
        if 'name' in response:
            self.name = response['name']
        if 'num' in response:
            self.num = response['num']
        if 'request_id' in response:
            self.request_id = response['request_id']
        if 'sex' in response:
            self.sex = response['sex']
        if 'start_date' in response:
            self.start_date = response['start_date']
        if 'success' in response:
            self.success = response['success']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']
        if 'vehicle_type' in response:
            self.vehicle_type = response['vehicle_type']
