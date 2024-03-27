#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SearchQueryBoxMarketingRequest(object):

    def __init__(self):
        self._brand_id = None
        self._fuzzy_matching = None
        self._item_id = None
        self._page_num = None
        self._page_size = None
        self._pid = None
        self._query_last_version = None
        self._query_serv_info = None
        self._status_list = None

    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value
    @property
    def fuzzy_matching(self):
        return self._fuzzy_matching

    @fuzzy_matching.setter
    def fuzzy_matching(self, value):
        self._fuzzy_matching = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
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
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def query_last_version(self):
        return self._query_last_version

    @query_last_version.setter
    def query_last_version(self, value):
        self._query_last_version = value
    @property
    def query_serv_info(self):
        return self._query_serv_info

    @query_serv_info.setter
    def query_serv_info(self, value):
        self._query_serv_info = value
    @property
    def status_list(self):
        return self._status_list

    @status_list.setter
    def status_list(self, value):
        if isinstance(value, list):
            self._status_list = list()
            for i in value:
                self._status_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.brand_id:
            if hasattr(self.brand_id, 'to_alipay_dict'):
                params['brand_id'] = self.brand_id.to_alipay_dict()
            else:
                params['brand_id'] = self.brand_id
        if self.fuzzy_matching:
            if hasattr(self.fuzzy_matching, 'to_alipay_dict'):
                params['fuzzy_matching'] = self.fuzzy_matching.to_alipay_dict()
            else:
                params['fuzzy_matching'] = self.fuzzy_matching
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
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
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.query_last_version:
            if hasattr(self.query_last_version, 'to_alipay_dict'):
                params['query_last_version'] = self.query_last_version.to_alipay_dict()
            else:
                params['query_last_version'] = self.query_last_version
        if self.query_serv_info:
            if hasattr(self.query_serv_info, 'to_alipay_dict'):
                params['query_serv_info'] = self.query_serv_info.to_alipay_dict()
            else:
                params['query_serv_info'] = self.query_serv_info
        if self.status_list:
            if isinstance(self.status_list, list):
                for i in range(0, len(self.status_list)):
                    element = self.status_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.status_list[i] = element.to_alipay_dict()
            if hasattr(self.status_list, 'to_alipay_dict'):
                params['status_list'] = self.status_list.to_alipay_dict()
            else:
                params['status_list'] = self.status_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SearchQueryBoxMarketingRequest()
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'fuzzy_matching' in d:
            o.fuzzy_matching = d['fuzzy_matching']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'pid' in d:
            o.pid = d['pid']
        if 'query_last_version' in d:
            o.query_last_version = d['query_last_version']
        if 'query_serv_info' in d:
            o.query_serv_info = d['query_serv_info']
        if 'status_list' in d:
            o.status_list = d['status_list']
        return o


