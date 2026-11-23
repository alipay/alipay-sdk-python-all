#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceOperationMallhomePointexchangeCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationMallhomePointexchangeCreateResponse, self).__init__()
        self._award_status = None
        self._exchange_order_id = None
        self._out_biz_no = None
        self._points_status = None
        self._prize_id = None
        self._request_id = None
        self._retryable = None

    @property
    def award_status(self):
        return self._award_status

    @award_status.setter
    def award_status(self, value):
        self._award_status = value
    @property
    def exchange_order_id(self):
        return self._exchange_order_id

    @exchange_order_id.setter
    def exchange_order_id(self, value):
        self._exchange_order_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def points_status(self):
        return self._points_status

    @points_status.setter
    def points_status(self, value):
        self._points_status = value
    @property
    def prize_id(self):
        return self._prize_id

    @prize_id.setter
    def prize_id(self, value):
        self._prize_id = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def retryable(self):
        return self._retryable

    @retryable.setter
    def retryable(self, value):
        self._retryable = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationMallhomePointexchangeCreateResponse, self).parse_response_content(response_content)
        if 'award_status' in response:
            self.award_status = response['award_status']
        if 'exchange_order_id' in response:
            self.exchange_order_id = response['exchange_order_id']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'points_status' in response:
            self.points_status = response['points_status']
        if 'prize_id' in response:
            self.prize_id = response['prize_id']
        if 'request_id' in response:
            self.request_id = response['request_id']
        if 'retryable' in response:
            self.retryable = response['retryable']
