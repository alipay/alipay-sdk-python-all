#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPeEvaluateBehaviorQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPeEvaluateBehaviorQueryResponse, self).__init__()
        self._evaluate_time = None
        self._open_id = None
        self._out_trade_no = None
        self._service_id = None
        self._user_id = None

    @property
    def evaluate_time(self):
        return self._evaluate_time

    @evaluate_time.setter
    def evaluate_time(self, value):
        self._evaluate_time = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPeEvaluateBehaviorQueryResponse, self).parse_response_content(response_content)
        if 'evaluate_time' in response:
            self.evaluate_time = response['evaluate_time']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'service_id' in response:
            self.service_id = response['service_id']
        if 'user_id' in response:
            self.user_id = response['user_id']
