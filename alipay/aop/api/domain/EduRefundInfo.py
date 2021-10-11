#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EduRefundInfo(object):

    def __init__(self):
        self._fund_change = None
        self._isv_order_no = None
        self._out_request_no = None
        self._refund_amount = None
        self._refund_detail_item_list = None
        self._refund_reason = None

    @property
    def fund_change(self):
        return self._fund_change

    @fund_change.setter
    def fund_change(self, value):
        self._fund_change = value
    @property
    def isv_order_no(self):
        return self._isv_order_no

    @isv_order_no.setter
    def isv_order_no(self, value):
        self._isv_order_no = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_detail_item_list(self):
        return self._refund_detail_item_list

    @refund_detail_item_list.setter
    def refund_detail_item_list(self, value):
        self._refund_detail_item_list = value
    @property
    def refund_reason(self):
        return self._refund_reason

    @refund_reason.setter
    def refund_reason(self, value):
        self._refund_reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.fund_change:
            if hasattr(self.fund_change, 'to_alipay_dict'):
                params['fund_change'] = self.fund_change.to_alipay_dict()
            else:
                params['fund_change'] = self.fund_change
        if self.isv_order_no:
            if hasattr(self.isv_order_no, 'to_alipay_dict'):
                params['isv_order_no'] = self.isv_order_no.to_alipay_dict()
            else:
                params['isv_order_no'] = self.isv_order_no
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_detail_item_list:
            if hasattr(self.refund_detail_item_list, 'to_alipay_dict'):
                params['refund_detail_item_list'] = self.refund_detail_item_list.to_alipay_dict()
            else:
                params['refund_detail_item_list'] = self.refund_detail_item_list
        if self.refund_reason:
            if hasattr(self.refund_reason, 'to_alipay_dict'):
                params['refund_reason'] = self.refund_reason.to_alipay_dict()
            else:
                params['refund_reason'] = self.refund_reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EduRefundInfo()
        if 'fund_change' in d:
            o.fund_change = d['fund_change']
        if 'isv_order_no' in d:
            o.isv_order_no = d['isv_order_no']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_detail_item_list' in d:
            o.refund_detail_item_list = d['refund_detail_item_list']
        if 'refund_reason' in d:
            o.refund_reason = d['refund_reason']
        return o


