#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbItemInfo(object):

    def __init__(self):
        self._avg_pop_value = None
        self._begin_time = None
        self._end_time = None
        self._ext_info = None
        self._item_id = None
        self._logo = None
        self._original_price = None
        self._quota = None
        self._sale_price = None
        self._shop_distance = None
        self._shop_id = None
        self._shop_name = None
        self._status = None
        self._title = None
        self._top = None
        self._total_quota = None
        self._url = None

    @property
    def avg_pop_value(self):
        return self._avg_pop_value

    @avg_pop_value.setter
    def avg_pop_value(self, value):
        self._avg_pop_value = value
    @property
    def begin_time(self):
        return self._begin_time

    @begin_time.setter
    def begin_time(self, value):
        self._begin_time = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def quota(self):
        return self._quota

    @quota.setter
    def quota(self, value):
        self._quota = value
    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, value):
        self._sale_price = value
    @property
    def shop_distance(self):
        return self._shop_distance

    @shop_distance.setter
    def shop_distance(self, value):
        self._shop_distance = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def top(self):
        return self._top

    @top.setter
    def top(self, value):
        self._top = value
    @property
    def total_quota(self):
        return self._total_quota

    @total_quota.setter
    def total_quota(self, value):
        self._total_quota = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.avg_pop_value:
            if hasattr(self.avg_pop_value, 'to_alipay_dict'):
                params['avg_pop_value'] = self.avg_pop_value.to_alipay_dict()
            else:
                params['avg_pop_value'] = self.avg_pop_value
        if self.begin_time:
            if hasattr(self.begin_time, 'to_alipay_dict'):
                params['begin_time'] = self.begin_time.to_alipay_dict()
            else:
                params['begin_time'] = self.begin_time
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.quota:
            if hasattr(self.quota, 'to_alipay_dict'):
                params['quota'] = self.quota.to_alipay_dict()
            else:
                params['quota'] = self.quota
        if self.sale_price:
            if hasattr(self.sale_price, 'to_alipay_dict'):
                params['sale_price'] = self.sale_price.to_alipay_dict()
            else:
                params['sale_price'] = self.sale_price
        if self.shop_distance:
            if hasattr(self.shop_distance, 'to_alipay_dict'):
                params['shop_distance'] = self.shop_distance.to_alipay_dict()
            else:
                params['shop_distance'] = self.shop_distance
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.top:
            if hasattr(self.top, 'to_alipay_dict'):
                params['top'] = self.top.to_alipay_dict()
            else:
                params['top'] = self.top
        if self.total_quota:
            if hasattr(self.total_quota, 'to_alipay_dict'):
                params['total_quota'] = self.total_quota.to_alipay_dict()
            else:
                params['total_quota'] = self.total_quota
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbItemInfo()
        if 'avg_pop_value' in d:
            o.avg_pop_value = d['avg_pop_value']
        if 'begin_time' in d:
            o.begin_time = d['begin_time']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'logo' in d:
            o.logo = d['logo']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'quota' in d:
            o.quota = d['quota']
        if 'sale_price' in d:
            o.sale_price = d['sale_price']
        if 'shop_distance' in d:
            o.shop_distance = d['shop_distance']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'status' in d:
            o.status = d['status']
        if 'title' in d:
            o.title = d['title']
        if 'top' in d:
            o.top = d['top']
        if 'total_quota' in d:
            o.total_quota = d['total_quota']
        if 'url' in d:
            o.url = d['url']
        return o


