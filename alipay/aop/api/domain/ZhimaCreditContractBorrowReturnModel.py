#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditContractBorrowReturnModel(object):

    def __init__(self):
        self._category = None
        self._ext = None
        self._out_trans_no = None
        self._service_id = None
        self._subjects_returned = None

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
    def subjects_returned(self):
        return self._subjects_returned

    @subjects_returned.setter
    def subjects_returned(self, value):
        self._subjects_returned = value


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
        if self.subjects_returned:
            if hasattr(self.subjects_returned, 'to_alipay_dict'):
                params['subjects_returned'] = self.subjects_returned.to_alipay_dict()
            else:
                params['subjects_returned'] = self.subjects_returned
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditContractBorrowReturnModel()
        if 'category' in d:
            o.category = d['category']
        if 'ext' in d:
            o.ext = d['ext']
        if 'out_trans_no' in d:
            o.out_trans_no = d['out_trans_no']
        if 'service_id' in d:
            o.service_id = d['service_id']
        if 'subjects_returned' in d:
            o.subjects_returned = d['subjects_returned']
        return o


