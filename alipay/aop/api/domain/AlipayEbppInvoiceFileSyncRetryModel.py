#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceFileSyncRetryModel(object):

    def __init__(self):
        self._einv_code = None
        self._einv_no = None
        self._file_url = None
        self._is_url_replace = None
        self._m_short_name = None
        self._out_biz_no = None
        self._user_id = None

    @property
    def einv_code(self):
        return self._einv_code

    @einv_code.setter
    def einv_code(self, value):
        self._einv_code = value
    @property
    def einv_no(self):
        return self._einv_no

    @einv_no.setter
    def einv_no(self, value):
        self._einv_no = value
    @property
    def file_url(self):
        return self._file_url

    @file_url.setter
    def file_url(self, value):
        self._file_url = value
    @property
    def is_url_replace(self):
        return self._is_url_replace

    @is_url_replace.setter
    def is_url_replace(self, value):
        self._is_url_replace = value
    @property
    def m_short_name(self):
        return self._m_short_name

    @m_short_name.setter
    def m_short_name(self, value):
        self._m_short_name = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.einv_code:
            if hasattr(self.einv_code, 'to_alipay_dict'):
                params['einv_code'] = self.einv_code.to_alipay_dict()
            else:
                params['einv_code'] = self.einv_code
        if self.einv_no:
            if hasattr(self.einv_no, 'to_alipay_dict'):
                params['einv_no'] = self.einv_no.to_alipay_dict()
            else:
                params['einv_no'] = self.einv_no
        if self.file_url:
            if hasattr(self.file_url, 'to_alipay_dict'):
                params['file_url'] = self.file_url.to_alipay_dict()
            else:
                params['file_url'] = self.file_url
        if self.is_url_replace:
            if hasattr(self.is_url_replace, 'to_alipay_dict'):
                params['is_url_replace'] = self.is_url_replace.to_alipay_dict()
            else:
                params['is_url_replace'] = self.is_url_replace
        if self.m_short_name:
            if hasattr(self.m_short_name, 'to_alipay_dict'):
                params['m_short_name'] = self.m_short_name.to_alipay_dict()
            else:
                params['m_short_name'] = self.m_short_name
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceFileSyncRetryModel()
        if 'einv_code' in d:
            o.einv_code = d['einv_code']
        if 'einv_no' in d:
            o.einv_no = d['einv_no']
        if 'file_url' in d:
            o.file_url = d['file_url']
        if 'is_url_replace' in d:
            o.is_url_replace = d['is_url_replace']
        if 'm_short_name' in d:
            o.m_short_name = d['m_short_name']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


