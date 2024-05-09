#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FinSymbolDetail import FinSymbolDetail


class FinAdditionArgs(object):

    def __init__(self):
        self._end_date = None
        self._selected_files = None
        self._start_date = None
        self._symbol_list = None

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def selected_files(self):
        return self._selected_files

    @selected_files.setter
    def selected_files(self, value):
        if isinstance(value, list):
            self._selected_files = list()
            for i in value:
                self._selected_files.append(i)
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def symbol_list(self):
        return self._symbol_list

    @symbol_list.setter
    def symbol_list(self, value):
        if isinstance(value, list):
            self._symbol_list = list()
            for i in value:
                if isinstance(i, FinSymbolDetail):
                    self._symbol_list.append(i)
                else:
                    self._symbol_list.append(FinSymbolDetail.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.selected_files:
            if isinstance(self.selected_files, list):
                for i in range(0, len(self.selected_files)):
                    element = self.selected_files[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.selected_files[i] = element.to_alipay_dict()
            if hasattr(self.selected_files, 'to_alipay_dict'):
                params['selected_files'] = self.selected_files.to_alipay_dict()
            else:
                params['selected_files'] = self.selected_files
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.symbol_list:
            if isinstance(self.symbol_list, list):
                for i in range(0, len(self.symbol_list)):
                    element = self.symbol_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.symbol_list[i] = element.to_alipay_dict()
            if hasattr(self.symbol_list, 'to_alipay_dict'):
                params['symbol_list'] = self.symbol_list.to_alipay_dict()
            else:
                params['symbol_list'] = self.symbol_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FinAdditionArgs()
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'selected_files' in d:
            o.selected_files = d['selected_files']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'symbol_list' in d:
            o.symbol_list = d['symbol_list']
        return o


