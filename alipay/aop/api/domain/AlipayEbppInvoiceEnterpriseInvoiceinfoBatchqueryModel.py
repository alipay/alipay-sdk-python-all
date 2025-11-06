#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceEnterpriseInvoiceinfoBatchqueryModel(object):

    def __init__(self):
        self._employee_id = None
        self._end_time = None
        self._enterprise_id = None
        self._page_num = None
        self._page_size = None
        self._reimburse_status_list = None
        self._start_time = None

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        self._employee_id = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def reimburse_status_list(self):
        return self._reimburse_status_list

    @reimburse_status_list.setter
    def reimburse_status_list(self, value):
        if isinstance(value, list):
            self._reimburse_status_list = list()
            for i in value:
                self._reimburse_status_list.append(i)
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.employee_id:
            if hasattr(self.employee_id, 'to_alipay_dict'):
                params['employee_id'] = self.employee_id.to_alipay_dict()
            else:
                params['employee_id'] = self.employee_id
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.reimburse_status_list:
            if isinstance(self.reimburse_status_list, list):
                for i in range(0, len(self.reimburse_status_list)):
                    element = self.reimburse_status_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.reimburse_status_list[i] = element.to_alipay_dict()
            if hasattr(self.reimburse_status_list, 'to_alipay_dict'):
                params['reimburse_status_list'] = self.reimburse_status_list.to_alipay_dict()
            else:
                params['reimburse_status_list'] = self.reimburse_status_list
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceEnterpriseInvoiceinfoBatchqueryModel()
        if 'employee_id' in d:
            o.employee_id = d['employee_id']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'reimburse_status_list' in d:
            o.reimburse_status_list = d['reimburse_status_list']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


