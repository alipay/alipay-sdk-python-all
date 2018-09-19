#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityDataInfoSecuritydataQueryModel(object):

    def __init__(self):
        self._biz_id = None
        self._ext = None
        self._subject = None
        self._system_name = None
        self._type = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def ext(self):
        return self._ext

    @ext.setter
    def ext(self, value):
        self._ext = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def system_name(self):
        return self._system_name

    @system_name.setter
    def system_name(self, value):
        self._system_name = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.ext:
            if hasattr(self.ext, 'to_alipay_dict'):
                params['ext'] = self.ext.to_alipay_dict()
            else:
                params['ext'] = self.ext
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        if self.system_name:
            if hasattr(self.system_name, 'to_alipay_dict'):
                params['system_name'] = self.system_name.to_alipay_dict()
            else:
                params['system_name'] = self.system_name
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
        o = AlipaySecurityDataInfoSecuritydataQueryModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'ext' in d:
            o.ext = d['ext']
        if 'subject' in d:
            o.subject = d['subject']
        if 'system_name' in d:
            o.system_name = d['system_name']
        if 'type' in d:
            o.type = d['type']
        return o


