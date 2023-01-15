#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundAllocTransferQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundAllocTransferQueryResponse, self).__init__()
        self._alloc_time = None
        self._amount = None
        self._biz_type = None
        self._certification_no = None
        self._certification_type = None
        self._order_id = None
        self._out_biz_no = None
        self._status = None

    @property
    def alloc_time(self):
        return self._alloc_time

    @alloc_time.setter
    def alloc_time(self, value):
        self._alloc_time = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def certification_no(self):
        return self._certification_no

    @certification_no.setter
    def certification_no(self, value):
        self._certification_no = value
    @property
    def certification_type(self):
        return self._certification_type

    @certification_type.setter
    def certification_type(self, value):
        self._certification_type = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundAllocTransferQueryResponse, self).parse_response_content(response_content)
        if 'alloc_time' in response:
            self.alloc_time = response['alloc_time']
        if 'amount' in response:
            self.amount = response['amount']
        if 'biz_type' in response:
            self.biz_type = response['biz_type']
        if 'certification_no' in response:
            self.certification_no = response['certification_no']
        if 'certification_type' in response:
            self.certification_type = response['certification_type']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'status' in response:
            self.status = response['status']
