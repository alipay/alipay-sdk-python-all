#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CloudbusTotalOdItem(object):

    def __init__(self):
        self._code = None
        self._message = None
        self._totalod = None
        self._weekend_od = None
        self._workday_od = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value
    @property
    def totalod(self):
        return self._totalod

    @totalod.setter
    def totalod(self, value):
        self._totalod = value
    @property
    def weekend_od(self):
        return self._weekend_od

    @weekend_od.setter
    def weekend_od(self, value):
        self._weekend_od = value
    @property
    def workday_od(self):
        return self._workday_od

    @workday_od.setter
    def workday_od(self, value):
        self._workday_od = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.message:
            if hasattr(self.message, 'to_alipay_dict'):
                params['message'] = self.message.to_alipay_dict()
            else:
                params['message'] = self.message
        if self.totalod:
            if hasattr(self.totalod, 'to_alipay_dict'):
                params['totalod'] = self.totalod.to_alipay_dict()
            else:
                params['totalod'] = self.totalod
        if self.weekend_od:
            if hasattr(self.weekend_od, 'to_alipay_dict'):
                params['weekend_od'] = self.weekend_od.to_alipay_dict()
            else:
                params['weekend_od'] = self.weekend_od
        if self.workday_od:
            if hasattr(self.workday_od, 'to_alipay_dict'):
                params['workday_od'] = self.workday_od.to_alipay_dict()
            else:
                params['workday_od'] = self.workday_od
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CloudbusTotalOdItem()
        if 'code' in d:
            o.code = d['code']
        if 'message' in d:
            o.message = d['message']
        if 'totalod' in d:
            o.totalod = d['totalod']
        if 'weekend_od' in d:
            o.weekend_od = d['weekend_od']
        if 'workday_od' in d:
            o.workday_od = d['workday_od']
        return o


