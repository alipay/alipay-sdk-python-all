#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankEcnyBizflowBatchqueryModel(object):

    def __init__(self):
        self._account_no = None
        self._gmt_end = None
        self._gmt_start = None
        self._next_cursor = None
        self._page_size = None
        self._request_no = None
        self._request_scene = None

    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def gmt_end(self):
        return self._gmt_end

    @gmt_end.setter
    def gmt_end(self, value):
        self._gmt_end = value
    @property
    def gmt_start(self):
        return self._gmt_start

    @gmt_start.setter
    def gmt_start(self, value):
        self._gmt_start = value
    @property
    def next_cursor(self):
        return self._next_cursor

    @next_cursor.setter
    def next_cursor(self, value):
        self._next_cursor = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def request_no(self):
        return self._request_no

    @request_no.setter
    def request_no(self, value):
        self._request_no = value
    @property
    def request_scene(self):
        return self._request_scene

    @request_scene.setter
    def request_scene(self, value):
        self._request_scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.gmt_end:
            if hasattr(self.gmt_end, 'to_alipay_dict'):
                params['gmt_end'] = self.gmt_end.to_alipay_dict()
            else:
                params['gmt_end'] = self.gmt_end
        if self.gmt_start:
            if hasattr(self.gmt_start, 'to_alipay_dict'):
                params['gmt_start'] = self.gmt_start.to_alipay_dict()
            else:
                params['gmt_start'] = self.gmt_start
        if self.next_cursor:
            if hasattr(self.next_cursor, 'to_alipay_dict'):
                params['next_cursor'] = self.next_cursor.to_alipay_dict()
            else:
                params['next_cursor'] = self.next_cursor
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.request_no:
            if hasattr(self.request_no, 'to_alipay_dict'):
                params['request_no'] = self.request_no.to_alipay_dict()
            else:
                params['request_no'] = self.request_no
        if self.request_scene:
            if hasattr(self.request_scene, 'to_alipay_dict'):
                params['request_scene'] = self.request_scene.to_alipay_dict()
            else:
                params['request_scene'] = self.request_scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankEcnyBizflowBatchqueryModel()
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'gmt_end' in d:
            o.gmt_end = d['gmt_end']
        if 'gmt_start' in d:
            o.gmt_start = d['gmt_start']
        if 'next_cursor' in d:
            o.next_cursor = d['next_cursor']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'request_no' in d:
            o.request_no = d['request_no']
        if 'request_scene' in d:
            o.request_scene = d['request_scene']
        return o


