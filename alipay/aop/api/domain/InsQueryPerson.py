#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsQueryPerson(object):

    def __init__(self):
        self._cert_no = None
        self._cert_type = None
        self._channel_user_id = None
        self._channel_user_source = None
        self._type = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def channel_user_id(self):
        return self._channel_user_id

    @channel_user_id.setter
    def channel_user_id(self, value):
        self._channel_user_id = value
    @property
    def channel_user_source(self):
        return self._channel_user_source

    @channel_user_source.setter
    def channel_user_source(self, value):
        self._channel_user_source = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.channel_user_id:
            if hasattr(self.channel_user_id, 'to_alipay_dict'):
                params['channel_user_id'] = self.channel_user_id.to_alipay_dict()
            else:
                params['channel_user_id'] = self.channel_user_id
        if self.channel_user_source:
            if hasattr(self.channel_user_source, 'to_alipay_dict'):
                params['channel_user_source'] = self.channel_user_source.to_alipay_dict()
            else:
                params['channel_user_source'] = self.channel_user_source
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsQueryPerson()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'channel_user_id' in d:
            o.channel_user_id = d['channel_user_id']
        if 'channel_user_source' in d:
            o.channel_user_source = d['channel_user_source']
        if 'type' in d:
            o.type = d['type']
        return o


