#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SearchOrderDetailDataBaseItems(object):

    def __init__(self):
        self._can_search = None
        self._desc = None
        self._img = None
        self._key_word = None
        self._name = None
        self._region = None
        self._serv_can_search = None
        self._serv_search_keywords = None
        self._template_id = None
        self._url = None

    @property
    def can_search(self):
        return self._can_search

    @can_search.setter
    def can_search(self, value):
        self._can_search = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def img(self):
        return self._img

    @img.setter
    def img(self, value):
        self._img = value
    @property
    def key_word(self):
        return self._key_word

    @key_word.setter
    def key_word(self, value):
        self._key_word = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, value):
        self._region = value
    @property
    def serv_can_search(self):
        return self._serv_can_search

    @serv_can_search.setter
    def serv_can_search(self, value):
        self._serv_can_search = value
    @property
    def serv_search_keywords(self):
        return self._serv_search_keywords

    @serv_search_keywords.setter
    def serv_search_keywords(self, value):
        self._serv_search_keywords = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.can_search:
            if hasattr(self.can_search, 'to_alipay_dict'):
                params['can_search'] = self.can_search.to_alipay_dict()
            else:
                params['can_search'] = self.can_search
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.img:
            if hasattr(self.img, 'to_alipay_dict'):
                params['img'] = self.img.to_alipay_dict()
            else:
                params['img'] = self.img
        if self.key_word:
            if hasattr(self.key_word, 'to_alipay_dict'):
                params['key_word'] = self.key_word.to_alipay_dict()
            else:
                params['key_word'] = self.key_word
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.region:
            if hasattr(self.region, 'to_alipay_dict'):
                params['region'] = self.region.to_alipay_dict()
            else:
                params['region'] = self.region
        if self.serv_can_search:
            if hasattr(self.serv_can_search, 'to_alipay_dict'):
                params['serv_can_search'] = self.serv_can_search.to_alipay_dict()
            else:
                params['serv_can_search'] = self.serv_can_search
        if self.serv_search_keywords:
            if hasattr(self.serv_search_keywords, 'to_alipay_dict'):
                params['serv_search_keywords'] = self.serv_search_keywords.to_alipay_dict()
            else:
                params['serv_search_keywords'] = self.serv_search_keywords
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SearchOrderDetailDataBaseItems()
        if 'can_search' in d:
            o.can_search = d['can_search']
        if 'desc' in d:
            o.desc = d['desc']
        if 'img' in d:
            o.img = d['img']
        if 'key_word' in d:
            o.key_word = d['key_word']
        if 'name' in d:
            o.name = d['name']
        if 'region' in d:
            o.region = d['region']
        if 'serv_can_search' in d:
            o.serv_can_search = d['serv_can_search']
        if 'serv_search_keywords' in d:
            o.serv_search_keywords = d['serv_search_keywords']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'url' in d:
            o.url = d['url']
        return o


