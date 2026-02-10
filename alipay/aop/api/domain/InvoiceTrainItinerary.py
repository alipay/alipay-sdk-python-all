#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceTrainItinerary(object):

    def __init__(self):
        self._departure = None
        self._departure_time = None
        self._destination = None
        self._seat_class = None
        self._seat_no = None
        self._train_no = None

    @property
    def departure(self):
        return self._departure

    @departure.setter
    def departure(self, value):
        self._departure = value
    @property
    def departure_time(self):
        return self._departure_time

    @departure_time.setter
    def departure_time(self, value):
        self._departure_time = value
    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, value):
        self._destination = value
    @property
    def seat_class(self):
        return self._seat_class

    @seat_class.setter
    def seat_class(self, value):
        self._seat_class = value
    @property
    def seat_no(self):
        return self._seat_no

    @seat_no.setter
    def seat_no(self, value):
        self._seat_no = value
    @property
    def train_no(self):
        return self._train_no

    @train_no.setter
    def train_no(self, value):
        self._train_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.departure:
            if hasattr(self.departure, 'to_alipay_dict'):
                params['departure'] = self.departure.to_alipay_dict()
            else:
                params['departure'] = self.departure
        if self.departure_time:
            if hasattr(self.departure_time, 'to_alipay_dict'):
                params['departure_time'] = self.departure_time.to_alipay_dict()
            else:
                params['departure_time'] = self.departure_time
        if self.destination:
            if hasattr(self.destination, 'to_alipay_dict'):
                params['destination'] = self.destination.to_alipay_dict()
            else:
                params['destination'] = self.destination
        if self.seat_class:
            if hasattr(self.seat_class, 'to_alipay_dict'):
                params['seat_class'] = self.seat_class.to_alipay_dict()
            else:
                params['seat_class'] = self.seat_class
        if self.seat_no:
            if hasattr(self.seat_no, 'to_alipay_dict'):
                params['seat_no'] = self.seat_no.to_alipay_dict()
            else:
                params['seat_no'] = self.seat_no
        if self.train_no:
            if hasattr(self.train_no, 'to_alipay_dict'):
                params['train_no'] = self.train_no.to_alipay_dict()
            else:
                params['train_no'] = self.train_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceTrainItinerary()
        if 'departure' in d:
            o.departure = d['departure']
        if 'departure_time' in d:
            o.departure_time = d['departure_time']
        if 'destination' in d:
            o.destination = d['destination']
        if 'seat_class' in d:
            o.seat_class = d['seat_class']
        if 'seat_no' in d:
            o.seat_no = d['seat_no']
        if 'train_no' in d:
            o.train_no = d['train_no']
        return o


