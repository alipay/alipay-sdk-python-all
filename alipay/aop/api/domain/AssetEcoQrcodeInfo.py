#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AssetEcoQrcodeInfo(object):

    def __init__(self):
        self._biz_code = None
        self._idempotent_num = None
        self._qrcode = None
        self._qrcode_img_url = None
        self._qrcode_url = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def idempotent_num(self):
        return self._idempotent_num

    @idempotent_num.setter
    def idempotent_num(self, value):
        self._idempotent_num = value
    @property
    def qrcode(self):
        return self._qrcode

    @qrcode.setter
    def qrcode(self, value):
        self._qrcode = value
    @property
    def qrcode_img_url(self):
        return self._qrcode_img_url

    @qrcode_img_url.setter
    def qrcode_img_url(self, value):
        self._qrcode_img_url = value
    @property
    def qrcode_url(self):
        return self._qrcode_url

    @qrcode_url.setter
    def qrcode_url(self, value):
        self._qrcode_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.idempotent_num:
            if hasattr(self.idempotent_num, 'to_alipay_dict'):
                params['idempotent_num'] = self.idempotent_num.to_alipay_dict()
            else:
                params['idempotent_num'] = self.idempotent_num
        if self.qrcode:
            if hasattr(self.qrcode, 'to_alipay_dict'):
                params['qrcode'] = self.qrcode.to_alipay_dict()
            else:
                params['qrcode'] = self.qrcode
        if self.qrcode_img_url:
            if hasattr(self.qrcode_img_url, 'to_alipay_dict'):
                params['qrcode_img_url'] = self.qrcode_img_url.to_alipay_dict()
            else:
                params['qrcode_img_url'] = self.qrcode_img_url
        if self.qrcode_url:
            if hasattr(self.qrcode_url, 'to_alipay_dict'):
                params['qrcode_url'] = self.qrcode_url.to_alipay_dict()
            else:
                params['qrcode_url'] = self.qrcode_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssetEcoQrcodeInfo()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'idempotent_num' in d:
            o.idempotent_num = d['idempotent_num']
        if 'qrcode' in d:
            o.qrcode = d['qrcode']
        if 'qrcode_img_url' in d:
            o.qrcode_img_url = d['qrcode_img_url']
        if 'qrcode_url' in d:
            o.qrcode_url = d['qrcode_url']
        return o


