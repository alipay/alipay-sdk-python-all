#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PurchaseInfo import PurchaseInfo


class RentOfflineShoppingDTO(object):

    def __init__(self):
        self._purchase_infos = None
        self._relate_order_id = None

    @property
    def purchase_infos(self):
        return self._purchase_infos

    @purchase_infos.setter
    def purchase_infos(self, value):
        if isinstance(value, list):
            self._purchase_infos = list()
            for i in value:
                if isinstance(i, PurchaseInfo):
                    self._purchase_infos.append(i)
                else:
                    self._purchase_infos.append(PurchaseInfo.from_alipay_dict(i))
    @property
    def relate_order_id(self):
        return self._relate_order_id

    @relate_order_id.setter
    def relate_order_id(self, value):
        self._relate_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.purchase_infos:
            if isinstance(self.purchase_infos, list):
                for i in range(0, len(self.purchase_infos)):
                    element = self.purchase_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.purchase_infos[i] = element.to_alipay_dict()
            if hasattr(self.purchase_infos, 'to_alipay_dict'):
                params['purchase_infos'] = self.purchase_infos.to_alipay_dict()
            else:
                params['purchase_infos'] = self.purchase_infos
        if self.relate_order_id:
            if hasattr(self.relate_order_id, 'to_alipay_dict'):
                params['relate_order_id'] = self.relate_order_id.to_alipay_dict()
            else:
                params['relate_order_id'] = self.relate_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentOfflineShoppingDTO()
        if 'purchase_infos' in d:
            o.purchase_infos = d['purchase_infos']
        if 'relate_order_id' in d:
            o.relate_order_id = d['relate_order_id']
        return o


