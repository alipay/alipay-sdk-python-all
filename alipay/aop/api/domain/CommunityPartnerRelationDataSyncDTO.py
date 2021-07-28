#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CommunityPartnerRelationDataSyncDTO(object):

    def __init__(self):
        self._rela_data = None
        self._rela_expire = None
        self._rela_status = None
        self._target_id = None

    @property
    def rela_data(self):
        return self._rela_data

    @rela_data.setter
    def rela_data(self, value):
        self._rela_data = value
    @property
    def rela_expire(self):
        return self._rela_expire

    @rela_expire.setter
    def rela_expire(self, value):
        self._rela_expire = value
    @property
    def rela_status(self):
        return self._rela_status

    @rela_status.setter
    def rela_status(self, value):
        self._rela_status = value
    @property
    def target_id(self):
        return self._target_id

    @target_id.setter
    def target_id(self, value):
        self._target_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.rela_data:
            if hasattr(self.rela_data, 'to_alipay_dict'):
                params['rela_data'] = self.rela_data.to_alipay_dict()
            else:
                params['rela_data'] = self.rela_data
        if self.rela_expire:
            if hasattr(self.rela_expire, 'to_alipay_dict'):
                params['rela_expire'] = self.rela_expire.to_alipay_dict()
            else:
                params['rela_expire'] = self.rela_expire
        if self.rela_status:
            if hasattr(self.rela_status, 'to_alipay_dict'):
                params['rela_status'] = self.rela_status.to_alipay_dict()
            else:
                params['rela_status'] = self.rela_status
        if self.target_id:
            if hasattr(self.target_id, 'to_alipay_dict'):
                params['target_id'] = self.target_id.to_alipay_dict()
            else:
                params['target_id'] = self.target_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CommunityPartnerRelationDataSyncDTO()
        if 'rela_data' in d:
            o.rela_data = d['rela_data']
        if 'rela_expire' in d:
            o.rela_expire = d['rela_expire']
        if 'rela_status' in d:
            o.rela_status = d['rela_status']
        if 'target_id' in d:
            o.target_id = d['target_id']
        return o


