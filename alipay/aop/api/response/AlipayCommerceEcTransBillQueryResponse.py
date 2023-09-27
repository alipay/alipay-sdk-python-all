#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcTransBillQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcTransBillQueryResponse, self).__init__()
        self._alipay_trans_order_id = None
        self._amount = None
        self._biz_trans_type = None
        self._create_time = None
        self._enterprise_id = None
        self._finish_time = None
        self._out_biz_no = None
        self._status = None

    @property
    def alipay_trans_order_id(self):
        return self._alipay_trans_order_id

    @alipay_trans_order_id.setter
    def alipay_trans_order_id(self, value):
        self._alipay_trans_order_id = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def biz_trans_type(self):
        return self._biz_trans_type

    @biz_trans_type.setter
    def biz_trans_type(self, value):
        self._biz_trans_type = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def finish_time(self):
        return self._finish_time

    @finish_time.setter
    def finish_time(self, value):
        self._finish_time = value
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
        response = super(AlipayCommerceEcTransBillQueryResponse, self).parse_response_content(response_content)
        if 'alipay_trans_order_id' in response:
            self.alipay_trans_order_id = response['alipay_trans_order_id']
        if 'amount' in response:
            self.amount = response['amount']
        if 'biz_trans_type' in response:
            self.biz_trans_type = response['biz_trans_type']
        if 'create_time' in response:
            self.create_time = response['create_time']
        if 'enterprise_id' in response:
            self.enterprise_id = response['enterprise_id']
        if 'finish_time' in response:
            self.finish_time = response['finish_time']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'status' in response:
            self.status = response['status']
