#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BsEnrollParticipantAddress import BsEnrollParticipantAddress


class BsEnrollParticipantResultDetail(object):

    def __init__(self):
        self._digital_poi_id = None
        self._digital_poi_name = None
        self._store_address = None

    @property
    def digital_poi_id(self):
        return self._digital_poi_id

    @digital_poi_id.setter
    def digital_poi_id(self, value):
        self._digital_poi_id = value
    @property
    def digital_poi_name(self):
        return self._digital_poi_name

    @digital_poi_name.setter
    def digital_poi_name(self, value):
        self._digital_poi_name = value
    @property
    def store_address(self):
        return self._store_address

    @store_address.setter
    def store_address(self, value):
        if isinstance(value, BsEnrollParticipantAddress):
            self._store_address = value
        else:
            self._store_address = BsEnrollParticipantAddress.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.digital_poi_id:
            if hasattr(self.digital_poi_id, 'to_alipay_dict'):
                params['digital_poi_id'] = self.digital_poi_id.to_alipay_dict()
            else:
                params['digital_poi_id'] = self.digital_poi_id
        if self.digital_poi_name:
            if hasattr(self.digital_poi_name, 'to_alipay_dict'):
                params['digital_poi_name'] = self.digital_poi_name.to_alipay_dict()
            else:
                params['digital_poi_name'] = self.digital_poi_name
        if self.store_address:
            if hasattr(self.store_address, 'to_alipay_dict'):
                params['store_address'] = self.store_address.to_alipay_dict()
            else:
                params['store_address'] = self.store_address
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BsEnrollParticipantResultDetail()
        if 'digital_poi_id' in d:
            o.digital_poi_id = d['digital_poi_id']
        if 'digital_poi_name' in d:
            o.digital_poi_name = d['digital_poi_name']
        if 'store_address' in d:
            o.store_address = d['store_address']
        return o


