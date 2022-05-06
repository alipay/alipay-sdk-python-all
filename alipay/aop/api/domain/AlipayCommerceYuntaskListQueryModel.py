#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceYuntaskListQueryModel(object):

    def __init__(self):
        self._end_time = None
        self._funder_id = None
        self._funder_type = None
        self._organizer_id = None
        self._organizer_type = None
        self._page = None
        self._page_size = None
        self._start_time = None
        self._status = None
        self._task_name = None
        self._task_template_id = None

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
    def funder_type(self):
        return self._funder_type

    @funder_type.setter
    def funder_type(self, value):
        self._funder_type = value
    @property
    def organizer_id(self):
        return self._organizer_id

    @organizer_id.setter
    def organizer_id(self, value):
        self._organizer_id = value
    @property
    def organizer_type(self):
        return self._organizer_type

    @organizer_type.setter
    def organizer_type(self, value):
        self._organizer_type = value
    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value
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
    def task_template_id(self):
        return self._task_template_id

    @task_template_id.setter
    def task_template_id(self, value):
        self._task_template_id = value


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
        if self.funder_type:
            if hasattr(self.funder_type, 'to_alipay_dict'):
                params['funder_type'] = self.funder_type.to_alipay_dict()
            else:
                params['funder_type'] = self.funder_type
        if self.organizer_id:
            if hasattr(self.organizer_id, 'to_alipay_dict'):
                params['organizer_id'] = self.organizer_id.to_alipay_dict()
            else:
                params['organizer_id'] = self.organizer_id
        if self.organizer_type:
            if hasattr(self.organizer_type, 'to_alipay_dict'):
                params['organizer_type'] = self.organizer_type.to_alipay_dict()
            else:
                params['organizer_type'] = self.organizer_type
        if self.page:
            if hasattr(self.page, 'to_alipay_dict'):
                params['page'] = self.page.to_alipay_dict()
            else:
                params['page'] = self.page
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
        if self.task_template_id:
            if hasattr(self.task_template_id, 'to_alipay_dict'):
                params['task_template_id'] = self.task_template_id.to_alipay_dict()
            else:
                params['task_template_id'] = self.task_template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceYuntaskListQueryModel()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'funder_id' in d:
            o.funder_id = d['funder_id']
        if 'funder_type' in d:
            o.funder_type = d['funder_type']
        if 'organizer_id' in d:
            o.organizer_id = d['organizer_id']
        if 'organizer_type' in d:
            o.organizer_type = d['organizer_type']
        if 'page' in d:
            o.page = d['page']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status' in d:
            o.status = d['status']
        if 'task_name' in d:
            o.task_name = d['task_name']
        if 'task_template_id' in d:
            o.task_template_id = d['task_template_id']
        return o


