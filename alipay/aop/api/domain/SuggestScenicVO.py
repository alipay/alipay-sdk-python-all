#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SuggestScenicVO(object):

    def __init__(self):
        self._suggest_pic_url = None
        self._suggest_rating = None
        self._suggest_time = None
        self._suggest_title = None

    @property
    def suggest_pic_url(self):
        return self._suggest_pic_url

    @suggest_pic_url.setter
    def suggest_pic_url(self, value):
        self._suggest_pic_url = value
    @property
    def suggest_rating(self):
        return self._suggest_rating

    @suggest_rating.setter
    def suggest_rating(self, value):
        self._suggest_rating = value
    @property
    def suggest_time(self):
        return self._suggest_time

    @suggest_time.setter
    def suggest_time(self, value):
        self._suggest_time = value
    @property
    def suggest_title(self):
        return self._suggest_title

    @suggest_title.setter
    def suggest_title(self, value):
        self._suggest_title = value


    def to_alipay_dict(self):
        params = dict()
        if self.suggest_pic_url:
            if hasattr(self.suggest_pic_url, 'to_alipay_dict'):
                params['suggest_pic_url'] = self.suggest_pic_url.to_alipay_dict()
            else:
                params['suggest_pic_url'] = self.suggest_pic_url
        if self.suggest_rating:
            if hasattr(self.suggest_rating, 'to_alipay_dict'):
                params['suggest_rating'] = self.suggest_rating.to_alipay_dict()
            else:
                params['suggest_rating'] = self.suggest_rating
        if self.suggest_time:
            if hasattr(self.suggest_time, 'to_alipay_dict'):
                params['suggest_time'] = self.suggest_time.to_alipay_dict()
            else:
                params['suggest_time'] = self.suggest_time
        if self.suggest_title:
            if hasattr(self.suggest_title, 'to_alipay_dict'):
                params['suggest_title'] = self.suggest_title.to_alipay_dict()
            else:
                params['suggest_title'] = self.suggest_title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SuggestScenicVO()
        if 'suggest_pic_url' in d:
            o.suggest_pic_url = d['suggest_pic_url']
        if 'suggest_rating' in d:
            o.suggest_rating = d['suggest_rating']
        if 'suggest_time' in d:
            o.suggest_time = d['suggest_time']
        if 'suggest_title' in d:
            o.suggest_title = d['suggest_title']
        return o


