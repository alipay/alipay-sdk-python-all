#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TestDemoWzw(object):

    def __init__(self):
        self._aaopen_id = None
        self._aauids = None
        self._id_type = None
        self._oid_open_id = None
        self._uid = None

    @property
    def aaopen_id(self):
        return self._aaopen_id

    @aaopen_id.setter
    def aaopen_id(self, value):
        self._aaopen_id = value
    @property
    def aauids(self):
        return self._aauids

    @aauids.setter
    def aauids(self, value):
        self._aauids = value
    @property
    def id_type(self):
        return self._id_type

    @id_type.setter
    def id_type(self, value):
        self._id_type = value
    @property
    def oid_open_id(self):
        return self._oid_open_id

    @oid_open_id.setter
    def oid_open_id(self, value):
        self._oid_open_id = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.aaopen_id:
            if hasattr(self.aaopen_id, 'to_alipay_dict'):
                params['aaopen_id'] = self.aaopen_id.to_alipay_dict()
            else:
                params['aaopen_id'] = self.aaopen_id
        if self.aauids:
            if hasattr(self.aauids, 'to_alipay_dict'):
                params['aauids'] = self.aauids.to_alipay_dict()
            else:
                params['aauids'] = self.aauids
        if self.id_type:
            if hasattr(self.id_type, 'to_alipay_dict'):
                params['id_type'] = self.id_type.to_alipay_dict()
            else:
                params['id_type'] = self.id_type
        if self.oid_open_id:
            if hasattr(self.oid_open_id, 'to_alipay_dict'):
                params['oid_open_id'] = self.oid_open_id.to_alipay_dict()
            else:
                params['oid_open_id'] = self.oid_open_id
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TestDemoWzw()
        if 'aaopen_id' in d:
            o.aaopen_id = d['aaopen_id']
        if 'aauids' in d:
            o.aauids = d['aauids']
        if 'id_type' in d:
            o.id_type = d['id_type']
        if 'oid_open_id' in d:
            o.oid_open_id = d['oid_open_id']
        if 'uid' in d:
            o.uid = d['uid']
        return o


