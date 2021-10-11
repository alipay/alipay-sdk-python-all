#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportTaxiDriverinfoQueryModel(object):

    def __init__(self):
        self._driver_cert_no = None
        self._request_time = None

    @property
    def driver_cert_no(self):
        return self._driver_cert_no

    @driver_cert_no.setter
    def driver_cert_no(self, value):
        self._driver_cert_no = value
    @property
    def request_time(self):
        return self._request_time

    @request_time.setter
    def request_time(self, value):
        self._request_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.driver_cert_no:
            if hasattr(self.driver_cert_no, 'to_alipay_dict'):
                params['driver_cert_no'] = self.driver_cert_no.to_alipay_dict()
            else:
                params['driver_cert_no'] = self.driver_cert_no
        if self.request_time:
            if hasattr(self.request_time, 'to_alipay_dict'):
                params['request_time'] = self.request_time.to_alipay_dict()
            else:
                params['request_time'] = self.request_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportTaxiDriverinfoQueryModel()
        if 'driver_cert_no' in d:
            o.driver_cert_no = d['driver_cert_no']
        if 'request_time' in d:
            o.request_time = d['request_time']
        return o


