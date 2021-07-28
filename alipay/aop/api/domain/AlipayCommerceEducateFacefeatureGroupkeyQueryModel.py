#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateFacefeatureGroupkeyQueryModel(object):

    def __init__(self):
        self._biz_code = None
        self._isv_name = None
        self._school_stdcode = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateFacefeatureGroupkeyQueryModel()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'isv_name' in d:
            o.isv_name = d['isv_name']
        if 'school_stdcode' in d:
            o.school_stdcode = d['school_stdcode']
        return o


