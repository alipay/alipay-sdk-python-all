#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalInsuranceEncryptfileTransformModel(object):

    def __init__(self):
        self._biz_type = None
        self._file_content_encrypt = None
        self._file_name = None
        self._file_size = None
        self._file_type = None
        self._request_no = None
        self._scene = None
        self._secret_key = None
        self._source = None
        self._tpa_id = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def file_content_encrypt(self):
        return self._file_content_encrypt

    @file_content_encrypt.setter
    def file_content_encrypt(self, value):
        self._file_content_encrypt = value
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
    @property
    def file_size(self):
        return self._file_size

    @file_size.setter
    def file_size(self, value):
        self._file_size = value
    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value
    @property
    def request_no(self):
        return self._request_no

    @request_no.setter
    def request_no(self, value):
        self._request_no = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def secret_key(self):
        return self._secret_key

    @secret_key.setter
    def secret_key(self, value):
        self._secret_key = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def tpa_id(self):
        return self._tpa_id

    @tpa_id.setter
    def tpa_id(self, value):
        self._tpa_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.file_content_encrypt:
            if hasattr(self.file_content_encrypt, 'to_alipay_dict'):
                params['file_content_encrypt'] = self.file_content_encrypt.to_alipay_dict()
            else:
                params['file_content_encrypt'] = self.file_content_encrypt
        if self.file_name:
            if hasattr(self.file_name, 'to_alipay_dict'):
                params['file_name'] = self.file_name.to_alipay_dict()
            else:
                params['file_name'] = self.file_name
        if self.file_size:
            if hasattr(self.file_size, 'to_alipay_dict'):
                params['file_size'] = self.file_size.to_alipay_dict()
            else:
                params['file_size'] = self.file_size
        if self.file_type:
            if hasattr(self.file_type, 'to_alipay_dict'):
                params['file_type'] = self.file_type.to_alipay_dict()
            else:
                params['file_type'] = self.file_type
        if self.request_no:
            if hasattr(self.request_no, 'to_alipay_dict'):
                params['request_no'] = self.request_no.to_alipay_dict()
            else:
                params['request_no'] = self.request_no
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.secret_key:
            if hasattr(self.secret_key, 'to_alipay_dict'):
                params['secret_key'] = self.secret_key.to_alipay_dict()
            else:
                params['secret_key'] = self.secret_key
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.tpa_id:
            if hasattr(self.tpa_id, 'to_alipay_dict'):
                params['tpa_id'] = self.tpa_id.to_alipay_dict()
            else:
                params['tpa_id'] = self.tpa_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalInsuranceEncryptfileTransformModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'file_content_encrypt' in d:
            o.file_content_encrypt = d['file_content_encrypt']
        if 'file_name' in d:
            o.file_name = d['file_name']
        if 'file_size' in d:
            o.file_size = d['file_size']
        if 'file_type' in d:
            o.file_type = d['file_type']
        if 'request_no' in d:
            o.request_no = d['request_no']
        if 'scene' in d:
            o.scene = d['scene']
        if 'secret_key' in d:
            o.secret_key = d['secret_key']
        if 'source' in d:
            o.source = d['source']
        if 'tpa_id' in d:
            o.tpa_id = d['tpa_id']
        return o


