#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FengdieActivitySchemaData import FengdieActivitySchemaData


class FengdieActivityPage(object):

    def __init__(self):
        self._id = None
        self._name = None
        self._schema = None
        self._snapshot = None
        self._title = None
        self._url = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def schema(self):
        return self._schema

    @schema.setter
    def schema(self, value):
        if isinstance(value, list):
            self._schema = list()
            for i in value:
                if isinstance(i, FengdieActivitySchemaData):
                    self._schema.append(i)
                else:
                    self._schema.append(FengdieActivitySchemaData.from_alipay_dict(i))
    @property
    def snapshot(self):
        return self._snapshot

    @snapshot.setter
    def snapshot(self, value):
        self._snapshot = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.schema:
            if isinstance(self.schema, list):
                for i in range(0, len(self.schema)):
                    element = self.schema[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.schema[i] = element.to_alipay_dict()
            if hasattr(self.schema, 'to_alipay_dict'):
                params['schema'] = self.schema.to_alipay_dict()
            else:
                params['schema'] = self.schema
        if self.snapshot:
            if hasattr(self.snapshot, 'to_alipay_dict'):
                params['snapshot'] = self.snapshot.to_alipay_dict()
            else:
                params['snapshot'] = self.snapshot
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
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
        o = FengdieActivityPage()
        if 'id' in d:
            o.id = d['id']
        if 'name' in d:
            o.name = d['name']
        if 'schema' in d:
            o.schema = d['schema']
        if 'snapshot' in d:
            o.snapshot = d['snapshot']
        if 'title' in d:
            o.title = d['title']
        if 'url' in d:
            o.url = d['url']
        return o


