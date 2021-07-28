#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiTradeBillDownloadurlQueryModel(object):

    def __init__(self):
        self._bill_date = None
        self._bill_type = None
        self._date_type = None
        self._file_type = None

    @property
    def bill_date(self):
        return self._bill_date

    @bill_date.setter
    def bill_date(self, value):
        self._bill_date = value
    @property
    def bill_type(self):
        return self._bill_type

    @bill_type.setter
    def bill_type(self, value):
        self._bill_type = value
    @property
    def date_type(self):
        return self._date_type

    @date_type.setter
    def date_type(self, value):
        self._date_type = value
    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_date:
            if hasattr(self.bill_date, 'to_alipay_dict'):
                params['bill_date'] = self.bill_date.to_alipay_dict()
            else:
                params['bill_date'] = self.bill_date
        if self.bill_type:
            if hasattr(self.bill_type, 'to_alipay_dict'):
                params['bill_type'] = self.bill_type.to_alipay_dict()
            else:
                params['bill_type'] = self.bill_type
        if self.date_type:
            if hasattr(self.date_type, 'to_alipay_dict'):
                params['date_type'] = self.date_type.to_alipay_dict()
            else:
                params['date_type'] = self.date_type
        if self.file_type:
            if hasattr(self.file_type, 'to_alipay_dict'):
                params['file_type'] = self.file_type.to_alipay_dict()
            else:
                params['file_type'] = self.file_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiTradeBillDownloadurlQueryModel()
        if 'bill_date' in d:
            o.bill_date = d['bill_date']
        if 'bill_type' in d:
            o.bill_type = d['bill_type']
        if 'date_type' in d:
            o.date_type = d['date_type']
        if 'file_type' in d:
            o.file_type = d['file_type']
        return o


