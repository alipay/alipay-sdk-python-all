#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrderSubmitContent import OrderSubmitContent


class TechriskInnovateSalesgptOrderModifyModel(object):

    def __init__(self):
        self._content = None
        self._method_name = None
        self._user_id = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if isinstance(value, OrderSubmitContent):
            self._content = value
        else:
            self._content = OrderSubmitContent.from_alipay_dict(value)
    @property
    def method_name(self):
        return self._method_name

    @method_name.setter
    def method_name(self, value):
        self._method_name = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.method_name:
            if hasattr(self.method_name, 'to_alipay_dict'):
                params['method_name'] = self.method_name.to_alipay_dict()
            else:
                params['method_name'] = self.method_name
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TechriskInnovateSalesgptOrderModifyModel()
        if 'content' in d:
            o.content = d['content']
        if 'method_name' in d:
            o.method_name = d['method_name']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


