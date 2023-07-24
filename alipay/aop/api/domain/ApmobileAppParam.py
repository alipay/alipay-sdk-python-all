#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ApmobileAppParam(object):

    def __init__(self):
        self._file_id = None
        self._privacy_policy_content = None
        self._privacy_policy_url = None

    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def privacy_policy_content(self):
        return self._privacy_policy_content

    @privacy_policy_content.setter
    def privacy_policy_content(self, value):
        self._privacy_policy_content = value
    @property
    def privacy_policy_url(self):
        return self._privacy_policy_url

    @privacy_policy_url.setter
    def privacy_policy_url(self, value):
        self._privacy_policy_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        if self.privacy_policy_content:
            if hasattr(self.privacy_policy_content, 'to_alipay_dict'):
                params['privacy_policy_content'] = self.privacy_policy_content.to_alipay_dict()
            else:
                params['privacy_policy_content'] = self.privacy_policy_content
        if self.privacy_policy_url:
            if hasattr(self.privacy_policy_url, 'to_alipay_dict'):
                params['privacy_policy_url'] = self.privacy_policy_url.to_alipay_dict()
            else:
                params['privacy_policy_url'] = self.privacy_policy_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApmobileAppParam()
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'privacy_policy_content' in d:
            o.privacy_policy_content = d['privacy_policy_content']
        if 'privacy_policy_url' in d:
            o.privacy_policy_url = d['privacy_policy_url']
        return o


