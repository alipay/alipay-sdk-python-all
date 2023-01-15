#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IndexTrendVO(object):

    def __init__(self):
        self._end_date = None
        self._index_desc = None
        self._index_key = None
        self._index_name = None
        self._index_value = None
        self._report_date = None
        self._start_date = None

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def index_desc(self):
        return self._index_desc

    @index_desc.setter
    def index_desc(self, value):
        self._index_desc = value
    @property
    def index_key(self):
        return self._index_key

    @index_key.setter
    def index_key(self, value):
        self._index_key = value
    @property
    def index_name(self):
        return self._index_name

    @index_name.setter
    def index_name(self, value):
        self._index_name = value
    @property
    def index_value(self):
        return self._index_value

    @index_value.setter
    def index_value(self, value):
        self._index_value = value
    @property
    def report_date(self):
        return self._report_date

    @report_date.setter
    def report_date(self, value):
        self._report_date = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.index_desc:
            if hasattr(self.index_desc, 'to_alipay_dict'):
                params['index_desc'] = self.index_desc.to_alipay_dict()
            else:
                params['index_desc'] = self.index_desc
        if self.index_key:
            if hasattr(self.index_key, 'to_alipay_dict'):
                params['index_key'] = self.index_key.to_alipay_dict()
            else:
                params['index_key'] = self.index_key
        if self.index_name:
            if hasattr(self.index_name, 'to_alipay_dict'):
                params['index_name'] = self.index_name.to_alipay_dict()
            else:
                params['index_name'] = self.index_name
        if self.index_value:
            if hasattr(self.index_value, 'to_alipay_dict'):
                params['index_value'] = self.index_value.to_alipay_dict()
            else:
                params['index_value'] = self.index_value
        if self.report_date:
            if hasattr(self.report_date, 'to_alipay_dict'):
                params['report_date'] = self.report_date.to_alipay_dict()
            else:
                params['report_date'] = self.report_date
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
        o = IndexTrendVO()
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'index_desc' in d:
            o.index_desc = d['index_desc']
        if 'index_key' in d:
            o.index_key = d['index_key']
        if 'index_name' in d:
            o.index_name = d['index_name']
        if 'index_value' in d:
            o.index_value = d['index_value']
        if 'report_date' in d:
            o.report_date = d['report_date']
        if 'start_date' in d:
            o.start_date = d['start_date']
        return o


