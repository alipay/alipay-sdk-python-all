#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdNfcdkPartsModifyModel(object):

    def __init__(self):
        self._brand_id = None
        self._tag_id = None
        self._tag_sn = None
        self._tuid = None
        self._vin = None

    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value
    @property
    def tag_id(self):
        return self._tag_id

    @tag_id.setter
    def tag_id(self, value):
        self._tag_id = value
    @property
    def tag_sn(self):
        return self._tag_sn

    @tag_sn.setter
    def tag_sn(self, value):
        self._tag_sn = value
    @property
    def tuid(self):
        return self._tuid

    @tuid.setter
    def tuid(self, value):
        self._tuid = value
    @property
    def vin(self):
        return self._vin

    @vin.setter
    def vin(self, value):
        self._vin = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_id:
            if hasattr(self.brand_id, 'to_alipay_dict'):
                params['brand_id'] = self.brand_id.to_alipay_dict()
            else:
                params['brand_id'] = self.brand_id
        if self.tag_id:
            if hasattr(self.tag_id, 'to_alipay_dict'):
                params['tag_id'] = self.tag_id.to_alipay_dict()
            else:
                params['tag_id'] = self.tag_id
        if self.tag_sn:
            if hasattr(self.tag_sn, 'to_alipay_dict'):
                params['tag_sn'] = self.tag_sn.to_alipay_dict()
            else:
                params['tag_sn'] = self.tag_sn
        if self.tuid:
            if hasattr(self.tuid, 'to_alipay_dict'):
                params['tuid'] = self.tuid.to_alipay_dict()
            else:
                params['tuid'] = self.tuid
        if self.vin:
            if hasattr(self.vin, 'to_alipay_dict'):
                params['vin'] = self.vin.to_alipay_dict()
            else:
                params['vin'] = self.vin
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdNfcdkPartsModifyModel()
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'tag_id' in d:
            o.tag_id = d['tag_id']
        if 'tag_sn' in d:
            o.tag_sn = d['tag_sn']
        if 'tuid' in d:
            o.tuid = d['tuid']
        if 'vin' in d:
            o.vin = d['vin']
        return o


