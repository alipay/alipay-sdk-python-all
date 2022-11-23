#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SelectedBillInfo import SelectedBillInfo


class AlipayEbppBillchargeOrderBatchcreateModel(object):

    def __init__(self):
        self._bill_list = None
        self._open_id = None
        self._out_biz_id = None
        self._source = None
        self._total_pay_amount = None
        self._user_id = None

    @property
    def bill_list(self):
        return self._bill_list

    @bill_list.setter
    def bill_list(self, value):
        if isinstance(value, list):
            self._bill_list = list()
            for i in value:
                if isinstance(i, SelectedBillInfo):
                    self._bill_list.append(i)
                else:
                    self._bill_list.append(SelectedBillInfo.from_alipay_dict(i))
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def total_pay_amount(self):
        return self._total_pay_amount

    @total_pay_amount.setter
    def total_pay_amount(self, value):
        self._total_pay_amount = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_list:
            if isinstance(self.bill_list, list):
                for i in range(0, len(self.bill_list)):
                    element = self.bill_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bill_list[i] = element.to_alipay_dict()
            if hasattr(self.bill_list, 'to_alipay_dict'):
                params['bill_list'] = self.bill_list.to_alipay_dict()
            else:
                params['bill_list'] = self.bill_list
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_biz_id:
            if hasattr(self.out_biz_id, 'to_alipay_dict'):
                params['out_biz_id'] = self.out_biz_id.to_alipay_dict()
            else:
                params['out_biz_id'] = self.out_biz_id
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.total_pay_amount:
            if hasattr(self.total_pay_amount, 'to_alipay_dict'):
                params['total_pay_amount'] = self.total_pay_amount.to_alipay_dict()
            else:
                params['total_pay_amount'] = self.total_pay_amount
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppBillchargeOrderBatchcreateModel()
        if 'bill_list' in d:
            o.bill_list = d['bill_list']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_biz_id' in d:
            o.out_biz_id = d['out_biz_id']
        if 'source' in d:
            o.source = d['source']
        if 'total_pay_amount' in d:
            o.total_pay_amount = d['total_pay_amount']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


