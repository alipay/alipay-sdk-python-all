#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceAdentitylibraryTmallgoodsCreateModel(object):

    def __init__(self):
        self._async_click_url = None
        self._async_exposure_url = None
        self._goods_id = None
        self._goods_name = None
        self._main_image_url = None
        self._price = None
        self._principal_id = None
        self._principal_oid = None
        self._principal_tag = None
        self._sync_click_url = None

    @property
    def async_click_url(self):
        return self._async_click_url

    @async_click_url.setter
    def async_click_url(self, value):
        self._async_click_url = value
    @property
    def async_exposure_url(self):
        return self._async_exposure_url

    @async_exposure_url.setter
    def async_exposure_url(self, value):
        self._async_exposure_url = value
    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value
    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value
    @property
    def main_image_url(self):
        return self._main_image_url

    @main_image_url.setter
    def main_image_url(self, value):
        self._main_image_url = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value
    @property
    def principal_oid(self):
        return self._principal_oid

    @principal_oid.setter
    def principal_oid(self, value):
        self._principal_oid = value
    @property
    def principal_tag(self):
        return self._principal_tag

    @principal_tag.setter
    def principal_tag(self, value):
        self._principal_tag = value
    @property
    def sync_click_url(self):
        return self._sync_click_url

    @sync_click_url.setter
    def sync_click_url(self, value):
        self._sync_click_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.async_click_url:
            if hasattr(self.async_click_url, 'to_alipay_dict'):
                params['async_click_url'] = self.async_click_url.to_alipay_dict()
            else:
                params['async_click_url'] = self.async_click_url
        if self.async_exposure_url:
            if hasattr(self.async_exposure_url, 'to_alipay_dict'):
                params['async_exposure_url'] = self.async_exposure_url.to_alipay_dict()
            else:
                params['async_exposure_url'] = self.async_exposure_url
        if self.goods_id:
            if hasattr(self.goods_id, 'to_alipay_dict'):
                params['goods_id'] = self.goods_id.to_alipay_dict()
            else:
                params['goods_id'] = self.goods_id
        if self.goods_name:
            if hasattr(self.goods_name, 'to_alipay_dict'):
                params['goods_name'] = self.goods_name.to_alipay_dict()
            else:
                params['goods_name'] = self.goods_name
        if self.main_image_url:
            if hasattr(self.main_image_url, 'to_alipay_dict'):
                params['main_image_url'] = self.main_image_url.to_alipay_dict()
            else:
                params['main_image_url'] = self.main_image_url
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.principal_id:
            if hasattr(self.principal_id, 'to_alipay_dict'):
                params['principal_id'] = self.principal_id.to_alipay_dict()
            else:
                params['principal_id'] = self.principal_id
        if self.principal_oid:
            if hasattr(self.principal_oid, 'to_alipay_dict'):
                params['principal_oid'] = self.principal_oid.to_alipay_dict()
            else:
                params['principal_oid'] = self.principal_oid
        if self.principal_tag:
            if hasattr(self.principal_tag, 'to_alipay_dict'):
                params['principal_tag'] = self.principal_tag.to_alipay_dict()
            else:
                params['principal_tag'] = self.principal_tag
        if self.sync_click_url:
            if hasattr(self.sync_click_url, 'to_alipay_dict'):
                params['sync_click_url'] = self.sync_click_url.to_alipay_dict()
            else:
                params['sync_click_url'] = self.sync_click_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAdentitylibraryTmallgoodsCreateModel()
        if 'async_click_url' in d:
            o.async_click_url = d['async_click_url']
        if 'async_exposure_url' in d:
            o.async_exposure_url = d['async_exposure_url']
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'main_image_url' in d:
            o.main_image_url = d['main_image_url']
        if 'price' in d:
            o.price = d['price']
        if 'principal_id' in d:
            o.principal_id = d['principal_id']
        if 'principal_oid' in d:
            o.principal_oid = d['principal_oid']
        if 'principal_tag' in d:
            o.principal_tag = d['principal_tag']
        if 'sync_click_url' in d:
            o.sync_click_url = d['sync_click_url']
        return o


