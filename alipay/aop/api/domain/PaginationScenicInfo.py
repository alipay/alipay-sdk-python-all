#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ScenicInfo import ScenicInfo


class PaginationScenicInfo(object):

    def __init__(self):
        self._page_no = None
        self._page_size = None
        self._scenic_info = None
        self._total_count = None
        self._total_page = None

    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def scenic_info(self):
        return self._scenic_info

    @scenic_info.setter
    def scenic_info(self, value):
        if isinstance(value, list):
            self._scenic_info = list()
            for i in value:
                if isinstance(i, ScenicInfo):
                    self._scenic_info.append(i)
                else:
                    self._scenic_info.append(ScenicInfo.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def total_page(self):
        return self._total_page

    @total_page.setter
    def total_page(self, value):
        self._total_page = value


    def to_alipay_dict(self):
        params = dict()
        if self.page_no:
            if hasattr(self.page_no, 'to_alipay_dict'):
                params['page_no'] = self.page_no.to_alipay_dict()
            else:
                params['page_no'] = self.page_no
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.scenic_info:
            if isinstance(self.scenic_info, list):
                for i in range(0, len(self.scenic_info)):
                    element = self.scenic_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.scenic_info[i] = element.to_alipay_dict()
            if hasattr(self.scenic_info, 'to_alipay_dict'):
                params['scenic_info'] = self.scenic_info.to_alipay_dict()
            else:
                params['scenic_info'] = self.scenic_info
        if self.total_count:
            if hasattr(self.total_count, 'to_alipay_dict'):
                params['total_count'] = self.total_count.to_alipay_dict()
            else:
                params['total_count'] = self.total_count
        if self.total_page:
            if hasattr(self.total_page, 'to_alipay_dict'):
                params['total_page'] = self.total_page.to_alipay_dict()
            else:
                params['total_page'] = self.total_page
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PaginationScenicInfo()
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'scenic_info' in d:
            o.scenic_info = d['scenic_info']
        if 'total_count' in d:
            o.total_count = d['total_count']
        if 'total_page' in d:
            o.total_page = d['total_page']
        return o


