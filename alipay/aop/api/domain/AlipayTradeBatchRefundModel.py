#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RefundDetail import RefundDetail


class AlipayTradeBatchRefundModel(object):

    def __init__(self):
        self._batch_no = None
        self._batch_num = None
        self._detail_data = None
        self._refund_date = None
        self._use_freeze_amount = None

    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def batch_num(self):
        return self._batch_num

    @batch_num.setter
    def batch_num(self, value):
        self._batch_num = value
    @property
    def detail_data(self):
        return self._detail_data

    @detail_data.setter
    def detail_data(self, value):
        if isinstance(value, list):
            self._detail_data = list()
            for i in value:
                if isinstance(i, RefundDetail):
                    self._detail_data.append(i)
                else:
                    self._detail_data.append(RefundDetail.from_alipay_dict(i))
    @property
    def refund_date(self):
        return self._refund_date

    @refund_date.setter
    def refund_date(self, value):
        self._refund_date = value
    @property
    def use_freeze_amount(self):
        return self._use_freeze_amount

    @use_freeze_amount.setter
    def use_freeze_amount(self, value):
        self._use_freeze_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.batch_num:
            if hasattr(self.batch_num, 'to_alipay_dict'):
                params['batch_num'] = self.batch_num.to_alipay_dict()
            else:
                params['batch_num'] = self.batch_num
        if self.detail_data:
            if isinstance(self.detail_data, list):
                for i in range(0, len(self.detail_data)):
                    element = self.detail_data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.detail_data[i] = element.to_alipay_dict()
            if hasattr(self.detail_data, 'to_alipay_dict'):
                params['detail_data'] = self.detail_data.to_alipay_dict()
            else:
                params['detail_data'] = self.detail_data
        if self.refund_date:
            if hasattr(self.refund_date, 'to_alipay_dict'):
                params['refund_date'] = self.refund_date.to_alipay_dict()
            else:
                params['refund_date'] = self.refund_date
        if self.use_freeze_amount:
            if hasattr(self.use_freeze_amount, 'to_alipay_dict'):
                params['use_freeze_amount'] = self.use_freeze_amount.to_alipay_dict()
            else:
                params['use_freeze_amount'] = self.use_freeze_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeBatchRefundModel()
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'batch_num' in d:
            o.batch_num = d['batch_num']
        if 'detail_data' in d:
            o.detail_data = d['detail_data']
        if 'refund_date' in d:
            o.refund_date = d['refund_date']
        if 'use_freeze_amount' in d:
            o.use_freeze_amount = d['use_freeze_amount']
        return o


