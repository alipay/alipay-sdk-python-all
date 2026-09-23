#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportTaxiBibifanQueryModel(object):

    def __init__(self):
        self._driver_cert_no = None
        self._end_date = None
        self._source = None
        self._start_date = None

    @property
    def driver_cert_no(self):
        return self._driver_cert_no

    @driver_cert_no.setter
    def driver_cert_no(self, value):
        self._driver_cert_no = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.driver_cert_no:
            if hasattr(self.driver_cert_no, 'to_alipay_dict'):
                params['driver_cert_no'] = self.driver_cert_no.to_alipay_dict()
            else:
                params['driver_cert_no'] = self.driver_cert_no
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportTaxiBibifanQueryModel()
        if 'driver_cert_no' in d:
            o.driver_cert_no = d['driver_cert_no']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'source' in d:
            o.source = d['source']
        if 'start_date' in d:
            o.start_date = d['start_date']
        return o


