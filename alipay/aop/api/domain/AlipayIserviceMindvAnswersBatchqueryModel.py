#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceMindvAnswersBatchqueryModel(object):

    def __init__(self):
        self._job_id = None
        self._page_num = None
        self._per_page_size = None
        self._snapshot_id = None
        self._user_id = None
        self._user_type = None

    @property
    def job_id(self):
        return self._job_id

    @job_id.setter
    def job_id(self, value):
        self._job_id = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def per_page_size(self):
        return self._per_page_size

    @per_page_size.setter
    def per_page_size(self, value):
        self._per_page_size = value
    @property
    def snapshot_id(self):
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, value):
        self._snapshot_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, value):
        self._user_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.job_id:
            if hasattr(self.job_id, 'to_alipay_dict'):
                params['job_id'] = self.job_id.to_alipay_dict()
            else:
                params['job_id'] = self.job_id
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.per_page_size:
            if hasattr(self.per_page_size, 'to_alipay_dict'):
                params['per_page_size'] = self.per_page_size.to_alipay_dict()
            else:
                params['per_page_size'] = self.per_page_size
        if self.snapshot_id:
            if hasattr(self.snapshot_id, 'to_alipay_dict'):
                params['snapshot_id'] = self.snapshot_id.to_alipay_dict()
            else:
                params['snapshot_id'] = self.snapshot_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_type:
            if hasattr(self.user_type, 'to_alipay_dict'):
                params['user_type'] = self.user_type.to_alipay_dict()
            else:
                params['user_type'] = self.user_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceMindvAnswersBatchqueryModel()
        if 'job_id' in d:
            o.job_id = d['job_id']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'per_page_size' in d:
            o.per_page_size = d['per_page_size']
        if 'snapshot_id' in d:
            o.snapshot_id = d['snapshot_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_type' in d:
            o.user_type = d['user_type']
        return o


