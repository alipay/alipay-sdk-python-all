#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ArticleCategoryInfo(object):

    def __init__(self):
        self._children = None
        self._description = None
        self._father_id = None
        self._id = None
        self._name = None
        self._tags = None

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, value):
        if isinstance(value, list):
            self._children = list()
            for i in value:
                self._children.append(i)
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def father_id(self):
        return self._father_id

    @father_id.setter
    def father_id(self, value):
        self._father_id = value
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
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        if isinstance(value, list):
            self._tags = list()
            for i in value:
                self._tags.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.children:
            if isinstance(self.children, list):
                for i in range(0, len(self.children)):
                    element = self.children[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.children[i] = element.to_alipay_dict()
            if hasattr(self.children, 'to_alipay_dict'):
                params['children'] = self.children.to_alipay_dict()
            else:
                params['children'] = self.children
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.father_id:
            if hasattr(self.father_id, 'to_alipay_dict'):
                params['father_id'] = self.father_id.to_alipay_dict()
            else:
                params['father_id'] = self.father_id
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ArticleCategoryInfo()
        if 'children' in d:
            o.children = d['children']
        if 'description' in d:
            o.description = d['description']
        if 'father_id' in d:
            o.father_id = d['father_id']
        if 'id' in d:
            o.id = d['id']
        if 'name' in d:
            o.name = d['name']
        if 'tags' in d:
            o.tags = d['tags']
        return o


