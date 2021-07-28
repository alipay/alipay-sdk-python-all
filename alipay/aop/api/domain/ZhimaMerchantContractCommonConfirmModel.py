#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaMerchantContractCommonConfirmModel(object):

    def __init__(self):
        self._ext_info = None
        self._offer_no = None
        self._out_biz_no = None
        self._sign_principal_id = None
        self._sign_principal_type = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def offer_no(self):
        return self._offer_no

    @offer_no.setter
    def offer_no(self, value):
        self._offer_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def sign_principal_id(self):
        return self._sign_principal_id

    @sign_principal_id.setter
    def sign_principal_id(self, value):
        self._sign_principal_id = value
    @property
    def sign_principal_type(self):
        return self._sign_principal_type

    @sign_principal_type.setter
    def sign_principal_type(self, value):
        self._sign_principal_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.offer_no:
            if hasattr(self.offer_no, 'to_alipay_dict'):
                params['offer_no'] = self.offer_no.to_alipay_dict()
            else:
                params['offer_no'] = self.offer_no
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.sign_principal_id:
            if hasattr(self.sign_principal_id, 'to_alipay_dict'):
                params['sign_principal_id'] = self.sign_principal_id.to_alipay_dict()
            else:
                params['sign_principal_id'] = self.sign_principal_id
        if self.sign_principal_type:
            if hasattr(self.sign_principal_type, 'to_alipay_dict'):
                params['sign_principal_type'] = self.sign_principal_type.to_alipay_dict()
            else:
                params['sign_principal_type'] = self.sign_principal_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaMerchantContractCommonConfirmModel()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'offer_no' in d:
            o.offer_no = d['offer_no']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'sign_principal_id' in d:
            o.sign_principal_id = d['sign_principal_id']
        if 'sign_principal_type' in d:
            o.sign_principal_type = d['sign_principal_type']
        return o


