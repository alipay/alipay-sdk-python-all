#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneApplicationGroupApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneApplicationGroupApplyResponse, self).__init__()
        self._application_no = None
        self._operation_id = None
        self._out_biz_no = None
        self._trade_no = None

    @property
    def application_no(self):
        return self._application_no

    @application_no.setter
    def application_no(self, value):
        self._application_no = value
    @property
    def operation_id(self):
        return self._operation_id

    @operation_id.setter
    def operation_id(self, value):
        self._operation_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneApplicationGroupApplyResponse, self).parse_response_content(response_content)
        if 'application_no' in response:
            self.application_no = response['application_no']
        if 'operation_id' in response:
            self.operation_id = response['operation_id']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
