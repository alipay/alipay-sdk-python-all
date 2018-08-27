#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryOrderQueryResponse, self).__init__()
        self._extend_field = None
        self._gmt_create = None
        self._gmt_pay = None
        self._gmt_refund = None
        self._gmt_success = None
        self._order_no = None
        self._out_order_no = None
        self._status = None

    @property
    def extend_field(self):
        return self._extend_field

    @extend_field.setter
    def extend_field(self, value):
        self._extend_field = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_pay(self):
        return self._gmt_pay

    @gmt_pay.setter
    def gmt_pay(self, value):
        self._gmt_pay = value
    @property
    def gmt_refund(self):
        return self._gmt_refund

    @gmt_refund.setter
    def gmt_refund(self, value):
        self._gmt_refund = value
    @property
    def gmt_success(self):
        return self._gmt_success

    @gmt_success.setter
    def gmt_success(self, value):
        self._gmt_success = value
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
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryOrderQueryResponse, self).parse_response_content(response_content)
        if 'extend_field' in response:
            self.extend_field = response['extend_field']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'gmt_pay' in response:
            self.gmt_pay = response['gmt_pay']
        if 'gmt_refund' in response:
            self.gmt_refund = response['gmt_refund']
        if 'gmt_success' in response:
            self.gmt_success = response['gmt_success']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'status' in response:
            self.status = response['status']
