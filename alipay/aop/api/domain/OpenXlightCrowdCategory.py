#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenXlightCrowdChildLevelOne import OpenXlightCrowdChildLevelOne


class OpenXlightCrowdCategory(object):

    def __init__(self):
        self._children = None
        self._name = None
        self._tag_id = None
        self._user_num = None

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, value):
        if isinstance(value, list):
            self._children = list()
            for i in value:
                if isinstance(i, OpenXlightCrowdChildLevelOne):
                    self._children.append(i)
                else:
                    self._children.append(OpenXlightCrowdChildLevelOne.from_alipay_dict(i))
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def tag_id(self):
        return self._tag_id

    @tag_id.setter
    def tag_id(self, value):
        self._tag_id = value
    @property
    def user_num(self):
        return self._user_num

    @user_num.setter
    def user_num(self, value):
        self._user_num = value


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
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.tag_id:
            if hasattr(self.tag_id, 'to_alipay_dict'):
                params['tag_id'] = self.tag_id.to_alipay_dict()
            else:
                params['tag_id'] = self.tag_id
        if self.user_num:
            if hasattr(self.user_num, 'to_alipay_dict'):
                params['user_num'] = self.user_num.to_alipay_dict()
            else:
                params['user_num'] = self.user_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenXlightCrowdCategory()
        if 'children' in d:
            o.children = d['children']
        if 'name' in d:
            o.name = d['name']
        if 'tag_id' in d:
            o.tag_id = d['tag_id']
        if 'user_num' in d:
            o.user_num = d['user_num']
        return o


