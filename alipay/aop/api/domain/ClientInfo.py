#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ClientInfo(object):

    def __init__(self):
        self._language = None
        self._os = None
        self._type = None
        self._version_no = None

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        self._language = value
    @property
    def os(self):
        return self._os

    @os.setter
    def os(self, value):
        self._os = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def version_no(self):
        return self._version_no

    @version_no.setter
    def version_no(self, value):
        self._version_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.language:
            if hasattr(self.language, 'to_alipay_dict'):
                params['language'] = self.language.to_alipay_dict()
            else:
                params['language'] = self.language
        if self.os:
            if hasattr(self.os, 'to_alipay_dict'):
                params['os'] = self.os.to_alipay_dict()
            else:
                params['os'] = self.os
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.version_no:
            if hasattr(self.version_no, 'to_alipay_dict'):
                params['version_no'] = self.version_no.to_alipay_dict()
            else:
                params['version_no'] = self.version_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ClientInfo()
        if 'language' in d:
            o.language = d['language']
        if 'os' in d:
            o.os = d['os']
        if 'type' in d:
            o.type = d['type']
        if 'version_no' in d:
            o.version_no = d['version_no']
        return o


