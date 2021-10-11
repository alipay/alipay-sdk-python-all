#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApSummaryBillViewQueryOrder import ApSummaryBillViewQueryOrder


class AlipayBossFncGfsettleprodSumapsummarybillQueryModel(object):

    def __init__(self):
        self._ap_summary_bill_view_query_orde = None

    @property
    def ap_summary_bill_view_query_orde(self):
        return self._ap_summary_bill_view_query_orde

    @ap_summary_bill_view_query_orde.setter
    def ap_summary_bill_view_query_orde(self, value):
        if isinstance(value, ApSummaryBillViewQueryOrder):
            self._ap_summary_bill_view_query_orde = value
        else:
            self._ap_summary_bill_view_query_orde = ApSummaryBillViewQueryOrder.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.ap_summary_bill_view_query_orde:
            if hasattr(self.ap_summary_bill_view_query_orde, 'to_alipay_dict'):
                params['ap_summary_bill_view_query_orde'] = self.ap_summary_bill_view_query_orde.to_alipay_dict()
            else:
                params['ap_summary_bill_view_query_orde'] = self.ap_summary_bill_view_query_orde
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncGfsettleprodSumapsummarybillQueryModel()
        if 'ap_summary_bill_view_query_orde' in d:
            o.ap_summary_bill_view_query_orde = d['ap_summary_bill_view_query_orde']
        return o


