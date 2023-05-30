#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeliveryFatigue import DeliveryFatigue


class AntfortuneStockDeliveryFatigueSyncModel(object):

    def __init__(self):
        self._agreement_no = None
        self._delivery_fatigue = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def delivery_fatigue(self):
        return self._delivery_fatigue

    @delivery_fatigue.setter
    def delivery_fatigue(self, value):
        if isinstance(value, list):
            self._delivery_fatigue = list()
            for i in value:
                if isinstance(i, DeliveryFatigue):
                    self._delivery_fatigue.append(i)
                else:
                    self._delivery_fatigue.append(DeliveryFatigue.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.delivery_fatigue:
            if isinstance(self.delivery_fatigue, list):
                for i in range(0, len(self.delivery_fatigue)):
                    element = self.delivery_fatigue[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.delivery_fatigue[i] = element.to_alipay_dict()
            if hasattr(self.delivery_fatigue, 'to_alipay_dict'):
                params['delivery_fatigue'] = self.delivery_fatigue.to_alipay_dict()
            else:
                params['delivery_fatigue'] = self.delivery_fatigue
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneStockDeliveryFatigueSyncModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'delivery_fatigue' in d:
            o.delivery_fatigue = d['delivery_fatigue']
        return o


