#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAipayDelegationPaytokenQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAipayDelegationPaytokenQueryResponse, self).__init__()
        self._biz_order_no = None
        self._delegation_id = None
        self._order_amount = None
        self._status = None
        self._valid_end_time = None

    @property
    def biz_order_no(self):
        return self._biz_order_no

    @biz_order_no.setter
    def biz_order_no(self, value):
        self._biz_order_no = value
    @property
    def delegation_id(self):
        return self._delegation_id

    @delegation_id.setter
    def delegation_id(self, value):
        self._delegation_id = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def valid_end_time(self):
        return self._valid_end_time

    @valid_end_time.setter
    def valid_end_time(self, value):
        self._valid_end_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayAipayDelegationPaytokenQueryResponse, self).parse_response_content(response_content)
        if 'biz_order_no' in response:
            self.biz_order_no = response['biz_order_no']
        if 'delegation_id' in response:
            self.delegation_id = response['delegation_id']
        if 'order_amount' in response:
            self.order_amount = response['order_amount']
        if 'status' in response:
            self.status = response['status']
        if 'valid_end_time' in response:
            self.valid_end_time = response['valid_end_time']
