#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WeikeTaskView(object):

    def __init__(self):
        self._desc = None
        self._id = None
        self._img = None
        self._name = None
        self._salary = None
        self._task_count = None
        self._url = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def img(self):
        return self._img

    @img.setter
    def img(self, value):
        self._img = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value
    @property
    def task_count(self):
        return self._task_count

    @task_count.setter
    def task_count(self, value):
        self._task_count = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.img:
            if hasattr(self.img, 'to_alipay_dict'):
                params['img'] = self.img.to_alipay_dict()
            else:
                params['img'] = self.img
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.salary:
            if hasattr(self.salary, 'to_alipay_dict'):
                params['salary'] = self.salary.to_alipay_dict()
            else:
                params['salary'] = self.salary
        if self.task_count:
            if hasattr(self.task_count, 'to_alipay_dict'):
                params['task_count'] = self.task_count.to_alipay_dict()
            else:
                params['task_count'] = self.task_count
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
        o = WeikeTaskView()
        if 'desc' in d:
            o.desc = d['desc']
        if 'id' in d:
            o.id = d['id']
        if 'img' in d:
            o.img = d['img']
        if 'name' in d:
            o.name = d['name']
        if 'salary' in d:
            o.salary = d['salary']
        if 'task_count' in d:
            o.task_count = d['task_count']
        if 'url' in d:
            o.url = d['url']
        return o


