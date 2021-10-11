#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniIsvQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniIsvQueryResponse, self).__init__()
        self._min_app_id = None
        self._order_no = None
        self._out_order_no = None
        self._pid = None
        self._status = None

    @property
    def min_app_id(self):
        return self._min_app_id

    @min_app_id.setter
    def min_app_id(self, value):
        self._min_app_id = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniIsvQueryResponse, self).parse_response_content(response_content)
        if 'min_app_id' in response:
            self.min_app_id = response['min_app_id']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'pid' in response:
            self.pid = response['pid']
        if 'status' in response:
            self.status = response['status']
