#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ParkingPaymentDiscountInfo import ParkingPaymentDiscountInfo


class AlipayCommerceTransportParkingPaymentinfoSyncModel(object):

    def __init__(self):
        self._alipay_trade_no = None
        self._discount_amount = None
        self._discount_information = None
        self._free_exit_minutes = None
        self._inactive_user = None
        self._is_encrypt_plate_no = None
        self._mobile_number = None
        self._open_appid = None
        self._open_id = None
        self._out_order_no = None
        self._out_serial_no = None
        self._pay_frequency = None
        self._payment_amount = None
        self._payment_time = None
        self._payment_type = None
        self._payment_user_open_id = None
        self._plate_color = None
        self._plate_no = None
        self._service_url = None
        self._total_amount = None

    @property
    def alipay_trade_no(self):
        return self._alipay_trade_no

    @alipay_trade_no.setter
    def alipay_trade_no(self, value):
        self._alipay_trade_no = value
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def discount_information(self):
        return self._discount_information

    @discount_information.setter
    def discount_information(self, value):
        if isinstance(value, list):
            self._discount_information = list()
            for i in value:
                if isinstance(i, ParkingPaymentDiscountInfo):
                    self._discount_information.append(i)
                else:
                    self._discount_information.append(ParkingPaymentDiscountInfo.from_alipay_dict(i))
    @property
    def free_exit_minutes(self):
        return self._free_exit_minutes

    @free_exit_minutes.setter
    def free_exit_minutes(self, value):
        self._free_exit_minutes = value
    @property
    def inactive_user(self):
        return self._inactive_user

    @inactive_user.setter
    def inactive_user(self, value):
        self._inactive_user = value
    @property
    def is_encrypt_plate_no(self):
        return self._is_encrypt_plate_no

    @is_encrypt_plate_no.setter
    def is_encrypt_plate_no(self, value):
        self._is_encrypt_plate_no = value
    @property
    def mobile_number(self):
        return self._mobile_number

    @mobile_number.setter
    def mobile_number(self, value):
        self._mobile_number = value
    @property
    def open_appid(self):
        return self._open_appid

    @open_appid.setter
    def open_appid(self, value):
        self._open_appid = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
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
    def pay_frequency(self):
        return self._pay_frequency

    @pay_frequency.setter
    def pay_frequency(self, value):
        self._pay_frequency = value
    @property
    def payment_amount(self):
        return self._payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self._payment_amount = value
    @property
    def payment_time(self):
        return self._payment_time

    @payment_time.setter
    def payment_time(self, value):
        self._payment_time = value
    @property
    def payment_type(self):
        return self._payment_type

    @payment_type.setter
    def payment_type(self, value):
        self._payment_type = value
    @property
    def payment_user_open_id(self):
        return self._payment_user_open_id

    @payment_user_open_id.setter
    def payment_user_open_id(self, value):
        self._payment_user_open_id = value
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
    def service_url(self):
        return self._service_url

    @service_url.setter
    def service_url(self, value):
        self._service_url = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_trade_no:
            if hasattr(self.alipay_trade_no, 'to_alipay_dict'):
                params['alipay_trade_no'] = self.alipay_trade_no.to_alipay_dict()
            else:
                params['alipay_trade_no'] = self.alipay_trade_no
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.discount_information:
            if isinstance(self.discount_information, list):
                for i in range(0, len(self.discount_information)):
                    element = self.discount_information[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.discount_information[i] = element.to_alipay_dict()
            if hasattr(self.discount_information, 'to_alipay_dict'):
                params['discount_information'] = self.discount_information.to_alipay_dict()
            else:
                params['discount_information'] = self.discount_information
        if self.free_exit_minutes:
            if hasattr(self.free_exit_minutes, 'to_alipay_dict'):
                params['free_exit_minutes'] = self.free_exit_minutes.to_alipay_dict()
            else:
                params['free_exit_minutes'] = self.free_exit_minutes
        if self.inactive_user:
            if hasattr(self.inactive_user, 'to_alipay_dict'):
                params['inactive_user'] = self.inactive_user.to_alipay_dict()
            else:
                params['inactive_user'] = self.inactive_user
        if self.is_encrypt_plate_no:
            if hasattr(self.is_encrypt_plate_no, 'to_alipay_dict'):
                params['is_encrypt_plate_no'] = self.is_encrypt_plate_no.to_alipay_dict()
            else:
                params['is_encrypt_plate_no'] = self.is_encrypt_plate_no
        if self.mobile_number:
            if hasattr(self.mobile_number, 'to_alipay_dict'):
                params['mobile_number'] = self.mobile_number.to_alipay_dict()
            else:
                params['mobile_number'] = self.mobile_number
        if self.open_appid:
            if hasattr(self.open_appid, 'to_alipay_dict'):
                params['open_appid'] = self.open_appid.to_alipay_dict()
            else:
                params['open_appid'] = self.open_appid
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
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
        if self.pay_frequency:
            if hasattr(self.pay_frequency, 'to_alipay_dict'):
                params['pay_frequency'] = self.pay_frequency.to_alipay_dict()
            else:
                params['pay_frequency'] = self.pay_frequency
        if self.payment_amount:
            if hasattr(self.payment_amount, 'to_alipay_dict'):
                params['payment_amount'] = self.payment_amount.to_alipay_dict()
            else:
                params['payment_amount'] = self.payment_amount
        if self.payment_time:
            if hasattr(self.payment_time, 'to_alipay_dict'):
                params['payment_time'] = self.payment_time.to_alipay_dict()
            else:
                params['payment_time'] = self.payment_time
        if self.payment_type:
            if hasattr(self.payment_type, 'to_alipay_dict'):
                params['payment_type'] = self.payment_type.to_alipay_dict()
            else:
                params['payment_type'] = self.payment_type
        if self.payment_user_open_id:
            if hasattr(self.payment_user_open_id, 'to_alipay_dict'):
                params['payment_user_open_id'] = self.payment_user_open_id.to_alipay_dict()
            else:
                params['payment_user_open_id'] = self.payment_user_open_id
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
        if self.service_url:
            if hasattr(self.service_url, 'to_alipay_dict'):
                params['service_url'] = self.service_url.to_alipay_dict()
            else:
                params['service_url'] = self.service_url
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
        o = AlipayCommerceTransportParkingPaymentinfoSyncModel()
        if 'alipay_trade_no' in d:
            o.alipay_trade_no = d['alipay_trade_no']
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'discount_information' in d:
            o.discount_information = d['discount_information']
        if 'free_exit_minutes' in d:
            o.free_exit_minutes = d['free_exit_minutes']
        if 'inactive_user' in d:
            o.inactive_user = d['inactive_user']
        if 'is_encrypt_plate_no' in d:
            o.is_encrypt_plate_no = d['is_encrypt_plate_no']
        if 'mobile_number' in d:
            o.mobile_number = d['mobile_number']
        if 'open_appid' in d:
            o.open_appid = d['open_appid']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'out_serial_no' in d:
            o.out_serial_no = d['out_serial_no']
        if 'pay_frequency' in d:
            o.pay_frequency = d['pay_frequency']
        if 'payment_amount' in d:
            o.payment_amount = d['payment_amount']
        if 'payment_time' in d:
            o.payment_time = d['payment_time']
        if 'payment_type' in d:
            o.payment_type = d['payment_type']
        if 'payment_user_open_id' in d:
            o.payment_user_open_id = d['payment_user_open_id']
        if 'plate_color' in d:
            o.plate_color = d['plate_color']
        if 'plate_no' in d:
            o.plate_no = d['plate_no']
        if 'service_url' in d:
            o.service_url = d['service_url']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


