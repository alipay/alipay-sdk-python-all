#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceTokenBatchqueryModel(object):

    def __init__(self):
        self._invoice_token = None
        self._scene = None

    @property
    def invoice_token(self):
        return self._invoice_token

    @invoice_token.setter
    def invoice_token(self, value):
        self._invoice_token = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.invoice_token:
            if hasattr(self.invoice_token, 'to_alipay_dict'):
                params['invoice_token'] = self.invoice_token.to_alipay_dict()
            else:
                params['invoice_token'] = self.invoice_token
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceTokenBatchqueryModel()
        if 'invoice_token' in d:
            o.invoice_token = d['invoice_token']
        if 'scene' in d:
            o.scene = d['scene']
        return o


