#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundAuthOperationCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundAuthOperationCancelResponse, self).__init__()
        self._action = None
        self._auth_no = None
        self._operation_id = None
        self._out_order_no = None
        self._out_request_no = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def auth_no(self):
        return self._auth_no

    @auth_no.setter
    def auth_no(self, value):
        self._auth_no = value
    @property
    def operation_id(self):
        return self._operation_id

    @operation_id.setter
    def operation_id(self, value):
        self._operation_id = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundAuthOperationCancelResponse, self).parse_response_content(response_content)
        if 'action' in response:
            self.action = response['action']
        if 'auth_no' in response:
            self.auth_no = response['auth_no']
        if 'operation_id' in response:
            self.operation_id = response['operation_id']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
