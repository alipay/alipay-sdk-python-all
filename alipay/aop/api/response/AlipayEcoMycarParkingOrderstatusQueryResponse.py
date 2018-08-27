#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoMycarParkingOrderstatusQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarParkingOrderstatusQueryResponse, self).__init__()
        self._alipay_order_id = None
        self._car_order_id = None
        self._equipment_order_id = None
        self._pay_money = None
        self._pay_status = None
        self._pay_time = None
        self._pay_type = None
        self._status = None

    @property
    def alipay_order_id(self):
        return self._alipay_order_id

    @alipay_order_id.setter
    def alipay_order_id(self, value):
        self._alipay_order_id = value
    @property
    def car_order_id(self):
        return self._car_order_id

    @car_order_id.setter
    def car_order_id(self, value):
        self._car_order_id = value
    @property
    def equipment_order_id(self):
        return self._equipment_order_id

    @equipment_order_id.setter
    def equipment_order_id(self, value):
        self._equipment_order_id = value
    @property
    def pay_money(self):
        return self._pay_money

    @pay_money.setter
    def pay_money(self, value):
        self._pay_money = value
    @property
    def pay_status(self):
        return self._pay_status

    @pay_status.setter
    def pay_status(self, value):
        self._pay_status = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def pay_type(self):
        return self._pay_type

    @pay_type.setter
    def pay_type(self, value):
        self._pay_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarParkingOrderstatusQueryResponse, self).parse_response_content(response_content)
        if 'alipay_order_id' in response:
            self.alipay_order_id = response['alipay_order_id']
        if 'car_order_id' in response:
            self.car_order_id = response['car_order_id']
        if 'equipment_order_id' in response:
            self.equipment_order_id = response['equipment_order_id']
        if 'pay_money' in response:
            self.pay_money = response['pay_money']
        if 'pay_status' in response:
            self.pay_status = response['pay_status']
        if 'pay_time' in response:
            self.pay_time = response['pay_time']
        if 'pay_type' in response:
            self.pay_type = response['pay_type']
        if 'status' in response:
            self.status = response['status']
