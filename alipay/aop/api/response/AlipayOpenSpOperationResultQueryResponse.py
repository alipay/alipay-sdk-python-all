#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSpOperationResultQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpOperationResultQueryResponse, self).__init__()
        self._bind_user_id = None
        self._handle_status = None
        self._merchant_no = None

    @property
    def bind_user_id(self):
        return self._bind_user_id

    @bind_user_id.setter
    def bind_user_id(self, value):
        self._bind_user_id = value
    @property
    def handle_status(self):
        return self._handle_status

    @handle_status.setter
    def handle_status(self, value):
        self._handle_status = value
    @property
    def merchant_no(self):
        return self._merchant_no

    @merchant_no.setter
    def merchant_no(self, value):
        self._merchant_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpOperationResultQueryResponse, self).parse_response_content(response_content)
        if 'bind_user_id' in response:
            self.bind_user_id = response['bind_user_id']
        if 'handle_status' in response:
            self.handle_status = response['handle_status']
        if 'merchant_no' in response:
            self.merchant_no = response['merchant_no']
