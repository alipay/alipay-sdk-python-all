#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPayDeviceNlinkNfccallbackSyncModel(object):

    def __init__(self):
        self._biz_code = None
        self._biz_user_id = None
        self._nfc_callback_content = None
        self._ntoken = None
        self._sub_biz_code = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def biz_user_id(self):
        return self._biz_user_id

    @biz_user_id.setter
    def biz_user_id(self, value):
        self._biz_user_id = value
    @property
    def nfc_callback_content(self):
        return self._nfc_callback_content

    @nfc_callback_content.setter
    def nfc_callback_content(self, value):
        self._nfc_callback_content = value
    @property
    def ntoken(self):
        return self._ntoken

    @ntoken.setter
    def ntoken(self, value):
        self._ntoken = value
    @property
    def sub_biz_code(self):
        return self._sub_biz_code

    @sub_biz_code.setter
    def sub_biz_code(self, value):
        self._sub_biz_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.biz_user_id:
            if hasattr(self.biz_user_id, 'to_alipay_dict'):
                params['biz_user_id'] = self.biz_user_id.to_alipay_dict()
            else:
                params['biz_user_id'] = self.biz_user_id
        if self.nfc_callback_content:
            if hasattr(self.nfc_callback_content, 'to_alipay_dict'):
                params['nfc_callback_content'] = self.nfc_callback_content.to_alipay_dict()
            else:
                params['nfc_callback_content'] = self.nfc_callback_content
        if self.ntoken:
            if hasattr(self.ntoken, 'to_alipay_dict'):
                params['ntoken'] = self.ntoken.to_alipay_dict()
            else:
                params['ntoken'] = self.ntoken
        if self.sub_biz_code:
            if hasattr(self.sub_biz_code, 'to_alipay_dict'):
                params['sub_biz_code'] = self.sub_biz_code.to_alipay_dict()
            else:
                params['sub_biz_code'] = self.sub_biz_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPayDeviceNlinkNfccallbackSyncModel()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'biz_user_id' in d:
            o.biz_user_id = d['biz_user_id']
        if 'nfc_callback_content' in d:
            o.nfc_callback_content = d['nfc_callback_content']
        if 'ntoken' in d:
            o.ntoken = d['ntoken']
        if 'sub_biz_code' in d:
            o.sub_biz_code = d['sub_biz_code']
        return o


