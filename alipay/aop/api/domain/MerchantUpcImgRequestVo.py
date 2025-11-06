#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MerchantUpcImgRequestVo(object):

    def __init__(self):
        self._apply_id = None
        self._goods_upc = None
        self._id = None
        self._img_url = None
        self._is_main = None
        self._merchant_app_id = None
        self._merchant_img_url = None
        self._merchant_pid = None

    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def goods_upc(self):
        return self._goods_upc

    @goods_upc.setter
    def goods_upc(self, value):
        self._goods_upc = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def img_url(self):
        return self._img_url

    @img_url.setter
    def img_url(self, value):
        self._img_url = value
    @property
    def is_main(self):
        return self._is_main

    @is_main.setter
    def is_main(self, value):
        self._is_main = value
    @property
    def merchant_app_id(self):
        return self._merchant_app_id

    @merchant_app_id.setter
    def merchant_app_id(self, value):
        self._merchant_app_id = value
    @property
    def merchant_img_url(self):
        return self._merchant_img_url

    @merchant_img_url.setter
    def merchant_img_url(self, value):
        self._merchant_img_url = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_id:
            if hasattr(self.apply_id, 'to_alipay_dict'):
                params['apply_id'] = self.apply_id.to_alipay_dict()
            else:
                params['apply_id'] = self.apply_id
        if self.goods_upc:
            if hasattr(self.goods_upc, 'to_alipay_dict'):
                params['goods_upc'] = self.goods_upc.to_alipay_dict()
            else:
                params['goods_upc'] = self.goods_upc
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.img_url:
            if hasattr(self.img_url, 'to_alipay_dict'):
                params['img_url'] = self.img_url.to_alipay_dict()
            else:
                params['img_url'] = self.img_url
        if self.is_main:
            if hasattr(self.is_main, 'to_alipay_dict'):
                params['is_main'] = self.is_main.to_alipay_dict()
            else:
                params['is_main'] = self.is_main
        if self.merchant_app_id:
            if hasattr(self.merchant_app_id, 'to_alipay_dict'):
                params['merchant_app_id'] = self.merchant_app_id.to_alipay_dict()
            else:
                params['merchant_app_id'] = self.merchant_app_id
        if self.merchant_img_url:
            if hasattr(self.merchant_img_url, 'to_alipay_dict'):
                params['merchant_img_url'] = self.merchant_img_url.to_alipay_dict()
            else:
                params['merchant_img_url'] = self.merchant_img_url
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantUpcImgRequestVo()
        if 'apply_id' in d:
            o.apply_id = d['apply_id']
        if 'goods_upc' in d:
            o.goods_upc = d['goods_upc']
        if 'id' in d:
            o.id = d['id']
        if 'img_url' in d:
            o.img_url = d['img_url']
        if 'is_main' in d:
            o.is_main = d['is_main']
        if 'merchant_app_id' in d:
            o.merchant_app_id = d['merchant_app_id']
        if 'merchant_img_url' in d:
            o.merchant_img_url = d['merchant_img_url']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        return o


