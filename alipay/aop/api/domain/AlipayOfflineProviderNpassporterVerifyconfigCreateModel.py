#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AuthorizationPageConfig import AuthorizationPageConfig
from alipay.aop.api.domain.CommonPageConfig import CommonPageConfig
from alipay.aop.api.domain.ResultPageConfig import ResultPageConfig
from alipay.aop.api.domain.SolutionConfig import SolutionConfig


class AlipayOfflineProviderNpassporterVerifyconfigCreateModel(object):

    def __init__(self):
        self._activity_code = None
        self._authorization_page_config = None
        self._common_page_config = None
        self._location_url = None
        self._out_biz_id = None
        self._result_page_config = None
        self._solution_code = None
        self._solution_config = None
        self._verify_app_id = None
        self._verify_pid = None
        self._verify_result_page_source = None

    @property
    def activity_code(self):
        return self._activity_code

    @activity_code.setter
    def activity_code(self, value):
        self._activity_code = value
    @property
    def authorization_page_config(self):
        return self._authorization_page_config

    @authorization_page_config.setter
    def authorization_page_config(self, value):
        if isinstance(value, AuthorizationPageConfig):
            self._authorization_page_config = value
        else:
            self._authorization_page_config = AuthorizationPageConfig.from_alipay_dict(value)
    @property
    def common_page_config(self):
        return self._common_page_config

    @common_page_config.setter
    def common_page_config(self, value):
        if isinstance(value, CommonPageConfig):
            self._common_page_config = value
        else:
            self._common_page_config = CommonPageConfig.from_alipay_dict(value)
    @property
    def location_url(self):
        return self._location_url

    @location_url.setter
    def location_url(self, value):
        self._location_url = value
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value
    @property
    def result_page_config(self):
        return self._result_page_config

    @result_page_config.setter
    def result_page_config(self, value):
        if isinstance(value, ResultPageConfig):
            self._result_page_config = value
        else:
            self._result_page_config = ResultPageConfig.from_alipay_dict(value)
    @property
    def solution_code(self):
        return self._solution_code

    @solution_code.setter
    def solution_code(self, value):
        self._solution_code = value
    @property
    def solution_config(self):
        return self._solution_config

    @solution_config.setter
    def solution_config(self, value):
        if isinstance(value, SolutionConfig):
            self._solution_config = value
        else:
            self._solution_config = SolutionConfig.from_alipay_dict(value)
    @property
    def verify_app_id(self):
        return self._verify_app_id

    @verify_app_id.setter
    def verify_app_id(self, value):
        self._verify_app_id = value
    @property
    def verify_pid(self):
        return self._verify_pid

    @verify_pid.setter
    def verify_pid(self, value):
        self._verify_pid = value
    @property
    def verify_result_page_source(self):
        return self._verify_result_page_source

    @verify_result_page_source.setter
    def verify_result_page_source(self, value):
        self._verify_result_page_source = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_code:
            if hasattr(self.activity_code, 'to_alipay_dict'):
                params['activity_code'] = self.activity_code.to_alipay_dict()
            else:
                params['activity_code'] = self.activity_code
        if self.authorization_page_config:
            if hasattr(self.authorization_page_config, 'to_alipay_dict'):
                params['authorization_page_config'] = self.authorization_page_config.to_alipay_dict()
            else:
                params['authorization_page_config'] = self.authorization_page_config
        if self.common_page_config:
            if hasattr(self.common_page_config, 'to_alipay_dict'):
                params['common_page_config'] = self.common_page_config.to_alipay_dict()
            else:
                params['common_page_config'] = self.common_page_config
        if self.location_url:
            if hasattr(self.location_url, 'to_alipay_dict'):
                params['location_url'] = self.location_url.to_alipay_dict()
            else:
                params['location_url'] = self.location_url
        if self.out_biz_id:
            if hasattr(self.out_biz_id, 'to_alipay_dict'):
                params['out_biz_id'] = self.out_biz_id.to_alipay_dict()
            else:
                params['out_biz_id'] = self.out_biz_id
        if self.result_page_config:
            if hasattr(self.result_page_config, 'to_alipay_dict'):
                params['result_page_config'] = self.result_page_config.to_alipay_dict()
            else:
                params['result_page_config'] = self.result_page_config
        if self.solution_code:
            if hasattr(self.solution_code, 'to_alipay_dict'):
                params['solution_code'] = self.solution_code.to_alipay_dict()
            else:
                params['solution_code'] = self.solution_code
        if self.solution_config:
            if hasattr(self.solution_config, 'to_alipay_dict'):
                params['solution_config'] = self.solution_config.to_alipay_dict()
            else:
                params['solution_config'] = self.solution_config
        if self.verify_app_id:
            if hasattr(self.verify_app_id, 'to_alipay_dict'):
                params['verify_app_id'] = self.verify_app_id.to_alipay_dict()
            else:
                params['verify_app_id'] = self.verify_app_id
        if self.verify_pid:
            if hasattr(self.verify_pid, 'to_alipay_dict'):
                params['verify_pid'] = self.verify_pid.to_alipay_dict()
            else:
                params['verify_pid'] = self.verify_pid
        if self.verify_result_page_source:
            if hasattr(self.verify_result_page_source, 'to_alipay_dict'):
                params['verify_result_page_source'] = self.verify_result_page_source.to_alipay_dict()
            else:
                params['verify_result_page_source'] = self.verify_result_page_source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderNpassporterVerifyconfigCreateModel()
        if 'activity_code' in d:
            o.activity_code = d['activity_code']
        if 'authorization_page_config' in d:
            o.authorization_page_config = d['authorization_page_config']
        if 'common_page_config' in d:
            o.common_page_config = d['common_page_config']
        if 'location_url' in d:
            o.location_url = d['location_url']
        if 'out_biz_id' in d:
            o.out_biz_id = d['out_biz_id']
        if 'result_page_config' in d:
            o.result_page_config = d['result_page_config']
        if 'solution_code' in d:
            o.solution_code = d['solution_code']
        if 'solution_config' in d:
            o.solution_config = d['solution_config']
        if 'verify_app_id' in d:
            o.verify_app_id = d['verify_app_id']
        if 'verify_pid' in d:
            o.verify_pid = d['verify_pid']
        if 'verify_result_page_source' in d:
            o.verify_result_page_source = d['verify_result_page_source']
        return o


