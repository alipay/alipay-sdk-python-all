#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppFacepayBillPayResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppFacepayBillPayResponse, self).__init__()
        self._bill_no = None
        self._biz_status = None
        self._charge_inst = None
        self._extend_field = None
        self._inst_no = None
        self._out_order_no = None
        self._status = None
        self._trade_date = None
        self._user_id = None

    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def biz_status(self):
        return self._biz_status

    @biz_status.setter
    def biz_status(self, value):
        self._biz_status = value
    @property
    def charge_inst(self):
        return self._charge_inst

    @charge_inst.setter
    def charge_inst(self, value):
        self._charge_inst = value
    @property
    def extend_field(self):
        return self._extend_field

    @extend_field.setter
    def extend_field(self, value):
        self._extend_field = value
    @property
    def inst_no(self):
        return self._inst_no

    @inst_no.setter
    def inst_no(self, value):
        self._inst_no = value
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
    @property
    def trade_date(self):
        return self._trade_date

    @trade_date.setter
    def trade_date(self, value):
        self._trade_date = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppFacepayBillPayResponse, self).parse_response_content(response_content)
        if 'bill_no' in response:
            self.bill_no = response['bill_no']
        if 'biz_status' in response:
            self.biz_status = response['biz_status']
        if 'charge_inst' in response:
            self.charge_inst = response['charge_inst']
        if 'extend_field' in response:
            self.extend_field = response['extend_field']
        if 'inst_no' in response:
            self.inst_no = response['inst_no']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'status' in response:
            self.status = response['status']
        if 'trade_date' in response:
            self.trade_date = response['trade_date']
        if 'user_id' in response:
            self.user_id = response['user_id']
