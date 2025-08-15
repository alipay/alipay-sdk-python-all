#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalEnterprisesubsidyClaimBatchqueryModel(object):

    def __init__(self):
        self._cur_company_id = None
        self._end_datetime = None
        self._father_company_id = None
        self._page_no = None
        self._page_size = None
        self._start_datetime = None

    @property
    def cur_company_id(self):
        return self._cur_company_id

    @cur_company_id.setter
    def cur_company_id(self, value):
        self._cur_company_id = value
    @property
    def end_datetime(self):
        return self._end_datetime

    @end_datetime.setter
    def end_datetime(self, value):
        self._end_datetime = value
    @property
    def father_company_id(self):
        return self._father_company_id

    @father_company_id.setter
    def father_company_id(self, value):
        self._father_company_id = value
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
    def start_datetime(self):
        return self._start_datetime

    @start_datetime.setter
    def start_datetime(self, value):
        self._start_datetime = value


    def to_alipay_dict(self):
        params = dict()
        if self.cur_company_id:
            if hasattr(self.cur_company_id, 'to_alipay_dict'):
                params['cur_company_id'] = self.cur_company_id.to_alipay_dict()
            else:
                params['cur_company_id'] = self.cur_company_id
        if self.end_datetime:
            if hasattr(self.end_datetime, 'to_alipay_dict'):
                params['end_datetime'] = self.end_datetime.to_alipay_dict()
            else:
                params['end_datetime'] = self.end_datetime
        if self.father_company_id:
            if hasattr(self.father_company_id, 'to_alipay_dict'):
                params['father_company_id'] = self.father_company_id.to_alipay_dict()
            else:
                params['father_company_id'] = self.father_company_id
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
        if self.start_datetime:
            if hasattr(self.start_datetime, 'to_alipay_dict'):
                params['start_datetime'] = self.start_datetime.to_alipay_dict()
            else:
                params['start_datetime'] = self.start_datetime
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalEnterprisesubsidyClaimBatchqueryModel()
        if 'cur_company_id' in d:
            o.cur_company_id = d['cur_company_id']
        if 'end_datetime' in d:
            o.end_datetime = d['end_datetime']
        if 'father_company_id' in d:
            o.father_company_id = d['father_company_id']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'start_datetime' in d:
            o.start_datetime = d['start_datetime']
        return o


