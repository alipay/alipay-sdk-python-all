#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShopItemInfo(object):

    def __init__(self):
        self._address = None
        self._category = None
        self._content = None
        self._detail_url = None
        self._floor = None
        self._id = None
        self._mini_app_id = None
        self._open_time = None
        self._operate_time = None
        self._shop_grade = None
        self._shop_name = None
        self._shop_phone_no = None
        self._shop_url = None
        self._status = None
        self._tags = None
        self._title = None
        self._total_sale_number = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, list):
            self._category = list()
            for i in value:
                self._category.append(i)
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def detail_url(self):
        return self._detail_url

    @detail_url.setter
    def detail_url(self, value):
        self._detail_url = value
    @property
    def floor(self):
        return self._floor

    @floor.setter
    def floor(self, value):
        self._floor = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def open_time(self):
        return self._open_time

    @open_time.setter
    def open_time(self, value):
        self._open_time = value
    @property
    def operate_time(self):
        return self._operate_time

    @operate_time.setter
    def operate_time(self, value):
        self._operate_time = value
    @property
    def shop_grade(self):
        return self._shop_grade

    @shop_grade.setter
    def shop_grade(self, value):
        self._shop_grade = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def shop_phone_no(self):
        return self._shop_phone_no

    @shop_phone_no.setter
    def shop_phone_no(self, value):
        self._shop_phone_no = value
    @property
    def shop_url(self):
        return self._shop_url

    @shop_url.setter
    def shop_url(self, value):
        if isinstance(value, list):
            self._shop_url = list()
            for i in value:
                self._shop_url.append(i)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        if isinstance(value, list):
            self._tags = list()
            for i in value:
                self._tags.append(i)
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def total_sale_number(self):
        return self._total_sale_number

    @total_sale_number.setter
    def total_sale_number(self, value):
        self._total_sale_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.category:
            if isinstance(self.category, list):
                for i in range(0, len(self.category)):
                    element = self.category[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.category[i] = element.to_alipay_dict()
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.detail_url:
            if hasattr(self.detail_url, 'to_alipay_dict'):
                params['detail_url'] = self.detail_url.to_alipay_dict()
            else:
                params['detail_url'] = self.detail_url
        if self.floor:
            if hasattr(self.floor, 'to_alipay_dict'):
                params['floor'] = self.floor.to_alipay_dict()
            else:
                params['floor'] = self.floor
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.open_time:
            if hasattr(self.open_time, 'to_alipay_dict'):
                params['open_time'] = self.open_time.to_alipay_dict()
            else:
                params['open_time'] = self.open_time
        if self.operate_time:
            if hasattr(self.operate_time, 'to_alipay_dict'):
                params['operate_time'] = self.operate_time.to_alipay_dict()
            else:
                params['operate_time'] = self.operate_time
        if self.shop_grade:
            if hasattr(self.shop_grade, 'to_alipay_dict'):
                params['shop_grade'] = self.shop_grade.to_alipay_dict()
            else:
                params['shop_grade'] = self.shop_grade
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.shop_phone_no:
            if hasattr(self.shop_phone_no, 'to_alipay_dict'):
                params['shop_phone_no'] = self.shop_phone_no.to_alipay_dict()
            else:
                params['shop_phone_no'] = self.shop_phone_no
        if self.shop_url:
            if isinstance(self.shop_url, list):
                for i in range(0, len(self.shop_url)):
                    element = self.shop_url[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_url[i] = element.to_alipay_dict()
            if hasattr(self.shop_url, 'to_alipay_dict'):
                params['shop_url'] = self.shop_url.to_alipay_dict()
            else:
                params['shop_url'] = self.shop_url
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.tags:
            if isinstance(self.tags, list):
                for i in range(0, len(self.tags)):
                    element = self.tags[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tags[i] = element.to_alipay_dict()
            if hasattr(self.tags, 'to_alipay_dict'):
                params['tags'] = self.tags.to_alipay_dict()
            else:
                params['tags'] = self.tags
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.total_sale_number:
            if hasattr(self.total_sale_number, 'to_alipay_dict'):
                params['total_sale_number'] = self.total_sale_number.to_alipay_dict()
            else:
                params['total_sale_number'] = self.total_sale_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopItemInfo()
        if 'address' in d:
            o.address = d['address']
        if 'category' in d:
            o.category = d['category']
        if 'content' in d:
            o.content = d['content']
        if 'detail_url' in d:
            o.detail_url = d['detail_url']
        if 'floor' in d:
            o.floor = d['floor']
        if 'id' in d:
            o.id = d['id']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'open_time' in d:
            o.open_time = d['open_time']
        if 'operate_time' in d:
            o.operate_time = d['operate_time']
        if 'shop_grade' in d:
            o.shop_grade = d['shop_grade']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_phone_no' in d:
            o.shop_phone_no = d['shop_phone_no']
        if 'shop_url' in d:
            o.shop_url = d['shop_url']
        if 'status' in d:
            o.status = d['status']
        if 'tags' in d:
            o.tags = d['tags']
        if 'title' in d:
            o.title = d['title']
        if 'total_sale_number' in d:
            o.total_sale_number = d['total_sale_number']
        return o


