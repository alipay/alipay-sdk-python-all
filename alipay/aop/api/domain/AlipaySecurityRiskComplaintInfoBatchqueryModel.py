#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityRiskComplaintInfoBatchqueryModel(object):

    def __init__(self):
        self._current_page_num = None
        self._gmt_complaint_end = None
        self._gmt_complaint_start = None
        self._gmt_process_end = None
        self._gmt_process_start = None
        self._page_size = None
        self._status_list = None
        self._task_id = None
        self._task_id_list = None
        self._trade_no = None

    @property
    def current_page_num(self):
        return self._current_page_num

    @current_page_num.setter
    def current_page_num(self, value):
        self._current_page_num = value
    @property
    def gmt_complaint_end(self):
        return self._gmt_complaint_end

    @gmt_complaint_end.setter
    def gmt_complaint_end(self, value):
        self._gmt_complaint_end = value
    @property
    def gmt_complaint_start(self):
        return self._gmt_complaint_start

    @gmt_complaint_start.setter
    def gmt_complaint_start(self, value):
        self._gmt_complaint_start = value
    @property
    def gmt_process_end(self):
        return self._gmt_process_end

    @gmt_process_end.setter
    def gmt_process_end(self, value):
        self._gmt_process_end = value
    @property
    def gmt_process_start(self):
        return self._gmt_process_start

    @gmt_process_start.setter
    def gmt_process_start(self, value):
        self._gmt_process_start = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def status_list(self):
        return self._status_list

    @status_list.setter
    def status_list(self, value):
        if isinstance(value, list):
            self._status_list = list()
            for i in value:
                self._status_list.append(i)
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def task_id_list(self):
        return self._task_id_list

    @task_id_list.setter
    def task_id_list(self, value):
        if isinstance(value, list):
            self._task_id_list = list()
            for i in value:
                self._task_id_list.append(i)
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.current_page_num:
            if hasattr(self.current_page_num, 'to_alipay_dict'):
                params['current_page_num'] = self.current_page_num.to_alipay_dict()
            else:
                params['current_page_num'] = self.current_page_num
        if self.gmt_complaint_end:
            if hasattr(self.gmt_complaint_end, 'to_alipay_dict'):
                params['gmt_complaint_end'] = self.gmt_complaint_end.to_alipay_dict()
            else:
                params['gmt_complaint_end'] = self.gmt_complaint_end
        if self.gmt_complaint_start:
            if hasattr(self.gmt_complaint_start, 'to_alipay_dict'):
                params['gmt_complaint_start'] = self.gmt_complaint_start.to_alipay_dict()
            else:
                params['gmt_complaint_start'] = self.gmt_complaint_start
        if self.gmt_process_end:
            if hasattr(self.gmt_process_end, 'to_alipay_dict'):
                params['gmt_process_end'] = self.gmt_process_end.to_alipay_dict()
            else:
                params['gmt_process_end'] = self.gmt_process_end
        if self.gmt_process_start:
            if hasattr(self.gmt_process_start, 'to_alipay_dict'):
                params['gmt_process_start'] = self.gmt_process_start.to_alipay_dict()
            else:
                params['gmt_process_start'] = self.gmt_process_start
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.status_list:
            if isinstance(self.status_list, list):
                for i in range(0, len(self.status_list)):
                    element = self.status_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.status_list[i] = element.to_alipay_dict()
            if hasattr(self.status_list, 'to_alipay_dict'):
                params['status_list'] = self.status_list.to_alipay_dict()
            else:
                params['status_list'] = self.status_list
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        if self.task_id_list:
            if isinstance(self.task_id_list, list):
                for i in range(0, len(self.task_id_list)):
                    element = self.task_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.task_id_list[i] = element.to_alipay_dict()
            if hasattr(self.task_id_list, 'to_alipay_dict'):
                params['task_id_list'] = self.task_id_list.to_alipay_dict()
            else:
                params['task_id_list'] = self.task_id_list
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskComplaintInfoBatchqueryModel()
        if 'current_page_num' in d:
            o.current_page_num = d['current_page_num']
        if 'gmt_complaint_end' in d:
            o.gmt_complaint_end = d['gmt_complaint_end']
        if 'gmt_complaint_start' in d:
            o.gmt_complaint_start = d['gmt_complaint_start']
        if 'gmt_process_end' in d:
            o.gmt_process_end = d['gmt_process_end']
        if 'gmt_process_start' in d:
            o.gmt_process_start = d['gmt_process_start']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'status_list' in d:
            o.status_list = d['status_list']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'task_id_list' in d:
            o.task_id_list = d['task_id_list']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


