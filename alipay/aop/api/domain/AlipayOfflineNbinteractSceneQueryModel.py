#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineNbinteractSceneQueryModel(object):

    def __init__(self):
        self._link_url_type = None
        self._sn = None
        self._supplier_id = None

    @property
    def link_url_type(self):
        return self._link_url_type

    @link_url_type.setter
    def link_url_type(self, value):
        self._link_url_type = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.link_url_type:
            if hasattr(self.link_url_type, 'to_alipay_dict'):
                params['link_url_type'] = self.link_url_type.to_alipay_dict()
            else:
                params['link_url_type'] = self.link_url_type
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        if self.supplier_id:
            if hasattr(self.supplier_id, 'to_alipay_dict'):
                params['supplier_id'] = self.supplier_id.to_alipay_dict()
            else:
                params['supplier_id'] = self.supplier_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineNbinteractSceneQueryModel()
        if 'link_url_type' in d:
            o.link_url_type = d['link_url_type']
        if 'sn' in d:
            o.sn = d['sn']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        return o


