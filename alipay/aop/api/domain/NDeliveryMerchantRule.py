#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NDeliveryMerchantInfos import NDeliveryMerchantInfos


class NDeliveryMerchantRule(object):

    def __init__(self):
        self._n_delivery_merchant_infos = None
        self._n_delivery_merchant_mode = None

    @property
    def n_delivery_merchant_infos(self):
        return self._n_delivery_merchant_infos

    @n_delivery_merchant_infos.setter
    def n_delivery_merchant_infos(self, value):
        if isinstance(value, list):
            self._n_delivery_merchant_infos = list()
            for i in value:
                if isinstance(i, NDeliveryMerchantInfos):
                    self._n_delivery_merchant_infos.append(i)
                else:
                    self._n_delivery_merchant_infos.append(NDeliveryMerchantInfos.from_alipay_dict(i))
    @property
    def n_delivery_merchant_mode(self):
        return self._n_delivery_merchant_mode

    @n_delivery_merchant_mode.setter
    def n_delivery_merchant_mode(self, value):
        self._n_delivery_merchant_mode = value


    def to_alipay_dict(self):
        params = dict()
        if self.n_delivery_merchant_infos:
            if isinstance(self.n_delivery_merchant_infos, list):
                for i in range(0, len(self.n_delivery_merchant_infos)):
                    element = self.n_delivery_merchant_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.n_delivery_merchant_infos[i] = element.to_alipay_dict()
            if hasattr(self.n_delivery_merchant_infos, 'to_alipay_dict'):
                params['n_delivery_merchant_infos'] = self.n_delivery_merchant_infos.to_alipay_dict()
            else:
                params['n_delivery_merchant_infos'] = self.n_delivery_merchant_infos
        if self.n_delivery_merchant_mode:
            if hasattr(self.n_delivery_merchant_mode, 'to_alipay_dict'):
                params['n_delivery_merchant_mode'] = self.n_delivery_merchant_mode.to_alipay_dict()
            else:
                params['n_delivery_merchant_mode'] = self.n_delivery_merchant_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NDeliveryMerchantRule()
        if 'n_delivery_merchant_infos' in d:
            o.n_delivery_merchant_infos = d['n_delivery_merchant_infos']
        if 'n_delivery_merchant_mode' in d:
            o.n_delivery_merchant_mode = d['n_delivery_merchant_mode']
        return o


