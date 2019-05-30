#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarParkingOrderPayModel(object):

    def __init__(self):
        self._agent_id = None
        self._body = None
        self._car_number = None
        self._car_number_color = None
        self._is_advance = None
        self._out_parking_id = None
        self._out_trade_no = None
        self._parking_id = None
        self._seller_id = None
        self._seller_logon_id = None
        self._subject = None
        self._total_fee = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
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
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
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
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'body' in d:
            o.body = d['body']
        if 'car_number' in d:
            o.car_number = d['car_number']
        if 'car_number_color' in d:
            o.car_number_color = d['car_number_color']
        if 'is_advance' in d:
            o.is_advance = d['is_advance']
        if 'out_parking_id' in d:
            o.out_parking_id = d['out_parking_id']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'parking_id' in d:
            o.parking_id = d['parking_id']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'seller_logon_id' in d:
            o.seller_logon_id = d['seller_logon_id']
        if 'subject' in d:
            o.subject = d['subject']
        if 'total_fee' in d:
            o.total_fee = d['total_fee']
        return o


