#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MerchantPriceRelInfo import MerchantPriceRelInfo
from alipay.aop.api.domain.SettleInMerchantLicense import SettleInMerchantLicense


class AlipayCommerceMerchantcardOpenCreateModel(object):

    def __init__(self):
        self._card_types = None
        self._merchant_name = None
        self._need_auth = None
        self._pid = None
        self._price_infos = None
        self._settle_in_merchant_license = None

    @property
    def card_types(self):
        return self._card_types

    @card_types.setter
    def card_types(self, value):
        if isinstance(value, list):
            self._card_types = list()
            for i in value:
                self._card_types.append(i)
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def need_auth(self):
        return self._need_auth

    @need_auth.setter
    def need_auth(self, value):
        self._need_auth = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def price_infos(self):
        return self._price_infos

    @price_infos.setter
    def price_infos(self, value):
        if isinstance(value, list):
            self._price_infos = list()
            for i in value:
                if isinstance(i, MerchantPriceRelInfo):
                    self._price_infos.append(i)
                else:
                    self._price_infos.append(MerchantPriceRelInfo.from_alipay_dict(i))
    @property
    def settle_in_merchant_license(self):
        return self._settle_in_merchant_license

    @settle_in_merchant_license.setter
    def settle_in_merchant_license(self, value):
        if isinstance(value, SettleInMerchantLicense):
            self._settle_in_merchant_license = value
        else:
            self._settle_in_merchant_license = SettleInMerchantLicense.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.card_types:
            if isinstance(self.card_types, list):
                for i in range(0, len(self.card_types)):
                    element = self.card_types[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.card_types[i] = element.to_alipay_dict()
            if hasattr(self.card_types, 'to_alipay_dict'):
                params['card_types'] = self.card_types.to_alipay_dict()
            else:
                params['card_types'] = self.card_types
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.need_auth:
            if hasattr(self.need_auth, 'to_alipay_dict'):
                params['need_auth'] = self.need_auth.to_alipay_dict()
            else:
                params['need_auth'] = self.need_auth
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.price_infos:
            if isinstance(self.price_infos, list):
                for i in range(0, len(self.price_infos)):
                    element = self.price_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.price_infos[i] = element.to_alipay_dict()
            if hasattr(self.price_infos, 'to_alipay_dict'):
                params['price_infos'] = self.price_infos.to_alipay_dict()
            else:
                params['price_infos'] = self.price_infos
        if self.settle_in_merchant_license:
            if hasattr(self.settle_in_merchant_license, 'to_alipay_dict'):
                params['settle_in_merchant_license'] = self.settle_in_merchant_license.to_alipay_dict()
            else:
                params['settle_in_merchant_license'] = self.settle_in_merchant_license
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMerchantcardOpenCreateModel()
        if 'card_types' in d:
            o.card_types = d['card_types']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'need_auth' in d:
            o.need_auth = d['need_auth']
        if 'pid' in d:
            o.pid = d['pid']
        if 'price_infos' in d:
            o.price_infos = d['price_infos']
        if 'settle_in_merchant_license' in d:
            o.settle_in_merchant_license = d['settle_in_merchant_license']
        return o


