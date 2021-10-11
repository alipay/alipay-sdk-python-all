#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApSummaryBillViewQueryOrder import ApSummaryBillViewQueryOrder


class AlipayBossFncGfsettleprodApsummarybillQueryModel(object):

    def __init__(self):
        self._ap_summary_bill_view_query_order = None

    @property
    def ap_summary_bill_view_query_order(self):
        return self._ap_summary_bill_view_query_order

    @ap_summary_bill_view_query_order.setter
    def ap_summary_bill_view_query_order(self, value):
        if isinstance(value, ApSummaryBillViewQueryOrder):
            self._ap_summary_bill_view_query_order = value
        else:
            self._ap_summary_bill_view_query_order = ApSummaryBillViewQueryOrder.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.ap_summary_bill_view_query_order:
            if hasattr(self.ap_summary_bill_view_query_order, 'to_alipay_dict'):
                params['ap_summary_bill_view_query_order'] = self.ap_summary_bill_view_query_order.to_alipay_dict()
            else:
                params['ap_summary_bill_view_query_order'] = self.ap_summary_bill_view_query_order
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncGfsettleprodApsummarybillQueryModel()
        if 'ap_summary_bill_view_query_order' in d:
            o.ap_summary_bill_view_query_order = d['ap_summary_bill_view_query_order']
        return o


