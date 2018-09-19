#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PassTemplateDetail(object):

    def __init__(self):
        self._create_time = None
        self._modify_time = None
        self._tpl_content = None
        self._tpl_id = None
        self._tpl_params = None

    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def modify_time(self):
        return self._modify_time

    @modify_time.setter
    def modify_time(self, value):
        self._modify_time = value
    @property
    def tpl_content(self):
        return self._tpl_content

    @tpl_content.setter
    def tpl_content(self, value):
        self._tpl_content = value
    @property
    def tpl_id(self):
        return self._tpl_id

    @tpl_id.setter
    def tpl_id(self, value):
        self._tpl_id = value
    @property
    def tpl_params(self):
        return self._tpl_params

    @tpl_params.setter
    def tpl_params(self, value):
        if isinstance(value, list):
            self._tpl_params = list()
            for i in value:
                self._tpl_params.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.modify_time:
            if hasattr(self.modify_time, 'to_alipay_dict'):
                params['modify_time'] = self.modify_time.to_alipay_dict()
            else:
                params['modify_time'] = self.modify_time
        if self.tpl_content:
            if hasattr(self.tpl_content, 'to_alipay_dict'):
                params['tpl_content'] = self.tpl_content.to_alipay_dict()
            else:
                params['tpl_content'] = self.tpl_content
        if self.tpl_id:
            if hasattr(self.tpl_id, 'to_alipay_dict'):
                params['tpl_id'] = self.tpl_id.to_alipay_dict()
            else:
                params['tpl_id'] = self.tpl_id
        if self.tpl_params:
            if isinstance(self.tpl_params, list):
                for i in range(0, len(self.tpl_params)):
                    element = self.tpl_params[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tpl_params[i] = element.to_alipay_dict()
            if hasattr(self.tpl_params, 'to_alipay_dict'):
                params['tpl_params'] = self.tpl_params.to_alipay_dict()
            else:
                params['tpl_params'] = self.tpl_params
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PassTemplateDetail()
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'modify_time' in d:
            o.modify_time = d['modify_time']
        if 'tpl_content' in d:
            o.tpl_content = d['tpl_content']
        if 'tpl_id' in d:
            o.tpl_id = d['tpl_id']
        if 'tpl_params' in d:
            o.tpl_params = d['tpl_params']
        return o


