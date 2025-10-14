#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryOfflinelaborRegisterQueryModel(object):

    def __init__(self):
        self._application_status = None
        self._job_id = None
        self._job_name = None
        self._out_regist_id = None
        self._out_regist_no = None
        self._out_register_id = None
        self._out_register_no = None
        self._page_num = None
        self._page_size = None
        self._project_id = None
        self._project_name = None
        self._reg_end_date = None
        self._reg_start_date = None
        self._user_name = None
        self._user_phone_number = None

    @property
    def application_status(self):
        return self._application_status

    @application_status.setter
    def application_status(self, value):
        self._application_status = value
    @property
    def job_id(self):
        return self._job_id

    @job_id.setter
    def job_id(self, value):
        self._job_id = value
    @property
    def job_name(self):
        return self._job_name

    @job_name.setter
    def job_name(self, value):
        self._job_name = value
    @property
    def out_regist_id(self):
        return self._out_regist_id

    @out_regist_id.setter
    def out_regist_id(self, value):
        self._out_regist_id = value
    @property
    def out_regist_no(self):
        return self._out_regist_no

    @out_regist_no.setter
    def out_regist_no(self, value):
        self._out_regist_no = value
    @property
    def out_register_id(self):
        return self._out_register_id

    @out_register_id.setter
    def out_register_id(self, value):
        self._out_register_id = value
    @property
    def out_register_no(self):
        return self._out_register_no

    @out_register_no.setter
    def out_register_no(self, value):
        self._out_register_no = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def project_name(self):
        return self._project_name

    @project_name.setter
    def project_name(self, value):
        self._project_name = value
    @property
    def reg_end_date(self):
        return self._reg_end_date

    @reg_end_date.setter
    def reg_end_date(self, value):
        self._reg_end_date = value
    @property
    def reg_start_date(self):
        return self._reg_start_date

    @reg_start_date.setter
    def reg_start_date(self, value):
        self._reg_start_date = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value
    @property
    def user_phone_number(self):
        return self._user_phone_number

    @user_phone_number.setter
    def user_phone_number(self, value):
        self._user_phone_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.application_status:
            if hasattr(self.application_status, 'to_alipay_dict'):
                params['application_status'] = self.application_status.to_alipay_dict()
            else:
                params['application_status'] = self.application_status
        if self.job_id:
            if hasattr(self.job_id, 'to_alipay_dict'):
                params['job_id'] = self.job_id.to_alipay_dict()
            else:
                params['job_id'] = self.job_id
        if self.job_name:
            if hasattr(self.job_name, 'to_alipay_dict'):
                params['job_name'] = self.job_name.to_alipay_dict()
            else:
                params['job_name'] = self.job_name
        if self.out_regist_id:
            if hasattr(self.out_regist_id, 'to_alipay_dict'):
                params['out_regist_id'] = self.out_regist_id.to_alipay_dict()
            else:
                params['out_regist_id'] = self.out_regist_id
        if self.out_regist_no:
            if hasattr(self.out_regist_no, 'to_alipay_dict'):
                params['out_regist_no'] = self.out_regist_no.to_alipay_dict()
            else:
                params['out_regist_no'] = self.out_regist_no
        if self.out_register_id:
            if hasattr(self.out_register_id, 'to_alipay_dict'):
                params['out_register_id'] = self.out_register_id.to_alipay_dict()
            else:
                params['out_register_id'] = self.out_register_id
        if self.out_register_no:
            if hasattr(self.out_register_no, 'to_alipay_dict'):
                params['out_register_no'] = self.out_register_no.to_alipay_dict()
            else:
                params['out_register_no'] = self.out_register_no
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        if self.project_name:
            if hasattr(self.project_name, 'to_alipay_dict'):
                params['project_name'] = self.project_name.to_alipay_dict()
            else:
                params['project_name'] = self.project_name
        if self.reg_end_date:
            if hasattr(self.reg_end_date, 'to_alipay_dict'):
                params['reg_end_date'] = self.reg_end_date.to_alipay_dict()
            else:
                params['reg_end_date'] = self.reg_end_date
        if self.reg_start_date:
            if hasattr(self.reg_start_date, 'to_alipay_dict'):
                params['reg_start_date'] = self.reg_start_date.to_alipay_dict()
            else:
                params['reg_start_date'] = self.reg_start_date
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        if self.user_phone_number:
            if hasattr(self.user_phone_number, 'to_alipay_dict'):
                params['user_phone_number'] = self.user_phone_number.to_alipay_dict()
            else:
                params['user_phone_number'] = self.user_phone_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryOfflinelaborRegisterQueryModel()
        if 'application_status' in d:
            o.application_status = d['application_status']
        if 'job_id' in d:
            o.job_id = d['job_id']
        if 'job_name' in d:
            o.job_name = d['job_name']
        if 'out_regist_id' in d:
            o.out_regist_id = d['out_regist_id']
        if 'out_regist_no' in d:
            o.out_regist_no = d['out_regist_no']
        if 'out_register_id' in d:
            o.out_register_id = d['out_register_id']
        if 'out_register_no' in d:
            o.out_register_no = d['out_register_no']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'project_name' in d:
            o.project_name = d['project_name']
        if 'reg_end_date' in d:
            o.reg_end_date = d['reg_end_date']
        if 'reg_start_date' in d:
            o.reg_start_date = d['reg_start_date']
        if 'user_name' in d:
            o.user_name = d['user_name']
        if 'user_phone_number' in d:
            o.user_phone_number = d['user_phone_number']
        return o


