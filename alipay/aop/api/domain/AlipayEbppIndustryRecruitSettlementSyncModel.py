#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryRecruitSettlementSyncModel(object):

    def __init__(self):
        self._attendance_time = None
        self._client_settlement_url = None
        self._job_salary = None
        self._job_salary_type = None
        self._out_apply_id = None
        self._out_attendance_ids = None
        self._out_job_id = None
        self._out_settlement_id = None
        self._out_user_id = None
        self._real_attendance_time = None
        self._real_settle_amount = None
        self._server_settlement_url = None
        self._settle_amount = None
        self._settle_status = None
        self._source = None

    @property
    def attendance_time(self):
        return self._attendance_time

    @attendance_time.setter
    def attendance_time(self, value):
        self._attendance_time = value
    @property
    def client_settlement_url(self):
        return self._client_settlement_url

    @client_settlement_url.setter
    def client_settlement_url(self, value):
        self._client_settlement_url = value
    @property
    def job_salary(self):
        return self._job_salary

    @job_salary.setter
    def job_salary(self, value):
        self._job_salary = value
    @property
    def job_salary_type(self):
        return self._job_salary_type

    @job_salary_type.setter
    def job_salary_type(self, value):
        self._job_salary_type = value
    @property
    def out_apply_id(self):
        return self._out_apply_id

    @out_apply_id.setter
    def out_apply_id(self, value):
        self._out_apply_id = value
    @property
    def out_attendance_ids(self):
        return self._out_attendance_ids

    @out_attendance_ids.setter
    def out_attendance_ids(self, value):
        if isinstance(value, list):
            self._out_attendance_ids = list()
            for i in value:
                self._out_attendance_ids.append(i)
    @property
    def out_job_id(self):
        return self._out_job_id

    @out_job_id.setter
    def out_job_id(self, value):
        self._out_job_id = value
    @property
    def out_settlement_id(self):
        return self._out_settlement_id

    @out_settlement_id.setter
    def out_settlement_id(self, value):
        self._out_settlement_id = value
    @property
    def out_user_id(self):
        return self._out_user_id

    @out_user_id.setter
    def out_user_id(self, value):
        self._out_user_id = value
    @property
    def real_attendance_time(self):
        return self._real_attendance_time

    @real_attendance_time.setter
    def real_attendance_time(self, value):
        self._real_attendance_time = value
    @property
    def real_settle_amount(self):
        return self._real_settle_amount

    @real_settle_amount.setter
    def real_settle_amount(self, value):
        self._real_settle_amount = value
    @property
    def server_settlement_url(self):
        return self._server_settlement_url

    @server_settlement_url.setter
    def server_settlement_url(self, value):
        self._server_settlement_url = value
    @property
    def settle_amount(self):
        return self._settle_amount

    @settle_amount.setter
    def settle_amount(self, value):
        self._settle_amount = value
    @property
    def settle_status(self):
        return self._settle_status

    @settle_status.setter
    def settle_status(self, value):
        self._settle_status = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.attendance_time:
            if hasattr(self.attendance_time, 'to_alipay_dict'):
                params['attendance_time'] = self.attendance_time.to_alipay_dict()
            else:
                params['attendance_time'] = self.attendance_time
        if self.client_settlement_url:
            if hasattr(self.client_settlement_url, 'to_alipay_dict'):
                params['client_settlement_url'] = self.client_settlement_url.to_alipay_dict()
            else:
                params['client_settlement_url'] = self.client_settlement_url
        if self.job_salary:
            if hasattr(self.job_salary, 'to_alipay_dict'):
                params['job_salary'] = self.job_salary.to_alipay_dict()
            else:
                params['job_salary'] = self.job_salary
        if self.job_salary_type:
            if hasattr(self.job_salary_type, 'to_alipay_dict'):
                params['job_salary_type'] = self.job_salary_type.to_alipay_dict()
            else:
                params['job_salary_type'] = self.job_salary_type
        if self.out_apply_id:
            if hasattr(self.out_apply_id, 'to_alipay_dict'):
                params['out_apply_id'] = self.out_apply_id.to_alipay_dict()
            else:
                params['out_apply_id'] = self.out_apply_id
        if self.out_attendance_ids:
            if isinstance(self.out_attendance_ids, list):
                for i in range(0, len(self.out_attendance_ids)):
                    element = self.out_attendance_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.out_attendance_ids[i] = element.to_alipay_dict()
            if hasattr(self.out_attendance_ids, 'to_alipay_dict'):
                params['out_attendance_ids'] = self.out_attendance_ids.to_alipay_dict()
            else:
                params['out_attendance_ids'] = self.out_attendance_ids
        if self.out_job_id:
            if hasattr(self.out_job_id, 'to_alipay_dict'):
                params['out_job_id'] = self.out_job_id.to_alipay_dict()
            else:
                params['out_job_id'] = self.out_job_id
        if self.out_settlement_id:
            if hasattr(self.out_settlement_id, 'to_alipay_dict'):
                params['out_settlement_id'] = self.out_settlement_id.to_alipay_dict()
            else:
                params['out_settlement_id'] = self.out_settlement_id
        if self.out_user_id:
            if hasattr(self.out_user_id, 'to_alipay_dict'):
                params['out_user_id'] = self.out_user_id.to_alipay_dict()
            else:
                params['out_user_id'] = self.out_user_id
        if self.real_attendance_time:
            if hasattr(self.real_attendance_time, 'to_alipay_dict'):
                params['real_attendance_time'] = self.real_attendance_time.to_alipay_dict()
            else:
                params['real_attendance_time'] = self.real_attendance_time
        if self.real_settle_amount:
            if hasattr(self.real_settle_amount, 'to_alipay_dict'):
                params['real_settle_amount'] = self.real_settle_amount.to_alipay_dict()
            else:
                params['real_settle_amount'] = self.real_settle_amount
        if self.server_settlement_url:
            if hasattr(self.server_settlement_url, 'to_alipay_dict'):
                params['server_settlement_url'] = self.server_settlement_url.to_alipay_dict()
            else:
                params['server_settlement_url'] = self.server_settlement_url
        if self.settle_amount:
            if hasattr(self.settle_amount, 'to_alipay_dict'):
                params['settle_amount'] = self.settle_amount.to_alipay_dict()
            else:
                params['settle_amount'] = self.settle_amount
        if self.settle_status:
            if hasattr(self.settle_status, 'to_alipay_dict'):
                params['settle_status'] = self.settle_status.to_alipay_dict()
            else:
                params['settle_status'] = self.settle_status
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryRecruitSettlementSyncModel()
        if 'attendance_time' in d:
            o.attendance_time = d['attendance_time']
        if 'client_settlement_url' in d:
            o.client_settlement_url = d['client_settlement_url']
        if 'job_salary' in d:
            o.job_salary = d['job_salary']
        if 'job_salary_type' in d:
            o.job_salary_type = d['job_salary_type']
        if 'out_apply_id' in d:
            o.out_apply_id = d['out_apply_id']
        if 'out_attendance_ids' in d:
            o.out_attendance_ids = d['out_attendance_ids']
        if 'out_job_id' in d:
            o.out_job_id = d['out_job_id']
        if 'out_settlement_id' in d:
            o.out_settlement_id = d['out_settlement_id']
        if 'out_user_id' in d:
            o.out_user_id = d['out_user_id']
        if 'real_attendance_time' in d:
            o.real_attendance_time = d['real_attendance_time']
        if 'real_settle_amount' in d:
            o.real_settle_amount = d['real_settle_amount']
        if 'server_settlement_url' in d:
            o.server_settlement_url = d['server_settlement_url']
        if 'settle_amount' in d:
            o.settle_amount = d['settle_amount']
        if 'settle_status' in d:
            o.settle_status = d['settle_status']
        if 'source' in d:
            o.source = d['source']
        return o


