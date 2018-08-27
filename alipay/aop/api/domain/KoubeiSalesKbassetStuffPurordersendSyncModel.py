#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AccessPurchaseOrderSend import AccessPurchaseOrderSend


class KoubeiSalesKbassetStuffPurordersendSyncModel(object):

    def __init__(self):
        self._purchase_order_sends = None

    @property
    def purchase_order_sends(self):
        return self._purchase_order_sends

    @purchase_order_sends.setter
    def purchase_order_sends(self, value):
        if isinstance(value, list):
            self._purchase_order_sends = list()
            for i in value:
                if isinstance(i, AccessPurchaseOrderSend):
                    self._purchase_order_sends.append(i)
                else:
                    self._purchase_order_sends.append(AccessPurchaseOrderSend.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.purchase_order_sends:
            if isinstance(self.purchase_order_sends, list):
                for i in range(0, len(self.purchase_order_sends)):
                    element = self.purchase_order_sends[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.purchase_order_sends[i] = element.to_alipay_dict()
            if hasattr(self.purchase_order_sends, 'to_alipay_dict'):
                params['purchase_order_sends'] = self.purchase_order_sends.to_alipay_dict()
            else:
                params['purchase_order_sends'] = self.purchase_order_sends
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiSalesKbassetStuffPurordersendSyncModel()
        if 'purchase_order_sends' in d:
            o.purchase_order_sends = d['purchase_order_sends']
        return o


