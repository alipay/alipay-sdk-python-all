#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ListCallDetailRecordsRequest(object):

    def __init__(self):
        self._agent_id = None
        self._contact_id = None
        self._contact_type = None
        self._end_time = None
        self._order_by_field = None
        self._page_no = None
        self._page_size = None
        self._sort_order = None
        self._start_time = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def contact_id(self):
        return self._contact_id

    @contact_id.setter
    def contact_id(self, value):
        self._contact_id = value
    @property
    def contact_type(self):
        return self._contact_type

    @contact_type.setter
    def contact_type(self, value):
        self._contact_type = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def order_by_field(self):
        return self._order_by_field

    @order_by_field.setter
    def order_by_field(self, value):
        self._order_by_field = value
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
    def sort_order(self):
        return self._sort_order

    @sort_order.setter
    def sort_order(self, value):
        self._sort_order = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
        if self.contact_id:
            if hasattr(self.contact_id, 'to_alipay_dict'):
                params['contact_id'] = self.contact_id.to_alipay_dict()
            else:
                params['contact_id'] = self.contact_id
        if self.contact_type:
            if hasattr(self.contact_type, 'to_alipay_dict'):
                params['contact_type'] = self.contact_type.to_alipay_dict()
            else:
                params['contact_type'] = self.contact_type
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.order_by_field:
            if hasattr(self.order_by_field, 'to_alipay_dict'):
                params['order_by_field'] = self.order_by_field.to_alipay_dict()
            else:
                params['order_by_field'] = self.order_by_field
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
        if self.sort_order:
            if hasattr(self.sort_order, 'to_alipay_dict'):
                params['sort_order'] = self.sort_order.to_alipay_dict()
            else:
                params['sort_order'] = self.sort_order
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
        o = ListCallDetailRecordsRequest()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'contact_id' in d:
            o.contact_id = d['contact_id']
        if 'contact_type' in d:
            o.contact_type = d['contact_type']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'order_by_field' in d:
            o.order_by_field = d['order_by_field']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'sort_order' in d:
            o.sort_order = d['sort_order']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


