#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AntArchiveIdentityCertificate import AntArchiveIdentityCertificate
from alipay.aop.api.domain.AntArchiveIdentityCertificate import AntArchiveIdentityCertificate


class AlipayUserAntarchiveIdentityrelationAddModel(object):

    def __init__(self):
        self._ext_info = None
        self._rel_biz_type = None
        self._rel_type = None
        self._source_identity_certificate = None
        self._target_identity_certificate = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def rel_biz_type(self):
        return self._rel_biz_type

    @rel_biz_type.setter
    def rel_biz_type(self, value):
        self._rel_biz_type = value
    @property
    def rel_type(self):
        return self._rel_type

    @rel_type.setter
    def rel_type(self, value):
        self._rel_type = value
    @property
    def source_identity_certificate(self):
        return self._source_identity_certificate

    @source_identity_certificate.setter
    def source_identity_certificate(self, value):
        if isinstance(value, AntArchiveIdentityCertificate):
            self._source_identity_certificate = value
        else:
            self._source_identity_certificate = AntArchiveIdentityCertificate.from_alipay_dict(value)
    @property
    def target_identity_certificate(self):
        return self._target_identity_certificate

    @target_identity_certificate.setter
    def target_identity_certificate(self, value):
        if isinstance(value, AntArchiveIdentityCertificate):
            self._target_identity_certificate = value
        else:
            self._target_identity_certificate = AntArchiveIdentityCertificate.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.rel_biz_type:
            if hasattr(self.rel_biz_type, 'to_alipay_dict'):
                params['rel_biz_type'] = self.rel_biz_type.to_alipay_dict()
            else:
                params['rel_biz_type'] = self.rel_biz_type
        if self.rel_type:
            if hasattr(self.rel_type, 'to_alipay_dict'):
                params['rel_type'] = self.rel_type.to_alipay_dict()
            else:
                params['rel_type'] = self.rel_type
        if self.source_identity_certificate:
            if hasattr(self.source_identity_certificate, 'to_alipay_dict'):
                params['source_identity_certificate'] = self.source_identity_certificate.to_alipay_dict()
            else:
                params['source_identity_certificate'] = self.source_identity_certificate
        if self.target_identity_certificate:
            if hasattr(self.target_identity_certificate, 'to_alipay_dict'):
                params['target_identity_certificate'] = self.target_identity_certificate.to_alipay_dict()
            else:
                params['target_identity_certificate'] = self.target_identity_certificate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAntarchiveIdentityrelationAddModel()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'rel_biz_type' in d:
            o.rel_biz_type = d['rel_biz_type']
        if 'rel_type' in d:
            o.rel_type = d['rel_type']
        if 'source_identity_certificate' in d:
            o.source_identity_certificate = d['source_identity_certificate']
        if 'target_identity_certificate' in d:
            o.target_identity_certificate = d['target_identity_certificate']
        return o


