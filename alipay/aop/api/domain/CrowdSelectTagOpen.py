#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CrowdSelectTagCategoryOpen import CrowdSelectTagCategoryOpen


class CrowdSelectTagOpen(object):

    def __init__(self):
        self._category_tag_option_list = None
        self._tag_id = None
        self._tag_name = None

    @property
    def category_tag_option_list(self):
        return self._category_tag_option_list

    @category_tag_option_list.setter
    def category_tag_option_list(self, value):
        if isinstance(value, list):
            self._category_tag_option_list = list()
            for i in value:
                if isinstance(i, CrowdSelectTagCategoryOpen):
                    self._category_tag_option_list.append(i)
                else:
                    self._category_tag_option_list.append(CrowdSelectTagCategoryOpen.from_alipay_dict(i))
    @property
    def tag_id(self):
        return self._tag_id

    @tag_id.setter
    def tag_id(self, value):
        self._tag_id = value
    @property
    def tag_name(self):
        return self._tag_name

    @tag_name.setter
    def tag_name(self, value):
        self._tag_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.category_tag_option_list:
            if isinstance(self.category_tag_option_list, list):
                for i in range(0, len(self.category_tag_option_list)):
                    element = self.category_tag_option_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.category_tag_option_list[i] = element.to_alipay_dict()
            if hasattr(self.category_tag_option_list, 'to_alipay_dict'):
                params['category_tag_option_list'] = self.category_tag_option_list.to_alipay_dict()
            else:
                params['category_tag_option_list'] = self.category_tag_option_list
        if self.tag_id:
            if hasattr(self.tag_id, 'to_alipay_dict'):
                params['tag_id'] = self.tag_id.to_alipay_dict()
            else:
                params['tag_id'] = self.tag_id
        if self.tag_name:
            if hasattr(self.tag_name, 'to_alipay_dict'):
                params['tag_name'] = self.tag_name.to_alipay_dict()
            else:
                params['tag_name'] = self.tag_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CrowdSelectTagOpen()
        if 'category_tag_option_list' in d:
            o.category_tag_option_list = d['category_tag_option_list']
        if 'tag_id' in d:
            o.tag_id = d['tag_id']
        if 'tag_name' in d:
            o.tag_name = d['tag_name']
        return o


