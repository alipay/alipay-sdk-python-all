#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SpuDetail import SpuDetail


class AlipayIserviceCcmSwKnowledgeModifyModel(object):

    def __init__(self):
        self._category_id = None
        self._category_name = None
        self._content = None
        self._ext_id = None
        self._extend_titles = None
        self._icon = None
        self._id = None
        self._is_delete = None
        self._is_searchable = None
        self._library_id = None
        self._library_name = None
        self._spu = None
        self._tags = None
        self._title = None

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, value):
        self._category_name = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def ext_id(self):
        return self._ext_id

    @ext_id.setter
    def ext_id(self, value):
        self._ext_id = value
    @property
    def extend_titles(self):
        return self._extend_titles

    @extend_titles.setter
    def extend_titles(self, value):
        if isinstance(value, list):
            self._extend_titles = list()
            for i in value:
                self._extend_titles.append(i)
    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def is_delete(self):
        return self._is_delete

    @is_delete.setter
    def is_delete(self, value):
        self._is_delete = value
    @property
    def is_searchable(self):
        return self._is_searchable

    @is_searchable.setter
    def is_searchable(self, value):
        self._is_searchable = value
    @property
    def library_id(self):
        return self._library_id

    @library_id.setter
    def library_id(self, value):
        self._library_id = value
    @property
    def library_name(self):
        return self._library_name

    @library_name.setter
    def library_name(self, value):
        self._library_name = value
    @property
    def spu(self):
        return self._spu

    @spu.setter
    def spu(self, value):
        if isinstance(value, SpuDetail):
            self._spu = value
        else:
            self._spu = SpuDetail.from_alipay_dict(value)
    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        if isinstance(value, list):
            self._tags = list()
            for i in value:
                self._tags.append(i)
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.category_name:
            if hasattr(self.category_name, 'to_alipay_dict'):
                params['category_name'] = self.category_name.to_alipay_dict()
            else:
                params['category_name'] = self.category_name
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.ext_id:
            if hasattr(self.ext_id, 'to_alipay_dict'):
                params['ext_id'] = self.ext_id.to_alipay_dict()
            else:
                params['ext_id'] = self.ext_id
        if self.extend_titles:
            if isinstance(self.extend_titles, list):
                for i in range(0, len(self.extend_titles)):
                    element = self.extend_titles[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.extend_titles[i] = element.to_alipay_dict()
            if hasattr(self.extend_titles, 'to_alipay_dict'):
                params['extend_titles'] = self.extend_titles.to_alipay_dict()
            else:
                params['extend_titles'] = self.extend_titles
        if self.icon:
            if hasattr(self.icon, 'to_alipay_dict'):
                params['icon'] = self.icon.to_alipay_dict()
            else:
                params['icon'] = self.icon
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.is_delete:
            if hasattr(self.is_delete, 'to_alipay_dict'):
                params['is_delete'] = self.is_delete.to_alipay_dict()
            else:
                params['is_delete'] = self.is_delete
        if self.is_searchable:
            if hasattr(self.is_searchable, 'to_alipay_dict'):
                params['is_searchable'] = self.is_searchable.to_alipay_dict()
            else:
                params['is_searchable'] = self.is_searchable
        if self.library_id:
            if hasattr(self.library_id, 'to_alipay_dict'):
                params['library_id'] = self.library_id.to_alipay_dict()
            else:
                params['library_id'] = self.library_id
        if self.library_name:
            if hasattr(self.library_name, 'to_alipay_dict'):
                params['library_name'] = self.library_name.to_alipay_dict()
            else:
                params['library_name'] = self.library_name
        if self.spu:
            if hasattr(self.spu, 'to_alipay_dict'):
                params['spu'] = self.spu.to_alipay_dict()
            else:
                params['spu'] = self.spu
        if self.tags:
            if isinstance(self.tags, list):
                for i in range(0, len(self.tags)):
                    element = self.tags[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tags[i] = element.to_alipay_dict()
            if hasattr(self.tags, 'to_alipay_dict'):
                params['tags'] = self.tags.to_alipay_dict()
            else:
                params['tags'] = self.tags
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
        o = AlipayIserviceCcmSwKnowledgeModifyModel()
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'category_name' in d:
            o.category_name = d['category_name']
        if 'content' in d:
            o.content = d['content']
        if 'ext_id' in d:
            o.ext_id = d['ext_id']
        if 'extend_titles' in d:
            o.extend_titles = d['extend_titles']
        if 'icon' in d:
            o.icon = d['icon']
        if 'id' in d:
            o.id = d['id']
        if 'is_delete' in d:
            o.is_delete = d['is_delete']
        if 'is_searchable' in d:
            o.is_searchable = d['is_searchable']
        if 'library_id' in d:
            o.library_id = d['library_id']
        if 'library_name' in d:
            o.library_name = d['library_name']
        if 'spu' in d:
            o.spu = d['spu']
        if 'tags' in d:
            o.tags = d['tags']
        if 'title' in d:
            o.title = d['title']
        return o


