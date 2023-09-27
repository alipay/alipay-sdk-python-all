#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MpcSkuVO import MpcSkuVO


class MpcItemVO(object):

    def __init__(self):
        self._category_id = None
        self._detail_page_model = None
        self._img_url = None
        self._main_pic = None
        self._mpc_item_id = None
        self._mpc_sku_vo = None
        self._out_item_id = None
        self._path = None
        self._price = None
        self._title = None

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def detail_page_model(self):
        return self._detail_page_model

    @detail_page_model.setter
    def detail_page_model(self, value):
        self._detail_page_model = value
    @property
    def img_url(self):
        return self._img_url

    @img_url.setter
    def img_url(self, value):
        self._img_url = value
    @property
    def main_pic(self):
        return self._main_pic

    @main_pic.setter
    def main_pic(self, value):
        self._main_pic = value
    @property
    def mpc_item_id(self):
        return self._mpc_item_id

    @mpc_item_id.setter
    def mpc_item_id(self, value):
        self._mpc_item_id = value
    @property
    def mpc_sku_vo(self):
        return self._mpc_sku_vo

    @mpc_sku_vo.setter
    def mpc_sku_vo(self, value):
        if isinstance(value, list):
            self._mpc_sku_vo = list()
            for i in value:
                if isinstance(i, MpcSkuVO):
                    self._mpc_sku_vo.append(i)
                else:
                    self._mpc_sku_vo.append(MpcSkuVO.from_alipay_dict(i))
    @property
    def out_item_id(self):
        return self._out_item_id

    @out_item_id.setter
    def out_item_id(self, value):
        self._out_item_id = value
    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.detail_page_model:
            if hasattr(self.detail_page_model, 'to_alipay_dict'):
                params['detail_page_model'] = self.detail_page_model.to_alipay_dict()
            else:
                params['detail_page_model'] = self.detail_page_model
        if self.img_url:
            if hasattr(self.img_url, 'to_alipay_dict'):
                params['img_url'] = self.img_url.to_alipay_dict()
            else:
                params['img_url'] = self.img_url
        if self.main_pic:
            if hasattr(self.main_pic, 'to_alipay_dict'):
                params['main_pic'] = self.main_pic.to_alipay_dict()
            else:
                params['main_pic'] = self.main_pic
        if self.mpc_item_id:
            if hasattr(self.mpc_item_id, 'to_alipay_dict'):
                params['mpc_item_id'] = self.mpc_item_id.to_alipay_dict()
            else:
                params['mpc_item_id'] = self.mpc_item_id
        if self.mpc_sku_vo:
            if isinstance(self.mpc_sku_vo, list):
                for i in range(0, len(self.mpc_sku_vo)):
                    element = self.mpc_sku_vo[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.mpc_sku_vo[i] = element.to_alipay_dict()
            if hasattr(self.mpc_sku_vo, 'to_alipay_dict'):
                params['mpc_sku_vo'] = self.mpc_sku_vo.to_alipay_dict()
            else:
                params['mpc_sku_vo'] = self.mpc_sku_vo
        if self.out_item_id:
            if hasattr(self.out_item_id, 'to_alipay_dict'):
                params['out_item_id'] = self.out_item_id.to_alipay_dict()
            else:
                params['out_item_id'] = self.out_item_id
        if self.path:
            if hasattr(self.path, 'to_alipay_dict'):
                params['path'] = self.path.to_alipay_dict()
            else:
                params['path'] = self.path
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MpcItemVO()
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'detail_page_model' in d:
            o.detail_page_model = d['detail_page_model']
        if 'img_url' in d:
            o.img_url = d['img_url']
        if 'main_pic' in d:
            o.main_pic = d['main_pic']
        if 'mpc_item_id' in d:
            o.mpc_item_id = d['mpc_item_id']
        if 'mpc_sku_vo' in d:
            o.mpc_sku_vo = d['mpc_sku_vo']
        if 'out_item_id' in d:
            o.out_item_id = d['out_item_id']
        if 'path' in d:
            o.path = d['path']
        if 'price' in d:
            o.price = d['price']
        if 'title' in d:
            o.title = d['title']
        return o


