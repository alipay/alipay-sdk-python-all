#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZmepAnnualReportWebsiteInfo(object):

    def __init__(self):
        self._website_name = None
        self._website_type = None
        self._website_url = None

    @property
    def website_name(self):
        return self._website_name

    @website_name.setter
    def website_name(self, value):
        self._website_name = value
    @property
    def website_type(self):
        return self._website_type

    @website_type.setter
    def website_type(self, value):
        self._website_type = value
    @property
    def website_url(self):
        return self._website_url

    @website_url.setter
    def website_url(self, value):
        self._website_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.website_name:
            if hasattr(self.website_name, 'to_alipay_dict'):
                params['website_name'] = self.website_name.to_alipay_dict()
            else:
                params['website_name'] = self.website_name
        if self.website_type:
            if hasattr(self.website_type, 'to_alipay_dict'):
                params['website_type'] = self.website_type.to_alipay_dict()
            else:
                params['website_type'] = self.website_type
        if self.website_url:
            if hasattr(self.website_url, 'to_alipay_dict'):
                params['website_url'] = self.website_url.to_alipay_dict()
            else:
                params['website_url'] = self.website_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZmepAnnualReportWebsiteInfo()
        if 'website_name' in d:
            o.website_name = d['website_name']
        if 'website_type' in d:
            o.website_type = d['website_type']
        if 'website_url' in d:
            o.website_url = d['website_url']
        return o


