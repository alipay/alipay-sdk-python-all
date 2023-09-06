#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryPerformOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryPerformOrderQueryResponse, self).__init__()
        self._alloc_status = None
        self._bill_amount = None
        self._bill_no = None
        self._chargeoff_status = None
        self._create_type = None
        self._gmt_alloc = None
        self._gmt_chargeoff_finish = None
        self._gmt_chargeoff_start = None
        self._gmt_create = None
        self._gmt_pay = None
        self._gmt_refund = None
        self._gmt_settle = None
        self._inst_code = None
        self._inst_group = None
        self._item_id = None
        self._out_no = None
        self._pay_amount = None
        self._service_code = None
        self._settle_status = None
        self._status = None
        self._trade_no = None
        self._unique_code = None

    @property
    def alloc_status(self):
        return self._alloc_status

    @alloc_status.setter
    def alloc_status(self, value):
        self._alloc_status = value
    @property
    def bill_amount(self):
        return self._bill_amount

    @bill_amount.setter
    def bill_amount(self, value):
        self._bill_amount = value
    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def chargeoff_status(self):
        return self._chargeoff_status

    @chargeoff_status.setter
    def chargeoff_status(self, value):
        self._chargeoff_status = value
    @property
    def create_type(self):
        return self._create_type

    @create_type.setter
    def create_type(self, value):
        self._create_type = value
    @property
    def gmt_alloc(self):
        return self._gmt_alloc

    @gmt_alloc.setter
    def gmt_alloc(self, value):
        self._gmt_alloc = value
    @property
    def gmt_chargeoff_finish(self):
        return self._gmt_chargeoff_finish

    @gmt_chargeoff_finish.setter
    def gmt_chargeoff_finish(self, value):
        self._gmt_chargeoff_finish = value
    @property
    def gmt_chargeoff_start(self):
        return self._gmt_chargeoff_start

    @gmt_chargeoff_start.setter
    def gmt_chargeoff_start(self, value):
        self._gmt_chargeoff_start = value
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
    def gmt_settle(self):
        return self._gmt_settle

    @gmt_settle.setter
    def gmt_settle(self, value):
        self._gmt_settle = value
    @property
    def inst_code(self):
        return self._inst_code

    @inst_code.setter
    def inst_code(self, value):
        self._inst_code = value
    @property
    def inst_group(self):
        return self._inst_group

    @inst_group.setter
    def inst_group(self, value):
        self._inst_group = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def out_no(self):
        return self._out_no

    @out_no.setter
    def out_no(self, value):
        self._out_no = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
    @property
    def settle_status(self):
        return self._settle_status

    @settle_status.setter
    def settle_status(self, value):
        self._settle_status = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def unique_code(self):
        return self._unique_code

    @unique_code.setter
    def unique_code(self, value):
        self._unique_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryPerformOrderQueryResponse, self).parse_response_content(response_content)
        if 'alloc_status' in response:
            self.alloc_status = response['alloc_status']
        if 'bill_amount' in response:
            self.bill_amount = response['bill_amount']
        if 'bill_no' in response:
            self.bill_no = response['bill_no']
        if 'chargeoff_status' in response:
            self.chargeoff_status = response['chargeoff_status']
        if 'create_type' in response:
            self.create_type = response['create_type']
        if 'gmt_alloc' in response:
            self.gmt_alloc = response['gmt_alloc']
        if 'gmt_chargeoff_finish' in response:
            self.gmt_chargeoff_finish = response['gmt_chargeoff_finish']
        if 'gmt_chargeoff_start' in response:
            self.gmt_chargeoff_start = response['gmt_chargeoff_start']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'gmt_pay' in response:
            self.gmt_pay = response['gmt_pay']
        if 'gmt_refund' in response:
            self.gmt_refund = response['gmt_refund']
        if 'gmt_settle' in response:
            self.gmt_settle = response['gmt_settle']
        if 'inst_code' in response:
            self.inst_code = response['inst_code']
        if 'inst_group' in response:
            self.inst_group = response['inst_group']
        if 'item_id' in response:
            self.item_id = response['item_id']
        if 'out_no' in response:
            self.out_no = response['out_no']
        if 'pay_amount' in response:
            self.pay_amount = response['pay_amount']
        if 'service_code' in response:
            self.service_code = response['service_code']
        if 'settle_status' in response:
            self.settle_status = response['settle_status']
        if 'status' in response:
            self.status = response['status']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
        if 'unique_code' in response:
            self.unique_code = response['unique_code']
