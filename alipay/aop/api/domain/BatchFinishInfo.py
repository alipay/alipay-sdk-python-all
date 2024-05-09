#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BatchFinishInfo(object):

    def __init__(self):
        self._batch_amount = None
        self._batch_currency = None
        self._batch_id = None
        self._batch_num = None
        self._batch_status = None
        self._batch_type = None
        self._dimension = None
        self._gmt_success = None
        self._out_request_no = None

    @property
    def batch_amount(self):
        return self._batch_amount

    @batch_amount.setter
    def batch_amount(self, value):
        self._batch_amount = value
    @property
    def batch_currency(self):
        return self._batch_currency

    @batch_currency.setter
    def batch_currency(self, value):
        self._batch_currency = value
    @property
    def batch_id(self):
        return self._batch_id

    @batch_id.setter
    def batch_id(self, value):
        self._batch_id = value
    @property
    def batch_num(self):
        return self._batch_num

    @batch_num.setter
    def batch_num(self, value):
        self._batch_num = value
    @property
    def batch_status(self):
        return self._batch_status

    @batch_status.setter
    def batch_status(self, value):
        self._batch_status = value
    @property
    def batch_type(self):
        return self._batch_type

    @batch_type.setter
    def batch_type(self, value):
        self._batch_type = value
    @property
    def dimension(self):
        return self._dimension

    @dimension.setter
    def dimension(self, value):
        self._dimension = value
    @property
    def gmt_success(self):
        return self._gmt_success

    @gmt_success.setter
    def gmt_success(self, value):
        self._gmt_success = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_amount:
            if hasattr(self.batch_amount, 'to_alipay_dict'):
                params['batch_amount'] = self.batch_amount.to_alipay_dict()
            else:
                params['batch_amount'] = self.batch_amount
        if self.batch_currency:
            if hasattr(self.batch_currency, 'to_alipay_dict'):
                params['batch_currency'] = self.batch_currency.to_alipay_dict()
            else:
                params['batch_currency'] = self.batch_currency
        if self.batch_id:
            if hasattr(self.batch_id, 'to_alipay_dict'):
                params['batch_id'] = self.batch_id.to_alipay_dict()
            else:
                params['batch_id'] = self.batch_id
        if self.batch_num:
            if hasattr(self.batch_num, 'to_alipay_dict'):
                params['batch_num'] = self.batch_num.to_alipay_dict()
            else:
                params['batch_num'] = self.batch_num
        if self.batch_status:
            if hasattr(self.batch_status, 'to_alipay_dict'):
                params['batch_status'] = self.batch_status.to_alipay_dict()
            else:
                params['batch_status'] = self.batch_status
        if self.batch_type:
            if hasattr(self.batch_type, 'to_alipay_dict'):
                params['batch_type'] = self.batch_type.to_alipay_dict()
            else:
                params['batch_type'] = self.batch_type
        if self.dimension:
            if hasattr(self.dimension, 'to_alipay_dict'):
                params['dimension'] = self.dimension.to_alipay_dict()
            else:
                params['dimension'] = self.dimension
        if self.gmt_success:
            if hasattr(self.gmt_success, 'to_alipay_dict'):
                params['gmt_success'] = self.gmt_success.to_alipay_dict()
            else:
                params['gmt_success'] = self.gmt_success
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BatchFinishInfo()
        if 'batch_amount' in d:
            o.batch_amount = d['batch_amount']
        if 'batch_currency' in d:
            o.batch_currency = d['batch_currency']
        if 'batch_id' in d:
            o.batch_id = d['batch_id']
        if 'batch_num' in d:
            o.batch_num = d['batch_num']
        if 'batch_status' in d:
            o.batch_status = d['batch_status']
        if 'batch_type' in d:
            o.batch_type = d['batch_type']
        if 'dimension' in d:
            o.dimension = d['dimension']
        if 'gmt_success' in d:
            o.gmt_success = d['gmt_success']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        return o


