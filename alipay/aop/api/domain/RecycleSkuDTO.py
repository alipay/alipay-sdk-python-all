#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecycleSkuAttrDTO import RecycleSkuAttrDTO
from alipay.aop.api.domain.RecycleSkuPriceDTO import RecycleSkuPriceDTO


class RecycleSkuDTO(object):

    def __init__(self):
        self._expired_time = None
        self._sku_attrs = None
        self._sku_price = None
        self._status = None

    @property
    def expired_time(self):
        return self._expired_time

    @expired_time.setter
    def expired_time(self, value):
        self._expired_time = value
    @property
    def sku_attrs(self):
        return self._sku_attrs

    @sku_attrs.setter
    def sku_attrs(self, value):
        if isinstance(value, list):
            self._sku_attrs = list()
            for i in value:
                if isinstance(i, RecycleSkuAttrDTO):
                    self._sku_attrs.append(i)
                else:
                    self._sku_attrs.append(RecycleSkuAttrDTO.from_alipay_dict(i))
    @property
    def sku_price(self):
        return self._sku_price

    @sku_price.setter
    def sku_price(self, value):
        if isinstance(value, RecycleSkuPriceDTO):
            self._sku_price = value
        else:
            self._sku_price = RecycleSkuPriceDTO.from_alipay_dict(value)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.expired_time:
            if hasattr(self.expired_time, 'to_alipay_dict'):
                params['expired_time'] = self.expired_time.to_alipay_dict()
            else:
                params['expired_time'] = self.expired_time
        if self.sku_attrs:
            if isinstance(self.sku_attrs, list):
                for i in range(0, len(self.sku_attrs)):
                    element = self.sku_attrs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sku_attrs[i] = element.to_alipay_dict()
            if hasattr(self.sku_attrs, 'to_alipay_dict'):
                params['sku_attrs'] = self.sku_attrs.to_alipay_dict()
            else:
                params['sku_attrs'] = self.sku_attrs
        if self.sku_price:
            if hasattr(self.sku_price, 'to_alipay_dict'):
                params['sku_price'] = self.sku_price.to_alipay_dict()
            else:
                params['sku_price'] = self.sku_price
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleSkuDTO()
        if 'expired_time' in d:
            o.expired_time = d['expired_time']
        if 'sku_attrs' in d:
            o.sku_attrs = d['sku_attrs']
        if 'sku_price' in d:
            o.sku_price = d['sku_price']
        if 'status' in d:
            o.status = d['status']
        return o


