#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportParkingFeeQueryModel(object):

    def __init__(self):
        self._license_plate_no = None
        self._request_channel = None

    @property
    def license_plate_no(self):
        return self._license_plate_no

    @license_plate_no.setter
    def license_plate_no(self, value):
        self._license_plate_no = value
    @property
    def request_channel(self):
        return self._request_channel

    @request_channel.setter
    def request_channel(self, value):
        self._request_channel = value


    def to_alipay_dict(self):
        params = dict()
        if self.license_plate_no:
            if hasattr(self.license_plate_no, 'to_alipay_dict'):
                params['license_plate_no'] = self.license_plate_no.to_alipay_dict()
            else:
                params['license_plate_no'] = self.license_plate_no
        if self.request_channel:
            if hasattr(self.request_channel, 'to_alipay_dict'):
                params['request_channel'] = self.request_channel.to_alipay_dict()
            else:
                params['request_channel'] = self.request_channel
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportParkingFeeQueryModel()
        if 'license_plate_no' in d:
            o.license_plate_no = d['license_plate_no']
        if 'request_channel' in d:
            o.request_channel = d['request_channel']
        return o


