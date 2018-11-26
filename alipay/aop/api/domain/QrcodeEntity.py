#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QrcodeEntity(object):

    def __init__(self):
        self._desk_id = None
        self._qrcode_id = None
        self._relation_id = None
        self._shop_id = None

    @property
    def desk_id(self):
        return self._desk_id

    @desk_id.setter
    def desk_id(self, value):
        self._desk_id = value
    @property
    def qrcode_id(self):
        return self._qrcode_id

    @qrcode_id.setter
    def qrcode_id(self, value):
        self._qrcode_id = value
    @property
    def relation_id(self):
        return self._relation_id

    @relation_id.setter
    def relation_id(self, value):
        self._relation_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.desk_id:
            if hasattr(self.desk_id, 'to_alipay_dict'):
                params['desk_id'] = self.desk_id.to_alipay_dict()
            else:
                params['desk_id'] = self.desk_id
        if self.qrcode_id:
            if hasattr(self.qrcode_id, 'to_alipay_dict'):
                params['qrcode_id'] = self.qrcode_id.to_alipay_dict()
            else:
                params['qrcode_id'] = self.qrcode_id
        if self.relation_id:
            if hasattr(self.relation_id, 'to_alipay_dict'):
                params['relation_id'] = self.relation_id.to_alipay_dict()
            else:
                params['relation_id'] = self.relation_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QrcodeEntity()
        if 'desk_id' in d:
            o.desk_id = d['desk_id']
        if 'qrcode_id' in d:
            o.qrcode_id = d['qrcode_id']
        if 'relation_id' in d:
            o.relation_id = d['relation_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


