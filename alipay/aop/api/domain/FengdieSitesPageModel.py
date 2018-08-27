#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FengdieActivitySchemaModel import FengdieActivitySchemaModel


class FengdieSitesPageModel(object):

    def __init__(self):
        self._alias = None
        self._schema = None
        self._snapshot = None
        self._url = None

    @property
    def alias(self):
        return self._alias

    @alias.setter
    def alias(self, value):
        self._alias = value
    @property
    def schema(self):
        return self._schema

    @schema.setter
    def schema(self, value):
        if isinstance(value, list):
            self._schema = list()
            for i in value:
                if isinstance(i, FengdieActivitySchemaModel):
                    self._schema.append(i)
                else:
                    self._schema.append(FengdieActivitySchemaModel.from_alipay_dict(i))
    @property
    def snapshot(self):
        return self._snapshot

    @snapshot.setter
    def snapshot(self, value):
        self._snapshot = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.alias:
            if hasattr(self.alias, 'to_alipay_dict'):
                params['alias'] = self.alias.to_alipay_dict()
            else:
                params['alias'] = self.alias
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
        o = FengdieSitesPageModel()
        if 'alias' in d:
            o.alias = d['alias']
        if 'schema' in d:
            o.schema = d['schema']
        if 'snapshot' in d:
            o.snapshot = d['snapshot']
        if 'url' in d:
            o.url = d['url']
        return o


