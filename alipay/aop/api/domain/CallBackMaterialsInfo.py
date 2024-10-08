#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CallBackMaterialsInfo(object):

    def __init__(self):
        self._desk_no = None
        self._qr_code_url = None

    @property
    def desk_no(self):
        return self._desk_no

    @desk_no.setter
    def desk_no(self, value):
        self._desk_no = value
    @property
    def qr_code_url(self):
        return self._qr_code_url

    @qr_code_url.setter
    def qr_code_url(self, value):
        self._qr_code_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.desk_no:
            if hasattr(self.desk_no, 'to_alipay_dict'):
                params['desk_no'] = self.desk_no.to_alipay_dict()
            else:
                params['desk_no'] = self.desk_no
        if self.qr_code_url:
            if hasattr(self.qr_code_url, 'to_alipay_dict'):
                params['qr_code_url'] = self.qr_code_url.to_alipay_dict()
            else:
                params['qr_code_url'] = self.qr_code_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CallBackMaterialsInfo()
        if 'desk_no' in d:
            o.desk_no = d['desk_no']
        if 'qr_code_url' in d:
            o.qr_code_url = d['qr_code_url']
        return o


