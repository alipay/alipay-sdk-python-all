#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeliveryMerchantInfo import DeliveryMerchantInfo


class DeliveryTargetRule(object):

    def __init__(self):
        self._delivery_merchant_infos = None

    @property
    def delivery_merchant_infos(self):
        return self._delivery_merchant_infos

    @delivery_merchant_infos.setter
    def delivery_merchant_infos(self, value):
        if isinstance(value, list):
            self._delivery_merchant_infos = list()
            for i in value:
                if isinstance(i, DeliveryMerchantInfo):
                    self._delivery_merchant_infos.append(i)
                else:
                    self._delivery_merchant_infos.append(DeliveryMerchantInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_merchant_infos:
            if isinstance(self.delivery_merchant_infos, list):
                for i in range(0, len(self.delivery_merchant_infos)):
                    element = self.delivery_merchant_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.delivery_merchant_infos[i] = element.to_alipay_dict()
            if hasattr(self.delivery_merchant_infos, 'to_alipay_dict'):
                params['delivery_merchant_infos'] = self.delivery_merchant_infos.to_alipay_dict()
            else:
                params['delivery_merchant_infos'] = self.delivery_merchant_infos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliveryTargetRule()
        if 'delivery_merchant_infos' in d:
            o.delivery_merchant_infos = d['delivery_merchant_infos']
        return o


