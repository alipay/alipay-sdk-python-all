#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NppQrCodeDTO(object):

    def __init__(self):
        self._code_color = None
        self._code_intro = None
        self._code_no = None
        self._code_status = None
        self._code_value = None

    @property
    def code_color(self):
        return self._code_color

    @code_color.setter
    def code_color(self, value):
        self._code_color = value
    @property
    def code_intro(self):
        return self._code_intro

    @code_intro.setter
    def code_intro(self, value):
        self._code_intro = value
    @property
    def code_no(self):
        return self._code_no

    @code_no.setter
    def code_no(self, value):
        self._code_no = value
    @property
    def code_status(self):
        return self._code_status

    @code_status.setter
    def code_status(self, value):
        self._code_status = value
    @property
    def code_value(self):
        return self._code_value

    @code_value.setter
    def code_value(self, value):
        self._code_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.code_color:
            if hasattr(self.code_color, 'to_alipay_dict'):
                params['code_color'] = self.code_color.to_alipay_dict()
            else:
                params['code_color'] = self.code_color
        if self.code_intro:
            if hasattr(self.code_intro, 'to_alipay_dict'):
                params['code_intro'] = self.code_intro.to_alipay_dict()
            else:
                params['code_intro'] = self.code_intro
        if self.code_no:
            if hasattr(self.code_no, 'to_alipay_dict'):
                params['code_no'] = self.code_no.to_alipay_dict()
            else:
                params['code_no'] = self.code_no
        if self.code_status:
            if hasattr(self.code_status, 'to_alipay_dict'):
                params['code_status'] = self.code_status.to_alipay_dict()
            else:
                params['code_status'] = self.code_status
        if self.code_value:
            if hasattr(self.code_value, 'to_alipay_dict'):
                params['code_value'] = self.code_value.to_alipay_dict()
            else:
                params['code_value'] = self.code_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NppQrCodeDTO()
        if 'code_color' in d:
            o.code_color = d['code_color']
        if 'code_intro' in d:
            o.code_intro = d['code_intro']
        if 'code_no' in d:
            o.code_no = d['code_no']
        if 'code_status' in d:
            o.code_status = d['code_status']
        if 'code_value' in d:
            o.code_value = d['code_value']
        return o


