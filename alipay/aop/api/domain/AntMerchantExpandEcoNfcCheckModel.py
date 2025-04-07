#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandEcoNfcCheckModel(object):

    def __init__(self):
        self._nfc_token = None
        self._tag_id = None
        self._upload_qrcode_url = None

    @property
    def nfc_token(self):
        return self._nfc_token

    @nfc_token.setter
    def nfc_token(self, value):
        self._nfc_token = value
    @property
    def tag_id(self):
        return self._tag_id

    @tag_id.setter
    def tag_id(self, value):
        self._tag_id = value
    @property
    def upload_qrcode_url(self):
        return self._upload_qrcode_url

    @upload_qrcode_url.setter
    def upload_qrcode_url(self, value):
        self._upload_qrcode_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.nfc_token:
            if hasattr(self.nfc_token, 'to_alipay_dict'):
                params['nfc_token'] = self.nfc_token.to_alipay_dict()
            else:
                params['nfc_token'] = self.nfc_token
        if self.tag_id:
            if hasattr(self.tag_id, 'to_alipay_dict'):
                params['tag_id'] = self.tag_id.to_alipay_dict()
            else:
                params['tag_id'] = self.tag_id
        if self.upload_qrcode_url:
            if hasattr(self.upload_qrcode_url, 'to_alipay_dict'):
                params['upload_qrcode_url'] = self.upload_qrcode_url.to_alipay_dict()
            else:
                params['upload_qrcode_url'] = self.upload_qrcode_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandEcoNfcCheckModel()
        if 'nfc_token' in d:
            o.nfc_token = d['nfc_token']
        if 'tag_id' in d:
            o.tag_id = d['tag_id']
        if 'upload_qrcode_url' in d:
            o.upload_qrcode_url = d['upload_qrcode_url']
        return o


