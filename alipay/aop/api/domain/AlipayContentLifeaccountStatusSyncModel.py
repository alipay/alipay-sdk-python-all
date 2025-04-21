#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayContentLifeaccountStatusSyncModel(object):

    def __init__(self):
        self._account_status = None
        self._hdf_id_encrypted = None
        self._public_id = None

    @property
    def account_status(self):
        return self._account_status

    @account_status.setter
    def account_status(self, value):
        self._account_status = value
    @property
    def hdf_id_encrypted(self):
        return self._hdf_id_encrypted

    @hdf_id_encrypted.setter
    def hdf_id_encrypted(self, value):
        self._hdf_id_encrypted = value
    @property
    def public_id(self):
        return self._public_id

    @public_id.setter
    def public_id(self, value):
        self._public_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_status:
            if hasattr(self.account_status, 'to_alipay_dict'):
                params['account_status'] = self.account_status.to_alipay_dict()
            else:
                params['account_status'] = self.account_status
        if self.hdf_id_encrypted:
            if hasattr(self.hdf_id_encrypted, 'to_alipay_dict'):
                params['hdf_id_encrypted'] = self.hdf_id_encrypted.to_alipay_dict()
            else:
                params['hdf_id_encrypted'] = self.hdf_id_encrypted
        if self.public_id:
            if hasattr(self.public_id, 'to_alipay_dict'):
                params['public_id'] = self.public_id.to_alipay_dict()
            else:
                params['public_id'] = self.public_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayContentLifeaccountStatusSyncModel()
        if 'account_status' in d:
            o.account_status = d['account_status']
        if 'hdf_id_encrypted' in d:
            o.hdf_id_encrypted = d['hdf_id_encrypted']
        if 'public_id' in d:
            o.public_id = d['public_id']
        return o


