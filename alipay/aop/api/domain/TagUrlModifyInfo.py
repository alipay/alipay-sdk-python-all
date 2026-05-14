#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TagUrlModifyInfo(object):

    def __init__(self):
        self._route_url = None
        self._tag_id = None
        self._tag_sn = None

    @property
    def route_url(self):
        return self._route_url

    @route_url.setter
    def route_url(self, value):
        self._route_url = value
    @property
    def tag_id(self):
        return self._tag_id

    @tag_id.setter
    def tag_id(self, value):
        self._tag_id = value
    @property
    def tag_sn(self):
        return self._tag_sn

    @tag_sn.setter
    def tag_sn(self, value):
        self._tag_sn = value


    def to_alipay_dict(self):
        params = dict()
        if self.route_url:
            if hasattr(self.route_url, 'to_alipay_dict'):
                params['route_url'] = self.route_url.to_alipay_dict()
            else:
                params['route_url'] = self.route_url
        if self.tag_id:
            if hasattr(self.tag_id, 'to_alipay_dict'):
                params['tag_id'] = self.tag_id.to_alipay_dict()
            else:
                params['tag_id'] = self.tag_id
        if self.tag_sn:
            if hasattr(self.tag_sn, 'to_alipay_dict'):
                params['tag_sn'] = self.tag_sn.to_alipay_dict()
            else:
                params['tag_sn'] = self.tag_sn
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TagUrlModifyInfo()
        if 'route_url' in d:
            o.route_url = d['route_url']
        if 'tag_id' in d:
            o.tag_id = d['tag_id']
        if 'tag_sn' in d:
            o.tag_sn = d['tag_sn']
        return o


