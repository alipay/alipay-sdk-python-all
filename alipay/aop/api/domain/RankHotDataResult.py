#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RankHotDataResult(object):

    def __init__(self):
        self._hot_id = None
        self._index = None
        self._label = None
        self._publish_time = None
        self._rank = None
        self._series_id = None
        self._title = None
        self._unique_id = None

    @property
    def hot_id(self):
        return self._hot_id

    @hot_id.setter
    def hot_id(self, value):
        self._hot_id = value
    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        self._index = value
    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, value):
        self._label = value
    @property
    def publish_time(self):
        return self._publish_time

    @publish_time.setter
    def publish_time(self, value):
        self._publish_time = value
    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        self._rank = value
    @property
    def series_id(self):
        return self._series_id

    @series_id.setter
    def series_id(self, value):
        self._series_id = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def unique_id(self):
        return self._unique_id

    @unique_id.setter
    def unique_id(self, value):
        if isinstance(value, list):
            self._unique_id = list()
            for i in value:
                self._unique_id.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.hot_id:
            if hasattr(self.hot_id, 'to_alipay_dict'):
                params['hot_id'] = self.hot_id.to_alipay_dict()
            else:
                params['hot_id'] = self.hot_id
        if self.index:
            if hasattr(self.index, 'to_alipay_dict'):
                params['index'] = self.index.to_alipay_dict()
            else:
                params['index'] = self.index
        if self.label:
            if hasattr(self.label, 'to_alipay_dict'):
                params['label'] = self.label.to_alipay_dict()
            else:
                params['label'] = self.label
        if self.publish_time:
            if hasattr(self.publish_time, 'to_alipay_dict'):
                params['publish_time'] = self.publish_time.to_alipay_dict()
            else:
                params['publish_time'] = self.publish_time
        if self.rank:
            if hasattr(self.rank, 'to_alipay_dict'):
                params['rank'] = self.rank.to_alipay_dict()
            else:
                params['rank'] = self.rank
        if self.series_id:
            if hasattr(self.series_id, 'to_alipay_dict'):
                params['series_id'] = self.series_id.to_alipay_dict()
            else:
                params['series_id'] = self.series_id
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.unique_id:
            if isinstance(self.unique_id, list):
                for i in range(0, len(self.unique_id)):
                    element = self.unique_id[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.unique_id[i] = element.to_alipay_dict()
            if hasattr(self.unique_id, 'to_alipay_dict'):
                params['unique_id'] = self.unique_id.to_alipay_dict()
            else:
                params['unique_id'] = self.unique_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RankHotDataResult()
        if 'hot_id' in d:
            o.hot_id = d['hot_id']
        if 'index' in d:
            o.index = d['index']
        if 'label' in d:
            o.label = d['label']
        if 'publish_time' in d:
            o.publish_time = d['publish_time']
        if 'rank' in d:
            o.rank = d['rank']
        if 'series_id' in d:
            o.series_id = d['series_id']
        if 'title' in d:
            o.title = d['title']
        if 'unique_id' in d:
            o.unique_id = d['unique_id']
        return o


