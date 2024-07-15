#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayAccountInstfundAllocationBatchqueryModel(object):

    def __init__(self):
        self._max_gmt_execute_time = None
        self._min_gmt_execute_time = None
        self._out_biz_no = None
        self._page_num = None
        self._page_size = None
        self._status = None

    @property
    def max_gmt_execute_time(self):
        return self._max_gmt_execute_time

    @max_gmt_execute_time.setter
    def max_gmt_execute_time(self, value):
        self._max_gmt_execute_time = value
    @property
    def min_gmt_execute_time(self):
        return self._min_gmt_execute_time

    @min_gmt_execute_time.setter
    def min_gmt_execute_time(self, value):
        self._min_gmt_execute_time = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
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
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.max_gmt_execute_time:
            if hasattr(self.max_gmt_execute_time, 'to_alipay_dict'):
                params['max_gmt_execute_time'] = self.max_gmt_execute_time.to_alipay_dict()
            else:
                params['max_gmt_execute_time'] = self.max_gmt_execute_time
        if self.min_gmt_execute_time:
            if hasattr(self.min_gmt_execute_time, 'to_alipay_dict'):
                params['min_gmt_execute_time'] = self.min_gmt_execute_time.to_alipay_dict()
            else:
                params['min_gmt_execute_time'] = self.min_gmt_execute_time
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
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
        o = AlipayAccountInstfundAllocationBatchqueryModel()
        if 'max_gmt_execute_time' in d:
            o.max_gmt_execute_time = d['max_gmt_execute_time']
        if 'min_gmt_execute_time' in d:
            o.min_gmt_execute_time = d['min_gmt_execute_time']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'status' in d:
            o.status = d['status']
        return o


