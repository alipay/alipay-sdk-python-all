#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataAiserviceJunengLoanQueryModel(object):

    def __init__(self):
        self._extension_info = None
        self._hashed_cert_no = None
        self._institution_uuid = None
        self._request_uuid = None
        self._user_feature = None

    @property
    def extension_info(self):
        return self._extension_info

    @extension_info.setter
    def extension_info(self, value):
        self._extension_info = value
    @property
    def hashed_cert_no(self):
        return self._hashed_cert_no

    @hashed_cert_no.setter
    def hashed_cert_no(self, value):
        self._hashed_cert_no = value
    @property
    def institution_uuid(self):
        return self._institution_uuid

    @institution_uuid.setter
    def institution_uuid(self, value):
        self._institution_uuid = value
    @property
    def request_uuid(self):
        return self._request_uuid

    @request_uuid.setter
    def request_uuid(self, value):
        self._request_uuid = value
    @property
    def user_feature(self):
        return self._user_feature

    @user_feature.setter
    def user_feature(self, value):
        self._user_feature = value


    def to_alipay_dict(self):
        params = dict()
        if self.extension_info:
            if hasattr(self.extension_info, 'to_alipay_dict'):
                params['extension_info'] = self.extension_info.to_alipay_dict()
            else:
                params['extension_info'] = self.extension_info
        if self.hashed_cert_no:
            if hasattr(self.hashed_cert_no, 'to_alipay_dict'):
                params['hashed_cert_no'] = self.hashed_cert_no.to_alipay_dict()
            else:
                params['hashed_cert_no'] = self.hashed_cert_no
        if self.institution_uuid:
            if hasattr(self.institution_uuid, 'to_alipay_dict'):
                params['institution_uuid'] = self.institution_uuid.to_alipay_dict()
            else:
                params['institution_uuid'] = self.institution_uuid
        if self.request_uuid:
            if hasattr(self.request_uuid, 'to_alipay_dict'):
                params['request_uuid'] = self.request_uuid.to_alipay_dict()
            else:
                params['request_uuid'] = self.request_uuid
        if self.user_feature:
            if hasattr(self.user_feature, 'to_alipay_dict'):
                params['user_feature'] = self.user_feature.to_alipay_dict()
            else:
                params['user_feature'] = self.user_feature
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataAiserviceJunengLoanQueryModel()
        if 'extension_info' in d:
            o.extension_info = d['extension_info']
        if 'hashed_cert_no' in d:
            o.hashed_cert_no = d['hashed_cert_no']
        if 'institution_uuid' in d:
            o.institution_uuid = d['institution_uuid']
        if 'request_uuid' in d:
            o.request_uuid = d['request_uuid']
        if 'user_feature' in d:
            o.user_feature = d['user_feature']
        return o


