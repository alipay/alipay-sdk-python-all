#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbAdvertContentPassword import KbAdvertContentPassword
from alipay.aop.api.domain.KbAdvertContentShareCode import KbAdvertContentShareCode


class KbAdvertSpecialAdvContentModifyResponse(object):

    def __init__(self):
        self._code = None
        self._content_password = None
        self._content_share_code = None
        self._content_type = None
        self._msg = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def content_password(self):
        return self._content_password

    @content_password.setter
    def content_password(self, value):
        if isinstance(value, KbAdvertContentPassword):
            self._content_password = value
        else:
            self._content_password = KbAdvertContentPassword.from_alipay_dict(value)
    @property
    def content_share_code(self):
        return self._content_share_code

    @content_share_code.setter
    def content_share_code(self, value):
        if isinstance(value, KbAdvertContentShareCode):
            self._content_share_code = value
        else:
            self._content_share_code = KbAdvertContentShareCode.from_alipay_dict(value)
    @property
    def content_type(self):
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        self._content_type = value
    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.content_password:
            if hasattr(self.content_password, 'to_alipay_dict'):
                params['content_password'] = self.content_password.to_alipay_dict()
            else:
                params['content_password'] = self.content_password
        if self.content_share_code:
            if hasattr(self.content_share_code, 'to_alipay_dict'):
                params['content_share_code'] = self.content_share_code.to_alipay_dict()
            else:
                params['content_share_code'] = self.content_share_code
        if self.content_type:
            if hasattr(self.content_type, 'to_alipay_dict'):
                params['content_type'] = self.content_type.to_alipay_dict()
            else:
                params['content_type'] = self.content_type
        if self.msg:
            if hasattr(self.msg, 'to_alipay_dict'):
                params['msg'] = self.msg.to_alipay_dict()
            else:
                params['msg'] = self.msg
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbAdvertSpecialAdvContentModifyResponse()
        if 'code' in d:
            o.code = d['code']
        if 'content_password' in d:
            o.content_password = d['content_password']
        if 'content_share_code' in d:
            o.content_share_code = d['content_share_code']
        if 'content_type' in d:
            o.content_type = d['content_type']
        if 'msg' in d:
            o.msg = d['msg']
        return o


