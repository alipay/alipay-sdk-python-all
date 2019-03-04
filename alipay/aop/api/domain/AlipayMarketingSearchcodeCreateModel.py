#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingSearchcodeCreateModel(object):

    def __init__(self):
        self._biz_linked_id = None
        self._biz_type = None
        self._desc = None
        self._timeout = None
        self._title = None
        self._url = None

    @property
    def biz_linked_id(self):
        return self._biz_linked_id

    @biz_linked_id.setter
    def biz_linked_id(self, value):
        self._biz_linked_id = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def timeout(self):
        return self._timeout

    @timeout.setter
    def timeout(self, value):
        self._timeout = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_linked_id:
            if hasattr(self.biz_linked_id, 'to_alipay_dict'):
                params['biz_linked_id'] = self.biz_linked_id.to_alipay_dict()
            else:
                params['biz_linked_id'] = self.biz_linked_id
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.timeout:
            if hasattr(self.timeout, 'to_alipay_dict'):
                params['timeout'] = self.timeout.to_alipay_dict()
            else:
                params['timeout'] = self.timeout
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
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
        o = AlipayMarketingSearchcodeCreateModel()
        if 'biz_linked_id' in d:
            o.biz_linked_id = d['biz_linked_id']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'desc' in d:
            o.desc = d['desc']
        if 'timeout' in d:
            o.timeout = d['timeout']
        if 'title' in d:
            o.title = d['title']
        if 'url' in d:
            o.url = d['url']
        return o


