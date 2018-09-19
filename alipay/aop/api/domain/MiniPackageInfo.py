#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MiniPackageInfo(object):

    def __init__(self):
        self._doc_url = None
        self._package_desc = None
        self._package_name = None
        self._package_open_type = None
        self._status = None

    @property
    def doc_url(self):
        return self._doc_url

    @doc_url.setter
    def doc_url(self, value):
        self._doc_url = value
    @property
    def package_desc(self):
        return self._package_desc

    @package_desc.setter
    def package_desc(self, value):
        self._package_desc = value
    @property
    def package_name(self):
        return self._package_name

    @package_name.setter
    def package_name(self, value):
        self._package_name = value
    @property
    def package_open_type(self):
        return self._package_open_type

    @package_open_type.setter
    def package_open_type(self, value):
        self._package_open_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.doc_url:
            if hasattr(self.doc_url, 'to_alipay_dict'):
                params['doc_url'] = self.doc_url.to_alipay_dict()
            else:
                params['doc_url'] = self.doc_url
        if self.package_desc:
            if hasattr(self.package_desc, 'to_alipay_dict'):
                params['package_desc'] = self.package_desc.to_alipay_dict()
            else:
                params['package_desc'] = self.package_desc
        if self.package_name:
            if hasattr(self.package_name, 'to_alipay_dict'):
                params['package_name'] = self.package_name.to_alipay_dict()
            else:
                params['package_name'] = self.package_name
        if self.package_open_type:
            if hasattr(self.package_open_type, 'to_alipay_dict'):
                params['package_open_type'] = self.package_open_type.to_alipay_dict()
            else:
                params['package_open_type'] = self.package_open_type
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
        o = MiniPackageInfo()
        if 'doc_url' in d:
            o.doc_url = d['doc_url']
        if 'package_desc' in d:
            o.package_desc = d['package_desc']
        if 'package_name' in d:
            o.package_name = d['package_name']
        if 'package_open_type' in d:
            o.package_open_type = d['package_open_type']
        if 'status' in d:
            o.status = d['status']
        return o


