#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceCityfacilitatorIotbspFwjnfcUploadModel(object):

    def __init__(self):
        self._fetch_time = None
        self._nfc_sn = None
        self._open_id = None
        self._pid = None
        self._upper_sn = None
        self._url = None

    @property
    def fetch_time(self):
        return self._fetch_time

    @fetch_time.setter
    def fetch_time(self, value):
        self._fetch_time = value
    @property
    def nfc_sn(self):
        return self._nfc_sn

    @nfc_sn.setter
    def nfc_sn(self, value):
        self._nfc_sn = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def upper_sn(self):
        return self._upper_sn

    @upper_sn.setter
    def upper_sn(self, value):
        self._upper_sn = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.fetch_time:
            if hasattr(self.fetch_time, 'to_alipay_dict'):
                params['fetch_time'] = self.fetch_time.to_alipay_dict()
            else:
                params['fetch_time'] = self.fetch_time
        if self.nfc_sn:
            if hasattr(self.nfc_sn, 'to_alipay_dict'):
                params['nfc_sn'] = self.nfc_sn.to_alipay_dict()
            else:
                params['nfc_sn'] = self.nfc_sn
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.upper_sn:
            if hasattr(self.upper_sn, 'to_alipay_dict'):
                params['upper_sn'] = self.upper_sn.to_alipay_dict()
            else:
                params['upper_sn'] = self.upper_sn
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
        o = AlipayCommerceCityfacilitatorIotbspFwjnfcUploadModel()
        if 'fetch_time' in d:
            o.fetch_time = d['fetch_time']
        if 'nfc_sn' in d:
            o.nfc_sn = d['nfc_sn']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'pid' in d:
            o.pid = d['pid']
        if 'upper_sn' in d:
            o.upper_sn = d['upper_sn']
        if 'url' in d:
            o.url = d['url']
        return o


