#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenSearchImageBO(object):

    def __init__(self):
        self._biz_id = None
        self._doc_url = None
        self._generated_desc = None
        self._pic_height = None
        self._pic_url = None
        self._pic_width = None
        self._sort_values = None
        self._title = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def doc_url(self):
        return self._doc_url

    @doc_url.setter
    def doc_url(self, value):
        self._doc_url = value
    @property
    def generated_desc(self):
        return self._generated_desc

    @generated_desc.setter
    def generated_desc(self, value):
        self._generated_desc = value
    @property
    def pic_height(self):
        return self._pic_height

    @pic_height.setter
    def pic_height(self, value):
        self._pic_height = value
    @property
    def pic_url(self):
        return self._pic_url

    @pic_url.setter
    def pic_url(self, value):
        self._pic_url = value
    @property
    def pic_width(self):
        return self._pic_width

    @pic_width.setter
    def pic_width(self, value):
        self._pic_width = value
    @property
    def sort_values(self):
        return self._sort_values

    @sort_values.setter
    def sort_values(self, value):
        self._sort_values = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.doc_url:
            if hasattr(self.doc_url, 'to_alipay_dict'):
                params['doc_url'] = self.doc_url.to_alipay_dict()
            else:
                params['doc_url'] = self.doc_url
        if self.generated_desc:
            if hasattr(self.generated_desc, 'to_alipay_dict'):
                params['generated_desc'] = self.generated_desc.to_alipay_dict()
            else:
                params['generated_desc'] = self.generated_desc
        if self.pic_height:
            if hasattr(self.pic_height, 'to_alipay_dict'):
                params['pic_height'] = self.pic_height.to_alipay_dict()
            else:
                params['pic_height'] = self.pic_height
        if self.pic_url:
            if hasattr(self.pic_url, 'to_alipay_dict'):
                params['pic_url'] = self.pic_url.to_alipay_dict()
            else:
                params['pic_url'] = self.pic_url
        if self.pic_width:
            if hasattr(self.pic_width, 'to_alipay_dict'):
                params['pic_width'] = self.pic_width.to_alipay_dict()
            else:
                params['pic_width'] = self.pic_width
        if self.sort_values:
            if hasattr(self.sort_values, 'to_alipay_dict'):
                params['sort_values'] = self.sort_values.to_alipay_dict()
            else:
                params['sort_values'] = self.sort_values
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
        o = OpenSearchImageBO()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'doc_url' in d:
            o.doc_url = d['doc_url']
        if 'generated_desc' in d:
            o.generated_desc = d['generated_desc']
        if 'pic_height' in d:
            o.pic_height = d['pic_height']
        if 'pic_url' in d:
            o.pic_url = d['pic_url']
        if 'pic_width' in d:
            o.pic_width = d['pic_width']
        if 'sort_values' in d:
            o.sort_values = d['sort_values']
        if 'title' in d:
            o.title = d['title']
        return o


