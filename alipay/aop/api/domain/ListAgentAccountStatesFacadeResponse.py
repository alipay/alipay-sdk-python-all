#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AgentAccountStates import AgentAccountStates


class ListAgentAccountStatesFacadeResponse(object):

    def __init__(self):
        self._current = None
        self._list = None
        self._page_size = None
        self._total = None
        self._total_page = None

    @property
    def current(self):
        return self._current

    @current.setter
    def current(self, value):
        self._current = value
    @property
    def list(self):
        return self._list

    @list.setter
    def list(self, value):
        if isinstance(value, list):
            self._list = list()
            for i in value:
                if isinstance(i, AgentAccountStates):
                    self._list.append(i)
                else:
                    self._list.append(AgentAccountStates.from_alipay_dict(i))
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value
    @property
    def total_page(self):
        return self._total_page

    @total_page.setter
    def total_page(self, value):
        self._total_page = value


    def to_alipay_dict(self):
        params = dict()
        if self.current:
            if hasattr(self.current, 'to_alipay_dict'):
                params['current'] = self.current.to_alipay_dict()
            else:
                params['current'] = self.current
        if self.list:
            if isinstance(self.list, list):
                for i in range(0, len(self.list)):
                    element = self.list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.list[i] = element.to_alipay_dict()
            if hasattr(self.list, 'to_alipay_dict'):
                params['list'] = self.list.to_alipay_dict()
            else:
                params['list'] = self.list
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.total:
            if hasattr(self.total, 'to_alipay_dict'):
                params['total'] = self.total.to_alipay_dict()
            else:
                params['total'] = self.total
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
        o = ListAgentAccountStatesFacadeResponse()
        if 'current' in d:
            o.current = d['current']
        if 'list' in d:
            o.list = d['list']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'total' in d:
            o.total = d['total']
        if 'total_page' in d:
            o.total_page = d['total_page']
        return o


