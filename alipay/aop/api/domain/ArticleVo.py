#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ArticleVo(object):

    def __init__(self):
        self._article_content = None
        self._article_id = None
        self._article_title = None
        self._article_type = None
        self._avatar = None
        self._doctor_id = None
        self._doctor_name = None
        self._duration = None
        self._hospital_name = None
        self._third_class = None
        self._title = None

    @property
    def article_content(self):
        return self._article_content

    @article_content.setter
    def article_content(self, value):
        self._article_content = value
    @property
    def article_id(self):
        return self._article_id

    @article_id.setter
    def article_id(self, value):
        self._article_id = value
    @property
    def article_title(self):
        return self._article_title

    @article_title.setter
    def article_title(self, value):
        self._article_title = value
    @property
    def article_type(self):
        return self._article_type

    @article_type.setter
    def article_type(self, value):
        self._article_type = value
    @property
    def avatar(self):
        return self._avatar

    @avatar.setter
    def avatar(self, value):
        self._avatar = value
    @property
    def doctor_id(self):
        return self._doctor_id

    @doctor_id.setter
    def doctor_id(self, value):
        self._doctor_id = value
    @property
    def doctor_name(self):
        return self._doctor_name

    @doctor_name.setter
    def doctor_name(self, value):
        self._doctor_name = value
    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value
    @property
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self._hospital_name = value
    @property
    def third_class(self):
        return self._third_class

    @third_class.setter
    def third_class(self, value):
        self._third_class = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.article_content:
            if hasattr(self.article_content, 'to_alipay_dict'):
                params['article_content'] = self.article_content.to_alipay_dict()
            else:
                params['article_content'] = self.article_content
        if self.article_id:
            if hasattr(self.article_id, 'to_alipay_dict'):
                params['article_id'] = self.article_id.to_alipay_dict()
            else:
                params['article_id'] = self.article_id
        if self.article_title:
            if hasattr(self.article_title, 'to_alipay_dict'):
                params['article_title'] = self.article_title.to_alipay_dict()
            else:
                params['article_title'] = self.article_title
        if self.article_type:
            if hasattr(self.article_type, 'to_alipay_dict'):
                params['article_type'] = self.article_type.to_alipay_dict()
            else:
                params['article_type'] = self.article_type
        if self.avatar:
            if hasattr(self.avatar, 'to_alipay_dict'):
                params['avatar'] = self.avatar.to_alipay_dict()
            else:
                params['avatar'] = self.avatar
        if self.doctor_id:
            if hasattr(self.doctor_id, 'to_alipay_dict'):
                params['doctor_id'] = self.doctor_id.to_alipay_dict()
            else:
                params['doctor_id'] = self.doctor_id
        if self.doctor_name:
            if hasattr(self.doctor_name, 'to_alipay_dict'):
                params['doctor_name'] = self.doctor_name.to_alipay_dict()
            else:
                params['doctor_name'] = self.doctor_name
        if self.duration:
            if hasattr(self.duration, 'to_alipay_dict'):
                params['duration'] = self.duration.to_alipay_dict()
            else:
                params['duration'] = self.duration
        if self.hospital_name:
            if hasattr(self.hospital_name, 'to_alipay_dict'):
                params['hospital_name'] = self.hospital_name.to_alipay_dict()
            else:
                params['hospital_name'] = self.hospital_name
        if self.third_class:
            if hasattr(self.third_class, 'to_alipay_dict'):
                params['third_class'] = self.third_class.to_alipay_dict()
            else:
                params['third_class'] = self.third_class
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
        o = ArticleVo()
        if 'article_content' in d:
            o.article_content = d['article_content']
        if 'article_id' in d:
            o.article_id = d['article_id']
        if 'article_title' in d:
            o.article_title = d['article_title']
        if 'article_type' in d:
            o.article_type = d['article_type']
        if 'avatar' in d:
            o.avatar = d['avatar']
        if 'doctor_id' in d:
            o.doctor_id = d['doctor_id']
        if 'doctor_name' in d:
            o.doctor_name = d['doctor_name']
        if 'duration' in d:
            o.duration = d['duration']
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        if 'third_class' in d:
            o.third_class = d['third_class']
        if 'title' in d:
            o.title = d['title']
        return o


