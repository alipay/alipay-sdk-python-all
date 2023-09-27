#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DetectCheckLabel import DetectCheckLabel


class AlipaySecurityRiskContentSyncDetectResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskContentSyncDetectResponse, self).__init__()
        self._detect_check_labels = None
        self._is_meter = None
        self._is_sync = None
        self._meter_products = None
        self._request_id = None
        self._result_code = None
        self._result_msg = None
        self._suggestion = None

    @property
    def detect_check_labels(self):
        return self._detect_check_labels

    @detect_check_labels.setter
    def detect_check_labels(self, value):
        if isinstance(value, DetectCheckLabel):
            self._detect_check_labels = value
        else:
            self._detect_check_labels = DetectCheckLabel.from_alipay_dict(value)
    @property
    def is_meter(self):
        return self._is_meter

    @is_meter.setter
    def is_meter(self, value):
        self._is_meter = value
    @property
    def is_sync(self):
        return self._is_sync

    @is_sync.setter
    def is_sync(self, value):
        self._is_sync = value
    @property
    def meter_products(self):
        return self._meter_products

    @meter_products.setter
    def meter_products(self, value):
        self._meter_products = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
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
    def suggestion(self):
        return self._suggestion

    @suggestion.setter
    def suggestion(self, value):
        self._suggestion = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskContentSyncDetectResponse, self).parse_response_content(response_content)
        if 'detect_check_labels' in response:
            self.detect_check_labels = response['detect_check_labels']
        if 'is_meter' in response:
            self.is_meter = response['is_meter']
        if 'is_sync' in response:
            self.is_sync = response['is_sync']
        if 'meter_products' in response:
            self.meter_products = response['meter_products']
        if 'request_id' in response:
            self.request_id = response['request_id']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_msg' in response:
            self.result_msg = response['result_msg']
        if 'suggestion' in response:
            self.suggestion = response['suggestion']
