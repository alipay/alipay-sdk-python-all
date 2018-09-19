#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AccessReturnQrcode(object):

    def __init__(self):
        self._asset_purchase_id = None
        self._express_no = None
        self._out_biz_no = None
        self._qrcode = None

    @property
    def asset_purchase_id(self):
        return self._asset_purchase_id

    @asset_purchase_id.setter
    def asset_purchase_id(self, value):
        self._asset_purchase_id = value
    @property
    def express_no(self):
        return self._express_no

    @express_no.setter
    def express_no(self, value):
        self._express_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def qrcode(self):
        return self._qrcode

    @qrcode.setter
    def qrcode(self, value):
        self._qrcode = value


    def to_alipay_dict(self):
        params = dict()
        if self.asset_purchase_id:
            if hasattr(self.asset_purchase_id, 'to_alipay_dict'):
                params['asset_purchase_id'] = self.asset_purchase_id.to_alipay_dict()
            else:
                params['asset_purchase_id'] = self.asset_purchase_id
        if self.express_no:
            if hasattr(self.express_no, 'to_alipay_dict'):
                params['express_no'] = self.express_no.to_alipay_dict()
            else:
                params['express_no'] = self.express_no
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.qrcode:
            if hasattr(self.qrcode, 'to_alipay_dict'):
                params['qrcode'] = self.qrcode.to_alipay_dict()
            else:
                params['qrcode'] = self.qrcode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AccessReturnQrcode()
        if 'asset_purchase_id' in d:
            o.asset_purchase_id = d['asset_purchase_id']
        if 'express_no' in d:
            o.express_no = d['express_no']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'qrcode' in d:
            o.qrcode = d['qrcode']
        return o


