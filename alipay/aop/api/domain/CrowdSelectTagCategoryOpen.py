#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CrowdSelectTagOptionOpen import CrowdSelectTagOptionOpen


class CrowdSelectTagCategoryOpen(object):

    def __init__(self):
        self._tag_option_category_id = None
        self._tag_option_category_name = None
        self._tag_option_list = None

    @property
    def tag_option_category_id(self):
        return self._tag_option_category_id

    @tag_option_category_id.setter
    def tag_option_category_id(self, value):
        self._tag_option_category_id = value
    @property
    def tag_option_category_name(self):
        return self._tag_option_category_name

    @tag_option_category_name.setter
    def tag_option_category_name(self, value):
        self._tag_option_category_name = value
    @property
    def tag_option_list(self):
        return self._tag_option_list

    @tag_option_list.setter
    def tag_option_list(self, value):
        if isinstance(value, list):
            self._tag_option_list = list()
            for i in value:
                if isinstance(i, CrowdSelectTagOptionOpen):
                    self._tag_option_list.append(i)
                else:
                    self._tag_option_list.append(CrowdSelectTagOptionOpen.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.tag_option_category_id:
            if hasattr(self.tag_option_category_id, 'to_alipay_dict'):
                params['tag_option_category_id'] = self.tag_option_category_id.to_alipay_dict()
            else:
                params['tag_option_category_id'] = self.tag_option_category_id
        if self.tag_option_category_name:
            if hasattr(self.tag_option_category_name, 'to_alipay_dict'):
                params['tag_option_category_name'] = self.tag_option_category_name.to_alipay_dict()
            else:
                params['tag_option_category_name'] = self.tag_option_category_name
        if self.tag_option_list:
            if isinstance(self.tag_option_list, list):
                for i in range(0, len(self.tag_option_list)):
                    element = self.tag_option_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tag_option_list[i] = element.to_alipay_dict()
            if hasattr(self.tag_option_list, 'to_alipay_dict'):
                params['tag_option_list'] = self.tag_option_list.to_alipay_dict()
            else:
                params['tag_option_list'] = self.tag_option_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CrowdSelectTagCategoryOpen()
        if 'tag_option_category_id' in d:
            o.tag_option_category_id = d['tag_option_category_id']
        if 'tag_option_category_name' in d:
            o.tag_option_category_name = d['tag_option_category_name']
        if 'tag_option_list' in d:
            o.tag_option_list = d['tag_option_list']
        return o


