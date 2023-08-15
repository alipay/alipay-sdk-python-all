#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniCloudAositemQueryModel(object):

    def __init__(self):
        self._aggregation_field = None
        self._cate = None
        self._city_code = None
        self._client_env = None
        self._device_id = None
        self._ext_rep_filed = None
        self._filters = None
        self._item_id_list = None
        self._latitude = None
        self._longitude = None
        self._open_id = None
        self._orders = None
        self._page_num = None
        self._page_size = None
        self._project_id = None
        self._query = None
        self._tags = None
        self._user_id = None
        self._user_id_type = None

    @property
    def aggregation_field(self):
        return self._aggregation_field

    @aggregation_field.setter
    def aggregation_field(self, value):
        self._aggregation_field = value
    @property
    def cate(self):
        return self._cate

    @cate.setter
    def cate(self, value):
        if isinstance(value, list):
            self._cate = list()
            for i in value:
                self._cate.append(i)
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def client_env(self):
        return self._client_env

    @client_env.setter
    def client_env(self, value):
        self._client_env = value
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def ext_rep_filed(self):
        return self._ext_rep_filed

    @ext_rep_filed.setter
    def ext_rep_filed(self, value):
        self._ext_rep_filed = value
    @property
    def filters(self):
        return self._filters

    @filters.setter
    def filters(self, value):
        if isinstance(value, list):
            self._filters = list()
            for i in value:
                self._filters.append(i)
    @property
    def item_id_list(self):
        return self._item_id_list

    @item_id_list.setter
    def item_id_list(self, value):
        if isinstance(value, list):
            self._item_id_list = list()
            for i in value:
                self._item_id_list.append(i)
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def orders(self):
        return self._orders

    @orders.setter
    def orders(self, value):
        if isinstance(value, list):
            self._orders = list()
            for i in value:
                self._orders.append(i)
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value
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
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_id_type(self):
        return self._user_id_type

    @user_id_type.setter
    def user_id_type(self, value):
        self._user_id_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.aggregation_field:
            if hasattr(self.aggregation_field, 'to_alipay_dict'):
                params['aggregation_field'] = self.aggregation_field.to_alipay_dict()
            else:
                params['aggregation_field'] = self.aggregation_field
        if self.cate:
            if isinstance(self.cate, list):
                for i in range(0, len(self.cate)):
                    element = self.cate[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.cate[i] = element.to_alipay_dict()
            if hasattr(self.cate, 'to_alipay_dict'):
                params['cate'] = self.cate.to_alipay_dict()
            else:
                params['cate'] = self.cate
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.client_env:
            if hasattr(self.client_env, 'to_alipay_dict'):
                params['client_env'] = self.client_env.to_alipay_dict()
            else:
                params['client_env'] = self.client_env
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.ext_rep_filed:
            if hasattr(self.ext_rep_filed, 'to_alipay_dict'):
                params['ext_rep_filed'] = self.ext_rep_filed.to_alipay_dict()
            else:
                params['ext_rep_filed'] = self.ext_rep_filed
        if self.filters:
            if isinstance(self.filters, list):
                for i in range(0, len(self.filters)):
                    element = self.filters[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.filters[i] = element.to_alipay_dict()
            if hasattr(self.filters, 'to_alipay_dict'):
                params['filters'] = self.filters.to_alipay_dict()
            else:
                params['filters'] = self.filters
        if self.item_id_list:
            if isinstance(self.item_id_list, list):
                for i in range(0, len(self.item_id_list)):
                    element = self.item_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_id_list[i] = element.to_alipay_dict()
            if hasattr(self.item_id_list, 'to_alipay_dict'):
                params['item_id_list'] = self.item_id_list.to_alipay_dict()
            else:
                params['item_id_list'] = self.item_id_list
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.orders:
            if isinstance(self.orders, list):
                for i in range(0, len(self.orders)):
                    element = self.orders[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.orders[i] = element.to_alipay_dict()
            if hasattr(self.orders, 'to_alipay_dict'):
                params['orders'] = self.orders.to_alipay_dict()
            else:
                params['orders'] = self.orders
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
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
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_id_type:
            if hasattr(self.user_id_type, 'to_alipay_dict'):
                params['user_id_type'] = self.user_id_type.to_alipay_dict()
            else:
                params['user_id_type'] = self.user_id_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniCloudAositemQueryModel()
        if 'aggregation_field' in d:
            o.aggregation_field = d['aggregation_field']
        if 'cate' in d:
            o.cate = d['cate']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'client_env' in d:
            o.client_env = d['client_env']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'ext_rep_filed' in d:
            o.ext_rep_filed = d['ext_rep_filed']
        if 'filters' in d:
            o.filters = d['filters']
        if 'item_id_list' in d:
            o.item_id_list = d['item_id_list']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'orders' in d:
            o.orders = d['orders']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'query' in d:
            o.query = d['query']
        if 'tags' in d:
            o.tags = d['tags']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_id_type' in d:
            o.user_id_type = d['user_id_type']
        return o


