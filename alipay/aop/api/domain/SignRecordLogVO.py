#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SignRecordLogVO(object):

    def __init__(self):
        self._s_version = None
        self._status = None
        self._trans_date = None

    @property
    def s_version(self):
        return self._s_version

    @s_version.setter
    def s_version(self, value):
        self._s_version = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def trans_date(self):
        return self._trans_date

    @trans_date.setter
    def trans_date(self, value):
        self._trans_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.s_version:
            if hasattr(self.s_version, 'to_alipay_dict'):
                params['s_version'] = self.s_version.to_alipay_dict()
            else:
                params['s_version'] = self.s_version
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.trans_date:
            if hasattr(self.trans_date, 'to_alipay_dict'):
                params['trans_date'] = self.trans_date.to_alipay_dict()
            else:
                params['trans_date'] = self.trans_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SignRecordLogVO()
        if 's_version' in d:
            o.s_version = d['s_version']
        if 'status' in d:
            o.status = d['status']
        if 'trans_date' in d:
            o.trans_date = d['trans_date']
        return o


