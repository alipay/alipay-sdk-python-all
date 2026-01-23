#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QualInstanceDTO(object):

    def __init__(self):
        self._gmt_active = None
        self._gmt_apply = None
        self._gmt_expired = None
        self._gmt_use = None
        self._qual_id = None
        self._qual_instance_id = None
        self._status = None

    @property
    def gmt_active(self):
        return self._gmt_active

    @gmt_active.setter
    def gmt_active(self, value):
        self._gmt_active = value
    @property
    def gmt_apply(self):
        return self._gmt_apply

    @gmt_apply.setter
    def gmt_apply(self, value):
        self._gmt_apply = value
    @property
    def gmt_expired(self):
        return self._gmt_expired

    @gmt_expired.setter
    def gmt_expired(self, value):
        self._gmt_expired = value
    @property
    def gmt_use(self):
        return self._gmt_use

    @gmt_use.setter
    def gmt_use(self, value):
        self._gmt_use = value
    @property
    def qual_id(self):
        return self._qual_id

    @qual_id.setter
    def qual_id(self, value):
        self._qual_id = value
    @property
    def qual_instance_id(self):
        return self._qual_instance_id

    @qual_instance_id.setter
    def qual_instance_id(self, value):
        self._qual_instance_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_active:
            if hasattr(self.gmt_active, 'to_alipay_dict'):
                params['gmt_active'] = self.gmt_active.to_alipay_dict()
            else:
                params['gmt_active'] = self.gmt_active
        if self.gmt_apply:
            if hasattr(self.gmt_apply, 'to_alipay_dict'):
                params['gmt_apply'] = self.gmt_apply.to_alipay_dict()
            else:
                params['gmt_apply'] = self.gmt_apply
        if self.gmt_expired:
            if hasattr(self.gmt_expired, 'to_alipay_dict'):
                params['gmt_expired'] = self.gmt_expired.to_alipay_dict()
            else:
                params['gmt_expired'] = self.gmt_expired
        if self.gmt_use:
            if hasattr(self.gmt_use, 'to_alipay_dict'):
                params['gmt_use'] = self.gmt_use.to_alipay_dict()
            else:
                params['gmt_use'] = self.gmt_use
        if self.qual_id:
            if hasattr(self.qual_id, 'to_alipay_dict'):
                params['qual_id'] = self.qual_id.to_alipay_dict()
            else:
                params['qual_id'] = self.qual_id
        if self.qual_instance_id:
            if hasattr(self.qual_instance_id, 'to_alipay_dict'):
                params['qual_instance_id'] = self.qual_instance_id.to_alipay_dict()
            else:
                params['qual_instance_id'] = self.qual_instance_id
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
        o = QualInstanceDTO()
        if 'gmt_active' in d:
            o.gmt_active = d['gmt_active']
        if 'gmt_apply' in d:
            o.gmt_apply = d['gmt_apply']
        if 'gmt_expired' in d:
            o.gmt_expired = d['gmt_expired']
        if 'gmt_use' in d:
            o.gmt_use = d['gmt_use']
        if 'qual_id' in d:
            o.qual_id = d['qual_id']
        if 'qual_instance_id' in d:
            o.qual_instance_id = d['qual_instance_id']
        if 'status' in d:
            o.status = d['status']
        return o


