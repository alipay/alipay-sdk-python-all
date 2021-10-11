#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CollectReceiptQueryOpenApiOrder import CollectReceiptQueryOpenApiOrder


class AlipayBossFncCollectreceiptReceiptQueryModel(object):

    def __init__(self):
        self._collect_receipt_query_open_api_order = None

    @property
    def collect_receipt_query_open_api_order(self):
        return self._collect_receipt_query_open_api_order

    @collect_receipt_query_open_api_order.setter
    def collect_receipt_query_open_api_order(self, value):
        if isinstance(value, CollectReceiptQueryOpenApiOrder):
            self._collect_receipt_query_open_api_order = value
        else:
            self._collect_receipt_query_open_api_order = CollectReceiptQueryOpenApiOrder.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.collect_receipt_query_open_api_order:
            if hasattr(self.collect_receipt_query_open_api_order, 'to_alipay_dict'):
                params['collect_receipt_query_open_api_order'] = self.collect_receipt_query_open_api_order.to_alipay_dict()
            else:
                params['collect_receipt_query_open_api_order'] = self.collect_receipt_query_open_api_order
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncCollectreceiptReceiptQueryModel()
        if 'collect_receipt_query_open_api_order' in d:
            o.collect_receipt_query_open_api_order = d['collect_receipt_query_open_api_order']
        return o


