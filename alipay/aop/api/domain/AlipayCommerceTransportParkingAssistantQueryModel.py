#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportParkingAssistantQueryModel(object):

    def __init__(self):
        self._license_plate_color = None
        self._license_plate_no = None

    @property
    def license_plate_color(self):
        return self._license_plate_color

    @license_plate_color.setter
    def license_plate_color(self, value):
        self._license_plate_color = value
    @property
    def license_plate_no(self):
        return self._license_plate_no

    @license_plate_no.setter
    def license_plate_no(self, value):
        self._license_plate_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.license_plate_color:
            if hasattr(self.license_plate_color, 'to_alipay_dict'):
                params['license_plate_color'] = self.license_plate_color.to_alipay_dict()
            else:
                params['license_plate_color'] = self.license_plate_color
        if self.license_plate_no:
            if hasattr(self.license_plate_no, 'to_alipay_dict'):
                params['license_plate_no'] = self.license_plate_no.to_alipay_dict()
            else:
                params['license_plate_no'] = self.license_plate_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportParkingAssistantQueryModel()
        if 'license_plate_color' in d:
            o.license_plate_color = d['license_plate_color']
        if 'license_plate_no' in d:
            o.license_plate_no = d['license_plate_no']
        return o


