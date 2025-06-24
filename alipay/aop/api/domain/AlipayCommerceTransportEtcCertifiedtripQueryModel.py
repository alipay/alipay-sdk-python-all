#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportEtcCertifiedtripQueryModel(object):

    def __init__(self):
        self._auth_agreement_no = None
        self._end_time = None
        self._out_waybill_no = None
        self._page_num = None
        self._page_size = None
        self._push_trip = None
        self._start_time = None

    @property
    def auth_agreement_no(self):
        return self._auth_agreement_no

    @auth_agreement_no.setter
    def auth_agreement_no(self, value):
        self._auth_agreement_no = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def out_waybill_no(self):
        return self._out_waybill_no

    @out_waybill_no.setter
    def out_waybill_no(self, value):
        self._out_waybill_no = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def push_trip(self):
        return self._push_trip

    @push_trip.setter
    def push_trip(self, value):
        self._push_trip = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_agreement_no:
            if hasattr(self.auth_agreement_no, 'to_alipay_dict'):
                params['auth_agreement_no'] = self.auth_agreement_no.to_alipay_dict()
            else:
                params['auth_agreement_no'] = self.auth_agreement_no
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.out_waybill_no:
            if hasattr(self.out_waybill_no, 'to_alipay_dict'):
                params['out_waybill_no'] = self.out_waybill_no.to_alipay_dict()
            else:
                params['out_waybill_no'] = self.out_waybill_no
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.push_trip:
            if hasattr(self.push_trip, 'to_alipay_dict'):
                params['push_trip'] = self.push_trip.to_alipay_dict()
            else:
                params['push_trip'] = self.push_trip
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportEtcCertifiedtripQueryModel()
        if 'auth_agreement_no' in d:
            o.auth_agreement_no = d['auth_agreement_no']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'out_waybill_no' in d:
            o.out_waybill_no = d['out_waybill_no']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'push_trip' in d:
            o.push_trip = d['push_trip']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


