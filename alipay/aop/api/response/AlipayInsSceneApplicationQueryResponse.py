#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsPolicy import InsPolicy


class AlipayInsSceneApplicationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneApplicationQueryResponse, self).__init__()
        self._application_no = None
        self._application_status = None
        self._operation_id = None
        self._out_biz_no = None
        self._policys = None
        self._trade_no = None

    @property
    def application_no(self):
        return self._application_no

    @application_no.setter
    def application_no(self, value):
        self._application_no = value
    @property
    def application_status(self):
        return self._application_status

    @application_status.setter
    def application_status(self, value):
        self._application_status = value
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
    def policys(self):
        return self._policys

    @policys.setter
    def policys(self, value):
        if isinstance(value, list):
            self._policys = list()
            for i in value:
                if isinstance(i, InsPolicy):
                    self._policys.append(i)
                else:
                    self._policys.append(InsPolicy.from_alipay_dict(i))
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneApplicationQueryResponse, self).parse_response_content(response_content)
        if 'application_no' in response:
            self.application_no = response['application_no']
        if 'application_status' in response:
            self.application_status = response['application_status']
        if 'operation_id' in response:
            self.operation_id = response['operation_id']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'policys' in response:
            self.policys = response['policys']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
