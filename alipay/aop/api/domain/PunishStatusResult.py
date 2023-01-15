#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PunishStatusResult(object):

    def __init__(self):
        self._demand_code = None
        self._entity_id = None
        self._pc_relieve_url = None
        self._relieve_url = None
        self._status = None

    @property
    def demand_code(self):
        return self._demand_code

    @demand_code.setter
    def demand_code(self, value):
        self._demand_code = value
    @property
    def entity_id(self):
        return self._entity_id

    @entity_id.setter
    def entity_id(self, value):
        self._entity_id = value
    @property
    def pc_relieve_url(self):
        return self._pc_relieve_url

    @pc_relieve_url.setter
    def pc_relieve_url(self, value):
        self._pc_relieve_url = value
    @property
    def relieve_url(self):
        return self._relieve_url

    @relieve_url.setter
    def relieve_url(self, value):
        self._relieve_url = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.demand_code:
            if hasattr(self.demand_code, 'to_alipay_dict'):
                params['demand_code'] = self.demand_code.to_alipay_dict()
            else:
                params['demand_code'] = self.demand_code
        if self.entity_id:
            if hasattr(self.entity_id, 'to_alipay_dict'):
                params['entity_id'] = self.entity_id.to_alipay_dict()
            else:
                params['entity_id'] = self.entity_id
        if self.pc_relieve_url:
            if hasattr(self.pc_relieve_url, 'to_alipay_dict'):
                params['pc_relieve_url'] = self.pc_relieve_url.to_alipay_dict()
            else:
                params['pc_relieve_url'] = self.pc_relieve_url
        if self.relieve_url:
            if hasattr(self.relieve_url, 'to_alipay_dict'):
                params['relieve_url'] = self.relieve_url.to_alipay_dict()
            else:
                params['relieve_url'] = self.relieve_url
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PunishStatusResult()
        if 'demand_code' in d:
            o.demand_code = d['demand_code']
        if 'entity_id' in d:
            o.entity_id = d['entity_id']
        if 'pc_relieve_url' in d:
            o.pc_relieve_url = d['pc_relieve_url']
        if 'relieve_url' in d:
            o.relieve_url = d['relieve_url']
        if 'status' in d:
            o.status = d['status']
        return o


