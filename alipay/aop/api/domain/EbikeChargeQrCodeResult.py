#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EbikeChargeQrCodeResult(object):

    def __init__(self):
        self._biz_no = None
        self._link_code = None
        self._qr_code = None
        self._qr_code_url = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def link_code(self):
        return self._link_code

    @link_code.setter
    def link_code(self, value):
        self._link_code = value
    @property
    def qr_code(self):
        return self._qr_code

    @qr_code.setter
    def qr_code(self, value):
        self._qr_code = value
    @property
    def qr_code_url(self):
        return self._qr_code_url

    @qr_code_url.setter
    def qr_code_url(self, value):
        self._qr_code_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.link_code:
            if hasattr(self.link_code, 'to_alipay_dict'):
                params['link_code'] = self.link_code.to_alipay_dict()
            else:
                params['link_code'] = self.link_code
        if self.qr_code:
            if hasattr(self.qr_code, 'to_alipay_dict'):
                params['qr_code'] = self.qr_code.to_alipay_dict()
            else:
                params['qr_code'] = self.qr_code
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
        o = EbikeChargeQrCodeResult()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'link_code' in d:
            o.link_code = d['link_code']
        if 'qr_code' in d:
            o.qr_code = d['qr_code']
        if 'qr_code_url' in d:
            o.qr_code_url = d['qr_code_url']
        return o


