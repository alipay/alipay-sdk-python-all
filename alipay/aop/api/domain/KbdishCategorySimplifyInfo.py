#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbdishCookDetailSimplifyInfo import KbdishCookDetailSimplifyInfo


class KbdishCategorySimplifyInfo(object):

    def __init__(self):
        self._category_name = None
        self._dish_list = None
        self._hidden = None
        self._label_image = None
        self._sort = None

    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, value):
        self._category_name = value
    @property
    def dish_list(self):
        return self._dish_list

    @dish_list.setter
    def dish_list(self, value):
        if isinstance(value, list):
            self._dish_list = list()
            for i in value:
                if isinstance(i, KbdishCookDetailSimplifyInfo):
                    self._dish_list.append(i)
                else:
                    self._dish_list.append(KbdishCookDetailSimplifyInfo.from_alipay_dict(i))
    @property
    def hidden(self):
        return self._hidden

    @hidden.setter
    def hidden(self, value):
        self._hidden = value
    @property
    def label_image(self):
        return self._label_image

    @label_image.setter
    def label_image(self, value):
        self._label_image = value
    @property
    def sort(self):
        return self._sort

    @sort.setter
    def sort(self, value):
        self._sort = value


    def to_alipay_dict(self):
        params = dict()
        if self.category_name:
            if hasattr(self.category_name, 'to_alipay_dict'):
                params['category_name'] = self.category_name.to_alipay_dict()
            else:
                params['category_name'] = self.category_name
        if self.dish_list:
            if isinstance(self.dish_list, list):
                for i in range(0, len(self.dish_list)):
                    element = self.dish_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dish_list[i] = element.to_alipay_dict()
            if hasattr(self.dish_list, 'to_alipay_dict'):
                params['dish_list'] = self.dish_list.to_alipay_dict()
            else:
                params['dish_list'] = self.dish_list
        if self.hidden:
            if hasattr(self.hidden, 'to_alipay_dict'):
                params['hidden'] = self.hidden.to_alipay_dict()
            else:
                params['hidden'] = self.hidden
        if self.label_image:
            if hasattr(self.label_image, 'to_alipay_dict'):
                params['label_image'] = self.label_image.to_alipay_dict()
            else:
                params['label_image'] = self.label_image
        if self.sort:
            if hasattr(self.sort, 'to_alipay_dict'):
                params['sort'] = self.sort.to_alipay_dict()
            else:
                params['sort'] = self.sort
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbdishCategorySimplifyInfo()
        if 'category_name' in d:
            o.category_name = d['category_name']
        if 'dish_list' in d:
            o.dish_list = d['dish_list']
        if 'hidden' in d:
            o.hidden = d['hidden']
        if 'label_image' in d:
            o.label_image = d['label_image']
        if 'sort' in d:
            o.sort = d['sort']
        return o


