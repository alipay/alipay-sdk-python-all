#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AppSecurityExt(object):

    def __init__(self):
        self._alipay_public_key = None
        self._biz_id = None
        self._cert_sn = None
        self._partner_private_key = None
        self._partner_public_key = None
        self._public_key_source = None
        self._signature_type = None

    @property
    def alipay_public_key(self):
        return self._alipay_public_key

    @alipay_public_key.setter
    def alipay_public_key(self, value):
        self._alipay_public_key = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def cert_sn(self):
        return self._cert_sn

    @cert_sn.setter
    def cert_sn(self, value):
        self._cert_sn = value
    @property
    def partner_private_key(self):
        return self._partner_private_key

    @partner_private_key.setter
    def partner_private_key(self, value):
        self._partner_private_key = value
    @property
    def partner_public_key(self):
        return self._partner_public_key

    @partner_public_key.setter
    def partner_public_key(self, value):
        self._partner_public_key = value
    @property
    def public_key_source(self):
        return self._public_key_source

    @public_key_source.setter
    def public_key_source(self, value):
        self._public_key_source = value
    @property
    def signature_type(self):
        return self._signature_type

    @signature_type.setter
    def signature_type(self, value):
        self._signature_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_public_key:
            if hasattr(self.alipay_public_key, 'to_alipay_dict'):
                params['alipay_public_key'] = self.alipay_public_key.to_alipay_dict()
            else:
                params['alipay_public_key'] = self.alipay_public_key
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.cert_sn:
            if hasattr(self.cert_sn, 'to_alipay_dict'):
                params['cert_sn'] = self.cert_sn.to_alipay_dict()
            else:
                params['cert_sn'] = self.cert_sn
        if self.partner_private_key:
            if hasattr(self.partner_private_key, 'to_alipay_dict'):
                params['partner_private_key'] = self.partner_private_key.to_alipay_dict()
            else:
                params['partner_private_key'] = self.partner_private_key
        if self.partner_public_key:
            if hasattr(self.partner_public_key, 'to_alipay_dict'):
                params['partner_public_key'] = self.partner_public_key.to_alipay_dict()
            else:
                params['partner_public_key'] = self.partner_public_key
        if self.public_key_source:
            if hasattr(self.public_key_source, 'to_alipay_dict'):
                params['public_key_source'] = self.public_key_source.to_alipay_dict()
            else:
                params['public_key_source'] = self.public_key_source
        if self.signature_type:
            if hasattr(self.signature_type, 'to_alipay_dict'):
                params['signature_type'] = self.signature_type.to_alipay_dict()
            else:
                params['signature_type'] = self.signature_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AppSecurityExt()
        if 'alipay_public_key' in d:
            o.alipay_public_key = d['alipay_public_key']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'cert_sn' in d:
            o.cert_sn = d['cert_sn']
        if 'partner_private_key' in d:
            o.partner_private_key = d['partner_private_key']
        if 'partner_public_key' in d:
            o.partner_public_key = d['partner_public_key']
        if 'public_key_source' in d:
            o.public_key_source = d['public_key_source']
        if 'signature_type' in d:
            o.signature_type = d['signature_type']
        return o


