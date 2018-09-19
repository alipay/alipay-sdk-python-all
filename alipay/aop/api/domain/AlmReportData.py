#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlmReportData(object):

    def __init__(self):
        self._biz_type = None
        self._date_type = None
        self._report_date = None
        self._report_name = None
        self._report_value = None
        self._sub_biz_type = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def date_type(self):
        return self._date_type

    @date_type.setter
    def date_type(self, value):
        self._date_type = value
    @property
    def report_date(self):
        return self._report_date

    @report_date.setter
    def report_date(self, value):
        self._report_date = value
    @property
    def report_name(self):
        return self._report_name

    @report_name.setter
    def report_name(self, value):
        self._report_name = value
    @property
    def report_value(self):
        return self._report_value

    @report_value.setter
    def report_value(self, value):
        self._report_value = value
    @property
    def sub_biz_type(self):
        return self._sub_biz_type

    @sub_biz_type.setter
    def sub_biz_type(self, value):
        self._sub_biz_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.date_type:
            if hasattr(self.date_type, 'to_alipay_dict'):
                params['date_type'] = self.date_type.to_alipay_dict()
            else:
                params['date_type'] = self.date_type
        if self.report_date:
            if hasattr(self.report_date, 'to_alipay_dict'):
                params['report_date'] = self.report_date.to_alipay_dict()
            else:
                params['report_date'] = self.report_date
        if self.report_name:
            if hasattr(self.report_name, 'to_alipay_dict'):
                params['report_name'] = self.report_name.to_alipay_dict()
            else:
                params['report_name'] = self.report_name
        if self.report_value:
            if hasattr(self.report_value, 'to_alipay_dict'):
                params['report_value'] = self.report_value.to_alipay_dict()
            else:
                params['report_value'] = self.report_value
        if self.sub_biz_type:
            if hasattr(self.sub_biz_type, 'to_alipay_dict'):
                params['sub_biz_type'] = self.sub_biz_type.to_alipay_dict()
            else:
                params['sub_biz_type'] = self.sub_biz_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlmReportData()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'date_type' in d:
            o.date_type = d['date_type']
        if 'report_date' in d:
            o.report_date = d['report_date']
        if 'report_name' in d:
            o.report_name = d['report_name']
        if 'report_value' in d:
            o.report_value = d['report_value']
        if 'sub_biz_type' in d:
            o.sub_biz_type = d['sub_biz_type']
        return o


