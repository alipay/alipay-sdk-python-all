#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CommunityService(object):

    def __init__(self):
        self._billkey_url = None
        self._daily_end = None
        self._daily_start = None
        self._out_bill_url = None
        self._service_type = None

    @property
    def billkey_url(self):
        return self._billkey_url

    @billkey_url.setter
    def billkey_url(self, value):
        self._billkey_url = value
    @property
    def daily_end(self):
        return self._daily_end

    @daily_end.setter
    def daily_end(self, value):
        self._daily_end = value
    @property
    def daily_start(self):
        return self._daily_start

    @daily_start.setter
    def daily_start(self, value):
        self._daily_start = value
    @property
    def out_bill_url(self):
        return self._out_bill_url

    @out_bill_url.setter
    def out_bill_url(self, value):
        self._out_bill_url = value
    @property
    def service_type(self):
        return self._service_type

    @service_type.setter
    def service_type(self, value):
        self._service_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.billkey_url:
            if hasattr(self.billkey_url, 'to_alipay_dict'):
                params['billkey_url'] = self.billkey_url.to_alipay_dict()
            else:
                params['billkey_url'] = self.billkey_url
        if self.daily_end:
            if hasattr(self.daily_end, 'to_alipay_dict'):
                params['daily_end'] = self.daily_end.to_alipay_dict()
            else:
                params['daily_end'] = self.daily_end
        if self.daily_start:
            if hasattr(self.daily_start, 'to_alipay_dict'):
                params['daily_start'] = self.daily_start.to_alipay_dict()
            else:
                params['daily_start'] = self.daily_start
        if self.out_bill_url:
            if hasattr(self.out_bill_url, 'to_alipay_dict'):
                params['out_bill_url'] = self.out_bill_url.to_alipay_dict()
            else:
                params['out_bill_url'] = self.out_bill_url
        if self.service_type:
            if hasattr(self.service_type, 'to_alipay_dict'):
                params['service_type'] = self.service_type.to_alipay_dict()
            else:
                params['service_type'] = self.service_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CommunityService()
        if 'billkey_url' in d:
            o.billkey_url = d['billkey_url']
        if 'daily_end' in d:
            o.daily_end = d['daily_end']
        if 'daily_start' in d:
            o.daily_start = d['daily_start']
        if 'out_bill_url' in d:
            o.out_bill_url = d['out_bill_url']
        if 'service_type' in d:
            o.service_type = d['service_type']
        return o


