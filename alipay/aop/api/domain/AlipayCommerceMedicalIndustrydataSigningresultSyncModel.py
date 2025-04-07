#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalIndustrydataSigningresultSyncModel(object):

    def __init__(self):
        self._hospital_code = None
        self._id = None
        self._rejection_reason = None
        self._seller_id = None
        self._status = None
        self._store_id = None

    @property
    def hospital_code(self):
        return self._hospital_code

    @hospital_code.setter
    def hospital_code(self, value):
        self._hospital_code = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def rejection_reason(self):
        return self._rejection_reason

    @rejection_reason.setter
    def rejection_reason(self, value):
        self._rejection_reason = value
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
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.hospital_code:
            if hasattr(self.hospital_code, 'to_alipay_dict'):
                params['hospital_code'] = self.hospital_code.to_alipay_dict()
            else:
                params['hospital_code'] = self.hospital_code
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.rejection_reason:
            if hasattr(self.rejection_reason, 'to_alipay_dict'):
                params['rejection_reason'] = self.rejection_reason.to_alipay_dict()
            else:
                params['rejection_reason'] = self.rejection_reason
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
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalIndustrydataSigningresultSyncModel()
        if 'hospital_code' in d:
            o.hospital_code = d['hospital_code']
        if 'id' in d:
            o.id = d['id']
        if 'rejection_reason' in d:
            o.rejection_reason = d['rejection_reason']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'status' in d:
            o.status = d['status']
        if 'store_id' in d:
            o.store_id = d['store_id']
        return o


