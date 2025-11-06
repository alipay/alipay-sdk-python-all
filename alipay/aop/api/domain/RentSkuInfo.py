#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentSkuAttrInfo import RentSkuAttrInfo


class RentSkuInfo(object):

    def __init__(self):
        self._attrs = None
        self._out_sku_id = None
        self._spu_id = None

    @property
    def attrs(self):
        return self._attrs

    @attrs.setter
    def attrs(self, value):
        if isinstance(value, list):
            self._attrs = list()
            for i in value:
                if isinstance(i, RentSkuAttrInfo):
                    self._attrs.append(i)
                else:
                    self._attrs.append(RentSkuAttrInfo.from_alipay_dict(i))
    @property
    def out_sku_id(self):
        return self._out_sku_id

    @out_sku_id.setter
    def out_sku_id(self, value):
        self._out_sku_id = value
    @property
    def spu_id(self):
        return self._spu_id

    @spu_id.setter
    def spu_id(self, value):
        self._spu_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.attrs:
            if isinstance(self.attrs, list):
                for i in range(0, len(self.attrs)):
                    element = self.attrs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attrs[i] = element.to_alipay_dict()
            if hasattr(self.attrs, 'to_alipay_dict'):
                params['attrs'] = self.attrs.to_alipay_dict()
            else:
                params['attrs'] = self.attrs
        if self.out_sku_id:
            if hasattr(self.out_sku_id, 'to_alipay_dict'):
                params['out_sku_id'] = self.out_sku_id.to_alipay_dict()
            else:
                params['out_sku_id'] = self.out_sku_id
        if self.spu_id:
            if hasattr(self.spu_id, 'to_alipay_dict'):
                params['spu_id'] = self.spu_id.to_alipay_dict()
            else:
                params['spu_id'] = self.spu_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentSkuInfo()
        if 'attrs' in d:
            o.attrs = d['attrs']
        if 'out_sku_id' in d:
            o.out_sku_id = d['out_sku_id']
        if 'spu_id' in d:
            o.spu_id = d['spu_id']
        return o


