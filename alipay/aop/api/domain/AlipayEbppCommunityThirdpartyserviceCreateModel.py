#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppCommunityThirdpartyserviceCreateModel(object):

    def __init__(self):
        self._check_video_url = None
        self._community_short_name = None
        self._out_community_id = None
        self._service_code = None
        self._service_url = None

    @property
    def check_video_url(self):
        return self._check_video_url

    @check_video_url.setter
    def check_video_url(self, value):
        self._check_video_url = value
    @property
    def community_short_name(self):
        return self._community_short_name

    @community_short_name.setter
    def community_short_name(self, value):
        self._community_short_name = value
    @property
    def out_community_id(self):
        return self._out_community_id

    @out_community_id.setter
    def out_community_id(self, value):
        self._out_community_id = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
    @property
    def service_url(self):
        return self._service_url

    @service_url.setter
    def service_url(self, value):
        self._service_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.check_video_url:
            if hasattr(self.check_video_url, 'to_alipay_dict'):
                params['check_video_url'] = self.check_video_url.to_alipay_dict()
            else:
                params['check_video_url'] = self.check_video_url
        if self.community_short_name:
            if hasattr(self.community_short_name, 'to_alipay_dict'):
                params['community_short_name'] = self.community_short_name.to_alipay_dict()
            else:
                params['community_short_name'] = self.community_short_name
        if self.out_community_id:
            if hasattr(self.out_community_id, 'to_alipay_dict'):
                params['out_community_id'] = self.out_community_id.to_alipay_dict()
            else:
                params['out_community_id'] = self.out_community_id
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        if self.service_url:
            if hasattr(self.service_url, 'to_alipay_dict'):
                params['service_url'] = self.service_url.to_alipay_dict()
            else:
                params['service_url'] = self.service_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppCommunityThirdpartyserviceCreateModel()
        if 'check_video_url' in d:
            o.check_video_url = d['check_video_url']
        if 'community_short_name' in d:
            o.community_short_name = d['community_short_name']
        if 'out_community_id' in d:
            o.out_community_id = d['out_community_id']
        if 'service_code' in d:
            o.service_code = d['service_code']
        if 'service_url' in d:
            o.service_url = d['service_url']
        return o


