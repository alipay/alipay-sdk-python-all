#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCustomerJobworthQuickhireSyncModel(object):

    def __init__(self):
        self._recruit_code_id = None
        self._service_id = None
        self._sync_status = None

    @property
    def recruit_code_id(self):
        return self._recruit_code_id

    @recruit_code_id.setter
    def recruit_code_id(self, value):
        self._recruit_code_id = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
    @property
    def sync_status(self):
        return self._sync_status

    @sync_status.setter
    def sync_status(self, value):
        self._sync_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.recruit_code_id:
            if hasattr(self.recruit_code_id, 'to_alipay_dict'):
                params['recruit_code_id'] = self.recruit_code_id.to_alipay_dict()
            else:
                params['recruit_code_id'] = self.recruit_code_id
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        if self.sync_status:
            if hasattr(self.sync_status, 'to_alipay_dict'):
                params['sync_status'] = self.sync_status.to_alipay_dict()
            else:
                params['sync_status'] = self.sync_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCustomerJobworthQuickhireSyncModel()
        if 'recruit_code_id' in d:
            o.recruit_code_id = d['recruit_code_id']
        if 'service_id' in d:
            o.service_id = d['service_id']
        if 'sync_status' in d:
            o.sync_status = d['sync_status']
        return o


