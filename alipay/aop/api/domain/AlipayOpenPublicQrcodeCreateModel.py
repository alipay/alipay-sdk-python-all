#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CodeInfo import CodeInfo


class AlipayOpenPublicQrcodeCreateModel(object):

    def __init__(self):
        self._code_info = None
        self._code_type = None
        self._expire_second = None
        self._show_logo = None

    @property
    def code_info(self):
        return self._code_info

    @code_info.setter
    def code_info(self, value):
        if isinstance(value, CodeInfo):
            self._code_info = value
        else:
            self._code_info = CodeInfo.from_alipay_dict(value)
    @property
    def code_type(self):
        return self._code_type

    @code_type.setter
    def code_type(self, value):
        self._code_type = value
    @property
    def expire_second(self):
        return self._expire_second

    @expire_second.setter
    def expire_second(self, value):
        self._expire_second = value
    @property
    def show_logo(self):
        return self._show_logo

    @show_logo.setter
    def show_logo(self, value):
        self._show_logo = value


    def to_alipay_dict(self):
        params = dict()
        if self.code_info:
            if hasattr(self.code_info, 'to_alipay_dict'):
                params['code_info'] = self.code_info.to_alipay_dict()
            else:
                params['code_info'] = self.code_info
        if self.code_type:
            if hasattr(self.code_type, 'to_alipay_dict'):
                params['code_type'] = self.code_type.to_alipay_dict()
            else:
                params['code_type'] = self.code_type
        if self.expire_second:
            if hasattr(self.expire_second, 'to_alipay_dict'):
                params['expire_second'] = self.expire_second.to_alipay_dict()
            else:
                params['expire_second'] = self.expire_second
        if self.show_logo:
            if hasattr(self.show_logo, 'to_alipay_dict'):
                params['show_logo'] = self.show_logo.to_alipay_dict()
            else:
                params['show_logo'] = self.show_logo
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenPublicQrcodeCreateModel()
        if 'code_info' in d:
            o.code_info = d['code_info']
        if 'code_type' in d:
            o.code_type = d['code_type']
        if 'expire_second' in d:
            o.expire_second = d['expire_second']
        if 'show_logo' in d:
            o.show_logo = d['show_logo']
        return o


