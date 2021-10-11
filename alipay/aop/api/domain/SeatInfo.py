#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SeatInfo(object):

    def __init__(self):
        self._seat_class = None
        self._seat_no = None

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


    def to_alipay_dict(self):
        params = dict()
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SeatInfo()
        if 'seat_class' in d:
            o.seat_class = d['seat_class']
        if 'seat_no' in d:
            o.seat_no = d['seat_no']
        return o


