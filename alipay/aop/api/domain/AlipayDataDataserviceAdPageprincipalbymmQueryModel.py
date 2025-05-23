#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceAdPageprincipalbymmQueryModel(object):

    def __init__(self):
        self._alipay_oid = None
        self._biz_token = None
        self._current = None
        self._key_word = None
        self._page_size = None
        self._principal_tag = None
        self._status = None

    @property
    def alipay_oid(self):
        return self._alipay_oid

    @alipay_oid.setter
    def alipay_oid(self, value):
        self._alipay_oid = value
    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def current(self):
        return self._current

    @current.setter
    def current(self, value):
        self._current = value
    @property
    def key_word(self):
        return self._key_word

    @key_word.setter
    def key_word(self, value):
        self._key_word = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def principal_tag(self):
        return self._principal_tag

    @principal_tag.setter
    def principal_tag(self, value):
        self._principal_tag = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_oid:
            if hasattr(self.alipay_oid, 'to_alipay_dict'):
                params['alipay_oid'] = self.alipay_oid.to_alipay_dict()
            else:
                params['alipay_oid'] = self.alipay_oid
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.current:
            if hasattr(self.current, 'to_alipay_dict'):
                params['current'] = self.current.to_alipay_dict()
            else:
                params['current'] = self.current
        if self.key_word:
            if hasattr(self.key_word, 'to_alipay_dict'):
                params['key_word'] = self.key_word.to_alipay_dict()
            else:
                params['key_word'] = self.key_word
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.principal_tag:
            if hasattr(self.principal_tag, 'to_alipay_dict'):
                params['principal_tag'] = self.principal_tag.to_alipay_dict()
            else:
                params['principal_tag'] = self.principal_tag
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAdPageprincipalbymmQueryModel()
        if 'alipay_oid' in d:
            o.alipay_oid = d['alipay_oid']
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'current' in d:
            o.current = d['current']
        if 'key_word' in d:
            o.key_word = d['key_word']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'principal_tag' in d:
            o.principal_tag = d['principal_tag']
        if 'status' in d:
            o.status = d['status']
        return o


