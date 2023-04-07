#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherAvailableGoodsInfo(object):

    def __init__(self):
        self._available_goods_sku_ids = None
        self._exclude_goods_sku_ids = None
        self._goods_description = None
        self._goods_detail = None
        self._goods_detail_images = None
        self._goods_detail_rich_description = None
        self._goods_name = None
        self._origin_amount = None

    @property
    def available_goods_sku_ids(self):
        return self._available_goods_sku_ids

    @available_goods_sku_ids.setter
    def available_goods_sku_ids(self, value):
        if isinstance(value, list):
            self._available_goods_sku_ids = list()
            for i in value:
                self._available_goods_sku_ids.append(i)
    @property
    def exclude_goods_sku_ids(self):
        return self._exclude_goods_sku_ids

    @exclude_goods_sku_ids.setter
    def exclude_goods_sku_ids(self, value):
        if isinstance(value, list):
            self._exclude_goods_sku_ids = list()
            for i in value:
                self._exclude_goods_sku_ids.append(i)
    @property
    def goods_description(self):
        return self._goods_description

    @goods_description.setter
    def goods_description(self, value):
        self._goods_description = value
    @property
    def goods_detail(self):
        return self._goods_detail

    @goods_detail.setter
    def goods_detail(self, value):
        self._goods_detail = value
    @property
    def goods_detail_images(self):
        return self._goods_detail_images

    @goods_detail_images.setter
    def goods_detail_images(self, value):
        if isinstance(value, list):
            self._goods_detail_images = list()
            for i in value:
                self._goods_detail_images.append(i)
    @property
    def goods_detail_rich_description(self):
        return self._goods_detail_rich_description

    @goods_detail_rich_description.setter
    def goods_detail_rich_description(self, value):
        self._goods_detail_rich_description = value
    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value
    @property
    def origin_amount(self):
        return self._origin_amount

    @origin_amount.setter
    def origin_amount(self, value):
        self._origin_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.available_goods_sku_ids:
            if isinstance(self.available_goods_sku_ids, list):
                for i in range(0, len(self.available_goods_sku_ids)):
                    element = self.available_goods_sku_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.available_goods_sku_ids[i] = element.to_alipay_dict()
            if hasattr(self.available_goods_sku_ids, 'to_alipay_dict'):
                params['available_goods_sku_ids'] = self.available_goods_sku_ids.to_alipay_dict()
            else:
                params['available_goods_sku_ids'] = self.available_goods_sku_ids
        if self.exclude_goods_sku_ids:
            if isinstance(self.exclude_goods_sku_ids, list):
                for i in range(0, len(self.exclude_goods_sku_ids)):
                    element = self.exclude_goods_sku_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.exclude_goods_sku_ids[i] = element.to_alipay_dict()
            if hasattr(self.exclude_goods_sku_ids, 'to_alipay_dict'):
                params['exclude_goods_sku_ids'] = self.exclude_goods_sku_ids.to_alipay_dict()
            else:
                params['exclude_goods_sku_ids'] = self.exclude_goods_sku_ids
        if self.goods_description:
            if hasattr(self.goods_description, 'to_alipay_dict'):
                params['goods_description'] = self.goods_description.to_alipay_dict()
            else:
                params['goods_description'] = self.goods_description
        if self.goods_detail:
            if hasattr(self.goods_detail, 'to_alipay_dict'):
                params['goods_detail'] = self.goods_detail.to_alipay_dict()
            else:
                params['goods_detail'] = self.goods_detail
        if self.goods_detail_images:
            if isinstance(self.goods_detail_images, list):
                for i in range(0, len(self.goods_detail_images)):
                    element = self.goods_detail_images[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_detail_images[i] = element.to_alipay_dict()
            if hasattr(self.goods_detail_images, 'to_alipay_dict'):
                params['goods_detail_images'] = self.goods_detail_images.to_alipay_dict()
            else:
                params['goods_detail_images'] = self.goods_detail_images
        if self.goods_detail_rich_description:
            if hasattr(self.goods_detail_rich_description, 'to_alipay_dict'):
                params['goods_detail_rich_description'] = self.goods_detail_rich_description.to_alipay_dict()
            else:
                params['goods_detail_rich_description'] = self.goods_detail_rich_description
        if self.goods_name:
            if hasattr(self.goods_name, 'to_alipay_dict'):
                params['goods_name'] = self.goods_name.to_alipay_dict()
            else:
                params['goods_name'] = self.goods_name
        if self.origin_amount:
            if hasattr(self.origin_amount, 'to_alipay_dict'):
                params['origin_amount'] = self.origin_amount.to_alipay_dict()
            else:
                params['origin_amount'] = self.origin_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherAvailableGoodsInfo()
        if 'available_goods_sku_ids' in d:
            o.available_goods_sku_ids = d['available_goods_sku_ids']
        if 'exclude_goods_sku_ids' in d:
            o.exclude_goods_sku_ids = d['exclude_goods_sku_ids']
        if 'goods_description' in d:
            o.goods_description = d['goods_description']
        if 'goods_detail' in d:
            o.goods_detail = d['goods_detail']
        if 'goods_detail_images' in d:
            o.goods_detail_images = d['goods_detail_images']
        if 'goods_detail_rich_description' in d:
            o.goods_detail_rich_description = d['goods_detail_rich_description']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'origin_amount' in d:
            o.origin_amount = d['origin_amount']
        return o


