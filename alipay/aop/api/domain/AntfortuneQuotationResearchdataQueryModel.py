#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneQuotationResearchdataQueryModel(object):

    def __init__(self):
        self._end_date = None
        self._ext = None
        self._fields = None
        self._opt = None
        self._request_id = None
        self._start_date = None
        self._symbols = None
        self._table = None
        self._target_system = None

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def ext(self):
        return self._ext

    @ext.setter
    def ext(self, value):
        self._ext = value
    @property
    def fields(self):
        return self._fields

    @fields.setter
    def fields(self, value):
        if isinstance(value, list):
            self._fields = list()
            for i in value:
                self._fields.append(i)
    @property
    def opt(self):
        return self._opt

    @opt.setter
    def opt(self, value):
        self._opt = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def symbols(self):
        return self._symbols

    @symbols.setter
    def symbols(self, value):
        if isinstance(value, list):
            self._symbols = list()
            for i in value:
                self._symbols.append(i)
    @property
    def table(self):
        return self._table

    @table.setter
    def table(self, value):
        self._table = value
    @property
    def target_system(self):
        return self._target_system

    @target_system.setter
    def target_system(self, value):
        self._target_system = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.ext:
            if hasattr(self.ext, 'to_alipay_dict'):
                params['ext'] = self.ext.to_alipay_dict()
            else:
                params['ext'] = self.ext
        if self.fields:
            if isinstance(self.fields, list):
                for i in range(0, len(self.fields)):
                    element = self.fields[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fields[i] = element.to_alipay_dict()
            if hasattr(self.fields, 'to_alipay_dict'):
                params['fields'] = self.fields.to_alipay_dict()
            else:
                params['fields'] = self.fields
        if self.opt:
            if hasattr(self.opt, 'to_alipay_dict'):
                params['opt'] = self.opt.to_alipay_dict()
            else:
                params['opt'] = self.opt
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.symbols:
            if isinstance(self.symbols, list):
                for i in range(0, len(self.symbols)):
                    element = self.symbols[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.symbols[i] = element.to_alipay_dict()
            if hasattr(self.symbols, 'to_alipay_dict'):
                params['symbols'] = self.symbols.to_alipay_dict()
            else:
                params['symbols'] = self.symbols
        if self.table:
            if hasattr(self.table, 'to_alipay_dict'):
                params['table'] = self.table.to_alipay_dict()
            else:
                params['table'] = self.table
        if self.target_system:
            if hasattr(self.target_system, 'to_alipay_dict'):
                params['target_system'] = self.target_system.to_alipay_dict()
            else:
                params['target_system'] = self.target_system
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneQuotationResearchdataQueryModel()
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'ext' in d:
            o.ext = d['ext']
        if 'fields' in d:
            o.fields = d['fields']
        if 'opt' in d:
            o.opt = d['opt']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'symbols' in d:
            o.symbols = d['symbols']
        if 'table' in d:
            o.table = d['table']
        if 'target_system' in d:
            o.target_system = d['target_system']
        return o


