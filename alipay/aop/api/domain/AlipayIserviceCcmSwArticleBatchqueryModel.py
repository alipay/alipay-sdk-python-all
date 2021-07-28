#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCcmSwArticleBatchqueryModel(object):

    def __init__(self):
        self._category_id = None
        self._ccs_instance_id = None
        self._end_time = None
        self._ids = None
        self._keyword = None
        self._keywords = None
        self._library_id = None
        self._page_num = None
        self._page_size = None
        self._search_all_category = None
        self._search_category_type = None
        self._start_time = None
        self._status = None

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def ccs_instance_id(self):
        return self._ccs_instance_id

    @ccs_instance_id.setter
    def ccs_instance_id(self, value):
        self._ccs_instance_id = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def ids(self):
        return self._ids

    @ids.setter
    def ids(self, value):
        if isinstance(value, list):
            self._ids = list()
            for i in value:
                self._ids.append(i)
    @property
    def keyword(self):
        return self._keyword

    @keyword.setter
    def keyword(self, value):
        self._keyword = value
    @property
    def keywords(self):
        return self._keywords

    @keywords.setter
    def keywords(self, value):
        if isinstance(value, list):
            self._keywords = list()
            for i in value:
                self._keywords.append(i)
    @property
    def library_id(self):
        return self._library_id

    @library_id.setter
    def library_id(self, value):
        self._library_id = value
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
    def search_all_category(self):
        return self._search_all_category

    @search_all_category.setter
    def search_all_category(self, value):
        self._search_all_category = value
    @property
    def search_category_type(self):
        return self._search_category_type

    @search_category_type.setter
    def search_category_type(self, value):
        self._search_category_type = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.ccs_instance_id:
            if hasattr(self.ccs_instance_id, 'to_alipay_dict'):
                params['ccs_instance_id'] = self.ccs_instance_id.to_alipay_dict()
            else:
                params['ccs_instance_id'] = self.ccs_instance_id
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.ids:
            if isinstance(self.ids, list):
                for i in range(0, len(self.ids)):
                    element = self.ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ids[i] = element.to_alipay_dict()
            if hasattr(self.ids, 'to_alipay_dict'):
                params['ids'] = self.ids.to_alipay_dict()
            else:
                params['ids'] = self.ids
        if self.keyword:
            if hasattr(self.keyword, 'to_alipay_dict'):
                params['keyword'] = self.keyword.to_alipay_dict()
            else:
                params['keyword'] = self.keyword
        if self.keywords:
            if isinstance(self.keywords, list):
                for i in range(0, len(self.keywords)):
                    element = self.keywords[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.keywords[i] = element.to_alipay_dict()
            if hasattr(self.keywords, 'to_alipay_dict'):
                params['keywords'] = self.keywords.to_alipay_dict()
            else:
                params['keywords'] = self.keywords
        if self.library_id:
            if hasattr(self.library_id, 'to_alipay_dict'):
                params['library_id'] = self.library_id.to_alipay_dict()
            else:
                params['library_id'] = self.library_id
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
        if self.search_all_category:
            if hasattr(self.search_all_category, 'to_alipay_dict'):
                params['search_all_category'] = self.search_all_category.to_alipay_dict()
            else:
                params['search_all_category'] = self.search_all_category
        if self.search_category_type:
            if hasattr(self.search_category_type, 'to_alipay_dict'):
                params['search_category_type'] = self.search_category_type.to_alipay_dict()
            else:
                params['search_category_type'] = self.search_category_type
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCcmSwArticleBatchqueryModel()
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'ccs_instance_id' in d:
            o.ccs_instance_id = d['ccs_instance_id']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'ids' in d:
            o.ids = d['ids']
        if 'keyword' in d:
            o.keyword = d['keyword']
        if 'keywords' in d:
            o.keywords = d['keywords']
        if 'library_id' in d:
            o.library_id = d['library_id']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'search_all_category' in d:
            o.search_all_category = d['search_all_category']
        if 'search_category_type' in d:
            o.search_category_type = d['search_category_type']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status' in d:
            o.status = d['status']
        return o


