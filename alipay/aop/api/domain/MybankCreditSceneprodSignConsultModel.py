#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditSceneprodSignConsultModel(object):

    def __init__(self):
        self._app_seq_no = None
        self._data_info = None
        self._sign_stage = None
        self._site = None
        self._site_user_id = None

    @property
    def app_seq_no(self):
        return self._app_seq_no

    @app_seq_no.setter
    def app_seq_no(self, value):
        self._app_seq_no = value
    @property
    def data_info(self):
        return self._data_info

    @data_info.setter
    def data_info(self, value):
        self._data_info = value
    @property
    def sign_stage(self):
        return self._sign_stage

    @sign_stage.setter
    def sign_stage(self, value):
        self._sign_stage = value
    @property
    def site(self):
        return self._site

    @site.setter
    def site(self, value):
        self._site = value
    @property
    def site_user_id(self):
        return self._site_user_id

    @site_user_id.setter
    def site_user_id(self, value):
        self._site_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_seq_no:
            if hasattr(self.app_seq_no, 'to_alipay_dict'):
                params['app_seq_no'] = self.app_seq_no.to_alipay_dict()
            else:
                params['app_seq_no'] = self.app_seq_no
        if self.data_info:
            if hasattr(self.data_info, 'to_alipay_dict'):
                params['data_info'] = self.data_info.to_alipay_dict()
            else:
                params['data_info'] = self.data_info
        if self.sign_stage:
            if hasattr(self.sign_stage, 'to_alipay_dict'):
                params['sign_stage'] = self.sign_stage.to_alipay_dict()
            else:
                params['sign_stage'] = self.sign_stage
        if self.site:
            if hasattr(self.site, 'to_alipay_dict'):
                params['site'] = self.site.to_alipay_dict()
            else:
                params['site'] = self.site
        if self.site_user_id:
            if hasattr(self.site_user_id, 'to_alipay_dict'):
                params['site_user_id'] = self.site_user_id.to_alipay_dict()
            else:
                params['site_user_id'] = self.site_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditSceneprodSignConsultModel()
        if 'app_seq_no' in d:
            o.app_seq_no = d['app_seq_no']
        if 'data_info' in d:
            o.data_info = d['data_info']
        if 'sign_stage' in d:
            o.sign_stage = d['sign_stage']
        if 'site' in d:
            o.site = d['site']
        if 'site_user_id' in d:
            o.site_user_id = d['site_user_id']
        return o


