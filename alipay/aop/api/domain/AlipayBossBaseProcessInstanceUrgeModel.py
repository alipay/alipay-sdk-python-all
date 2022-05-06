#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossBaseProcessInstanceUrgeModel(object):

    def __init__(self):
        self._code = None
        self._msg_template = None
        self._msg_type_list = None
        self._puid = None
        self._title = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def msg_template(self):
        return self._msg_template

    @msg_template.setter
    def msg_template(self, value):
        self._msg_template = value
    @property
    def msg_type_list(self):
        return self._msg_type_list

    @msg_type_list.setter
    def msg_type_list(self, value):
        if isinstance(value, list):
            self._msg_type_list = list()
            for i in value:
                self._msg_type_list.append(i)
    @property
    def puid(self):
        return self._puid

    @puid.setter
    def puid(self, value):
        self._puid = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.msg_template:
            if hasattr(self.msg_template, 'to_alipay_dict'):
                params['msg_template'] = self.msg_template.to_alipay_dict()
            else:
                params['msg_template'] = self.msg_template
        if self.msg_type_list:
            if isinstance(self.msg_type_list, list):
                for i in range(0, len(self.msg_type_list)):
                    element = self.msg_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.msg_type_list[i] = element.to_alipay_dict()
            if hasattr(self.msg_type_list, 'to_alipay_dict'):
                params['msg_type_list'] = self.msg_type_list.to_alipay_dict()
            else:
                params['msg_type_list'] = self.msg_type_list
        if self.puid:
            if hasattr(self.puid, 'to_alipay_dict'):
                params['puid'] = self.puid.to_alipay_dict()
            else:
                params['puid'] = self.puid
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
        o = AlipayBossBaseProcessInstanceUrgeModel()
        if 'code' in d:
            o.code = d['code']
        if 'msg_template' in d:
            o.msg_template = d['msg_template']
        if 'msg_type_list' in d:
            o.msg_type_list = d['msg_type_list']
        if 'puid' in d:
            o.puid = d['puid']
        if 'title' in d:
            o.title = d['title']
        return o


