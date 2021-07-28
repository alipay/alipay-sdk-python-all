#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditUserOpenCertifyInitializeModel(object):

    def __init__(self):
        self._biz_code = None
        self._face_contrast_picture = None
        self._identity_param = None
        self._merchant_config = None
        self._outer_order_no = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def face_contrast_picture(self):
        return self._face_contrast_picture

    @face_contrast_picture.setter
    def face_contrast_picture(self, value):
        self._face_contrast_picture = value
    @property
    def identity_param(self):
        return self._identity_param

    @identity_param.setter
    def identity_param(self, value):
        self._identity_param = value
    @property
    def merchant_config(self):
        return self._merchant_config

    @merchant_config.setter
    def merchant_config(self, value):
        self._merchant_config = value
    @property
    def outer_order_no(self):
        return self._outer_order_no

    @outer_order_no.setter
    def outer_order_no(self, value):
        self._outer_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.face_contrast_picture:
            if hasattr(self.face_contrast_picture, 'to_alipay_dict'):
                params['face_contrast_picture'] = self.face_contrast_picture.to_alipay_dict()
            else:
                params['face_contrast_picture'] = self.face_contrast_picture
        if self.identity_param:
            if hasattr(self.identity_param, 'to_alipay_dict'):
                params['identity_param'] = self.identity_param.to_alipay_dict()
            else:
                params['identity_param'] = self.identity_param
        if self.merchant_config:
            if hasattr(self.merchant_config, 'to_alipay_dict'):
                params['merchant_config'] = self.merchant_config.to_alipay_dict()
            else:
                params['merchant_config'] = self.merchant_config
        if self.outer_order_no:
            if hasattr(self.outer_order_no, 'to_alipay_dict'):
                params['outer_order_no'] = self.outer_order_no.to_alipay_dict()
            else:
                params['outer_order_no'] = self.outer_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditUserOpenCertifyInitializeModel()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'face_contrast_picture' in d:
            o.face_contrast_picture = d['face_contrast_picture']
        if 'identity_param' in d:
            o.identity_param = d['identity_param']
        if 'merchant_config' in d:
            o.merchant_config = d['merchant_config']
        if 'outer_order_no' in d:
            o.outer_order_no = d['outer_order_no']
        return o


