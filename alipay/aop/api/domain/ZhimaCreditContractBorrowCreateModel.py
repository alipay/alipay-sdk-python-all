#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditContractBorrowCreateModel(object):

    def __init__(self):
        self._category = None
        self._ext = None
        self._gmt_borrow = None
        self._gmt_due = None
        self._out_trans_no = None
        self._service_id = None
        self._subjects_borrowed = None

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def ext(self):
        return self._ext

    @ext.setter
    def ext(self, value):
        self._ext = value
    @property
    def gmt_borrow(self):
        return self._gmt_borrow

    @gmt_borrow.setter
    def gmt_borrow(self, value):
        self._gmt_borrow = value
    @property
    def gmt_due(self):
        return self._gmt_due

    @gmt_due.setter
    def gmt_due(self, value):
        self._gmt_due = value
    @property
    def out_trans_no(self):
        return self._out_trans_no

    @out_trans_no.setter
    def out_trans_no(self, value):
        self._out_trans_no = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
    @property
    def subjects_borrowed(self):
        return self._subjects_borrowed

    @subjects_borrowed.setter
    def subjects_borrowed(self, value):
        self._subjects_borrowed = value


    def to_alipay_dict(self):
        params = dict()
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.ext:
            if hasattr(self.ext, 'to_alipay_dict'):
                params['ext'] = self.ext.to_alipay_dict()
            else:
                params['ext'] = self.ext
        if self.gmt_borrow:
            if hasattr(self.gmt_borrow, 'to_alipay_dict'):
                params['gmt_borrow'] = self.gmt_borrow.to_alipay_dict()
            else:
                params['gmt_borrow'] = self.gmt_borrow
        if self.gmt_due:
            if hasattr(self.gmt_due, 'to_alipay_dict'):
                params['gmt_due'] = self.gmt_due.to_alipay_dict()
            else:
                params['gmt_due'] = self.gmt_due
        if self.out_trans_no:
            if hasattr(self.out_trans_no, 'to_alipay_dict'):
                params['out_trans_no'] = self.out_trans_no.to_alipay_dict()
            else:
                params['out_trans_no'] = self.out_trans_no
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        if self.subjects_borrowed:
            if hasattr(self.subjects_borrowed, 'to_alipay_dict'):
                params['subjects_borrowed'] = self.subjects_borrowed.to_alipay_dict()
            else:
                params['subjects_borrowed'] = self.subjects_borrowed
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditContractBorrowCreateModel()
        if 'category' in d:
            o.category = d['category']
        if 'ext' in d:
            o.ext = d['ext']
        if 'gmt_borrow' in d:
            o.gmt_borrow = d['gmt_borrow']
        if 'gmt_due' in d:
            o.gmt_due = d['gmt_due']
        if 'out_trans_no' in d:
            o.out_trans_no = d['out_trans_no']
        if 'service_id' in d:
            o.service_id = d['service_id']
        if 'subjects_borrowed' in d:
            o.subjects_borrowed = d['subjects_borrowed']
        return o


