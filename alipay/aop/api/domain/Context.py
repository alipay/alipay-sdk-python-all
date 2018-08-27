#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Keyword import Keyword
from alipay.aop.api.domain.Keyword import Keyword
from alipay.aop.api.domain.Keyword import Keyword
from alipay.aop.api.domain.Keyword import Keyword


class Context(object):

    def __init__(self):
        self._action_name = None
        self._first = None
        self._head_color = None
        self._keyword1 = None
        self._keyword2 = None
        self._remark = None
        self._url = None

    @property
    def action_name(self):
        return self._action_name

    @action_name.setter
    def action_name(self, value):
        self._action_name = value
    @property
    def first(self):
        return self._first

    @first.setter
    def first(self, value):
        if isinstance(value, Keyword):
            self._first = value
        else:
            self._first = Keyword.from_alipay_dict(value)
    @property
    def head_color(self):
        return self._head_color

    @head_color.setter
    def head_color(self, value):
        self._head_color = value
    @property
    def keyword1(self):
        return self._keyword1

    @keyword1.setter
    def keyword1(self, value):
        if isinstance(value, Keyword):
            self._keyword1 = value
        else:
            self._keyword1 = Keyword.from_alipay_dict(value)
    @property
    def keyword2(self):
        return self._keyword2

    @keyword2.setter
    def keyword2(self, value):
        if isinstance(value, Keyword):
            self._keyword2 = value
        else:
            self._keyword2 = Keyword.from_alipay_dict(value)
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        if isinstance(value, Keyword):
            self._remark = value
        else:
            self._remark = Keyword.from_alipay_dict(value)
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_name:
            if hasattr(self.action_name, 'to_alipay_dict'):
                params['action_name'] = self.action_name.to_alipay_dict()
            else:
                params['action_name'] = self.action_name
        if self.first:
            if hasattr(self.first, 'to_alipay_dict'):
                params['first'] = self.first.to_alipay_dict()
            else:
                params['first'] = self.first
        if self.head_color:
            if hasattr(self.head_color, 'to_alipay_dict'):
                params['head_color'] = self.head_color.to_alipay_dict()
            else:
                params['head_color'] = self.head_color
        if self.keyword1:
            if hasattr(self.keyword1, 'to_alipay_dict'):
                params['keyword1'] = self.keyword1.to_alipay_dict()
            else:
                params['keyword1'] = self.keyword1
        if self.keyword2:
            if hasattr(self.keyword2, 'to_alipay_dict'):
                params['keyword2'] = self.keyword2.to_alipay_dict()
            else:
                params['keyword2'] = self.keyword2
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
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
        o = Context()
        if 'action_name' in d:
            o.action_name = d['action_name']
        if 'first' in d:
            o.first = d['first']
        if 'head_color' in d:
            o.head_color = d['head_color']
        if 'keyword1' in d:
            o.keyword1 = d['keyword1']
        if 'keyword2' in d:
            o.keyword2 = d['keyword2']
        if 'remark' in d:
            o.remark = d['remark']
        if 'url' in d:
            o.url = d['url']
        return o


