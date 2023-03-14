#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServiceProductPreviewInfo(object):

    def __init__(self):
        self._id = None
        self._preview_url = None
        self._preview_url_name = None
        self._service_id = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def preview_url(self):
        return self._preview_url

    @preview_url.setter
    def preview_url(self, value):
        self._preview_url = value
    @property
    def preview_url_name(self):
        return self._preview_url_name

    @preview_url_name.setter
    def preview_url_name(self, value):
        self._preview_url_name = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.preview_url:
            if hasattr(self.preview_url, 'to_alipay_dict'):
                params['preview_url'] = self.preview_url.to_alipay_dict()
            else:
                params['preview_url'] = self.preview_url
        if self.preview_url_name:
            if hasattr(self.preview_url_name, 'to_alipay_dict'):
                params['preview_url_name'] = self.preview_url_name.to_alipay_dict()
            else:
                params['preview_url_name'] = self.preview_url_name
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceProductPreviewInfo()
        if 'id' in d:
            o.id = d['id']
        if 'preview_url' in d:
            o.preview_url = d['preview_url']
        if 'preview_url_name' in d:
            o.preview_url_name = d['preview_url_name']
        if 'service_id' in d:
            o.service_id = d['service_id']
        return o


