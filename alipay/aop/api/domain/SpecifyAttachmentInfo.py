#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SpecifyAttachmentInfo(object):

    def __init__(self):
        self._allow_more_uploads = None
        self._allow_more_uploads_max_count = None
        self._collect_cert_types = None
        self._collect_common_codes = None
        self._third_party_user_id = None

    @property
    def allow_more_uploads(self):
        return self._allow_more_uploads

    @allow_more_uploads.setter
    def allow_more_uploads(self, value):
        self._allow_more_uploads = value
    @property
    def allow_more_uploads_max_count(self):
        return self._allow_more_uploads_max_count

    @allow_more_uploads_max_count.setter
    def allow_more_uploads_max_count(self, value):
        self._allow_more_uploads_max_count = value
    @property
    def collect_cert_types(self):
        return self._collect_cert_types

    @collect_cert_types.setter
    def collect_cert_types(self, value):
        if isinstance(value, list):
            self._collect_cert_types = list()
            for i in value:
                self._collect_cert_types.append(i)
    @property
    def collect_common_codes(self):
        return self._collect_common_codes

    @collect_common_codes.setter
    def collect_common_codes(self, value):
        if isinstance(value, list):
            self._collect_common_codes = list()
            for i in value:
                self._collect_common_codes.append(i)
    @property
    def third_party_user_id(self):
        return self._third_party_user_id

    @third_party_user_id.setter
    def third_party_user_id(self, value):
        self._third_party_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.allow_more_uploads:
            if hasattr(self.allow_more_uploads, 'to_alipay_dict'):
                params['allow_more_uploads'] = self.allow_more_uploads.to_alipay_dict()
            else:
                params['allow_more_uploads'] = self.allow_more_uploads
        if self.allow_more_uploads_max_count:
            if hasattr(self.allow_more_uploads_max_count, 'to_alipay_dict'):
                params['allow_more_uploads_max_count'] = self.allow_more_uploads_max_count.to_alipay_dict()
            else:
                params['allow_more_uploads_max_count'] = self.allow_more_uploads_max_count
        if self.collect_cert_types:
            if isinstance(self.collect_cert_types, list):
                for i in range(0, len(self.collect_cert_types)):
                    element = self.collect_cert_types[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.collect_cert_types[i] = element.to_alipay_dict()
            if hasattr(self.collect_cert_types, 'to_alipay_dict'):
                params['collect_cert_types'] = self.collect_cert_types.to_alipay_dict()
            else:
                params['collect_cert_types'] = self.collect_cert_types
        if self.collect_common_codes:
            if isinstance(self.collect_common_codes, list):
                for i in range(0, len(self.collect_common_codes)):
                    element = self.collect_common_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.collect_common_codes[i] = element.to_alipay_dict()
            if hasattr(self.collect_common_codes, 'to_alipay_dict'):
                params['collect_common_codes'] = self.collect_common_codes.to_alipay_dict()
            else:
                params['collect_common_codes'] = self.collect_common_codes
        if self.third_party_user_id:
            if hasattr(self.third_party_user_id, 'to_alipay_dict'):
                params['third_party_user_id'] = self.third_party_user_id.to_alipay_dict()
            else:
                params['third_party_user_id'] = self.third_party_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SpecifyAttachmentInfo()
        if 'allow_more_uploads' in d:
            o.allow_more_uploads = d['allow_more_uploads']
        if 'allow_more_uploads_max_count' in d:
            o.allow_more_uploads_max_count = d['allow_more_uploads_max_count']
        if 'collect_cert_types' in d:
            o.collect_cert_types = d['collect_cert_types']
        if 'collect_common_codes' in d:
            o.collect_common_codes = d['collect_common_codes']
        if 'third_party_user_id' in d:
            o.third_party_user_id = d['third_party_user_id']
        return o


