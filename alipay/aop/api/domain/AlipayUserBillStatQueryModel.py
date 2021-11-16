#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserBillStatQueryModel(object):

    def __init__(self):
        self._begin_date = None
        self._consume_sites = None
        self._end_date = None

    @property
    def begin_date(self):
        return self._begin_date

    @begin_date.setter
    def begin_date(self, value):
        self._begin_date = value
    @property
    def consume_sites(self):
        return self._consume_sites

    @consume_sites.setter
    def consume_sites(self, value):
        if isinstance(value, list):
            self._consume_sites = list()
            for i in value:
                self._consume_sites.append(i)
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.begin_date:
            if hasattr(self.begin_date, 'to_alipay_dict'):
                params['begin_date'] = self.begin_date.to_alipay_dict()
            else:
                params['begin_date'] = self.begin_date
        if self.consume_sites:
            if isinstance(self.consume_sites, list):
                for i in range(0, len(self.consume_sites)):
                    element = self.consume_sites[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.consume_sites[i] = element.to_alipay_dict()
            if hasattr(self.consume_sites, 'to_alipay_dict'):
                params['consume_sites'] = self.consume_sites.to_alipay_dict()
            else:
                params['consume_sites'] = self.consume_sites
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserBillStatQueryModel()
        if 'begin_date' in d:
            o.begin_date = d['begin_date']
        if 'consume_sites' in d:
            o.consume_sites = d['consume_sites']
        if 'end_date' in d:
            o.end_date = d['end_date']
        return o


