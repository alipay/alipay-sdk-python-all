#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAntbookcontentChapterQueryModel(object):

    def __init__(self):
        self._latest_audit_status = None
        self._out_book_id = None
        self._page_num = None
        self._page_size = None

    @property
    def latest_audit_status(self):
        return self._latest_audit_status

    @latest_audit_status.setter
    def latest_audit_status(self, value):
        self._latest_audit_status = value
    @property
    def out_book_id(self):
        return self._out_book_id

    @out_book_id.setter
    def out_book_id(self, value):
        self._out_book_id = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.latest_audit_status:
            if hasattr(self.latest_audit_status, 'to_alipay_dict'):
                params['latest_audit_status'] = self.latest_audit_status.to_alipay_dict()
            else:
                params['latest_audit_status'] = self.latest_audit_status
        if self.out_book_id:
            if hasattr(self.out_book_id, 'to_alipay_dict'):
                params['out_book_id'] = self.out_book_id.to_alipay_dict()
            else:
                params['out_book_id'] = self.out_book_id
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAntbookcontentChapterQueryModel()
        if 'latest_audit_status' in d:
            o.latest_audit_status = d['latest_audit_status']
        if 'out_book_id' in d:
            o.out_book_id = d['out_book_id']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o


