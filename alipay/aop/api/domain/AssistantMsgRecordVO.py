#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AssistantMsgRecordVO(object):

    def __init__(self):
        self._biz_type = None
        self._content_id = None
        self._gmt_published = None
        self._name = None
        self._status = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def content_id(self):
        return self._content_id

    @content_id.setter
    def content_id(self, value):
        self._content_id = value
    @property
    def gmt_published(self):
        return self._gmt_published

    @gmt_published.setter
    def gmt_published(self, value):
        self._gmt_published = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.content_id:
            if hasattr(self.content_id, 'to_alipay_dict'):
                params['content_id'] = self.content_id.to_alipay_dict()
            else:
                params['content_id'] = self.content_id
        if self.gmt_published:
            if hasattr(self.gmt_published, 'to_alipay_dict'):
                params['gmt_published'] = self.gmt_published.to_alipay_dict()
            else:
                params['gmt_published'] = self.gmt_published
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssistantMsgRecordVO()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'content_id' in d:
            o.content_id = d['content_id']
        if 'gmt_published' in d:
            o.gmt_published = d['gmt_published']
        if 'name' in d:
            o.name = d['name']
        if 'status' in d:
            o.status = d['status']
        return o


