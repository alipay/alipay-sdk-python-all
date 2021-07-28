#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCampaignPromotionactivityConsumerviewBatchqueryModel(object):

    def __init__(self):
        self._goods_ids = None
        self._merchant_pid = None
        self._only_current_isv = None

    @property
    def goods_ids(self):
        return self._goods_ids

    @goods_ids.setter
    def goods_ids(self, value):
        if isinstance(value, list):
            self._goods_ids = list()
            for i in value:
                self._goods_ids.append(i)
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def only_current_isv(self):
        return self._only_current_isv

    @only_current_isv.setter
    def only_current_isv(self, value):
        self._only_current_isv = value


    def to_alipay_dict(self):
        params = dict()
        if self.goods_ids:
            if isinstance(self.goods_ids, list):
                for i in range(0, len(self.goods_ids)):
                    element = self.goods_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_ids[i] = element.to_alipay_dict()
            if hasattr(self.goods_ids, 'to_alipay_dict'):
                params['goods_ids'] = self.goods_ids.to_alipay_dict()
            else:
                params['goods_ids'] = self.goods_ids
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.only_current_isv:
            if hasattr(self.only_current_isv, 'to_alipay_dict'):
                params['only_current_isv'] = self.only_current_isv.to_alipay_dict()
            else:
                params['only_current_isv'] = self.only_current_isv
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCampaignPromotionactivityConsumerviewBatchqueryModel()
        if 'goods_ids' in d:
            o.goods_ids = d['goods_ids']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'only_current_isv' in d:
            o.only_current_isv = d['only_current_isv']
        return o


