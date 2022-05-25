#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeliveryAvailableScope import DeliveryAvailableScope
from alipay.aop.api.domain.DeliveryMerchantInfo import DeliveryMerchantInfo


class DeliveryTargetRule(object):

    def __init__(self):
        self._delivery_available_scope = None
        self._delivery_merchant_infos = None
        self._delivery_promo_tags = None
        self._delivery_recall_mode = None

    @property
    def delivery_available_scope(self):
        return self._delivery_available_scope

    @delivery_available_scope.setter
    def delivery_available_scope(self, value):
        if isinstance(value, DeliveryAvailableScope):
            self._delivery_available_scope = value
        else:
            self._delivery_available_scope = DeliveryAvailableScope.from_alipay_dict(value)
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
    def delivery_promo_tags(self):
        return self._delivery_promo_tags

    @delivery_promo_tags.setter
    def delivery_promo_tags(self, value):
        self._delivery_promo_tags = value
    @property
    def delivery_recall_mode(self):
        return self._delivery_recall_mode

    @delivery_recall_mode.setter
    def delivery_recall_mode(self, value):
        self._delivery_recall_mode = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_available_scope:
            if hasattr(self.delivery_available_scope, 'to_alipay_dict'):
                params['delivery_available_scope'] = self.delivery_available_scope.to_alipay_dict()
            else:
                params['delivery_available_scope'] = self.delivery_available_scope
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
        if self.delivery_promo_tags:
            if hasattr(self.delivery_promo_tags, 'to_alipay_dict'):
                params['delivery_promo_tags'] = self.delivery_promo_tags.to_alipay_dict()
            else:
                params['delivery_promo_tags'] = self.delivery_promo_tags
        if self.delivery_recall_mode:
            if hasattr(self.delivery_recall_mode, 'to_alipay_dict'):
                params['delivery_recall_mode'] = self.delivery_recall_mode.to_alipay_dict()
            else:
                params['delivery_recall_mode'] = self.delivery_recall_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliveryTargetRule()
        if 'delivery_available_scope' in d:
            o.delivery_available_scope = d['delivery_available_scope']
        if 'delivery_merchant_infos' in d:
            o.delivery_merchant_infos = d['delivery_merchant_infos']
        if 'delivery_promo_tags' in d:
            o.delivery_promo_tags = d['delivery_promo_tags']
        if 'delivery_recall_mode' in d:
            o.delivery_recall_mode = d['delivery_recall_mode']
        return o


