#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundCouponOrderAppPayResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundCouponOrderAppPayResponse, self).__init__()
        self._amount = None
        self._auth_no = None
        self._gmt_trans = None
        self._operation_id = None
        self._out_order_no = None
        self._out_request_no = None
        self._status = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def auth_no(self):
        return self._auth_no

    @auth_no.setter
    def auth_no(self, value):
        self._auth_no = value
    @property
    def gmt_trans(self):
        return self._gmt_trans

    @gmt_trans.setter
    def gmt_trans(self, value):
        self._gmt_trans = value
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
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundCouponOrderAppPayResponse, self).parse_response_content(response_content)
        if 'amount' in response:
            self.amount = response['amount']
        if 'auth_no' in response:
            self.auth_no = response['auth_no']
        if 'gmt_trans' in response:
            self.gmt_trans = response['gmt_trans']
        if 'operation_id' in response:
            self.operation_id = response['operation_id']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'status' in response:
            self.status = response['status']
