#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IpRoleInfoDTO(object):

    def __init__(self):
        self._gmt_create = None
        self._ip_role_id = None
        self._job = None
        self._phone = None
        self._real_name = None
        self._reg_from = None
        self._remark = None
        self._work_no = None

    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        self._job = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def real_name(self):
        return self._real_name

    @real_name.setter
    def real_name(self, value):
        self._real_name = value
    @property
    def reg_from(self):
        return self._reg_from

    @reg_from.setter
    def reg_from(self, value):
        self._reg_from = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def work_no(self):
        return self._work_no

    @work_no.setter
    def work_no(self, value):
        self._work_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.job:
            if hasattr(self.job, 'to_alipay_dict'):
                params['job'] = self.job.to_alipay_dict()
            else:
                params['job'] = self.job
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.real_name:
            if hasattr(self.real_name, 'to_alipay_dict'):
                params['real_name'] = self.real_name.to_alipay_dict()
            else:
                params['real_name'] = self.real_name
        if self.reg_from:
            if hasattr(self.reg_from, 'to_alipay_dict'):
                params['reg_from'] = self.reg_from.to_alipay_dict()
            else:
                params['reg_from'] = self.reg_from
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.work_no:
            if hasattr(self.work_no, 'to_alipay_dict'):
                params['work_no'] = self.work_no.to_alipay_dict()
            else:
                params['work_no'] = self.work_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IpRoleInfoDTO()
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'job' in d:
            o.job = d['job']
        if 'phone' in d:
            o.phone = d['phone']
        if 'real_name' in d:
            o.real_name = d['real_name']
        if 'reg_from' in d:
            o.reg_from = d['reg_from']
        if 'remark' in d:
            o.remark = d['remark']
        if 'work_no' in d:
            o.work_no = d['work_no']
        return o


