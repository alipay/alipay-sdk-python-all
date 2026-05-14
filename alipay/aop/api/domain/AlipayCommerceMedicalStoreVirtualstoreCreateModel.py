#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalStoreVirtualstoreCreateModel(object):

    def __init__(self):
        self._channel = None
        self._hdf_space_code = None
        self._hdf_space_leader_code = None
        self._hdf_space_user_name = None
        self._hdf_subject_code = None
        self._hdf_subject_name = None
        self._hdf_subject_type = None
        self._seller_id = None
        self._status = None
        self._store_code = None
        self._store_name = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def hdf_space_code(self):
        return self._hdf_space_code

    @hdf_space_code.setter
    def hdf_space_code(self, value):
        self._hdf_space_code = value
    @property
    def hdf_space_leader_code(self):
        return self._hdf_space_leader_code

    @hdf_space_leader_code.setter
    def hdf_space_leader_code(self, value):
        self._hdf_space_leader_code = value
    @property
    def hdf_space_user_name(self):
        return self._hdf_space_user_name

    @hdf_space_user_name.setter
    def hdf_space_user_name(self, value):
        self._hdf_space_user_name = value
    @property
    def hdf_subject_code(self):
        return self._hdf_subject_code

    @hdf_subject_code.setter
    def hdf_subject_code(self, value):
        self._hdf_subject_code = value
    @property
    def hdf_subject_name(self):
        return self._hdf_subject_name

    @hdf_subject_name.setter
    def hdf_subject_name(self, value):
        self._hdf_subject_name = value
    @property
    def hdf_subject_type(self):
        return self._hdf_subject_type

    @hdf_subject_type.setter
    def hdf_subject_type(self, value):
        self._hdf_subject_type = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def store_code(self):
        return self._store_code

    @store_code.setter
    def store_code(self, value):
        self._store_code = value
    @property
    def store_name(self):
        return self._store_name

    @store_name.setter
    def store_name(self, value):
        self._store_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.hdf_space_code:
            if hasattr(self.hdf_space_code, 'to_alipay_dict'):
                params['hdf_space_code'] = self.hdf_space_code.to_alipay_dict()
            else:
                params['hdf_space_code'] = self.hdf_space_code
        if self.hdf_space_leader_code:
            if hasattr(self.hdf_space_leader_code, 'to_alipay_dict'):
                params['hdf_space_leader_code'] = self.hdf_space_leader_code.to_alipay_dict()
            else:
                params['hdf_space_leader_code'] = self.hdf_space_leader_code
        if self.hdf_space_user_name:
            if hasattr(self.hdf_space_user_name, 'to_alipay_dict'):
                params['hdf_space_user_name'] = self.hdf_space_user_name.to_alipay_dict()
            else:
                params['hdf_space_user_name'] = self.hdf_space_user_name
        if self.hdf_subject_code:
            if hasattr(self.hdf_subject_code, 'to_alipay_dict'):
                params['hdf_subject_code'] = self.hdf_subject_code.to_alipay_dict()
            else:
                params['hdf_subject_code'] = self.hdf_subject_code
        if self.hdf_subject_name:
            if hasattr(self.hdf_subject_name, 'to_alipay_dict'):
                params['hdf_subject_name'] = self.hdf_subject_name.to_alipay_dict()
            else:
                params['hdf_subject_name'] = self.hdf_subject_name
        if self.hdf_subject_type:
            if hasattr(self.hdf_subject_type, 'to_alipay_dict'):
                params['hdf_subject_type'] = self.hdf_subject_type.to_alipay_dict()
            else:
                params['hdf_subject_type'] = self.hdf_subject_type
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.store_code:
            if hasattr(self.store_code, 'to_alipay_dict'):
                params['store_code'] = self.store_code.to_alipay_dict()
            else:
                params['store_code'] = self.store_code
        if self.store_name:
            if hasattr(self.store_name, 'to_alipay_dict'):
                params['store_name'] = self.store_name.to_alipay_dict()
            else:
                params['store_name'] = self.store_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalStoreVirtualstoreCreateModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'hdf_space_code' in d:
            o.hdf_space_code = d['hdf_space_code']
        if 'hdf_space_leader_code' in d:
            o.hdf_space_leader_code = d['hdf_space_leader_code']
        if 'hdf_space_user_name' in d:
            o.hdf_space_user_name = d['hdf_space_user_name']
        if 'hdf_subject_code' in d:
            o.hdf_subject_code = d['hdf_subject_code']
        if 'hdf_subject_name' in d:
            o.hdf_subject_name = d['hdf_subject_name']
        if 'hdf_subject_type' in d:
            o.hdf_subject_type = d['hdf_subject_type']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'status' in d:
            o.status = d['status']
        if 'store_code' in d:
            o.store_code = d['store_code']
        if 'store_name' in d:
            o.store_name = d['store_name']
        return o


