#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiRetailWmsSupplierreportQueryModel(object):

    def __init__(self):
        self._end_time = None
        self._page_no = None
        self._page_size = None
        self._start_time = None
        self._state = None
        self._supplier_report_id = None
        self._warehouse_code = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
    @property
    def supplier_report_id(self):
        return self._supplier_report_id

    @supplier_report_id.setter
    def supplier_report_id(self, value):
        self._supplier_report_id = value
    @property
    def warehouse_code(self):
        return self._warehouse_code

    @warehouse_code.setter
    def warehouse_code(self, value):
        self._warehouse_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.page_no:
            if hasattr(self.page_no, 'to_alipay_dict'):
                params['page_no'] = self.page_no.to_alipay_dict()
            else:
                params['page_no'] = self.page_no
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.state:
            if hasattr(self.state, 'to_alipay_dict'):
                params['state'] = self.state.to_alipay_dict()
            else:
                params['state'] = self.state
        if self.supplier_report_id:
            if hasattr(self.supplier_report_id, 'to_alipay_dict'):
                params['supplier_report_id'] = self.supplier_report_id.to_alipay_dict()
            else:
                params['supplier_report_id'] = self.supplier_report_id
        if self.warehouse_code:
            if hasattr(self.warehouse_code, 'to_alipay_dict'):
                params['warehouse_code'] = self.warehouse_code.to_alipay_dict()
            else:
                params['warehouse_code'] = self.warehouse_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiRetailWmsSupplierreportQueryModel()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'state' in d:
            o.state = d['state']
        if 'supplier_report_id' in d:
            o.supplier_report_id = d['supplier_report_id']
        if 'warehouse_code' in d:
            o.warehouse_code = d['warehouse_code']
        return o


