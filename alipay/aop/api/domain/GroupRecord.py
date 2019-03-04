#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Hit import Hit


class GroupRecord(object):

    def __init__(self):
        self._count = None
        self._group_id = None
        self._group_name = None
        self._has_more = None
        self._hits = None
        self._more_link_name = None
        self._more_link_url = None
        self._total_count = None

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, value):
        self._group_name = value
    @property
    def has_more(self):
        return self._has_more

    @has_more.setter
    def has_more(self, value):
        self._has_more = value
    @property
    def hits(self):
        return self._hits

    @hits.setter
    def hits(self, value):
        if isinstance(value, list):
            self._hits = list()
            for i in value:
                if isinstance(i, Hit):
                    self._hits.append(i)
                else:
                    self._hits.append(Hit.from_alipay_dict(i))
    @property
    def more_link_name(self):
        return self._more_link_name

    @more_link_name.setter
    def more_link_name(self, value):
        self._more_link_name = value
    @property
    def more_link_url(self):
        return self._more_link_url

    @more_link_url.setter
    def more_link_url(self, value):
        self._more_link_url = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.group_name:
            if hasattr(self.group_name, 'to_alipay_dict'):
                params['group_name'] = self.group_name.to_alipay_dict()
            else:
                params['group_name'] = self.group_name
        if self.has_more:
            if hasattr(self.has_more, 'to_alipay_dict'):
                params['has_more'] = self.has_more.to_alipay_dict()
            else:
                params['has_more'] = self.has_more
        if self.hits:
            if isinstance(self.hits, list):
                for i in range(0, len(self.hits)):
                    element = self.hits[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.hits[i] = element.to_alipay_dict()
            if hasattr(self.hits, 'to_alipay_dict'):
                params['hits'] = self.hits.to_alipay_dict()
            else:
                params['hits'] = self.hits
        if self.more_link_name:
            if hasattr(self.more_link_name, 'to_alipay_dict'):
                params['more_link_name'] = self.more_link_name.to_alipay_dict()
            else:
                params['more_link_name'] = self.more_link_name
        if self.more_link_url:
            if hasattr(self.more_link_url, 'to_alipay_dict'):
                params['more_link_url'] = self.more_link_url.to_alipay_dict()
            else:
                params['more_link_url'] = self.more_link_url
        if self.total_count:
            if hasattr(self.total_count, 'to_alipay_dict'):
                params['total_count'] = self.total_count.to_alipay_dict()
            else:
                params['total_count'] = self.total_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupRecord()
        if 'count' in d:
            o.count = d['count']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'group_name' in d:
            o.group_name = d['group_name']
        if 'has_more' in d:
            o.has_more = d['has_more']
        if 'hits' in d:
            o.hits = d['hits']
        if 'more_link_name' in d:
            o.more_link_name = d['more_link_name']
        if 'more_link_url' in d:
            o.more_link_url = d['more_link_url']
        if 'total_count' in d:
            o.total_count = d['total_count']
        return o


