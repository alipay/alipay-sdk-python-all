#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CollectReceiptRefundApplyOrder import CollectReceiptRefundApplyOrder


class AlipayBossFncGfsettleprodCollectreceiptRefundModel(object):

    def __init__(self):
        self._collect_receipt_refund_apply_order = None

    @property
    def collect_receipt_refund_apply_order(self):
        return self._collect_receipt_refund_apply_order

    @collect_receipt_refund_apply_order.setter
    def collect_receipt_refund_apply_order(self, value):
        if isinstance(value, CollectReceiptRefundApplyOrder):
            self._collect_receipt_refund_apply_order = value
        else:
            self._collect_receipt_refund_apply_order = CollectReceiptRefundApplyOrder.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.collect_receipt_refund_apply_order:
            if hasattr(self.collect_receipt_refund_apply_order, 'to_alipay_dict'):
                params['collect_receipt_refund_apply_order'] = self.collect_receipt_refund_apply_order.to_alipay_dict()
            else:
                params['collect_receipt_refund_apply_order'] = self.collect_receipt_refund_apply_order
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncGfsettleprodCollectreceiptRefundModel()
        if 'collect_receipt_refund_apply_order' in d:
            o.collect_receipt_refund_apply_order = d['collect_receipt_refund_apply_order']
        return o


