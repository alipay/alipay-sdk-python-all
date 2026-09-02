#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExternalItemPic(object):

    def __init__(self):
        self._pic_desc = None
        self._pic_mark = None
        self._pic_type = None
        self._sort = None
        self._source_url = None

    @property
    def pic_desc(self):
        return self._pic_desc

    @pic_desc.setter
    def pic_desc(self, value):
        self._pic_desc = value
    @property
    def pic_mark(self):
        return self._pic_mark

    @pic_mark.setter
    def pic_mark(self, value):
        self._pic_mark = value
    @property
    def pic_type(self):
        return self._pic_type

    @pic_type.setter
    def pic_type(self, value):
        self._pic_type = value
    @property
    def sort(self):
        return self._sort

    @sort.setter
    def sort(self, value):
        self._sort = value
    @property
    def source_url(self):
        return self._source_url

    @source_url.setter
    def source_url(self, value):
        self._source_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.pic_desc:
            if hasattr(self.pic_desc, 'to_alipay_dict'):
                params['pic_desc'] = self.pic_desc.to_alipay_dict()
            else:
                params['pic_desc'] = self.pic_desc
        if self.pic_mark:
            if hasattr(self.pic_mark, 'to_alipay_dict'):
                params['pic_mark'] = self.pic_mark.to_alipay_dict()
            else:
                params['pic_mark'] = self.pic_mark
        if self.pic_type:
            if hasattr(self.pic_type, 'to_alipay_dict'):
                params['pic_type'] = self.pic_type.to_alipay_dict()
            else:
                params['pic_type'] = self.pic_type
        if self.sort:
            if hasattr(self.sort, 'to_alipay_dict'):
                params['sort'] = self.sort.to_alipay_dict()
            else:
                params['sort'] = self.sort
        if self.source_url:
            if hasattr(self.source_url, 'to_alipay_dict'):
                params['source_url'] = self.source_url.to_alipay_dict()
            else:
                params['source_url'] = self.source_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExternalItemPic()
        if 'pic_desc' in d:
            o.pic_desc = d['pic_desc']
        if 'pic_mark' in d:
            o.pic_mark = d['pic_mark']
        if 'pic_type' in d:
            o.pic_type = d['pic_type']
        if 'sort' in d:
            o.sort = d['sort']
        if 'source_url' in d:
            o.source_url = d['source_url']
        return o


