#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ReplyRecordResponse(object):

    def __init__(self):
        self._content = None
        self._gmt_create = None
        self._images = None
        self._replier_name = None
        self._replier_role = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def images(self):
        return self._images

    @images.setter
    def images(self, value):
        if isinstance(value, list):
            self._images = list()
            for i in value:
                self._images.append(i)
    @property
    def replier_name(self):
        return self._replier_name

    @replier_name.setter
    def replier_name(self, value):
        self._replier_name = value
    @property
    def replier_role(self):
        return self._replier_role

    @replier_role.setter
    def replier_role(self, value):
        self._replier_role = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.images:
            if isinstance(self.images, list):
                for i in range(0, len(self.images)):
                    element = self.images[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.images[i] = element.to_alipay_dict()
            if hasattr(self.images, 'to_alipay_dict'):
                params['images'] = self.images.to_alipay_dict()
            else:
                params['images'] = self.images
        if self.replier_name:
            if hasattr(self.replier_name, 'to_alipay_dict'):
                params['replier_name'] = self.replier_name.to_alipay_dict()
            else:
                params['replier_name'] = self.replier_name
        if self.replier_role:
            if hasattr(self.replier_role, 'to_alipay_dict'):
                params['replier_role'] = self.replier_role.to_alipay_dict()
            else:
                params['replier_role'] = self.replier_role
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReplyRecordResponse()
        if 'content' in d:
            o.content = d['content']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'images' in d:
            o.images = d['images']
        if 'replier_name' in d:
            o.replier_name = d['replier_name']
        if 'replier_role' in d:
            o.replier_role = d['replier_role']
        return o


