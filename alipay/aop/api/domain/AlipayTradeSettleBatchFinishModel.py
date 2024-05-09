#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BatchDetailUserInfo import BatchDetailUserInfo


class AlipayTradeSettleBatchFinishModel(object):

    def __init__(self):
        self._batch_amount = None
        self._batch_currency = None
        self._batch_detail_info = None
        self._batch_num = None
        self._batch_type = None
        self._dimension = None
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
    def batch_detail_info(self):
        return self._batch_detail_info

    @batch_detail_info.setter
    def batch_detail_info(self, value):
        if isinstance(value, BatchDetailUserInfo):
            self._batch_detail_info = value
        else:
            self._batch_detail_info = BatchDetailUserInfo.from_alipay_dict(value)
    @property
    def batch_num(self):
        return self._batch_num

    @batch_num.setter
    def batch_num(self, value):
        self._batch_num = value
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
        if self.batch_detail_info:
            if hasattr(self.batch_detail_info, 'to_alipay_dict'):
                params['batch_detail_info'] = self.batch_detail_info.to_alipay_dict()
            else:
                params['batch_detail_info'] = self.batch_detail_info
        if self.batch_num:
            if hasattr(self.batch_num, 'to_alipay_dict'):
                params['batch_num'] = self.batch_num.to_alipay_dict()
            else:
                params['batch_num'] = self.batch_num
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
        o = AlipayTradeSettleBatchFinishModel()
        if 'batch_amount' in d:
            o.batch_amount = d['batch_amount']
        if 'batch_currency' in d:
            o.batch_currency = d['batch_currency']
        if 'batch_detail_info' in d:
            o.batch_detail_info = d['batch_detail_info']
        if 'batch_num' in d:
            o.batch_num = d['batch_num']
        if 'batch_type' in d:
            o.batch_type = d['batch_type']
        if 'dimension' in d:
            o.dimension = d['dimension']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        return o


