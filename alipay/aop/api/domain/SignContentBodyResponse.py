#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SignContentBodyResponse(object):

    def __init__(self):
        self._alipayapp_rsa_content = None
        self._file_name = None
        self._innerapp_rsa_content = None

    @property
    def alipayapp_rsa_content(self):
        return self._alipayapp_rsa_content

    @alipayapp_rsa_content.setter
    def alipayapp_rsa_content(self, value):
        self._alipayapp_rsa_content = value
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
    @property
    def innerapp_rsa_content(self):
        return self._innerapp_rsa_content

    @innerapp_rsa_content.setter
    def innerapp_rsa_content(self, value):
        self._innerapp_rsa_content = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipayapp_rsa_content:
            if hasattr(self.alipayapp_rsa_content, 'to_alipay_dict'):
                params['alipayapp_rsa_content'] = self.alipayapp_rsa_content.to_alipay_dict()
            else:
                params['alipayapp_rsa_content'] = self.alipayapp_rsa_content
        if self.file_name:
            if hasattr(self.file_name, 'to_alipay_dict'):
                params['file_name'] = self.file_name.to_alipay_dict()
            else:
                params['file_name'] = self.file_name
        if self.innerapp_rsa_content:
            if hasattr(self.innerapp_rsa_content, 'to_alipay_dict'):
                params['innerapp_rsa_content'] = self.innerapp_rsa_content.to_alipay_dict()
            else:
                params['innerapp_rsa_content'] = self.innerapp_rsa_content
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SignContentBodyResponse()
        if 'alipayapp_rsa_content' in d:
            o.alipayapp_rsa_content = d['alipayapp_rsa_content']
        if 'file_name' in d:
            o.file_name = d['file_name']
        if 'innerapp_rsa_content' in d:
            o.innerapp_rsa_content = d['innerapp_rsa_content']
        return o


