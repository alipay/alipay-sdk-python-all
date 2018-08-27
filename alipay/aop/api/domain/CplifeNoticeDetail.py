#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CplifeNoticeImg import CplifeNoticeImg


class CplifeNoticeDetail(object):

    def __init__(self):
        self._content = None
        self._end_time = None
        self._image_list = None
        self._start_time = None
        self._stickied = None
        self._title = None
        self._type = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def image_list(self):
        return self._image_list

    @image_list.setter
    def image_list(self, value):
        if isinstance(value, list):
            self._image_list = list()
            for i in value:
                if isinstance(i, CplifeNoticeImg):
                    self._image_list.append(i)
                else:
                    self._image_list.append(CplifeNoticeImg.from_alipay_dict(i))
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def stickied(self):
        return self._stickied

    @stickied.setter
    def stickied(self, value):
        self._stickied = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.image_list:
            if isinstance(self.image_list, list):
                for i in range(0, len(self.image_list)):
                    element = self.image_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.image_list[i] = element.to_alipay_dict()
            if hasattr(self.image_list, 'to_alipay_dict'):
                params['image_list'] = self.image_list.to_alipay_dict()
            else:
                params['image_list'] = self.image_list
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.stickied:
            if hasattr(self.stickied, 'to_alipay_dict'):
                params['stickied'] = self.stickied.to_alipay_dict()
            else:
                params['stickied'] = self.stickied
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CplifeNoticeDetail()
        if 'content' in d:
            o.content = d['content']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'image_list' in d:
            o.image_list = d['image_list']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'stickied' in d:
            o.stickied = d['stickied']
        if 'title' in d:
            o.title = d['title']
        if 'type' in d:
            o.type = d['type']
        return o


