#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaOpenAppKolReportQueryModel(object):

    def __init__(self):
        self._corp_name = None
        self._end_date = None
        self._search_word = None
        self._start_date = None

    @property
    def corp_name(self):
        return self._corp_name

    @corp_name.setter
    def corp_name(self, value):
        self._corp_name = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def search_word(self):
        return self._search_word

    @search_word.setter
    def search_word(self, value):
        self._search_word = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.corp_name:
            if hasattr(self.corp_name, 'to_alipay_dict'):
                params['corp_name'] = self.corp_name.to_alipay_dict()
            else:
                params['corp_name'] = self.corp_name
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.search_word:
            if hasattr(self.search_word, 'to_alipay_dict'):
                params['search_word'] = self.search_word.to_alipay_dict()
            else:
                params['search_word'] = self.search_word
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
        o = ZhimaOpenAppKolReportQueryModel()
        if 'corp_name' in d:
            o.corp_name = d['corp_name']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'search_word' in d:
            o.search_word = d['search_word']
        if 'start_date' in d:
            o.start_date = d['start_date']
        return o


