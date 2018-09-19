#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbAdvertContentCodec import KbAdvertContentCodec
from alipay.aop.api.domain.KbAdvertContentPassword import KbAdvertContentPassword
from alipay.aop.api.domain.KbAdvertContentShareCode import KbAdvertContentShareCode
from alipay.aop.api.domain.KbAdvertContentShortLink import KbAdvertContentShortLink


class KbAdvertAdvContentResponse(object):

    def __init__(self):
        self._content_codec = None
        self._content_password = None
        self._content_share_code = None
        self._content_short_link = None
        self._content_type = None

    @property
    def content_codec(self):
        return self._content_codec

    @content_codec.setter
    def content_codec(self, value):
        if isinstance(value, KbAdvertContentCodec):
            self._content_codec = value
        else:
            self._content_codec = KbAdvertContentCodec.from_alipay_dict(value)
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
        if isinstance(value, list):
            self._content_share_code = list()
            for i in value:
                if isinstance(i, KbAdvertContentShareCode):
                    self._content_share_code.append(i)
                else:
                    self._content_share_code.append(KbAdvertContentShareCode.from_alipay_dict(i))
    @property
    def content_short_link(self):
        return self._content_short_link

    @content_short_link.setter
    def content_short_link(self, value):
        if isinstance(value, KbAdvertContentShortLink):
            self._content_short_link = value
        else:
            self._content_short_link = KbAdvertContentShortLink.from_alipay_dict(value)
    @property
    def content_type(self):
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        self._content_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.content_codec:
            if hasattr(self.content_codec, 'to_alipay_dict'):
                params['content_codec'] = self.content_codec.to_alipay_dict()
            else:
                params['content_codec'] = self.content_codec
        if self.content_password:
            if hasattr(self.content_password, 'to_alipay_dict'):
                params['content_password'] = self.content_password.to_alipay_dict()
            else:
                params['content_password'] = self.content_password
        if self.content_share_code:
            if isinstance(self.content_share_code, list):
                for i in range(0, len(self.content_share_code)):
                    element = self.content_share_code[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.content_share_code[i] = element.to_alipay_dict()
            if hasattr(self.content_share_code, 'to_alipay_dict'):
                params['content_share_code'] = self.content_share_code.to_alipay_dict()
            else:
                params['content_share_code'] = self.content_share_code
        if self.content_short_link:
            if hasattr(self.content_short_link, 'to_alipay_dict'):
                params['content_short_link'] = self.content_short_link.to_alipay_dict()
            else:
                params['content_short_link'] = self.content_short_link
        if self.content_type:
            if hasattr(self.content_type, 'to_alipay_dict'):
                params['content_type'] = self.content_type.to_alipay_dict()
            else:
                params['content_type'] = self.content_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbAdvertAdvContentResponse()
        if 'content_codec' in d:
            o.content_codec = d['content_codec']
        if 'content_password' in d:
            o.content_password = d['content_password']
        if 'content_share_code' in d:
            o.content_share_code = d['content_share_code']
        if 'content_short_link' in d:
            o.content_short_link = d['content_short_link']
        if 'content_type' in d:
            o.content_type = d['content_type']
        return o


