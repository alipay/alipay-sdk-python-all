#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.QrCodeBusinessParam import QrCodeBusinessParam


class AlipayCommerceOperationIsvQrcodeBindModel(object):

    def __init__(self):
        self._biz_scene = None
        self._business_params = None
        self._mini_type = None
        self._page = None
        self._qrcode_url = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def business_params(self):
        return self._business_params

    @business_params.setter
    def business_params(self, value):
        if isinstance(value, QrCodeBusinessParam):
            self._business_params = value
        else:
            self._business_params = QrCodeBusinessParam.from_alipay_dict(value)
    @property
    def mini_type(self):
        return self._mini_type

    @mini_type.setter
    def mini_type(self, value):
        self._mini_type = value
    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value
    @property
    def qrcode_url(self):
        return self._qrcode_url

    @qrcode_url.setter
    def qrcode_url(self, value):
        self._qrcode_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.business_params:
            if hasattr(self.business_params, 'to_alipay_dict'):
                params['business_params'] = self.business_params.to_alipay_dict()
            else:
                params['business_params'] = self.business_params
        if self.mini_type:
            if hasattr(self.mini_type, 'to_alipay_dict'):
                params['mini_type'] = self.mini_type.to_alipay_dict()
            else:
                params['mini_type'] = self.mini_type
        if self.page:
            if hasattr(self.page, 'to_alipay_dict'):
                params['page'] = self.page.to_alipay_dict()
            else:
                params['page'] = self.page
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
        o = AlipayCommerceOperationIsvQrcodeBindModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'business_params' in d:
            o.business_params = d['business_params']
        if 'mini_type' in d:
            o.mini_type = d['mini_type']
        if 'page' in d:
            o.page = d['page']
        if 'qrcode_url' in d:
            o.qrcode_url = d['qrcode_url']
        return o


