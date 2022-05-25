#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TagDTO import TagDTO
from alipay.aop.api.domain.TwoCategoryDTO import TwoCategoryDTO


class OneCategoryDTO(object):

    def __init__(self):
        self._category_id = None
        self._category_name = None
        self._tag_dto_list = None
        self._two_category_dto_list = None

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
    def tag_dto_list(self):
        return self._tag_dto_list

    @tag_dto_list.setter
    def tag_dto_list(self, value):
        if isinstance(value, list):
            self._tag_dto_list = list()
            for i in value:
                if isinstance(i, TagDTO):
                    self._tag_dto_list.append(i)
                else:
                    self._tag_dto_list.append(TagDTO.from_alipay_dict(i))
    @property
    def two_category_dto_list(self):
        return self._two_category_dto_list

    @two_category_dto_list.setter
    def two_category_dto_list(self, value):
        if isinstance(value, list):
            self._two_category_dto_list = list()
            for i in value:
                if isinstance(i, TwoCategoryDTO):
                    self._two_category_dto_list.append(i)
                else:
                    self._two_category_dto_list.append(TwoCategoryDTO.from_alipay_dict(i))


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
        if self.tag_dto_list:
            if isinstance(self.tag_dto_list, list):
                for i in range(0, len(self.tag_dto_list)):
                    element = self.tag_dto_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tag_dto_list[i] = element.to_alipay_dict()
            if hasattr(self.tag_dto_list, 'to_alipay_dict'):
                params['tag_dto_list'] = self.tag_dto_list.to_alipay_dict()
            else:
                params['tag_dto_list'] = self.tag_dto_list
        if self.two_category_dto_list:
            if isinstance(self.two_category_dto_list, list):
                for i in range(0, len(self.two_category_dto_list)):
                    element = self.two_category_dto_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.two_category_dto_list[i] = element.to_alipay_dict()
            if hasattr(self.two_category_dto_list, 'to_alipay_dict'):
                params['two_category_dto_list'] = self.two_category_dto_list.to_alipay_dict()
            else:
                params['two_category_dto_list'] = self.two_category_dto_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OneCategoryDTO()
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'category_name' in d:
            o.category_name = d['category_name']
        if 'tag_dto_list' in d:
            o.tag_dto_list = d['tag_dto_list']
        if 'two_category_dto_list' in d:
            o.two_category_dto_list = d['two_category_dto_list']
        return o


