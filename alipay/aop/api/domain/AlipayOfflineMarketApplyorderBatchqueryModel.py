#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineMarketApplyorderBatchqueryModel(object):

    def __init__(self):
        self._action = None
        self._apply_ids = None
        self._biz_id = None
        self._biz_type = None
        self._end_time = None
        self._op_id = None
        self._op_role = None
        self._page_no = None
        self._page_size = None
        self._request_ids = None
        self._start_time = None
        self._status = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def apply_ids(self):
        return self._apply_ids

    @apply_ids.setter
    def apply_ids(self, value):
        if isinstance(value, list):
            self._apply_ids = list()
            for i in value:
                self._apply_ids.append(i)
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def op_id(self):
        return self._op_id

    @op_id.setter
    def op_id(self, value):
        self._op_id = value
    @property
    def op_role(self):
        return self._op_role

    @op_role.setter
    def op_role(self, value):
        self._op_role = value
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
    def request_ids(self):
        return self._request_ids

    @request_ids.setter
    def request_ids(self, value):
        if isinstance(value, list):
            self._request_ids = list()
            for i in value:
                self._request_ids.append(i)
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


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.apply_ids:
            if isinstance(self.apply_ids, list):
                for i in range(0, len(self.apply_ids)):
                    element = self.apply_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.apply_ids[i] = element.to_alipay_dict()
            if hasattr(self.apply_ids, 'to_alipay_dict'):
                params['apply_ids'] = self.apply_ids.to_alipay_dict()
            else:
                params['apply_ids'] = self.apply_ids
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.op_id:
            if hasattr(self.op_id, 'to_alipay_dict'):
                params['op_id'] = self.op_id.to_alipay_dict()
            else:
                params['op_id'] = self.op_id
        if self.op_role:
            if hasattr(self.op_role, 'to_alipay_dict'):
                params['op_role'] = self.op_role.to_alipay_dict()
            else:
                params['op_role'] = self.op_role
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
        if self.request_ids:
            if isinstance(self.request_ids, list):
                for i in range(0, len(self.request_ids)):
                    element = self.request_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.request_ids[i] = element.to_alipay_dict()
            if hasattr(self.request_ids, 'to_alipay_dict'):
                params['request_ids'] = self.request_ids.to_alipay_dict()
            else:
                params['request_ids'] = self.request_ids
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineMarketApplyorderBatchqueryModel()
        if 'action' in d:
            o.action = d['action']
        if 'apply_ids' in d:
            o.apply_ids = d['apply_ids']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'op_id' in d:
            o.op_id = d['op_id']
        if 'op_role' in d:
            o.op_role = d['op_role']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'request_ids' in d:
            o.request_ids = d['request_ids']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status' in d:
            o.status = d['status']
        return o


