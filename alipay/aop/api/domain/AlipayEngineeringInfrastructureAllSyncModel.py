#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEngineeringInfrastructureAllSyncModel(object):

    def __init__(self):
        self._deal_source = None
        self._emp_id = None
        self._id = None
        self._opinion = None
        self._status = None

    @property
    def deal_source(self):
        return self._deal_source

    @deal_source.setter
    def deal_source(self, value):
        self._deal_source = value
    @property
    def emp_id(self):
        return self._emp_id

    @emp_id.setter
    def emp_id(self, value):
        self._emp_id = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def opinion(self):
        return self._opinion

    @opinion.setter
    def opinion(self, value):
        self._opinion = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.deal_source:
            if hasattr(self.deal_source, 'to_alipay_dict'):
                params['deal_source'] = self.deal_source.to_alipay_dict()
            else:
                params['deal_source'] = self.deal_source
        if self.emp_id:
            if hasattr(self.emp_id, 'to_alipay_dict'):
                params['emp_id'] = self.emp_id.to_alipay_dict()
            else:
                params['emp_id'] = self.emp_id
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.opinion:
            if hasattr(self.opinion, 'to_alipay_dict'):
                params['opinion'] = self.opinion.to_alipay_dict()
            else:
                params['opinion'] = self.opinion
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
        o = AlipayEngineeringInfrastructureAllSyncModel()
        if 'deal_source' in d:
            o.deal_source = d['deal_source']
        if 'emp_id' in d:
            o.emp_id = d['emp_id']
        if 'id' in d:
            o.id = d['id']
        if 'opinion' in d:
            o.opinion = d['opinion']
        if 'status' in d:
            o.status = d['status']
        return o


