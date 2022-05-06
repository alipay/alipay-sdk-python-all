#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ParkingOrderPromo import ParkingOrderPromo


class AlipayEcoMycarParkingPayApplyModel(object):

    def __init__(self):
        self._in_time = None
        self._out_order_no = None
        self._out_serial_no = None
        self._out_time = None
        self._parking_id = None
        self._pay_scene = None
        self._plate_color = None
        self._plate_no = None
        self._promo = None
        self._seller_id = None
        self._serial_no = None
        self._subject = None
        self._total_amount = None

    @property
    def in_time(self):
        return self._in_time

    @in_time.setter
    def in_time(self, value):
        self._in_time = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def out_serial_no(self):
        return self._out_serial_no

    @out_serial_no.setter
    def out_serial_no(self, value):
        self._out_serial_no = value
    @property
    def out_time(self):
        return self._out_time

    @out_time.setter
    def out_time(self, value):
        self._out_time = value
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
    def plate_color(self):
        return self._plate_color

    @plate_color.setter
    def plate_color(self, value):
        self._plate_color = value
    @property
    def plate_no(self):
        return self._plate_no

    @plate_no.setter
    def plate_no(self, value):
        self._plate_no = value
    @property
    def promo(self):
        return self._promo

    @promo.setter
    def promo(self, value):
        if isinstance(value, ParkingOrderPromo):
            self._promo = value
        else:
            self._promo = ParkingOrderPromo.from_alipay_dict(value)
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
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
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.in_time:
            if hasattr(self.in_time, 'to_alipay_dict'):
                params['in_time'] = self.in_time.to_alipay_dict()
            else:
                params['in_time'] = self.in_time
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.out_serial_no:
            if hasattr(self.out_serial_no, 'to_alipay_dict'):
                params['out_serial_no'] = self.out_serial_no.to_alipay_dict()
            else:
                params['out_serial_no'] = self.out_serial_no
        if self.out_time:
            if hasattr(self.out_time, 'to_alipay_dict'):
                params['out_time'] = self.out_time.to_alipay_dict()
            else:
                params['out_time'] = self.out_time
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
        if self.plate_color:
            if hasattr(self.plate_color, 'to_alipay_dict'):
                params['plate_color'] = self.plate_color.to_alipay_dict()
            else:
                params['plate_color'] = self.plate_color
        if self.plate_no:
            if hasattr(self.plate_no, 'to_alipay_dict'):
                params['plate_no'] = self.plate_no.to_alipay_dict()
            else:
                params['plate_no'] = self.plate_no
        if self.promo:
            if hasattr(self.promo, 'to_alipay_dict'):
                params['promo'] = self.promo.to_alipay_dict()
            else:
                params['promo'] = self.promo
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
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
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarParkingPayApplyModel()
        if 'in_time' in d:
            o.in_time = d['in_time']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'out_serial_no' in d:
            o.out_serial_no = d['out_serial_no']
        if 'out_time' in d:
            o.out_time = d['out_time']
        if 'parking_id' in d:
            o.parking_id = d['parking_id']
        if 'pay_scene' in d:
            o.pay_scene = d['pay_scene']
        if 'plate_color' in d:
            o.plate_color = d['plate_color']
        if 'plate_no' in d:
            o.plate_no = d['plate_no']
        if 'promo' in d:
            o.promo = d['promo']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'serial_no' in d:
            o.serial_no = d['serial_no']
        if 'subject' in d:
            o.subject = d['subject']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


