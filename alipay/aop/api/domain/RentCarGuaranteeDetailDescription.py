#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentCarGuaranteeSubDetailDescription import RentCarGuaranteeSubDetailDescription
from alipay.aop.api.domain.RentCarTableInfo import RentCarTableInfo


class RentCarGuaranteeDetailDescription(object):

    def __init__(self):
        self._contains = None
        self._content = None
        self._sub_content = None
        self._table = None
        self._title = None

    @property
    def contains(self):
        return self._contains

    @contains.setter
    def contains(self, value):
        self._contains = value
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
    def sub_content(self):
        return self._sub_content

    @sub_content.setter
    def sub_content(self, value):
        if isinstance(value, list):
            self._sub_content = list()
            for i in value:
                if isinstance(i, RentCarGuaranteeSubDetailDescription):
                    self._sub_content.append(i)
                else:
                    self._sub_content.append(RentCarGuaranteeSubDetailDescription.from_alipay_dict(i))
    @property
    def table(self):
        return self._table

    @table.setter
    def table(self, value):
        if isinstance(value, list):
            self._table = list()
            for i in value:
                if isinstance(i, RentCarTableInfo):
                    self._table.append(i)
                else:
                    self._table.append(RentCarTableInfo.from_alipay_dict(i))
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.contains:
            if hasattr(self.contains, 'to_alipay_dict'):
                params['contains'] = self.contains.to_alipay_dict()
            else:
                params['contains'] = self.contains
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
        if self.sub_content:
            if isinstance(self.sub_content, list):
                for i in range(0, len(self.sub_content)):
                    element = self.sub_content[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sub_content[i] = element.to_alipay_dict()
            if hasattr(self.sub_content, 'to_alipay_dict'):
                params['sub_content'] = self.sub_content.to_alipay_dict()
            else:
                params['sub_content'] = self.sub_content
        if self.table:
            if isinstance(self.table, list):
                for i in range(0, len(self.table)):
                    element = self.table[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.table[i] = element.to_alipay_dict()
            if hasattr(self.table, 'to_alipay_dict'):
                params['table'] = self.table.to_alipay_dict()
            else:
                params['table'] = self.table
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentCarGuaranteeDetailDescription()
        if 'contains' in d:
            o.contains = d['contains']
        if 'content' in d:
            o.content = d['content']
        if 'sub_content' in d:
            o.sub_content = d['sub_content']
        if 'table' in d:
            o.table = d['table']
        if 'title' in d:
            o.title = d['title']
        return o


