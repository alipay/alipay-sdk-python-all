#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FileTokenForUpload(object):

    def __init__(self):
        self._access_id = None
        self._dir = None
        self._expire = None
        self._host = None
        self._policy = None
        self._signature = None

    @property
    def access_id(self):
        return self._access_id

    @access_id.setter
    def access_id(self, value):
        self._access_id = value
    @property
    def dir(self):
        return self._dir

    @dir.setter
    def dir(self, value):
        self._dir = value
    @property
    def expire(self):
        return self._expire

    @expire.setter
    def expire(self, value):
        self._expire = value
    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, value):
        self._host = value
    @property
    def policy(self):
        return self._policy

    @policy.setter
    def policy(self, value):
        self._policy = value
    @property
    def signature(self):
        return self._signature

    @signature.setter
    def signature(self, value):
        self._signature = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_id:
            if hasattr(self.access_id, 'to_alipay_dict'):
                params['access_id'] = self.access_id.to_alipay_dict()
            else:
                params['access_id'] = self.access_id
        if self.dir:
            if hasattr(self.dir, 'to_alipay_dict'):
                params['dir'] = self.dir.to_alipay_dict()
            else:
                params['dir'] = self.dir
        if self.expire:
            if hasattr(self.expire, 'to_alipay_dict'):
                params['expire'] = self.expire.to_alipay_dict()
            else:
                params['expire'] = self.expire
        if self.host:
            if hasattr(self.host, 'to_alipay_dict'):
                params['host'] = self.host.to_alipay_dict()
            else:
                params['host'] = self.host
        if self.policy:
            if hasattr(self.policy, 'to_alipay_dict'):
                params['policy'] = self.policy.to_alipay_dict()
            else:
                params['policy'] = self.policy
        if self.signature:
            if hasattr(self.signature, 'to_alipay_dict'):
                params['signature'] = self.signature.to_alipay_dict()
            else:
                params['signature'] = self.signature
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FileTokenForUpload()
        if 'access_id' in d:
            o.access_id = d['access_id']
        if 'dir' in d:
            o.dir = d['dir']
        if 'expire' in d:
            o.expire = d['expire']
        if 'host' in d:
            o.host = d['host']
        if 'policy' in d:
            o.policy = d['policy']
        if 'signature' in d:
            o.signature = d['signature']
        return o


