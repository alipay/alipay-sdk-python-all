#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecommendQuestion(object):

    def __init__(self):
        self._click_action = None
        self._recommend_query = None
        self._sub_title = None
        self._title = None
        self._url = None

    @property
    def click_action(self):
        return self._click_action

    @click_action.setter
    def click_action(self, value):
        self._click_action = value
    @property
    def recommend_query(self):
        return self._recommend_query

    @recommend_query.setter
    def recommend_query(self, value):
        self._recommend_query = value
    @property
    def sub_title(self):
        return self._sub_title

    @sub_title.setter
    def sub_title(self, value):
        self._sub_title = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.click_action:
            if hasattr(self.click_action, 'to_alipay_dict'):
                params['click_action'] = self.click_action.to_alipay_dict()
            else:
                params['click_action'] = self.click_action
        if self.recommend_query:
            if hasattr(self.recommend_query, 'to_alipay_dict'):
                params['recommend_query'] = self.recommend_query.to_alipay_dict()
            else:
                params['recommend_query'] = self.recommend_query
        if self.sub_title:
            if hasattr(self.sub_title, 'to_alipay_dict'):
                params['sub_title'] = self.sub_title.to_alipay_dict()
            else:
                params['sub_title'] = self.sub_title
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
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
        o = RecommendQuestion()
        if 'click_action' in d:
            o.click_action = d['click_action']
        if 'recommend_query' in d:
            o.recommend_query = d['recommend_query']
        if 'sub_title' in d:
            o.sub_title = d['sub_title']
        if 'title' in d:
            o.title = d['title']
        if 'url' in d:
            o.url = d['url']
        return o


