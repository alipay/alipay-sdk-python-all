#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HomeApiContent import HomeApiContent


class HomeApiRequest(object):

    def __init__(self):
        self._biz_code = None
        self._biz_id = None
        self._content = None
        self._node_code = None
        self._user_id = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if isinstance(value, list):
            self._content = list()
            for i in value:
                if isinstance(i, HomeApiContent):
                    self._content.append(i)
                else:
                    self._content.append(HomeApiContent.from_alipay_dict(i))
    @property
    def node_code(self):
        return self._node_code

    @node_code.setter
    def node_code(self, value):
        self._node_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.content:
            if isinstance(self.content, list):
                for i in range(0, len(self.content)):
                    element = self.content[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.content[i] = element.to_alipay_dict()
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.node_code:
            if hasattr(self.node_code, 'to_alipay_dict'):
                params['node_code'] = self.node_code.to_alipay_dict()
            else:
                params['node_code'] = self.node_code
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
        o = HomeApiRequest()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'content' in d:
            o.content = d['content']
        if 'node_code' in d:
            o.node_code = d['node_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


