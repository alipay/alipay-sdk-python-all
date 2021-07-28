#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarParkingOrderPayModel(object):

    def __init__(self):
        self._after_pay_order = None
        self._agent_id = None
        self._billing_duration = None
        self._body = None
        self._car_number = None
        self._car_number_color = None
        self._in_duration = None
        self._in_time = None
        self._is_advance = None
        self._out_parking_id = None
        self._out_time = None
        self._out_trade_no = None
        self._parking_id = None
        self._pay_scene = None
        self._pay_version = None
        self._seller_id = None
        self._seller_logon_id = None
        self._serial_no = None
        self._subject = None
        self._total_fee = None

    @property
    def after_pay_order(self):
        return self._after_pay_order

    @after_pay_order.setter
    def after_pay_order(self, value):
        self._after_pay_order = value
    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def billing_duration(self):
        return self._billing_duration

    @billing_duration.setter
    def billing_duration(self, value):
        self._billing_duration = value
    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        self._body = value
    @property
    def car_number(self):
        return self._car_number

    @car_number.setter
    def car_number(self, value):
        self._car_number = value
    @property
    def car_number_color(self):
        return self._car_number_color

    @car_number_color.setter
    def car_number_color(self, value):
        self._car_number_color = value
    @property
    def in_duration(self):
        return self._in_duration

    @in_duration.setter
    def in_duration(self, value):
        self._in_duration = value
    @property
    def in_time(self):
        return self._in_time

    @in_time.setter
    def in_time(self, value):
        self._in_time = value
    @property
    def is_advance(self):
        return self._is_advance

    @is_advance.setter
    def is_advance(self, value):
        self._is_advance = value
    @property
    def out_parking_id(self):
        return self._out_parking_id

    @out_parking_id.setter
    def out_parking_id(self, value):
        self._out_parking_id = value
    @property
    def out_time(self):
        return self._out_time

    @out_time.setter
    def out_time(self, value):
        self._out_time = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def parking_id(self):
        return self._parking_id

    @parking_id.setter
    def parking_id(self, value):
        self._parking_id = value
    @property
    def pay_scene(self):
        return self._pay_scene

    @pay_scene.setter
    def pay_scene(self, value):
        self._pay_scene = value
    @property
    def pay_version(self):
        return self._pay_version

    @pay_version.setter
    def pay_version(self, value):
        self._pay_version = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def seller_logon_id(self):
        return self._seller_logon_id

    @seller_logon_id.setter
    def seller_logon_id(self, value):
        self._seller_logon_id = value
    @property
    def serial_no(self):
        return self._serial_no

    @serial_no.setter
    def serial_no(self, value):
        self._serial_no = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def total_fee(self):
        return self._total_fee

    @total_fee.setter
    def total_fee(self, value):
        self._total_fee = value


    def to_alipay_dict(self):
        params = dict()
        if self.after_pay_order:
            if hasattr(self.after_pay_order, 'to_alipay_dict'):
                params['after_pay_order'] = self.after_pay_order.to_alipay_dict()
            else:
                params['after_pay_order'] = self.after_pay_order
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
        if self.billing_duration:
            if hasattr(self.billing_duration, 'to_alipay_dict'):
                params['billing_duration'] = self.billing_duration.to_alipay_dict()
            else:
                params['billing_duration'] = self.billing_duration
        if self.body:
            if hasattr(self.body, 'to_alipay_dict'):
                params['body'] = self.body.to_alipay_dict()
            else:
                params['body'] = self.body
        if self.car_number:
            if hasattr(self.car_number, 'to_alipay_dict'):
                params['car_number'] = self.car_number.to_alipay_dict()
            else:
                params['car_number'] = self.car_number
        if self.car_number_color:
            if hasattr(self.car_number_color, 'to_alipay_dict'):
                params['car_number_color'] = self.car_number_color.to_alipay_dict()
            else:
                params['car_number_color'] = self.car_number_color
        if self.in_duration:
            if hasattr(self.in_duration, 'to_alipay_dict'):
                params['in_duration'] = self.in_duration.to_alipay_dict()
            else:
                params['in_duration'] = self.in_duration
        if self.in_time:
            if hasattr(self.in_time, 'to_alipay_dict'):
                params['in_time'] = self.in_time.to_alipay_dict()
            else:
                params['in_time'] = self.in_time
        if self.is_advance:
            if hasattr(self.is_advance, 'to_alipay_dict'):
                params['is_advance'] = self.is_advance.to_alipay_dict()
            else:
                params['is_advance'] = self.is_advance
        if self.out_parking_id:
            if hasattr(self.out_parking_id, 'to_alipay_dict'):
                params['out_parking_id'] = self.out_parking_id.to_alipay_dict()
            else:
                params['out_parking_id'] = self.out_parking_id
        if self.out_time:
            if hasattr(self.out_time, 'to_alipay_dict'):
                params['out_time'] = self.out_time.to_alipay_dict()
            else:
                params['out_time'] = self.out_time
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.parking_id:
            if hasattr(self.parking_id, 'to_alipay_dict'):
                params['parking_id'] = self.parking_id.to_alipay_dict()
            else:
                params['parking_id'] = self.parking_id
        if self.pay_scene:
            if hasattr(self.pay_scene, 'to_alipay_dict'):
                params['pay_scene'] = self.pay_scene.to_alipay_dict()
            else:
                params['pay_scene'] = self.pay_scene
        if self.pay_version:
            if hasattr(self.pay_version, 'to_alipay_dict'):
                params['pay_version'] = self.pay_version.to_alipay_dict()
            else:
                params['pay_version'] = self.pay_version
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.seller_logon_id:
            if hasattr(self.seller_logon_id, 'to_alipay_dict'):
                params['seller_logon_id'] = self.seller_logon_id.to_alipay_dict()
            else:
                params['seller_logon_id'] = self.seller_logon_id
        if self.serial_no:
            if hasattr(self.serial_no, 'to_alipay_dict'):
                params['serial_no'] = self.serial_no.to_alipay_dict()
            else:
                params['serial_no'] = self.serial_no
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        if self.total_fee:
            if hasattr(self.total_fee, 'to_alipay_dict'):
                params['total_fee'] = self.total_fee.to_alipay_dict()
            else:
                params['total_fee'] = self.total_fee
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarParkingOrderPayModel()
        if 'after_pay_order' in d:
            o.after_pay_order = d['after_pay_order']
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'billing_duration' in d:
            o.billing_duration = d['billing_duration']
        if 'body' in d:
            o.body = d['body']
        if 'car_number' in d:
            o.car_number = d['car_number']
        if 'car_number_color' in d:
            o.car_number_color = d['car_number_color']
        if 'in_duration' in d:
            o.in_duration = d['in_duration']
        if 'in_time' in d:
            o.in_time = d['in_time']
        if 'is_advance' in d:
            o.is_advance = d['is_advance']
        if 'out_parking_id' in d:
            o.out_parking_id = d['out_parking_id']
        if 'out_time' in d:
            o.out_time = d['out_time']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'parking_id' in d:
            o.parking_id = d['parking_id']
        if 'pay_scene' in d:
            o.pay_scene = d['pay_scene']
        if 'pay_version' in d:
            o.pay_version = d['pay_version']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'seller_logon_id' in d:
            o.seller_logon_id = d['seller_logon_id']
        if 'serial_no' in d:
            o.serial_no = d['serial_no']
        if 'subject' in d:
            o.subject = d['subject']
        if 'total_fee' in d:
            o.total_fee = d['total_fee']
        return o


