#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AppItemAttrVO import AppItemAttrVO
from alipay.aop.api.domain.LocalItemSkuQueryVO import LocalItemSkuQueryVO


class AlipayOpenAppLocalitemQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppLocalitemQueryResponse, self).__init__()
        self._attrs = None
        self._category_id = None
        self._create_time = None
        self._head_img = None
        self._image_list = None
        self._is_online = None
        self._item_id = None
        self._item_type = None
        self._out_item_id = None
        self._path = None
        self._skus = None
        self._spu_status = None
        self._stock_num = None
        self._title = None
        self._update_time = None

    @property
    def attrs(self):
        return self._attrs

    @attrs.setter
    def attrs(self, value):
        if isinstance(value, AppItemAttrVO):
            self._attrs = value
        else:
            self._attrs = AppItemAttrVO.from_alipay_dict(value)
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def head_img(self):
        return self._head_img

    @head_img.setter
    def head_img(self, value):
        self._head_img = value
    @property
    def image_list(self):
        return self._image_list

    @image_list.setter
    def image_list(self, value):
        if isinstance(value, list):
            self._image_list = list()
            for i in value:
                self._image_list.append(i)
    @property
    def is_online(self):
        return self._is_online

    @is_online.setter
    def is_online(self, value):
        self._is_online = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, value):
        self._item_type = value
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
    def skus(self):
        return self._skus

    @skus.setter
    def skus(self, value):
        if isinstance(value, list):
            self._skus = list()
            for i in value:
                if isinstance(i, LocalItemSkuQueryVO):
                    self._skus.append(i)
                else:
                    self._skus.append(LocalItemSkuQueryVO.from_alipay_dict(i))
    @property
    def spu_status(self):
        return self._spu_status

    @spu_status.setter
    def spu_status(self, value):
        self._spu_status = value
    @property
    def stock_num(self):
        return self._stock_num

    @stock_num.setter
    def stock_num(self, value):
        self._stock_num = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppLocalitemQueryResponse, self).parse_response_content(response_content)
        if 'attrs' in response:
            self.attrs = response['attrs']
        if 'category_id' in response:
            self.category_id = response['category_id']
        if 'create_time' in response:
            self.create_time = response['create_time']
        if 'head_img' in response:
            self.head_img = response['head_img']
        if 'image_list' in response:
            self.image_list = response['image_list']
        if 'is_online' in response:
            self.is_online = response['is_online']
        if 'item_id' in response:
            self.item_id = response['item_id']
        if 'item_type' in response:
            self.item_type = response['item_type']
        if 'out_item_id' in response:
            self.out_item_id = response['out_item_id']
        if 'path' in response:
            self.path = response['path']
        if 'skus' in response:
            self.skus = response['skus']
        if 'spu_status' in response:
            self.spu_status = response['spu_status']
        if 'stock_num' in response:
            self.stock_num = response['stock_num']
        if 'title' in response:
            self.title = response['title']
        if 'update_time' in response:
            self.update_time = response['update_time']
