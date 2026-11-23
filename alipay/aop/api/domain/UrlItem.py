#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UrlItem(object):

    def __init__(self):
        self._attachment_id = None
        self._file_path = None
        self._murl = None
        self._nurl = None
        self._signed = None
        self._turl = None
        self._url = None

    @property
    def attachment_id(self):
        return self._attachment_id

    @attachment_id.setter
    def attachment_id(self, value):
        self._attachment_id = value
    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, value):
        self._file_path = value
    @property
    def murl(self):
        return self._murl

    @murl.setter
    def murl(self, value):
        self._murl = value
    @property
    def nurl(self):
        return self._nurl

    @nurl.setter
    def nurl(self, value):
        self._nurl = value
    @property
    def signed(self):
        return self._signed

    @signed.setter
    def signed(self, value):
        self._signed = value
    @property
    def turl(self):
        return self._turl

    @turl.setter
    def turl(self, value):
        self._turl = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.attachment_id:
            if hasattr(self.attachment_id, 'to_alipay_dict'):
                params['attachment_id'] = self.attachment_id.to_alipay_dict()
            else:
                params['attachment_id'] = self.attachment_id
        if self.file_path:
            if hasattr(self.file_path, 'to_alipay_dict'):
                params['file_path'] = self.file_path.to_alipay_dict()
            else:
                params['file_path'] = self.file_path
        if self.murl:
            if hasattr(self.murl, 'to_alipay_dict'):
                params['murl'] = self.murl.to_alipay_dict()
            else:
                params['murl'] = self.murl
        if self.nurl:
            if hasattr(self.nurl, 'to_alipay_dict'):
                params['nurl'] = self.nurl.to_alipay_dict()
            else:
                params['nurl'] = self.nurl
        if self.signed:
            if hasattr(self.signed, 'to_alipay_dict'):
                params['signed'] = self.signed.to_alipay_dict()
            else:
                params['signed'] = self.signed
        if self.turl:
            if hasattr(self.turl, 'to_alipay_dict'):
                params['turl'] = self.turl.to_alipay_dict()
            else:
                params['turl'] = self.turl
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UrlItem()
        if 'attachment_id' in d:
            o.attachment_id = d['attachment_id']
        if 'file_path' in d:
            o.file_path = d['file_path']
        if 'murl' in d:
            o.murl = d['murl']
        if 'nurl' in d:
            o.nurl = d['nurl']
        if 'signed' in d:
            o.signed = d['signed']
        if 'turl' in d:
            o.turl = d['turl']
        if 'url' in d:
            o.url = d['url']
        return o


