#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeliveryMerchantInfo import DeliveryMerchantInfo


class DeliveryMerchantRule(object):

    def __init__(self):
        self._brand_id_list = None
        self._delivery_merchant_infos = None
        self._delivery_merchant_mode = None

    @property
    def brand_id_list(self):
        return self._brand_id_list

    @brand_id_list.setter
    def brand_id_list(self, value):
        if isinstance(value, list):
            self._brand_id_list = list()
            for i in value:
                self._brand_id_list.append(i)
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
    @property
    def delivery_merchant_mode(self):
        return self._delivery_merchant_mode

    @delivery_merchant_mode.setter
    def delivery_merchant_mode(self, value):
        self._delivery_merchant_mode = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_id_list:
            if isinstance(self.brand_id_list, list):
                for i in range(0, len(self.brand_id_list)):
                    element = self.brand_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.brand_id_list[i] = element.to_alipay_dict()
            if hasattr(self.brand_id_list, 'to_alipay_dict'):
                params['brand_id_list'] = self.brand_id_list.to_alipay_dict()
            else:
                params['brand_id_list'] = self.brand_id_list
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
        if self.delivery_merchant_mode:
            if hasattr(self.delivery_merchant_mode, 'to_alipay_dict'):
                params['delivery_merchant_mode'] = self.delivery_merchant_mode.to_alipay_dict()
            else:
                params['delivery_merchant_mode'] = self.delivery_merchant_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliveryMerchantRule()
        if 'brand_id_list' in d:
            o.brand_id_list = d['brand_id_list']
        if 'delivery_merchant_infos' in d:
            o.delivery_merchant_infos = d['delivery_merchant_infos']
        if 'delivery_merchant_mode' in d:
            o.delivery_merchant_mode = d['delivery_merchant_mode']
        return o


