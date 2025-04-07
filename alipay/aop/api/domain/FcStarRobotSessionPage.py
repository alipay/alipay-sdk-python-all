#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FcStarRobotSession import FcStarRobotSession


class FcStarRobotSessionPage(object):

    def __init__(self):
        self._count = None
        self._page = None
        self._page_size = None
        self._result_obj = None
        self._total_pages = None

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def result_obj(self):
        return self._result_obj

    @result_obj.setter
    def result_obj(self, value):
        if isinstance(value, list):
            self._result_obj = list()
            for i in value:
                if isinstance(i, FcStarRobotSession):
                    self._result_obj.append(i)
                else:
                    self._result_obj.append(FcStarRobotSession.from_alipay_dict(i))
    @property
    def total_pages(self):
        return self._total_pages

    @total_pages.setter
    def total_pages(self, value):
        self._total_pages = value


    def to_alipay_dict(self):
        params = dict()
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        if self.page:
            if hasattr(self.page, 'to_alipay_dict'):
                params['page'] = self.page.to_alipay_dict()
            else:
                params['page'] = self.page
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.result_obj:
            if isinstance(self.result_obj, list):
                for i in range(0, len(self.result_obj)):
                    element = self.result_obj[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.result_obj[i] = element.to_alipay_dict()
            if hasattr(self.result_obj, 'to_alipay_dict'):
                params['result_obj'] = self.result_obj.to_alipay_dict()
            else:
                params['result_obj'] = self.result_obj
        if self.total_pages:
            if hasattr(self.total_pages, 'to_alipay_dict'):
                params['total_pages'] = self.total_pages.to_alipay_dict()
            else:
                params['total_pages'] = self.total_pages
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FcStarRobotSessionPage()
        if 'count' in d:
            o.count = d['count']
        if 'page' in d:
            o.page = d['page']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'result_obj' in d:
            o.result_obj = d['result_obj']
        if 'total_pages' in d:
            o.total_pages = d['total_pages']
        return o


