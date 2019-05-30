#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppCommonBillQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppCommonBillQueryResponse, self).__init__()
        self._bill_key = None
        self._bill_no = None
        self._charge_inst = None
        self._chargeoff_inst = None
        self._extend_field = None
        self._gmt_create = None
        self._gmt_pay = None
        self._status = None

    @property
    def bill_key(self):
        return self._bill_key

    @bill_key.setter
    def bill_key(self, value):
        self._bill_key = value
    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def charge_inst(self):
        return self._charge_inst

    @charge_inst.setter
    def charge_inst(self, value):
        self._charge_inst = value
    @property
    def chargeoff_inst(self):
        return self._chargeoff_inst

    @chargeoff_inst.setter
    def chargeoff_inst(self, value):
        self._chargeoff_inst = value
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
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppCommonBillQueryResponse, self).parse_response_content(response_content)
        if 'bill_key' in response:
            self.bill_key = response['bill_key']
        if 'bill_no' in response:
            self.bill_no = response['bill_no']
        if 'charge_inst' in response:
            self.charge_inst = response['charge_inst']
        if 'chargeoff_inst' in response:
            self.chargeoff_inst = response['chargeoff_inst']
        if 'extend_field' in response:
            self.extend_field = response['extend_field']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'gmt_pay' in response:
            self.gmt_pay = response['gmt_pay']
        if 'status' in response:
            self.status = response['status']
