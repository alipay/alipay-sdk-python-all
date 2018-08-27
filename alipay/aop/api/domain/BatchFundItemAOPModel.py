#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FundItemAOPModel import FundItemAOPModel


class BatchFundItemAOPModel(object):

    def __init__(self):
        self._batch_no = None
        self._dback_refundtobank_processing_batch_amount = None
        self._dback_refundtobank_success_batch_amount = None
        self._fund_item_list = None
        self._gmt_biz_create_date = None
        self._order_id = None
        self._total_amount = None
        self._total_amount_with_service_fee = None

    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def dback_refundtobank_processing_batch_amount(self):
        return self._dback_refundtobank_processing_batch_amount

    @dback_refundtobank_processing_batch_amount.setter
    def dback_refundtobank_processing_batch_amount(self, value):
        self._dback_refundtobank_processing_batch_amount = value
    @property
    def dback_refundtobank_success_batch_amount(self):
        return self._dback_refundtobank_success_batch_amount

    @dback_refundtobank_success_batch_amount.setter
    def dback_refundtobank_success_batch_amount(self, value):
        self._dback_refundtobank_success_batch_amount = value
    @property
    def fund_item_list(self):
        return self._fund_item_list

    @fund_item_list.setter
    def fund_item_list(self, value):
        if isinstance(value, list):
            self._fund_item_list = list()
            for i in value:
                if isinstance(i, FundItemAOPModel):
                    self._fund_item_list.append(i)
                else:
                    self._fund_item_list.append(FundItemAOPModel.from_alipay_dict(i))
    @property
    def gmt_biz_create_date(self):
        return self._gmt_biz_create_date

    @gmt_biz_create_date.setter
    def gmt_biz_create_date(self, value):
        self._gmt_biz_create_date = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def total_amount_with_service_fee(self):
        return self._total_amount_with_service_fee

    @total_amount_with_service_fee.setter
    def total_amount_with_service_fee(self, value):
        self._total_amount_with_service_fee = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.dback_refundtobank_processing_batch_amount:
            if hasattr(self.dback_refundtobank_processing_batch_amount, 'to_alipay_dict'):
                params['dback_refundtobank_processing_batch_amount'] = self.dback_refundtobank_processing_batch_amount.to_alipay_dict()
            else:
                params['dback_refundtobank_processing_batch_amount'] = self.dback_refundtobank_processing_batch_amount
        if self.dback_refundtobank_success_batch_amount:
            if hasattr(self.dback_refundtobank_success_batch_amount, 'to_alipay_dict'):
                params['dback_refundtobank_success_batch_amount'] = self.dback_refundtobank_success_batch_amount.to_alipay_dict()
            else:
                params['dback_refundtobank_success_batch_amount'] = self.dback_refundtobank_success_batch_amount
        if self.fund_item_list:
            if isinstance(self.fund_item_list, list):
                for i in range(0, len(self.fund_item_list)):
                    element = self.fund_item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fund_item_list[i] = element.to_alipay_dict()
            if hasattr(self.fund_item_list, 'to_alipay_dict'):
                params['fund_item_list'] = self.fund_item_list.to_alipay_dict()
            else:
                params['fund_item_list'] = self.fund_item_list
        if self.gmt_biz_create_date:
            if hasattr(self.gmt_biz_create_date, 'to_alipay_dict'):
                params['gmt_biz_create_date'] = self.gmt_biz_create_date.to_alipay_dict()
            else:
                params['gmt_biz_create_date'] = self.gmt_biz_create_date
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.total_amount_with_service_fee:
            if hasattr(self.total_amount_with_service_fee, 'to_alipay_dict'):
                params['total_amount_with_service_fee'] = self.total_amount_with_service_fee.to_alipay_dict()
            else:
                params['total_amount_with_service_fee'] = self.total_amount_with_service_fee
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BatchFundItemAOPModel()
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'dback_refundtobank_processing_batch_amount' in d:
            o.dback_refundtobank_processing_batch_amount = d['dback_refundtobank_processing_batch_amount']
        if 'dback_refundtobank_success_batch_amount' in d:
            o.dback_refundtobank_success_batch_amount = d['dback_refundtobank_success_batch_amount']
        if 'fund_item_list' in d:
            o.fund_item_list = d['fund_item_list']
        if 'gmt_biz_create_date' in d:
            o.gmt_biz_create_date = d['gmt_biz_create_date']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'total_amount_with_service_fee' in d:
            o.total_amount_with_service_fee = d['total_amount_with_service_fee']
        return o


