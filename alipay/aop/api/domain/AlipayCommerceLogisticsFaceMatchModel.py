#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLogisticsFaceMatchModel(object):

    def __init__(self):
        self._biz_type = None
        self._face_group = None
        self._face_image = None
        self._face_rectangle = None
        self._merchant_code = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def face_group(self):
        return self._face_group

    @face_group.setter
    def face_group(self, value):
        self._face_group = value
    @property
    def face_image(self):
        return self._face_image

    @face_image.setter
    def face_image(self, value):
        self._face_image = value
    @property
    def face_rectangle(self):
        return self._face_rectangle

    @face_rectangle.setter
    def face_rectangle(self, value):
        self._face_rectangle = value
    @property
    def merchant_code(self):
        return self._merchant_code

    @merchant_code.setter
    def merchant_code(self, value):
        self._merchant_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.face_group:
            if hasattr(self.face_group, 'to_alipay_dict'):
                params['face_group'] = self.face_group.to_alipay_dict()
            else:
                params['face_group'] = self.face_group
        if self.face_image:
            if hasattr(self.face_image, 'to_alipay_dict'):
                params['face_image'] = self.face_image.to_alipay_dict()
            else:
                params['face_image'] = self.face_image
        if self.face_rectangle:
            if hasattr(self.face_rectangle, 'to_alipay_dict'):
                params['face_rectangle'] = self.face_rectangle.to_alipay_dict()
            else:
                params['face_rectangle'] = self.face_rectangle
        if self.merchant_code:
            if hasattr(self.merchant_code, 'to_alipay_dict'):
                params['merchant_code'] = self.merchant_code.to_alipay_dict()
            else:
                params['merchant_code'] = self.merchant_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsFaceMatchModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'face_group' in d:
            o.face_group = d['face_group']
        if 'face_image' in d:
            o.face_image = d['face_image']
        if 'face_rectangle' in d:
            o.face_rectangle = d['face_rectangle']
        if 'merchant_code' in d:
            o.merchant_code = d['merchant_code']
        return o


