#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenIotmbsCollectionfaceSyncModel(object):

    def __init__(self):
        self._biztid = None
        self._collection_state = None
        self._face_id = None
        self._out_request_id = None

    @property
    def biztid(self):
        return self._biztid

    @biztid.setter
    def biztid(self, value):
        self._biztid = value
    @property
    def collection_state(self):
        return self._collection_state

    @collection_state.setter
    def collection_state(self, value):
        self._collection_state = value
    @property
    def face_id(self):
        return self._face_id

    @face_id.setter
    def face_id(self, value):
        self._face_id = value
    @property
    def out_request_id(self):
        return self._out_request_id

    @out_request_id.setter
    def out_request_id(self, value):
        self._out_request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biztid:
            if hasattr(self.biztid, 'to_alipay_dict'):
                params['biztid'] = self.biztid.to_alipay_dict()
            else:
                params['biztid'] = self.biztid
        if self.collection_state:
            if hasattr(self.collection_state, 'to_alipay_dict'):
                params['collection_state'] = self.collection_state.to_alipay_dict()
            else:
                params['collection_state'] = self.collection_state
        if self.face_id:
            if hasattr(self.face_id, 'to_alipay_dict'):
                params['face_id'] = self.face_id.to_alipay_dict()
            else:
                params['face_id'] = self.face_id
        if self.out_request_id:
            if hasattr(self.out_request_id, 'to_alipay_dict'):
                params['out_request_id'] = self.out_request_id.to_alipay_dict()
            else:
                params['out_request_id'] = self.out_request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenIotmbsCollectionfaceSyncModel()
        if 'biztid' in d:
            o.biztid = d['biztid']
        if 'collection_state' in d:
            o.collection_state = d['collection_state']
        if 'face_id' in d:
            o.face_id = d['face_id']
        if 'out_request_id' in d:
            o.out_request_id = d['out_request_id']
        return o


