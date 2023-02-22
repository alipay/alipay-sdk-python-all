#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenOperationOpenbizmockSendModel(object):

    def __init__(self):
        self._id_type = None
        self._open_id = None
        self._uidaa = None

    @property
    def id_type(self):
        return self._id_type

    @id_type.setter
    def id_type(self, value):
        self._id_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def uidaa(self):
        return self._uidaa

    @uidaa.setter
    def uidaa(self, value):
        self._uidaa = value


    def to_alipay_dict(self):
        params = dict()
        if self.id_type:
            if hasattr(self.id_type, 'to_alipay_dict'):
                params['id_type'] = self.id_type.to_alipay_dict()
            else:
                params['id_type'] = self.id_type
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.uidaa:
            if hasattr(self.uidaa, 'to_alipay_dict'):
                params['uidaa'] = self.uidaa.to_alipay_dict()
            else:
                params['uidaa'] = self.uidaa
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenOperationOpenbizmockSendModel()
        if 'id_type' in d:
            o.id_type = d['id_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'uidaa' in d:
            o.uidaa = d['uidaa']
        return o


