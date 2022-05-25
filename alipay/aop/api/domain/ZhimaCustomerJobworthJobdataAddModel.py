#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.JobWorthJobdata import JobWorthJobdata


class ZhimaCustomerJobworthJobdataAddModel(object):

    def __init__(self):
        self._cert_no = None
        self._cert_type = None
        self._conn_key = None
        self._job_data_list = None
        self._user_id = None
        self._user_name = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def conn_key(self):
        return self._conn_key

    @conn_key.setter
    def conn_key(self, value):
        self._conn_key = value
    @property
    def job_data_list(self):
        return self._job_data_list

    @job_data_list.setter
    def job_data_list(self, value):
        if isinstance(value, list):
            self._job_data_list = list()
            for i in value:
                if isinstance(i, JobWorthJobdata):
                    self._job_data_list.append(i)
                else:
                    self._job_data_list.append(JobWorthJobdata.from_alipay_dict(i))
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.conn_key:
            if hasattr(self.conn_key, 'to_alipay_dict'):
                params['conn_key'] = self.conn_key.to_alipay_dict()
            else:
                params['conn_key'] = self.conn_key
        if self.job_data_list:
            if isinstance(self.job_data_list, list):
                for i in range(0, len(self.job_data_list)):
                    element = self.job_data_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.job_data_list[i] = element.to_alipay_dict()
            if hasattr(self.job_data_list, 'to_alipay_dict'):
                params['job_data_list'] = self.job_data_list.to_alipay_dict()
            else:
                params['job_data_list'] = self.job_data_list
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCustomerJobworthJobdataAddModel()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'conn_key' in d:
            o.conn_key = d['conn_key']
        if 'job_data_list' in d:
            o.job_data_list = d['job_data_list']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


