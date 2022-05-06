#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QrCodeOperationLog(object):

    def __init__(self):
        self._goods_id = None
        self._goods_name = None
        self._qr_code_id = None

    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value
    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value
    @property
    def qr_code_id(self):
        return self._qr_code_id

    @qr_code_id.setter
    def qr_code_id(self, value):
        self._qr_code_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.goods_id:
            if hasattr(self.goods_id, 'to_alipay_dict'):
                params['goods_id'] = self.goods_id.to_alipay_dict()
            else:
                params['goods_id'] = self.goods_id
        if self.goods_name:
            if hasattr(self.goods_name, 'to_alipay_dict'):
                params['goods_name'] = self.goods_name.to_alipay_dict()
            else:
                params['goods_name'] = self.goods_name
        if self.qr_code_id:
            if hasattr(self.qr_code_id, 'to_alipay_dict'):
                params['qr_code_id'] = self.qr_code_id.to_alipay_dict()
            else:
                params['qr_code_id'] = self.qr_code_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QrCodeOperationLog()
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'qr_code_id' in d:
            o.qr_code_id = d['qr_code_id']
        return o


