#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MerchantShopInfo import MerchantShopInfo


class AlipayOpenInstantdeliveryMerchantshopstatusModifyModel(object):

    def __init__(self):
        self._merchant_shop_infos = None
        self._out_biz_no = None

    @property
    def merchant_shop_infos(self):
        return self._merchant_shop_infos

    @merchant_shop_infos.setter
    def merchant_shop_infos(self, value):
        if isinstance(value, list):
            self._merchant_shop_infos = list()
            for i in value:
                if isinstance(i, MerchantShopInfo):
                    self._merchant_shop_infos.append(i)
                else:
                    self._merchant_shop_infos.append(MerchantShopInfo.from_alipay_dict(i))
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_shop_infos:
            if isinstance(self.merchant_shop_infos, list):
                for i in range(0, len(self.merchant_shop_infos)):
                    element = self.merchant_shop_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.merchant_shop_infos[i] = element.to_alipay_dict()
            if hasattr(self.merchant_shop_infos, 'to_alipay_dict'):
                params['merchant_shop_infos'] = self.merchant_shop_infos.to_alipay_dict()
            else:
                params['merchant_shop_infos'] = self.merchant_shop_infos
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenInstantdeliveryMerchantshopstatusModifyModel()
        if 'merchant_shop_infos' in d:
            o.merchant_shop_infos = d['merchant_shop_infos']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


