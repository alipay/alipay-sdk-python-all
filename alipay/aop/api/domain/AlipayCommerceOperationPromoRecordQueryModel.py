#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceOperationPromoRecordQueryModel(object):

    def __init__(self):
        self._activity_code = None
        self._page_no = None
        self._page_size = None
        self._query_data = None
        self._query_sub_record = None
        self._round_id = None
        self._subject_id = None
        self._subject_type = None

    @property
    def activity_code(self):
        return self._activity_code

    @activity_code.setter
    def activity_code(self, value):
        self._activity_code = value
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
    def query_data(self):
        return self._query_data

    @query_data.setter
    def query_data(self, value):
        self._query_data = value
    @property
    def query_sub_record(self):
        return self._query_sub_record

    @query_sub_record.setter
    def query_sub_record(self, value):
        self._query_sub_record = value
    @property
    def round_id(self):
        return self._round_id

    @round_id.setter
    def round_id(self, value):
        self._round_id = value
    @property
    def subject_id(self):
        return self._subject_id

    @subject_id.setter
    def subject_id(self, value):
        self._subject_id = value
    @property
    def subject_type(self):
        return self._subject_type

    @subject_type.setter
    def subject_type(self, value):
        self._subject_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_code:
            if hasattr(self.activity_code, 'to_alipay_dict'):
                params['activity_code'] = self.activity_code.to_alipay_dict()
            else:
                params['activity_code'] = self.activity_code
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
        if self.query_data:
            if hasattr(self.query_data, 'to_alipay_dict'):
                params['query_data'] = self.query_data.to_alipay_dict()
            else:
                params['query_data'] = self.query_data
        if self.query_sub_record:
            if hasattr(self.query_sub_record, 'to_alipay_dict'):
                params['query_sub_record'] = self.query_sub_record.to_alipay_dict()
            else:
                params['query_sub_record'] = self.query_sub_record
        if self.round_id:
            if hasattr(self.round_id, 'to_alipay_dict'):
                params['round_id'] = self.round_id.to_alipay_dict()
            else:
                params['round_id'] = self.round_id
        if self.subject_id:
            if hasattr(self.subject_id, 'to_alipay_dict'):
                params['subject_id'] = self.subject_id.to_alipay_dict()
            else:
                params['subject_id'] = self.subject_id
        if self.subject_type:
            if hasattr(self.subject_type, 'to_alipay_dict'):
                params['subject_type'] = self.subject_type.to_alipay_dict()
            else:
                params['subject_type'] = self.subject_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationPromoRecordQueryModel()
        if 'activity_code' in d:
            o.activity_code = d['activity_code']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'query_data' in d:
            o.query_data = d['query_data']
        if 'query_sub_record' in d:
            o.query_sub_record = d['query_sub_record']
        if 'round_id' in d:
            o.round_id = d['round_id']
        if 'subject_id' in d:
            o.subject_id = d['subject_id']
        if 'subject_type' in d:
            o.subject_type = d['subject_type']
        return o


