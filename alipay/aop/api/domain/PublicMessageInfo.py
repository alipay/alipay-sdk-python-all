#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ImageTextItem import ImageTextItem


class PublicMessageInfo(object):

    def __init__(self):
        self._articles = None
        self._message_id = None
        self._send_time = None
        self._status = None
        self._status_desc = None

    @property
    def articles(self):
        return self._articles

    @articles.setter
    def articles(self, value):
        if isinstance(value, list):
            self._articles = list()
            for i in value:
                if isinstance(i, ImageTextItem):
                    self._articles.append(i)
                else:
                    self._articles.append(ImageTextItem.from_alipay_dict(i))
    @property
    def message_id(self):
        return self._message_id

    @message_id.setter
    def message_id(self, value):
        self._message_id = value
    @property
    def send_time(self):
        return self._send_time

    @send_time.setter
    def send_time(self, value):
        self._send_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def status_desc(self):
        return self._status_desc

    @status_desc.setter
    def status_desc(self, value):
        self._status_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.articles:
            if isinstance(self.articles, list):
                for i in range(0, len(self.articles)):
                    element = self.articles[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.articles[i] = element.to_alipay_dict()
            if hasattr(self.articles, 'to_alipay_dict'):
                params['articles'] = self.articles.to_alipay_dict()
            else:
                params['articles'] = self.articles
        if self.message_id:
            if hasattr(self.message_id, 'to_alipay_dict'):
                params['message_id'] = self.message_id.to_alipay_dict()
            else:
                params['message_id'] = self.message_id
        if self.send_time:
            if hasattr(self.send_time, 'to_alipay_dict'):
                params['send_time'] = self.send_time.to_alipay_dict()
            else:
                params['send_time'] = self.send_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.status_desc:
            if hasattr(self.status_desc, 'to_alipay_dict'):
                params['status_desc'] = self.status_desc.to_alipay_dict()
            else:
                params['status_desc'] = self.status_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PublicMessageInfo()
        if 'articles' in d:
            o.articles = d['articles']
        if 'message_id' in d:
            o.message_id = d['message_id']
        if 'send_time' in d:
            o.send_time = d['send_time']
        if 'status' in d:
            o.status = d['status']
        if 'status_desc' in d:
            o.status_desc = d['status_desc']
        return o


