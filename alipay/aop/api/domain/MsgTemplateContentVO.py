#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KeywordVO import KeywordVO


class MsgTemplateContentVO(object):

    def __init__(self):
        self._jump_url = None
        self._keyword_list = None
        self._title = None

    @property
    def jump_url(self):
        return self._jump_url

    @jump_url.setter
    def jump_url(self, value):
        self._jump_url = value
    @property
    def keyword_list(self):
        return self._keyword_list

    @keyword_list.setter
    def keyword_list(self, value):
        if isinstance(value, list):
            self._keyword_list = list()
            for i in value:
                if isinstance(i, KeywordVO):
                    self._keyword_list.append(i)
                else:
                    self._keyword_list.append(KeywordVO.from_alipay_dict(i))
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.jump_url:
            if hasattr(self.jump_url, 'to_alipay_dict'):
                params['jump_url'] = self.jump_url.to_alipay_dict()
            else:
                params['jump_url'] = self.jump_url
        if self.keyword_list:
            if isinstance(self.keyword_list, list):
                for i in range(0, len(self.keyword_list)):
                    element = self.keyword_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.keyword_list[i] = element.to_alipay_dict()
            if hasattr(self.keyword_list, 'to_alipay_dict'):
                params['keyword_list'] = self.keyword_list.to_alipay_dict()
            else:
                params['keyword_list'] = self.keyword_list
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
        o = MsgTemplateContentVO()
        if 'jump_url' in d:
            o.jump_url = d['jump_url']
        if 'keyword_list' in d:
            o.keyword_list = d['keyword_list']
        if 'title' in d:
            o.title = d['title']
        return o


