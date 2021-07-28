#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniResourceRecordNotifyModel(object):

    def __init__(self):
        self._author_id = None
        self._mini_app_id = None
        self._params = None
        self._site_id = None
        self._source = None
        self._taobao_id = None
        self._taobao_nick = None

    @property
    def author_id(self):
        return self._author_id

    @author_id.setter
    def author_id(self, value):
        self._author_id = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        self._params = value
    @property
    def site_id(self):
        return self._site_id

    @site_id.setter
    def site_id(self, value):
        self._site_id = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def taobao_id(self):
        return self._taobao_id

    @taobao_id.setter
    def taobao_id(self, value):
        self._taobao_id = value
    @property
    def taobao_nick(self):
        return self._taobao_nick

    @taobao_nick.setter
    def taobao_nick(self, value):
        self._taobao_nick = value


    def to_alipay_dict(self):
        params = dict()
        if self.author_id:
            if hasattr(self.author_id, 'to_alipay_dict'):
                params['author_id'] = self.author_id.to_alipay_dict()
            else:
                params['author_id'] = self.author_id
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.params:
            if hasattr(self.params, 'to_alipay_dict'):
                params['params'] = self.params.to_alipay_dict()
            else:
                params['params'] = self.params
        if self.site_id:
            if hasattr(self.site_id, 'to_alipay_dict'):
                params['site_id'] = self.site_id.to_alipay_dict()
            else:
                params['site_id'] = self.site_id
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.taobao_id:
            if hasattr(self.taobao_id, 'to_alipay_dict'):
                params['taobao_id'] = self.taobao_id.to_alipay_dict()
            else:
                params['taobao_id'] = self.taobao_id
        if self.taobao_nick:
            if hasattr(self.taobao_nick, 'to_alipay_dict'):
                params['taobao_nick'] = self.taobao_nick.to_alipay_dict()
            else:
                params['taobao_nick'] = self.taobao_nick
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniResourceRecordNotifyModel()
        if 'author_id' in d:
            o.author_id = d['author_id']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'params' in d:
            o.params = d['params']
        if 'site_id' in d:
            o.site_id = d['site_id']
        if 'source' in d:
            o.source = d['source']
        if 'taobao_id' in d:
            o.taobao_id = d['taobao_id']
        if 'taobao_nick' in d:
            o.taobao_nick = d['taobao_nick']
        return o


