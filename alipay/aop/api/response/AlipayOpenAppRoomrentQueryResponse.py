#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AppItemAttrVO import AppItemAttrVO


class AlipayOpenAppRoomrentQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppRoomrentQueryResponse, self).__init__()
        self._attrs = None
        self._category_id = None
        self._create_time = None
        self._head_img = None
        self._item_id = None
        self._name = None
        self._out_item_id = None
        self._status = None
        self._stock_num = None
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
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def out_item_id(self):
        return self._out_item_id

    @out_item_id.setter
    def out_item_id(self, value):
        self._out_item_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def stock_num(self):
        return self._stock_num

    @stock_num.setter
    def stock_num(self, value):
        self._stock_num = value
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppRoomrentQueryResponse, self).parse_response_content(response_content)
        if 'attrs' in response:
            self.attrs = response['attrs']
        if 'category_id' in response:
            self.category_id = response['category_id']
        if 'create_time' in response:
            self.create_time = response['create_time']
        if 'head_img' in response:
            self.head_img = response['head_img']
        if 'item_id' in response:
            self.item_id = response['item_id']
        if 'name' in response:
            self.name = response['name']
        if 'out_item_id' in response:
            self.out_item_id = response['out_item_id']
        if 'status' in response:
            self.status = response['status']
        if 'stock_num' in response:
            self.stock_num = response['stock_num']
        if 'update_time' in response:
            self.update_time = response['update_time']
