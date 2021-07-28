#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandStoreShopserviceDeleteModel(object):

    def __init__(self):
        self._out_biz_no = None
        self._shop_id = None
        self._shop_service_id = None
        self._sku_id = None
        self._store_open_id = None

    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_service_id(self):
        return self._shop_service_id

    @shop_service_id.setter
    def shop_service_id(self, value):
        self._shop_service_id = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def store_open_id(self):
        return self._store_open_id

    @store_open_id.setter
    def store_open_id(self, value):
        self._store_open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.shop_service_id:
            if hasattr(self.shop_service_id, 'to_alipay_dict'):
                params['shop_service_id'] = self.shop_service_id.to_alipay_dict()
            else:
                params['shop_service_id'] = self.shop_service_id
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.store_open_id:
            if hasattr(self.store_open_id, 'to_alipay_dict'):
                params['store_open_id'] = self.store_open_id.to_alipay_dict()
            else:
                params['store_open_id'] = self.store_open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandStoreShopserviceDeleteModel()
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_service_id' in d:
            o.shop_service_id = d['shop_service_id']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'store_open_id' in d:
            o.store_open_id = d['store_open_id']
        return o


