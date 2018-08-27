#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppBillGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppBillGetResponse, self).__init__()
        self._alipay_order_no = None
        self._bill_date = None
        self._bill_key = None
        self._charge_inst = None
        self._charge_inst_name = None
        self._merchant_order_no = None
        self._order_status = None
        self._order_type = None
        self._owner_name = None
        self._pay_amount = None
        self._pay_time = None
        self._service_amount = None
        self._sub_order_type = None
        self._traffic_location = None
        self._traffic_regulations = None

    @property
    def alipay_order_no(self):
        return self._alipay_order_no

    @alipay_order_no.setter
    def alipay_order_no(self, value):
        self._alipay_order_no = value
    @property
    def bill_date(self):
        return self._bill_date

    @bill_date.setter
    def bill_date(self, value):
        self._bill_date = value
    @property
    def bill_key(self):
        return self._bill_key

    @bill_key.setter
    def bill_key(self, value):
        self._bill_key = value
    @property
    def charge_inst(self):
        return self._charge_inst

    @charge_inst.setter
    def charge_inst(self, value):
        self._charge_inst = value
    @property
    def charge_inst_name(self):
        return self._charge_inst_name

    @charge_inst_name.setter
    def charge_inst_name(self, value):
        self._charge_inst_name = value
    @property
    def merchant_order_no(self):
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self._merchant_order_no = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def owner_name(self):
        return self._owner_name

    @owner_name.setter
    def owner_name(self, value):
        self._owner_name = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def service_amount(self):
        return self._service_amount

    @service_amount.setter
    def service_amount(self, value):
        self._service_amount = value
    @property
    def sub_order_type(self):
        return self._sub_order_type

    @sub_order_type.setter
    def sub_order_type(self, value):
        self._sub_order_type = value
    @property
    def traffic_location(self):
        return self._traffic_location

    @traffic_location.setter
    def traffic_location(self, value):
        self._traffic_location = value
    @property
    def traffic_regulations(self):
        return self._traffic_regulations

    @traffic_regulations.setter
    def traffic_regulations(self, value):
        self._traffic_regulations = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppBillGetResponse, self).parse_response_content(response_content)
        if 'alipay_order_no' in response:
            self.alipay_order_no = response['alipay_order_no']
        if 'bill_date' in response:
            self.bill_date = response['bill_date']
        if 'bill_key' in response:
            self.bill_key = response['bill_key']
        if 'charge_inst' in response:
            self.charge_inst = response['charge_inst']
        if 'charge_inst_name' in response:
            self.charge_inst_name = response['charge_inst_name']
        if 'merchant_order_no' in response:
            self.merchant_order_no = response['merchant_order_no']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'order_type' in response:
            self.order_type = response['order_type']
        if 'owner_name' in response:
            self.owner_name = response['owner_name']
        if 'pay_amount' in response:
            self.pay_amount = response['pay_amount']
        if 'pay_time' in response:
            self.pay_time = response['pay_time']
        if 'service_amount' in response:
            self.service_amount = response['service_amount']
        if 'sub_order_type' in response:
            self.sub_order_type = response['sub_order_type']
        if 'traffic_location' in response:
            self.traffic_location = response['traffic_location']
        if 'traffic_regulations' in response:
            self.traffic_regulations = response['traffic_regulations']
