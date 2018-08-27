#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MedicalHospitalReportList(object):

    def __init__(self):
        self._report_date = None
        self._report_desc = None
        self._report_link = None
        self._report_name = None
        self._report_type = None

    @property
    def report_date(self):
        return self._report_date

    @report_date.setter
    def report_date(self, value):
        self._report_date = value
    @property
    def report_desc(self):
        return self._report_desc

    @report_desc.setter
    def report_desc(self, value):
        self._report_desc = value
    @property
    def report_link(self):
        return self._report_link

    @report_link.setter
    def report_link(self, value):
        self._report_link = value
    @property
    def report_name(self):
        return self._report_name

    @report_name.setter
    def report_name(self, value):
        self._report_name = value
    @property
    def report_type(self):
        return self._report_type

    @report_type.setter
    def report_type(self, value):
        self._report_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.report_date:
            if hasattr(self.report_date, 'to_alipay_dict'):
                params['report_date'] = self.report_date.to_alipay_dict()
            else:
                params['report_date'] = self.report_date
        if self.report_desc:
            if hasattr(self.report_desc, 'to_alipay_dict'):
                params['report_desc'] = self.report_desc.to_alipay_dict()
            else:
                params['report_desc'] = self.report_desc
        if self.report_link:
            if hasattr(self.report_link, 'to_alipay_dict'):
                params['report_link'] = self.report_link.to_alipay_dict()
            else:
                params['report_link'] = self.report_link
        if self.report_name:
            if hasattr(self.report_name, 'to_alipay_dict'):
                params['report_name'] = self.report_name.to_alipay_dict()
            else:
                params['report_name'] = self.report_name
        if self.report_type:
            if hasattr(self.report_type, 'to_alipay_dict'):
                params['report_type'] = self.report_type.to_alipay_dict()
            else:
                params['report_type'] = self.report_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalHospitalReportList()
        if 'report_date' in d:
            o.report_date = d['report_date']
        if 'report_desc' in d:
            o.report_desc = d['report_desc']
        if 'report_link' in d:
            o.report_link = d['report_link']
        if 'report_name' in d:
            o.report_name = d['report_name']
        if 'report_type' in d:
            o.report_type = d['report_type']
        return o


