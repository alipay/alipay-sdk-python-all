#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ChapterInfo(object):

    def __init__(self):
        self._book_name = None
        self._chapter_id = None
        self._chapter_name = None
        self._chapter_order = None
        self._latest_audit_status = None
        self._out_book_id = None
        self._status = None

    @property
    def book_name(self):
        return self._book_name

    @book_name.setter
    def book_name(self, value):
        self._book_name = value
    @property
    def chapter_id(self):
        return self._chapter_id

    @chapter_id.setter
    def chapter_id(self, value):
        self._chapter_id = value
    @property
    def chapter_name(self):
        return self._chapter_name

    @chapter_name.setter
    def chapter_name(self, value):
        self._chapter_name = value
    @property
    def chapter_order(self):
        return self._chapter_order

    @chapter_order.setter
    def chapter_order(self, value):
        self._chapter_order = value
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
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.book_name:
            if hasattr(self.book_name, 'to_alipay_dict'):
                params['book_name'] = self.book_name.to_alipay_dict()
            else:
                params['book_name'] = self.book_name
        if self.chapter_id:
            if hasattr(self.chapter_id, 'to_alipay_dict'):
                params['chapter_id'] = self.chapter_id.to_alipay_dict()
            else:
                params['chapter_id'] = self.chapter_id
        if self.chapter_name:
            if hasattr(self.chapter_name, 'to_alipay_dict'):
                params['chapter_name'] = self.chapter_name.to_alipay_dict()
            else:
                params['chapter_name'] = self.chapter_name
        if self.chapter_order:
            if hasattr(self.chapter_order, 'to_alipay_dict'):
                params['chapter_order'] = self.chapter_order.to_alipay_dict()
            else:
                params['chapter_order'] = self.chapter_order
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
        o = ChapterInfo()
        if 'book_name' in d:
            o.book_name = d['book_name']
        if 'chapter_id' in d:
            o.chapter_id = d['chapter_id']
        if 'chapter_name' in d:
            o.chapter_name = d['chapter_name']
        if 'chapter_order' in d:
            o.chapter_order = d['chapter_order']
        if 'latest_audit_status' in d:
            o.latest_audit_status = d['latest_audit_status']
        if 'out_book_id' in d:
            o.out_book_id = d['out_book_id']
        if 'status' in d:
            o.status = d['status']
        return o


