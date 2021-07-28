#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantShopcodeApplyorderBatchqueryModel(object):

    def __init__(self):
        self._apply_ids = None
        self._end_time = None
        self._merchant_login_ids = None
        self._operator_id = None
        self._page_no = None
        self._page_size = None
        self._request_ids = None
        self._smids = None
        self._start_time = None

    @property
    def apply_ids(self):
        return self._apply_ids

    @apply_ids.setter
    def apply_ids(self, value):
        if isinstance(value, list):
            self._apply_ids = list()
            for i in value:
                self._apply_ids.append(i)
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def merchant_login_ids(self):
        return self._merchant_login_ids

    @merchant_login_ids.setter
    def merchant_login_ids(self, value):
        if isinstance(value, list):
            self._merchant_login_ids = list()
            for i in value:
                self._merchant_login_ids.append(i)
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
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
    def request_ids(self):
        return self._request_ids

    @request_ids.setter
    def request_ids(self, value):
        if isinstance(value, list):
            self._request_ids = list()
            for i in value:
                self._request_ids.append(i)
    @property
    def smids(self):
        return self._smids

    @smids.setter
    def smids(self, value):
        if isinstance(value, list):
            self._smids = list()
            for i in value:
                self._smids.append(i)
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_ids:
            if isinstance(self.apply_ids, list):
                for i in range(0, len(self.apply_ids)):
                    element = self.apply_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.apply_ids[i] = element.to_alipay_dict()
            if hasattr(self.apply_ids, 'to_alipay_dict'):
                params['apply_ids'] = self.apply_ids.to_alipay_dict()
            else:
                params['apply_ids'] = self.apply_ids
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.merchant_login_ids:
            if isinstance(self.merchant_login_ids, list):
                for i in range(0, len(self.merchant_login_ids)):
                    element = self.merchant_login_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.merchant_login_ids[i] = element.to_alipay_dict()
            if hasattr(self.merchant_login_ids, 'to_alipay_dict'):
                params['merchant_login_ids'] = self.merchant_login_ids.to_alipay_dict()
            else:
                params['merchant_login_ids'] = self.merchant_login_ids
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
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
        if self.request_ids:
            if isinstance(self.request_ids, list):
                for i in range(0, len(self.request_ids)):
                    element = self.request_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.request_ids[i] = element.to_alipay_dict()
            if hasattr(self.request_ids, 'to_alipay_dict'):
                params['request_ids'] = self.request_ids.to_alipay_dict()
            else:
                params['request_ids'] = self.request_ids
        if self.smids:
            if isinstance(self.smids, list):
                for i in range(0, len(self.smids)):
                    element = self.smids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.smids[i] = element.to_alipay_dict()
            if hasattr(self.smids, 'to_alipay_dict'):
                params['smids'] = self.smids.to_alipay_dict()
            else:
                params['smids'] = self.smids
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantShopcodeApplyorderBatchqueryModel()
        if 'apply_ids' in d:
            o.apply_ids = d['apply_ids']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'merchant_login_ids' in d:
            o.merchant_login_ids = d['merchant_login_ids']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'request_ids' in d:
            o.request_ids = d['request_ids']
        if 'smids' in d:
            o.smids = d['smids']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


