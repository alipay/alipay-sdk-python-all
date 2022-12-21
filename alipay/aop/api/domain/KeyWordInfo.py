#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KeyWordInfo(object):

    def __init__(self):
        self._apply_no = None
        self._audit_key_word = None
        self._audit_reason = None
        self._audit_time = None
        self._config_id = None
        self._gmt_create = None
        self._key_word = None
        self._status = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def audit_key_word(self):
        return self._audit_key_word

    @audit_key_word.setter
    def audit_key_word(self, value):
        self._audit_key_word = value
    @property
    def audit_reason(self):
        return self._audit_reason

    @audit_reason.setter
    def audit_reason(self, value):
        self._audit_reason = value
    @property
    def audit_time(self):
        return self._audit_time

    @audit_time.setter
    def audit_time(self, value):
        self._audit_time = value
    @property
    def config_id(self):
        return self._config_id

    @config_id.setter
    def config_id(self, value):
        self._config_id = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def key_word(self):
        return self._key_word

    @key_word.setter
    def key_word(self, value):
        self._key_word = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.audit_key_word:
            if hasattr(self.audit_key_word, 'to_alipay_dict'):
                params['audit_key_word'] = self.audit_key_word.to_alipay_dict()
            else:
                params['audit_key_word'] = self.audit_key_word
        if self.audit_reason:
            if hasattr(self.audit_reason, 'to_alipay_dict'):
                params['audit_reason'] = self.audit_reason.to_alipay_dict()
            else:
                params['audit_reason'] = self.audit_reason
        if self.audit_time:
            if hasattr(self.audit_time, 'to_alipay_dict'):
                params['audit_time'] = self.audit_time.to_alipay_dict()
            else:
                params['audit_time'] = self.audit_time
        if self.config_id:
            if hasattr(self.config_id, 'to_alipay_dict'):
                params['config_id'] = self.config_id.to_alipay_dict()
            else:
                params['config_id'] = self.config_id
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.key_word:
            if hasattr(self.key_word, 'to_alipay_dict'):
                params['key_word'] = self.key_word.to_alipay_dict()
            else:
                params['key_word'] = self.key_word
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
        o = KeyWordInfo()
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'audit_key_word' in d:
            o.audit_key_word = d['audit_key_word']
        if 'audit_reason' in d:
            o.audit_reason = d['audit_reason']
        if 'audit_time' in d:
            o.audit_time = d['audit_time']
        if 'config_id' in d:
            o.config_id = d['config_id']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'key_word' in d:
            o.key_word = d['key_word']
        if 'status' in d:
            o.status = d['status']
        return o


