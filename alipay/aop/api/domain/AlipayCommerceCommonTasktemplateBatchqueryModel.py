#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceCommonTasktemplateBatchqueryModel(object):

    def __init__(self):
        self._end_time = None
        self._funder_id = None
        self._merchant_pid = None
        self._organizer_id = None
        self._page_no = None
        self._page_size = None
        self._start_time = None
        self._status = None
        self._task_name = None
        self._task_template_ids = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def funder_id(self):
        return self._funder_id

    @funder_id.setter
    def funder_id(self, value):
        self._funder_id = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def organizer_id(self):
        return self._organizer_id

    @organizer_id.setter
    def organizer_id(self, value):
        self._organizer_id = value
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
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def task_name(self):
        return self._task_name

    @task_name.setter
    def task_name(self, value):
        self._task_name = value
    @property
    def task_template_ids(self):
        return self._task_template_ids

    @task_template_ids.setter
    def task_template_ids(self, value):
        if isinstance(value, list):
            self._task_template_ids = list()
            for i in value:
                self._task_template_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.funder_id:
            if hasattr(self.funder_id, 'to_alipay_dict'):
                params['funder_id'] = self.funder_id.to_alipay_dict()
            else:
                params['funder_id'] = self.funder_id
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.organizer_id:
            if hasattr(self.organizer_id, 'to_alipay_dict'):
                params['organizer_id'] = self.organizer_id.to_alipay_dict()
            else:
                params['organizer_id'] = self.organizer_id
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
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.task_name:
            if hasattr(self.task_name, 'to_alipay_dict'):
                params['task_name'] = self.task_name.to_alipay_dict()
            else:
                params['task_name'] = self.task_name
        if self.task_template_ids:
            if isinstance(self.task_template_ids, list):
                for i in range(0, len(self.task_template_ids)):
                    element = self.task_template_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.task_template_ids[i] = element.to_alipay_dict()
            if hasattr(self.task_template_ids, 'to_alipay_dict'):
                params['task_template_ids'] = self.task_template_ids.to_alipay_dict()
            else:
                params['task_template_ids'] = self.task_template_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceCommonTasktemplateBatchqueryModel()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'funder_id' in d:
            o.funder_id = d['funder_id']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'organizer_id' in d:
            o.organizer_id = d['organizer_id']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status' in d:
            o.status = d['status']
        if 'task_name' in d:
            o.task_name = d['task_name']
        if 'task_template_ids' in d:
            o.task_template_ids = d['task_template_ids']
        return o


