#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreativeDetail import CreativeDetail
from alipay.aop.api.domain.PageInfo import PageInfo


class PageCreative(object):

    def __init__(self):
        self._list = None
        self._pagination = None

    @property
    def list(self):
        return self._list

    @list.setter
    def list(self, value):
        if isinstance(value, list):
            self._list = list()
            for i in value:
                if isinstance(i, CreativeDetail):
                    self._list.append(i)
                else:
                    self._list.append(CreativeDetail.from_alipay_dict(i))
    @property
    def pagination(self):
        return self._pagination

    @pagination.setter
    def pagination(self, value):
        if isinstance(value, PageInfo):
            self._pagination = value
        else:
            self._pagination = PageInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
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
        if self.pagination:
            if hasattr(self.pagination, 'to_alipay_dict'):
                params['pagination'] = self.pagination.to_alipay_dict()
            else:
                params['pagination'] = self.pagination
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PageCreative()
        if 'list' in d:
            o.list = d['list']
        if 'pagination' in d:
            o.pagination = d['pagination']
        return o


