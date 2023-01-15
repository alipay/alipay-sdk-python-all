#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PortraitValue import PortraitValue


class PortraitDataVO(object):

    def __init__(self):
        self._coverage = None
        self._data_list = None
        self._portrait_desc = None
        self._portrait_key = None
        self._portrait_name = None
        self._report_date = None

    @property
    def coverage(self):
        return self._coverage

    @coverage.setter
    def coverage(self, value):
        self._coverage = value
    @property
    def data_list(self):
        return self._data_list

    @data_list.setter
    def data_list(self, value):
        if isinstance(value, list):
            self._data_list = list()
            for i in value:
                if isinstance(i, PortraitValue):
                    self._data_list.append(i)
                else:
                    self._data_list.append(PortraitValue.from_alipay_dict(i))
    @property
    def portrait_desc(self):
        return self._portrait_desc

    @portrait_desc.setter
    def portrait_desc(self, value):
        self._portrait_desc = value
    @property
    def portrait_key(self):
        return self._portrait_key

    @portrait_key.setter
    def portrait_key(self, value):
        self._portrait_key = value
    @property
    def portrait_name(self):
        return self._portrait_name

    @portrait_name.setter
    def portrait_name(self, value):
        self._portrait_name = value
    @property
    def report_date(self):
        return self._report_date

    @report_date.setter
    def report_date(self, value):
        self._report_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.coverage:
            if hasattr(self.coverage, 'to_alipay_dict'):
                params['coverage'] = self.coverage.to_alipay_dict()
            else:
                params['coverage'] = self.coverage
        if self.data_list:
            if isinstance(self.data_list, list):
                for i in range(0, len(self.data_list)):
                    element = self.data_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.data_list[i] = element.to_alipay_dict()
            if hasattr(self.data_list, 'to_alipay_dict'):
                params['data_list'] = self.data_list.to_alipay_dict()
            else:
                params['data_list'] = self.data_list
        if self.portrait_desc:
            if hasattr(self.portrait_desc, 'to_alipay_dict'):
                params['portrait_desc'] = self.portrait_desc.to_alipay_dict()
            else:
                params['portrait_desc'] = self.portrait_desc
        if self.portrait_key:
            if hasattr(self.portrait_key, 'to_alipay_dict'):
                params['portrait_key'] = self.portrait_key.to_alipay_dict()
            else:
                params['portrait_key'] = self.portrait_key
        if self.portrait_name:
            if hasattr(self.portrait_name, 'to_alipay_dict'):
                params['portrait_name'] = self.portrait_name.to_alipay_dict()
            else:
                params['portrait_name'] = self.portrait_name
        if self.report_date:
            if hasattr(self.report_date, 'to_alipay_dict'):
                params['report_date'] = self.report_date.to_alipay_dict()
            else:
                params['report_date'] = self.report_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PortraitDataVO()
        if 'coverage' in d:
            o.coverage = d['coverage']
        if 'data_list' in d:
            o.data_list = d['data_list']
        if 'portrait_desc' in d:
            o.portrait_desc = d['portrait_desc']
        if 'portrait_key' in d:
            o.portrait_key = d['portrait_key']
        if 'portrait_name' in d:
            o.portrait_name = d['portrait_name']
        if 'report_date' in d:
            o.report_date = d['report_date']
        return o


