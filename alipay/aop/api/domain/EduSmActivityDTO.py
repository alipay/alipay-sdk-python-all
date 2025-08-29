#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EduSmActivityDTO(object):

    def __init__(self):
        self._activity_code = None
        self._audit_date = None
        self._audit_memo = None
        self._biz_code = None
        self._biz_id = None
        self._gmt_create = None
        self._isv_pid = None
        self._sm_cn_name = None
        self._sm_id = None
        self._sm_level = None
        self._sm_mcc = None
        self._sm_mcc_name = None
        self._sm_new_mcc = None
        self._sm_new_mcc_name = None
        self._status = None

    @property
    def activity_code(self):
        return self._activity_code

    @activity_code.setter
    def activity_code(self, value):
        self._activity_code = value
    @property
    def audit_date(self):
        return self._audit_date

    @audit_date.setter
    def audit_date(self, value):
        self._audit_date = value
    @property
    def audit_memo(self):
        return self._audit_memo

    @audit_memo.setter
    def audit_memo(self, value):
        self._audit_memo = value
    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def sm_cn_name(self):
        return self._sm_cn_name

    @sm_cn_name.setter
    def sm_cn_name(self, value):
        self._sm_cn_name = value
    @property
    def sm_id(self):
        return self._sm_id

    @sm_id.setter
    def sm_id(self, value):
        self._sm_id = value
    @property
    def sm_level(self):
        return self._sm_level

    @sm_level.setter
    def sm_level(self, value):
        self._sm_level = value
    @property
    def sm_mcc(self):
        return self._sm_mcc

    @sm_mcc.setter
    def sm_mcc(self, value):
        self._sm_mcc = value
    @property
    def sm_mcc_name(self):
        return self._sm_mcc_name

    @sm_mcc_name.setter
    def sm_mcc_name(self, value):
        self._sm_mcc_name = value
    @property
    def sm_new_mcc(self):
        return self._sm_new_mcc

    @sm_new_mcc.setter
    def sm_new_mcc(self, value):
        self._sm_new_mcc = value
    @property
    def sm_new_mcc_name(self):
        return self._sm_new_mcc_name

    @sm_new_mcc_name.setter
    def sm_new_mcc_name(self, value):
        self._sm_new_mcc_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_code:
            if hasattr(self.activity_code, 'to_alipay_dict'):
                params['activity_code'] = self.activity_code.to_alipay_dict()
            else:
                params['activity_code'] = self.activity_code
        if self.audit_date:
            if hasattr(self.audit_date, 'to_alipay_dict'):
                params['audit_date'] = self.audit_date.to_alipay_dict()
            else:
                params['audit_date'] = self.audit_date
        if self.audit_memo:
            if hasattr(self.audit_memo, 'to_alipay_dict'):
                params['audit_memo'] = self.audit_memo.to_alipay_dict()
            else:
                params['audit_memo'] = self.audit_memo
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.sm_cn_name:
            if hasattr(self.sm_cn_name, 'to_alipay_dict'):
                params['sm_cn_name'] = self.sm_cn_name.to_alipay_dict()
            else:
                params['sm_cn_name'] = self.sm_cn_name
        if self.sm_id:
            if hasattr(self.sm_id, 'to_alipay_dict'):
                params['sm_id'] = self.sm_id.to_alipay_dict()
            else:
                params['sm_id'] = self.sm_id
        if self.sm_level:
            if hasattr(self.sm_level, 'to_alipay_dict'):
                params['sm_level'] = self.sm_level.to_alipay_dict()
            else:
                params['sm_level'] = self.sm_level
        if self.sm_mcc:
            if hasattr(self.sm_mcc, 'to_alipay_dict'):
                params['sm_mcc'] = self.sm_mcc.to_alipay_dict()
            else:
                params['sm_mcc'] = self.sm_mcc
        if self.sm_mcc_name:
            if hasattr(self.sm_mcc_name, 'to_alipay_dict'):
                params['sm_mcc_name'] = self.sm_mcc_name.to_alipay_dict()
            else:
                params['sm_mcc_name'] = self.sm_mcc_name
        if self.sm_new_mcc:
            if hasattr(self.sm_new_mcc, 'to_alipay_dict'):
                params['sm_new_mcc'] = self.sm_new_mcc.to_alipay_dict()
            else:
                params['sm_new_mcc'] = self.sm_new_mcc
        if self.sm_new_mcc_name:
            if hasattr(self.sm_new_mcc_name, 'to_alipay_dict'):
                params['sm_new_mcc_name'] = self.sm_new_mcc_name.to_alipay_dict()
            else:
                params['sm_new_mcc_name'] = self.sm_new_mcc_name
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
        o = EduSmActivityDTO()
        if 'activity_code' in d:
            o.activity_code = d['activity_code']
        if 'audit_date' in d:
            o.audit_date = d['audit_date']
        if 'audit_memo' in d:
            o.audit_memo = d['audit_memo']
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'sm_cn_name' in d:
            o.sm_cn_name = d['sm_cn_name']
        if 'sm_id' in d:
            o.sm_id = d['sm_id']
        if 'sm_level' in d:
            o.sm_level = d['sm_level']
        if 'sm_mcc' in d:
            o.sm_mcc = d['sm_mcc']
        if 'sm_mcc_name' in d:
            o.sm_mcc_name = d['sm_mcc_name']
        if 'sm_new_mcc' in d:
            o.sm_new_mcc = d['sm_new_mcc']
        if 'sm_new_mcc_name' in d:
            o.sm_new_mcc_name = d['sm_new_mcc_name']
        if 'status' in d:
            o.status = d['status']
        return o


