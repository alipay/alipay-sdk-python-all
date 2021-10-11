#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderVehicleInfo(object):

    def __init__(self):
        self._license_plate_no = None
        self._memo = None
        self._shift_no = None

    @property
    def license_plate_no(self):
        return self._license_plate_no

    @license_plate_no.setter
    def license_plate_no(self, value):
        self._license_plate_no = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def shift_no(self):
        return self._shift_no

    @shift_no.setter
    def shift_no(self, value):
        self._shift_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.license_plate_no:
            if hasattr(self.license_plate_no, 'to_alipay_dict'):
                params['license_plate_no'] = self.license_plate_no.to_alipay_dict()
            else:
                params['license_plate_no'] = self.license_plate_no
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.shift_no:
            if hasattr(self.shift_no, 'to_alipay_dict'):
                params['shift_no'] = self.shift_no.to_alipay_dict()
            else:
                params['shift_no'] = self.shift_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderVehicleInfo()
        if 'license_plate_no' in d:
            o.license_plate_no = d['license_plate_no']
        if 'memo' in d:
            o.memo = d['memo']
        if 'shift_no' in d:
            o.shift_no = d['shift_no']
        return o


