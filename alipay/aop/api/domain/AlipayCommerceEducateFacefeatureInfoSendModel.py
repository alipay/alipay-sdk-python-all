#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateFacefeatureInfoSendModel(object):

    def __init__(self):
        self._alg_version = None
        self._biz_code = None
        self._cert_no = None
        self._cert_type = None
        self._ext_info = None
        self._isv_name = None
        self._school_stdcode = None
        self._user_ids = None

    @property
    def alg_version(self):
        return self._alg_version

    @alg_version.setter
    def alg_version(self, value):
        self._alg_version = value
    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def isv_name(self):
        return self._isv_name

    @isv_name.setter
    def isv_name(self, value):
        self._isv_name = value
    @property
    def school_stdcode(self):
        return self._school_stdcode

    @school_stdcode.setter
    def school_stdcode(self, value):
        self._school_stdcode = value
    @property
    def user_ids(self):
        return self._user_ids

    @user_ids.setter
    def user_ids(self, value):
        if isinstance(value, list):
            self._user_ids = list()
            for i in value:
                self._user_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.alg_version:
            if hasattr(self.alg_version, 'to_alipay_dict'):
                params['alg_version'] = self.alg_version.to_alipay_dict()
            else:
                params['alg_version'] = self.alg_version
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.isv_name:
            if hasattr(self.isv_name, 'to_alipay_dict'):
                params['isv_name'] = self.isv_name.to_alipay_dict()
            else:
                params['isv_name'] = self.isv_name
        if self.school_stdcode:
            if hasattr(self.school_stdcode, 'to_alipay_dict'):
                params['school_stdcode'] = self.school_stdcode.to_alipay_dict()
            else:
                params['school_stdcode'] = self.school_stdcode
        if self.user_ids:
            if isinstance(self.user_ids, list):
                for i in range(0, len(self.user_ids)):
                    element = self.user_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user_ids[i] = element.to_alipay_dict()
            if hasattr(self.user_ids, 'to_alipay_dict'):
                params['user_ids'] = self.user_ids.to_alipay_dict()
            else:
                params['user_ids'] = self.user_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateFacefeatureInfoSendModel()
        if 'alg_version' in d:
            o.alg_version = d['alg_version']
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'isv_name' in d:
            o.isv_name = d['isv_name']
        if 'school_stdcode' in d:
            o.school_stdcode = d['school_stdcode']
        if 'user_ids' in d:
            o.user_ids = d['user_ids']
        return o


