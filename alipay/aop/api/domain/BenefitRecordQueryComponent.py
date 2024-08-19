#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BenefitRecordQueryComponent(object):

    def __init__(self):
        self._end_query_date = None
        self._ldp_code = None
        self._page_index = None
        self._page_size = None
        self._source = None
        self._start_query_date = None

    @property
    def end_query_date(self):
        return self._end_query_date

    @end_query_date.setter
    def end_query_date(self, value):
        self._end_query_date = value
    @property
    def ldp_code(self):
        return self._ldp_code

    @ldp_code.setter
    def ldp_code(self, value):
        self._ldp_code = value
    @property
    def page_index(self):
        return self._page_index

    @page_index.setter
    def page_index(self, value):
        self._page_index = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def start_query_date(self):
        return self._start_query_date

    @start_query_date.setter
    def start_query_date(self, value):
        self._start_query_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_query_date:
            if hasattr(self.end_query_date, 'to_alipay_dict'):
                params['end_query_date'] = self.end_query_date.to_alipay_dict()
            else:
                params['end_query_date'] = self.end_query_date
        if self.ldp_code:
            if hasattr(self.ldp_code, 'to_alipay_dict'):
                params['ldp_code'] = self.ldp_code.to_alipay_dict()
            else:
                params['ldp_code'] = self.ldp_code
        if self.page_index:
            if hasattr(self.page_index, 'to_alipay_dict'):
                params['page_index'] = self.page_index.to_alipay_dict()
            else:
                params['page_index'] = self.page_index
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.start_query_date:
            if hasattr(self.start_query_date, 'to_alipay_dict'):
                params['start_query_date'] = self.start_query_date.to_alipay_dict()
            else:
                params['start_query_date'] = self.start_query_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitRecordQueryComponent()
        if 'end_query_date' in d:
            o.end_query_date = d['end_query_date']
        if 'ldp_code' in d:
            o.ldp_code = d['ldp_code']
        if 'page_index' in d:
            o.page_index = d['page_index']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'source' in d:
            o.source = d['source']
        if 'start_query_date' in d:
            o.start_query_date = d['start_query_date']
        return o


