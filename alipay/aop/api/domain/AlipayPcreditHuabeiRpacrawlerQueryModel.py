#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RpaCrawlerQueryCriteriaVO import RpaCrawlerQueryCriteriaVO


class AlipayPcreditHuabeiRpacrawlerQueryModel(object):

    def __init__(self):
        self._biz_type = None
        self._function_type = None
        self._offset = None
        self._out_biz_no = None
        self._page_size = None
        self._query_criteria = None
        self._sync_task_status = None
        self._task_id = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def function_type(self):
        return self._function_type

    @function_type.setter
    def function_type(self, value):
        self._function_type = value
    @property
    def offset(self):
        return self._offset

    @offset.setter
    def offset(self, value):
        self._offset = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def query_criteria(self):
        return self._query_criteria

    @query_criteria.setter
    def query_criteria(self, value):
        if isinstance(value, list):
            self._query_criteria = list()
            for i in value:
                if isinstance(i, RpaCrawlerQueryCriteriaVO):
                    self._query_criteria.append(i)
                else:
                    self._query_criteria.append(RpaCrawlerQueryCriteriaVO.from_alipay_dict(i))
    @property
    def sync_task_status(self):
        return self._sync_task_status

    @sync_task_status.setter
    def sync_task_status(self, value):
        self._sync_task_status = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.function_type:
            if hasattr(self.function_type, 'to_alipay_dict'):
                params['function_type'] = self.function_type.to_alipay_dict()
            else:
                params['function_type'] = self.function_type
        if self.offset:
            if hasattr(self.offset, 'to_alipay_dict'):
                params['offset'] = self.offset.to_alipay_dict()
            else:
                params['offset'] = self.offset
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.query_criteria:
            if isinstance(self.query_criteria, list):
                for i in range(0, len(self.query_criteria)):
                    element = self.query_criteria[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.query_criteria[i] = element.to_alipay_dict()
            if hasattr(self.query_criteria, 'to_alipay_dict'):
                params['query_criteria'] = self.query_criteria.to_alipay_dict()
            else:
                params['query_criteria'] = self.query_criteria
        if self.sync_task_status:
            if hasattr(self.sync_task_status, 'to_alipay_dict'):
                params['sync_task_status'] = self.sync_task_status.to_alipay_dict()
            else:
                params['sync_task_status'] = self.sync_task_status
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiRpacrawlerQueryModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'function_type' in d:
            o.function_type = d['function_type']
        if 'offset' in d:
            o.offset = d['offset']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'query_criteria' in d:
            o.query_criteria = d['query_criteria']
        if 'sync_task_status' in d:
            o.sync_task_status = d['sync_task_status']
        if 'task_id' in d:
            o.task_id = d['task_id']
        return o


