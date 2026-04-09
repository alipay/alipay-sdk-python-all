#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DepositFileList(object):

    def __init__(self):
        self._deposit_certify_url = None
        self._file_hash = None
        self._file_md_5 = None
        self._file_name = None
        self._tx_hash = None

    @property
    def deposit_certify_url(self):
        return self._deposit_certify_url

    @deposit_certify_url.setter
    def deposit_certify_url(self, value):
        self._deposit_certify_url = value
    @property
    def file_hash(self):
        return self._file_hash

    @file_hash.setter
    def file_hash(self, value):
        self._file_hash = value
    @property
    def file_md_5(self):
        return self._file_md_5

    @file_md_5.setter
    def file_md_5(self, value):
        self._file_md_5 = value
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
    @property
    def tx_hash(self):
        return self._tx_hash

    @tx_hash.setter
    def tx_hash(self, value):
        self._tx_hash = value


    def to_alipay_dict(self):
        params = dict()
        if self.deposit_certify_url:
            if hasattr(self.deposit_certify_url, 'to_alipay_dict'):
                params['deposit_certify_url'] = self.deposit_certify_url.to_alipay_dict()
            else:
                params['deposit_certify_url'] = self.deposit_certify_url
        if self.file_hash:
            if hasattr(self.file_hash, 'to_alipay_dict'):
                params['file_hash'] = self.file_hash.to_alipay_dict()
            else:
                params['file_hash'] = self.file_hash
        if self.file_md_5:
            if hasattr(self.file_md_5, 'to_alipay_dict'):
                params['file_md_5'] = self.file_md_5.to_alipay_dict()
            else:
                params['file_md_5'] = self.file_md_5
        if self.file_name:
            if hasattr(self.file_name, 'to_alipay_dict'):
                params['file_name'] = self.file_name.to_alipay_dict()
            else:
                params['file_name'] = self.file_name
        if self.tx_hash:
            if hasattr(self.tx_hash, 'to_alipay_dict'):
                params['tx_hash'] = self.tx_hash.to_alipay_dict()
            else:
                params['tx_hash'] = self.tx_hash
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DepositFileList()
        if 'deposit_certify_url' in d:
            o.deposit_certify_url = d['deposit_certify_url']
        if 'file_hash' in d:
            o.file_hash = d['file_hash']
        if 'file_md_5' in d:
            o.file_md_5 = d['file_md_5']
        if 'file_name' in d:
            o.file_name = d['file_name']
        if 'tx_hash' in d:
            o.tx_hash = d['tx_hash']
        return o


