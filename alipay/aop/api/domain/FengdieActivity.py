#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FengdieActivityPage import FengdieActivityPage


class FengdieActivity(object):

    def __init__(self):
        self._id = None
        self._is_online = None
        self._name = None
        self._nick_name = None
        self._offline_time = None
        self._page = None
        self._publish_time = None
        self._status = None
        self._template_id = None
        self._title = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def is_online(self):
        return self._is_online

    @is_online.setter
    def is_online(self, value):
        self._is_online = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def nick_name(self):
        return self._nick_name

    @nick_name.setter
    def nick_name(self, value):
        self._nick_name = value
    @property
    def offline_time(self):
        return self._offline_time

    @offline_time.setter
    def offline_time(self, value):
        self._offline_time = value
    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        if isinstance(value, list):
            self._page = list()
            for i in value:
                if isinstance(i, FengdieActivityPage):
                    self._page.append(i)
                else:
                    self._page.append(FengdieActivityPage.from_alipay_dict(i))
    @property
    def publish_time(self):
        return self._publish_time

    @publish_time.setter
    def publish_time(self, value):
        self._publish_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.is_online:
            if hasattr(self.is_online, 'to_alipay_dict'):
                params['is_online'] = self.is_online.to_alipay_dict()
            else:
                params['is_online'] = self.is_online
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.nick_name:
            if hasattr(self.nick_name, 'to_alipay_dict'):
                params['nick_name'] = self.nick_name.to_alipay_dict()
            else:
                params['nick_name'] = self.nick_name
        if self.offline_time:
            if hasattr(self.offline_time, 'to_alipay_dict'):
                params['offline_time'] = self.offline_time.to_alipay_dict()
            else:
                params['offline_time'] = self.offline_time
        if self.page:
            if isinstance(self.page, list):
                for i in range(0, len(self.page)):
                    element = self.page[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.page[i] = element.to_alipay_dict()
            if hasattr(self.page, 'to_alipay_dict'):
                params['page'] = self.page.to_alipay_dict()
            else:
                params['page'] = self.page
        if self.publish_time:
            if hasattr(self.publish_time, 'to_alipay_dict'):
                params['publish_time'] = self.publish_time.to_alipay_dict()
            else:
                params['publish_time'] = self.publish_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
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
        o = FengdieActivity()
        if 'id' in d:
            o.id = d['id']
        if 'is_online' in d:
            o.is_online = d['is_online']
        if 'name' in d:
            o.name = d['name']
        if 'nick_name' in d:
            o.nick_name = d['nick_name']
        if 'offline_time' in d:
            o.offline_time = d['offline_time']
        if 'page' in d:
            o.page = d['page']
        if 'publish_time' in d:
            o.publish_time = d['publish_time']
        if 'status' in d:
            o.status = d['status']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'title' in d:
            o.title = d['title']
        return o


