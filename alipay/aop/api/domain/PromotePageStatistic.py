#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PromotePageStatistic(object):

    def __init__(self):
        self._conversion_cnt = None
        self._page_id = None
        self._page_name = None
        self._pv = None
        self._report_date = None
        self._residence_time = None
        self._uv = None

    @property
    def conversion_cnt(self):
        return self._conversion_cnt

    @conversion_cnt.setter
    def conversion_cnt(self, value):
        self._conversion_cnt = value
    @property
    def page_id(self):
        return self._page_id

    @page_id.setter
    def page_id(self, value):
        self._page_id = value
    @property
    def page_name(self):
        return self._page_name

    @page_name.setter
    def page_name(self, value):
        self._page_name = value
    @property
    def pv(self):
        return self._pv

    @pv.setter
    def pv(self, value):
        self._pv = value
    @property
    def report_date(self):
        return self._report_date

    @report_date.setter
    def report_date(self, value):
        self._report_date = value
    @property
    def residence_time(self):
        return self._residence_time

    @residence_time.setter
    def residence_time(self, value):
        self._residence_time = value
    @property
    def uv(self):
        return self._uv

    @uv.setter
    def uv(self, value):
        self._uv = value


    def to_alipay_dict(self):
        params = dict()
        if self.conversion_cnt:
            if hasattr(self.conversion_cnt, 'to_alipay_dict'):
                params['conversion_cnt'] = self.conversion_cnt.to_alipay_dict()
            else:
                params['conversion_cnt'] = self.conversion_cnt
        if self.page_id:
            if hasattr(self.page_id, 'to_alipay_dict'):
                params['page_id'] = self.page_id.to_alipay_dict()
            else:
                params['page_id'] = self.page_id
        if self.page_name:
            if hasattr(self.page_name, 'to_alipay_dict'):
                params['page_name'] = self.page_name.to_alipay_dict()
            else:
                params['page_name'] = self.page_name
        if self.pv:
            if hasattr(self.pv, 'to_alipay_dict'):
                params['pv'] = self.pv.to_alipay_dict()
            else:
                params['pv'] = self.pv
        if self.report_date:
            if hasattr(self.report_date, 'to_alipay_dict'):
                params['report_date'] = self.report_date.to_alipay_dict()
            else:
                params['report_date'] = self.report_date
        if self.residence_time:
            if hasattr(self.residence_time, 'to_alipay_dict'):
                params['residence_time'] = self.residence_time.to_alipay_dict()
            else:
                params['residence_time'] = self.residence_time
        if self.uv:
            if hasattr(self.uv, 'to_alipay_dict'):
                params['uv'] = self.uv.to_alipay_dict()
            else:
                params['uv'] = self.uv
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PromotePageStatistic()
        if 'conversion_cnt' in d:
            o.conversion_cnt = d['conversion_cnt']
        if 'page_id' in d:
            o.page_id = d['page_id']
        if 'page_name' in d:
            o.page_name = d['page_name']
        if 'pv' in d:
            o.pv = d['pv']
        if 'report_date' in d:
            o.report_date = d['report_date']
        if 'residence_time' in d:
            o.residence_time = d['residence_time']
        if 'uv' in d:
            o.uv = d['uv']
        return o


