#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AIDongSubjectSyncDetail(object):

    def __init__(self):
        self._description = None
        self._head_image = None
        self._image = None
        self._lesson_id_list = None
        self._name = None
        self._tag = None

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def head_image(self):
        return self._head_image

    @head_image.setter
    def head_image(self, value):
        self._head_image = value
    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value
    @property
    def lesson_id_list(self):
        return self._lesson_id_list

    @lesson_id_list.setter
    def lesson_id_list(self, value):
        if isinstance(value, list):
            self._lesson_id_list = list()
            for i in value:
                self._lesson_id_list.append(i)
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, value):
        if isinstance(value, list):
            self._tag = list()
            for i in value:
                self._tag.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.head_image:
            if hasattr(self.head_image, 'to_alipay_dict'):
                params['head_image'] = self.head_image.to_alipay_dict()
            else:
                params['head_image'] = self.head_image
        if self.image:
            if hasattr(self.image, 'to_alipay_dict'):
                params['image'] = self.image.to_alipay_dict()
            else:
                params['image'] = self.image
        if self.lesson_id_list:
            if isinstance(self.lesson_id_list, list):
                for i in range(0, len(self.lesson_id_list)):
                    element = self.lesson_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.lesson_id_list[i] = element.to_alipay_dict()
            if hasattr(self.lesson_id_list, 'to_alipay_dict'):
                params['lesson_id_list'] = self.lesson_id_list.to_alipay_dict()
            else:
                params['lesson_id_list'] = self.lesson_id_list
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.tag:
            if isinstance(self.tag, list):
                for i in range(0, len(self.tag)):
                    element = self.tag[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tag[i] = element.to_alipay_dict()
            if hasattr(self.tag, 'to_alipay_dict'):
                params['tag'] = self.tag.to_alipay_dict()
            else:
                params['tag'] = self.tag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AIDongSubjectSyncDetail()
        if 'description' in d:
            o.description = d['description']
        if 'head_image' in d:
            o.head_image = d['head_image']
        if 'image' in d:
            o.image = d['image']
        if 'lesson_id_list' in d:
            o.lesson_id_list = d['lesson_id_list']
        if 'name' in d:
            o.name = d['name']
        if 'tag' in d:
            o.tag = d['tag']
        return o


