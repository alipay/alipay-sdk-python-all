#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SummaryBillViewQueryOrder import SummaryBillViewQueryOrder


class AlipayBossFncArsummarybillSummarybillBatchqueryModel(object):

    def __init__(self):
        self._summary_bill_view_query_order = None

    @property
    def summary_bill_view_query_order(self):
        return self._summary_bill_view_query_order

    @summary_bill_view_query_order.setter
    def summary_bill_view_query_order(self, value):
        if isinstance(value, SummaryBillViewQueryOrder):
            self._summary_bill_view_query_order = value
        else:
            self._summary_bill_view_query_order = SummaryBillViewQueryOrder.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.summary_bill_view_query_order:
            if hasattr(self.summary_bill_view_query_order, 'to_alipay_dict'):
                params['summary_bill_view_query_order'] = self.summary_bill_view_query_order.to_alipay_dict()
            else:
                params['summary_bill_view_query_order'] = self.summary_bill_view_query_order
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncArsummarybillSummarybillBatchqueryModel()
        if 'summary_bill_view_query_order' in d:
            o.summary_bill_view_query_order = d['summary_bill_view_query_order']
        return o


