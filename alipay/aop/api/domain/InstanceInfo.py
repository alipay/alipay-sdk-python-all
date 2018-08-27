#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InstanceInfo(object):

    def __init__(self):
        self._content = None
        self._ext_info = None
        self._gmt_end = None
        self._gmt_start = None
        self._instance_id = None
        self._instance_name = None
        self._type = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def gmt_end(self):
        return self._gmt_end

    @gmt_end.setter
    def gmt_end(self, value):
        self._gmt_end = value
    @property
    def gmt_start(self):
        return self._gmt_start

    @gmt_start.setter
    def gmt_start(self, value):
        self._gmt_start = value
    @property
    def instance_id(self):
        return self._instance_id

    @instance_id.setter
    def instance_id(self, value):
        self._instance_id = value
    @property
    def instance_name(self):
        return self._instance_name

    @instance_name.setter
    def instance_name(self, value):
        self._instance_name = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.gmt_end:
            if hasattr(self.gmt_end, 'to_alipay_dict'):
                params['gmt_end'] = self.gmt_end.to_alipay_dict()
            else:
                params['gmt_end'] = self.gmt_end
        if self.gmt_start:
            if hasattr(self.gmt_start, 'to_alipay_dict'):
                params['gmt_start'] = self.gmt_start.to_alipay_dict()
            else:
                params['gmt_start'] = self.gmt_start
        if self.instance_id:
            if hasattr(self.instance_id, 'to_alipay_dict'):
                params['instance_id'] = self.instance_id.to_alipay_dict()
            else:
                params['instance_id'] = self.instance_id
        if self.instance_name:
            if hasattr(self.instance_name, 'to_alipay_dict'):
                params['instance_name'] = self.instance_name.to_alipay_dict()
            else:
                params['instance_name'] = self.instance_name
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InstanceInfo()
        if 'content' in d:
            o.content = d['content']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'gmt_end' in d:
            o.gmt_end = d['gmt_end']
        if 'gmt_start' in d:
            o.gmt_start = d['gmt_start']
        if 'instance_id' in d:
            o.instance_id = d['instance_id']
        if 'instance_name' in d:
            o.instance_name = d['instance_name']
        if 'type' in d:
            o.type = d['type']
        return o


