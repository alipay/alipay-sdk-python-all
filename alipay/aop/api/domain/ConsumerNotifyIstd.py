#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ConsumerNotifyIstd(object):

    def __init__(self):
        self._goods_count = None
        self._goods_img = None
        self._goods_name = None
        self._merchant_mobile = None
        self._merchant_name = None
        self._tiny_app_id = None
        self._tiny_app_url = None

    @property
    def goods_count(self):
        return self._goods_count

    @goods_count.setter
    def goods_count(self, value):
        self._goods_count = value
    @property
    def goods_img(self):
        return self._goods_img

    @goods_img.setter
    def goods_img(self, value):
        self._goods_img = value
    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value
    @property
    def merchant_mobile(self):
        return self._merchant_mobile

    @merchant_mobile.setter
    def merchant_mobile(self, value):
        self._merchant_mobile = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def tiny_app_id(self):
        return self._tiny_app_id

    @tiny_app_id.setter
    def tiny_app_id(self, value):
        self._tiny_app_id = value
    @property
    def tiny_app_url(self):
        return self._tiny_app_url

    @tiny_app_url.setter
    def tiny_app_url(self, value):
        self._tiny_app_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.goods_count:
            if hasattr(self.goods_count, 'to_alipay_dict'):
                params['goods_count'] = self.goods_count.to_alipay_dict()
            else:
                params['goods_count'] = self.goods_count
        if self.goods_img:
            if hasattr(self.goods_img, 'to_alipay_dict'):
                params['goods_img'] = self.goods_img.to_alipay_dict()
            else:
                params['goods_img'] = self.goods_img
        if self.goods_name:
            if hasattr(self.goods_name, 'to_alipay_dict'):
                params['goods_name'] = self.goods_name.to_alipay_dict()
            else:
                params['goods_name'] = self.goods_name
        if self.merchant_mobile:
            if hasattr(self.merchant_mobile, 'to_alipay_dict'):
                params['merchant_mobile'] = self.merchant_mobile.to_alipay_dict()
            else:
                params['merchant_mobile'] = self.merchant_mobile
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.tiny_app_id:
            if hasattr(self.tiny_app_id, 'to_alipay_dict'):
                params['tiny_app_id'] = self.tiny_app_id.to_alipay_dict()
            else:
                params['tiny_app_id'] = self.tiny_app_id
        if self.tiny_app_url:
            if hasattr(self.tiny_app_url, 'to_alipay_dict'):
                params['tiny_app_url'] = self.tiny_app_url.to_alipay_dict()
            else:
                params['tiny_app_url'] = self.tiny_app_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConsumerNotifyIstd()
        if 'goods_count' in d:
            o.goods_count = d['goods_count']
        if 'goods_img' in d:
            o.goods_img = d['goods_img']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'merchant_mobile' in d:
            o.merchant_mobile = d['merchant_mobile']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'tiny_app_id' in d:
            o.tiny_app_id = d['tiny_app_id']
        if 'tiny_app_url' in d:
            o.tiny_app_url = d['tiny_app_url']
        return o


