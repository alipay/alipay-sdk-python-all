#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ScenicAuditInfo(object):

    def __init__(self):
        self._audit_msg = None
        self._audit_status = None
        self._import_gmt_create = None
        self._outer_id_isv = None
        self._outer_id_zfb = None
        self._scenic_app_id = None
        self._scenic_id = None

    @property
    def audit_msg(self):
        return self._audit_msg

    @audit_msg.setter
    def audit_msg(self, value):
        self._audit_msg = value
    @property
    def audit_status(self):
        return self._audit_status

    @audit_status.setter
    def audit_status(self, value):
        self._audit_status = value
    @property
    def import_gmt_create(self):
        return self._import_gmt_create

    @import_gmt_create.setter
    def import_gmt_create(self, value):
        self._import_gmt_create = value
    @property
    def outer_id_isv(self):
        return self._outer_id_isv

    @outer_id_isv.setter
    def outer_id_isv(self, value):
        self._outer_id_isv = value
    @property
    def outer_id_zfb(self):
        return self._outer_id_zfb

    @outer_id_zfb.setter
    def outer_id_zfb(self, value):
        self._outer_id_zfb = value
    @property
    def scenic_app_id(self):
        return self._scenic_app_id

    @scenic_app_id.setter
    def scenic_app_id(self, value):
        self._scenic_app_id = value
    @property
    def scenic_id(self):
        return self._scenic_id

    @scenic_id.setter
    def scenic_id(self, value):
        self._scenic_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.audit_msg:
            if hasattr(self.audit_msg, 'to_alipay_dict'):
                params['audit_msg'] = self.audit_msg.to_alipay_dict()
            else:
                params['audit_msg'] = self.audit_msg
        if self.audit_status:
            if hasattr(self.audit_status, 'to_alipay_dict'):
                params['audit_status'] = self.audit_status.to_alipay_dict()
            else:
                params['audit_status'] = self.audit_status
        if self.import_gmt_create:
            if hasattr(self.import_gmt_create, 'to_alipay_dict'):
                params['import_gmt_create'] = self.import_gmt_create.to_alipay_dict()
            else:
                params['import_gmt_create'] = self.import_gmt_create
        if self.outer_id_isv:
            if hasattr(self.outer_id_isv, 'to_alipay_dict'):
                params['outer_id_isv'] = self.outer_id_isv.to_alipay_dict()
            else:
                params['outer_id_isv'] = self.outer_id_isv
        if self.outer_id_zfb:
            if hasattr(self.outer_id_zfb, 'to_alipay_dict'):
                params['outer_id_zfb'] = self.outer_id_zfb.to_alipay_dict()
            else:
                params['outer_id_zfb'] = self.outer_id_zfb
        if self.scenic_app_id:
            if hasattr(self.scenic_app_id, 'to_alipay_dict'):
                params['scenic_app_id'] = self.scenic_app_id.to_alipay_dict()
            else:
                params['scenic_app_id'] = self.scenic_app_id
        if self.scenic_id:
            if hasattr(self.scenic_id, 'to_alipay_dict'):
                params['scenic_id'] = self.scenic_id.to_alipay_dict()
            else:
                params['scenic_id'] = self.scenic_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ScenicAuditInfo()
        if 'audit_msg' in d:
            o.audit_msg = d['audit_msg']
        if 'audit_status' in d:
            o.audit_status = d['audit_status']
        if 'import_gmt_create' in d:
            o.import_gmt_create = d['import_gmt_create']
        if 'outer_id_isv' in d:
            o.outer_id_isv = d['outer_id_isv']
        if 'outer_id_zfb' in d:
            o.outer_id_zfb = d['outer_id_zfb']
        if 'scenic_app_id' in d:
            o.scenic_app_id = d['scenic_app_id']
        if 'scenic_id' in d:
            o.scenic_id = d['scenic_id']
        return o


