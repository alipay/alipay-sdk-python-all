#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SealPosition import SealPosition


class FileSignature(object):

    def __init__(self):
        self._cert_no = None
        self._seal_id = None
        self._seal_position = None
        self._seal_type = None
        self._sign_reason = None
        self._signature_type = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def seal_id(self):
        return self._seal_id

    @seal_id.setter
    def seal_id(self, value):
        self._seal_id = value
    @property
    def seal_position(self):
        return self._seal_position

    @seal_position.setter
    def seal_position(self, value):
        if isinstance(value, SealPosition):
            self._seal_position = value
        else:
            self._seal_position = SealPosition.from_alipay_dict(value)
    @property
    def seal_type(self):
        return self._seal_type

    @seal_type.setter
    def seal_type(self, value):
        self._seal_type = value
    @property
    def sign_reason(self):
        return self._sign_reason

    @sign_reason.setter
    def sign_reason(self, value):
        self._sign_reason = value
    @property
    def signature_type(self):
        return self._signature_type

    @signature_type.setter
    def signature_type(self, value):
        self._signature_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.seal_id:
            if hasattr(self.seal_id, 'to_alipay_dict'):
                params['seal_id'] = self.seal_id.to_alipay_dict()
            else:
                params['seal_id'] = self.seal_id
        if self.seal_position:
            if hasattr(self.seal_position, 'to_alipay_dict'):
                params['seal_position'] = self.seal_position.to_alipay_dict()
            else:
                params['seal_position'] = self.seal_position
        if self.seal_type:
            if hasattr(self.seal_type, 'to_alipay_dict'):
                params['seal_type'] = self.seal_type.to_alipay_dict()
            else:
                params['seal_type'] = self.seal_type
        if self.sign_reason:
            if hasattr(self.sign_reason, 'to_alipay_dict'):
                params['sign_reason'] = self.sign_reason.to_alipay_dict()
            else:
                params['sign_reason'] = self.sign_reason
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
        o = FileSignature()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'seal_id' in d:
            o.seal_id = d['seal_id']
        if 'seal_position' in d:
            o.seal_position = d['seal_position']
        if 'seal_type' in d:
            o.seal_type = d['seal_type']
        if 'sign_reason' in d:
            o.sign_reason = d['sign_reason']
        if 'signature_type' in d:
            o.signature_type = d['signature_type']
        return o


