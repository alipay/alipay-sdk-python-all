#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandEcoEmptycodeCreateModel(object):

    def __init__(self):
        self._busi_platform = None
        self._code_pack_date = None
        self._eco_code = None
        self._qrcode_token = None
        self._shop_code = None

    @property
    def busi_platform(self):
        return self._busi_platform

    @busi_platform.setter
    def busi_platform(self, value):
        self._busi_platform = value
    @property
    def code_pack_date(self):
        return self._code_pack_date

    @code_pack_date.setter
    def code_pack_date(self, value):
        self._code_pack_date = value
    @property
    def eco_code(self):
        return self._eco_code

    @eco_code.setter
    def eco_code(self, value):
        self._eco_code = value
    @property
    def qrcode_token(self):
        return self._qrcode_token

    @qrcode_token.setter
    def qrcode_token(self, value):
        self._qrcode_token = value
    @property
    def shop_code(self):
        return self._shop_code

    @shop_code.setter
    def shop_code(self, value):
        self._shop_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.busi_platform:
            if hasattr(self.busi_platform, 'to_alipay_dict'):
                params['busi_platform'] = self.busi_platform.to_alipay_dict()
            else:
                params['busi_platform'] = self.busi_platform
        if self.code_pack_date:
            if hasattr(self.code_pack_date, 'to_alipay_dict'):
                params['code_pack_date'] = self.code_pack_date.to_alipay_dict()
            else:
                params['code_pack_date'] = self.code_pack_date
        if self.eco_code:
            if hasattr(self.eco_code, 'to_alipay_dict'):
                params['eco_code'] = self.eco_code.to_alipay_dict()
            else:
                params['eco_code'] = self.eco_code
        if self.qrcode_token:
            if hasattr(self.qrcode_token, 'to_alipay_dict'):
                params['qrcode_token'] = self.qrcode_token.to_alipay_dict()
            else:
                params['qrcode_token'] = self.qrcode_token
        if self.shop_code:
            if hasattr(self.shop_code, 'to_alipay_dict'):
                params['shop_code'] = self.shop_code.to_alipay_dict()
            else:
                params['shop_code'] = self.shop_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandEcoEmptycodeCreateModel()
        if 'busi_platform' in d:
            o.busi_platform = d['busi_platform']
        if 'code_pack_date' in d:
            o.code_pack_date = d['code_pack_date']
        if 'eco_code' in d:
            o.eco_code = d['eco_code']
        if 'qrcode_token' in d:
            o.qrcode_token = d['qrcode_token']
        if 'shop_code' in d:
            o.shop_code = d['shop_code']
        return o


