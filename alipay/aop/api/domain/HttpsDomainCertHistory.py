#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HttpsDomainCertHistory(object):

    def __init__(self):
        self._acme_log = None
        self._cert = None
        self._fullchain_cert = None
        self._key = None
        self._status = None
        self._update_time = None

    @property
    def acme_log(self):
        return self._acme_log

    @acme_log.setter
    def acme_log(self, value):
        self._acme_log = value
    @property
    def cert(self):
        return self._cert

    @cert.setter
    def cert(self, value):
        self._cert = value
    @property
    def fullchain_cert(self):
        return self._fullchain_cert

    @fullchain_cert.setter
    def fullchain_cert(self, value):
        self._fullchain_cert = value
    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.acme_log:
            if hasattr(self.acme_log, 'to_alipay_dict'):
                params['acme_log'] = self.acme_log.to_alipay_dict()
            else:
                params['acme_log'] = self.acme_log
        if self.cert:
            if hasattr(self.cert, 'to_alipay_dict'):
                params['cert'] = self.cert.to_alipay_dict()
            else:
                params['cert'] = self.cert
        if self.fullchain_cert:
            if hasattr(self.fullchain_cert, 'to_alipay_dict'):
                params['fullchain_cert'] = self.fullchain_cert.to_alipay_dict()
            else:
                params['fullchain_cert'] = self.fullchain_cert
        if self.key:
            if hasattr(self.key, 'to_alipay_dict'):
                params['key'] = self.key.to_alipay_dict()
            else:
                params['key'] = self.key
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.update_time:
            if hasattr(self.update_time, 'to_alipay_dict'):
                params['update_time'] = self.update_time.to_alipay_dict()
            else:
                params['update_time'] = self.update_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HttpsDomainCertHistory()
        if 'acme_log' in d:
            o.acme_log = d['acme_log']
        if 'cert' in d:
            o.cert = d['cert']
        if 'fullchain_cert' in d:
            o.fullchain_cert = d['fullchain_cert']
        if 'key' in d:
            o.key = d['key']
        if 'status' in d:
            o.status = d['status']
        if 'update_time' in d:
            o.update_time = d['update_time']
        return o


