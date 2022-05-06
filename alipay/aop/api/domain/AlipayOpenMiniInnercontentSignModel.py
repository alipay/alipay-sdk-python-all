#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SignContentBodyRequest import SignContentBodyRequest


class AlipayOpenMiniInnercontentSignModel(object):

    def __init__(self):
        self._content_list = None
        self._inst_code = None
        self._mini_app_id = None

    @property
    def content_list(self):
        return self._content_list

    @content_list.setter
    def content_list(self, value):
        if isinstance(value, list):
            self._content_list = list()
            for i in value:
                if isinstance(i, SignContentBodyRequest):
                    self._content_list.append(i)
                else:
                    self._content_list.append(SignContentBodyRequest.from_alipay_dict(i))
    @property
    def inst_code(self):
        return self._inst_code

    @inst_code.setter
    def inst_code(self, value):
        self._inst_code = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.content_list:
            if isinstance(self.content_list, list):
                for i in range(0, len(self.content_list)):
                    element = self.content_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.content_list[i] = element.to_alipay_dict()
            if hasattr(self.content_list, 'to_alipay_dict'):
                params['content_list'] = self.content_list.to_alipay_dict()
            else:
                params['content_list'] = self.content_list
        if self.inst_code:
            if hasattr(self.inst_code, 'to_alipay_dict'):
                params['inst_code'] = self.inst_code.to_alipay_dict()
            else:
                params['inst_code'] = self.inst_code
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniInnercontentSignModel()
        if 'content_list' in d:
            o.content_list = d['content_list']
        if 'inst_code' in d:
            o.inst_code = d['inst_code']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        return o


