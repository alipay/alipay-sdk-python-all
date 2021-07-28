#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPayAppSmartwearStatusQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPayAppSmartwearStatusQueryResponse, self).__init__()
        self._device_model = None
        self._product_type = None
        self._security_solution = None
        self._status = None

    @property
    def device_model(self):
        return self._device_model

    @device_model.setter
    def device_model(self, value):
        self._device_model = value
    @property
    def product_type(self):
        return self._product_type

    @product_type.setter
    def product_type(self, value):
        self._product_type = value
    @property
    def security_solution(self):
        return self._security_solution

    @security_solution.setter
    def security_solution(self, value):
        self._security_solution = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayPayAppSmartwearStatusQueryResponse, self).parse_response_content(response_content)
        if 'device_model' in response:
            self.device_model = response['device_model']
        if 'product_type' in response:
            self.product_type = response['product_type']
        if 'security_solution' in response:
            self.security_solution = response['security_solution']
        if 'status' in response:
            self.status = response['status']
