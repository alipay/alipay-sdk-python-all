#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DanmuGameUserInfo import DanmuGameUserInfo


class DanmuGameData(object):

    def __init__(self):
        self._content = None
        self._content_list = None
        self._count = None
        self._gift_count = None
        self._gift_id = None
        self._gift_name = None
        self._gift_total_price = None
        self._gift_unit_price = None
        self._head_url = None
        self._open_id = None
        self._unique_no = None
        self._user_info = None
        self._user_name = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if isinstance(value, list):
            self._content = list()
            for i in value:
                self._content.append(i)
    @property
    def content_list(self):
        return self._content_list

    @content_list.setter
    def content_list(self, value):
        if isinstance(value, list):
            self._content_list = list()
            for i in value:
                self._content_list.append(i)
    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def gift_count(self):
        return self._gift_count

    @gift_count.setter
    def gift_count(self, value):
        self._gift_count = value
    @property
    def gift_id(self):
        return self._gift_id

    @gift_id.setter
    def gift_id(self, value):
        self._gift_id = value
    @property
    def gift_name(self):
        return self._gift_name

    @gift_name.setter
    def gift_name(self, value):
        self._gift_name = value
    @property
    def gift_total_price(self):
        return self._gift_total_price

    @gift_total_price.setter
    def gift_total_price(self, value):
        self._gift_total_price = value
    @property
    def gift_unit_price(self):
        return self._gift_unit_price

    @gift_unit_price.setter
    def gift_unit_price(self, value):
        self._gift_unit_price = value
    @property
    def head_url(self):
        return self._head_url

    @head_url.setter
    def head_url(self, value):
        self._head_url = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def unique_no(self):
        return self._unique_no

    @unique_no.setter
    def unique_no(self, value):
        self._unique_no = value
    @property
    def user_info(self):
        return self._user_info

    @user_info.setter
    def user_info(self, value):
        if isinstance(value, DanmuGameUserInfo):
            self._user_info = value
        else:
            self._user_info = DanmuGameUserInfo.from_alipay_dict(value)
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if isinstance(self.content, list):
                for i in range(0, len(self.content)):
                    element = self.content[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.content[i] = element.to_alipay_dict()
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.content_list:
            if isinstance(self.content_list, list):
                for i in range(0, len(self.content_list)):
                    element = self.content_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.content_list[i] = element.to_alipay_dict()
            if hasattr(self.content_list, 'to_alipay_dict'):
                params['content_list'] = self.content_list.to_alipay_dict()
            else:
                params['content_list'] = self.content_list
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        if self.gift_count:
            if hasattr(self.gift_count, 'to_alipay_dict'):
                params['gift_count'] = self.gift_count.to_alipay_dict()
            else:
                params['gift_count'] = self.gift_count
        if self.gift_id:
            if hasattr(self.gift_id, 'to_alipay_dict'):
                params['gift_id'] = self.gift_id.to_alipay_dict()
            else:
                params['gift_id'] = self.gift_id
        if self.gift_name:
            if hasattr(self.gift_name, 'to_alipay_dict'):
                params['gift_name'] = self.gift_name.to_alipay_dict()
            else:
                params['gift_name'] = self.gift_name
        if self.gift_total_price:
            if hasattr(self.gift_total_price, 'to_alipay_dict'):
                params['gift_total_price'] = self.gift_total_price.to_alipay_dict()
            else:
                params['gift_total_price'] = self.gift_total_price
        if self.gift_unit_price:
            if hasattr(self.gift_unit_price, 'to_alipay_dict'):
                params['gift_unit_price'] = self.gift_unit_price.to_alipay_dict()
            else:
                params['gift_unit_price'] = self.gift_unit_price
        if self.head_url:
            if hasattr(self.head_url, 'to_alipay_dict'):
                params['head_url'] = self.head_url.to_alipay_dict()
            else:
                params['head_url'] = self.head_url
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.unique_no:
            if hasattr(self.unique_no, 'to_alipay_dict'):
                params['unique_no'] = self.unique_no.to_alipay_dict()
            else:
                params['unique_no'] = self.unique_no
        if self.user_info:
            if hasattr(self.user_info, 'to_alipay_dict'):
                params['user_info'] = self.user_info.to_alipay_dict()
            else:
                params['user_info'] = self.user_info
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DanmuGameData()
        if 'content' in d:
            o.content = d['content']
        if 'content_list' in d:
            o.content_list = d['content_list']
        if 'count' in d:
            o.count = d['count']
        if 'gift_count' in d:
            o.gift_count = d['gift_count']
        if 'gift_id' in d:
            o.gift_id = d['gift_id']
        if 'gift_name' in d:
            o.gift_name = d['gift_name']
        if 'gift_total_price' in d:
            o.gift_total_price = d['gift_total_price']
        if 'gift_unit_price' in d:
            o.gift_unit_price = d['gift_unit_price']
        if 'head_url' in d:
            o.head_url = d['head_url']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'unique_no' in d:
            o.unique_no = d['unique_no']
        if 'user_info' in d:
            o.user_info = d['user_info']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


