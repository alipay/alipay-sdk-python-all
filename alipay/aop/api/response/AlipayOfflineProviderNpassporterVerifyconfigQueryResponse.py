#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.VerifyConfigAuthorizationPageConfig import VerifyConfigAuthorizationPageConfig
from alipay.aop.api.domain.VerifyConfigCommonPageConfig import VerifyConfigCommonPageConfig
from alipay.aop.api.domain.VerifyConfigResultPageConfig import VerifyConfigResultPageConfig
from alipay.aop.api.domain.VerifyConfigSolutionConfig import VerifyConfigSolutionConfig


class AlipayOfflineProviderNpassporterVerifyconfigQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderNpassporterVerifyconfigQueryResponse, self).__init__()
        self._activity_code = None
        self._activity_name = None
        self._auth_no = None
        self._auth_url = None
        self._authorization_page_config = None
        self._common_page_config = None
        self._gmt_create = None
        self._gmt_modified = None
        self._location_url = None
        self._out_biz_id = None
        self._recent_verify_config_audit_desc = None
        self._recent_verify_config_id = None
        self._recent_verify_config_status = None
        self._result_page_config = None
        self._solution_code = None
        self._solution_config = None
        self._source = None
        self._status = None
        self._verify_app_id = None
        self._verify_config_id = None
        self._verify_pid = None
        self._verify_result_page_source = None

    @property
    def activity_code(self):
        return self._activity_code

    @activity_code.setter
    def activity_code(self, value):
        self._activity_code = value
    @property
    def activity_name(self):
        return self._activity_name

    @activity_name.setter
    def activity_name(self, value):
        self._activity_name = value
    @property
    def auth_no(self):
        return self._auth_no

    @auth_no.setter
    def auth_no(self, value):
        self._auth_no = value
    @property
    def auth_url(self):
        return self._auth_url

    @auth_url.setter
    def auth_url(self, value):
        self._auth_url = value
    @property
    def authorization_page_config(self):
        return self._authorization_page_config

    @authorization_page_config.setter
    def authorization_page_config(self, value):
        if isinstance(value, VerifyConfigAuthorizationPageConfig):
            self._authorization_page_config = value
        else:
            self._authorization_page_config = VerifyConfigAuthorizationPageConfig.from_alipay_dict(value)
    @property
    def common_page_config(self):
        return self._common_page_config

    @common_page_config.setter
    def common_page_config(self, value):
        if isinstance(value, VerifyConfigCommonPageConfig):
            self._common_page_config = value
        else:
            self._common_page_config = VerifyConfigCommonPageConfig.from_alipay_dict(value)
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
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
    def recent_verify_config_audit_desc(self):
        return self._recent_verify_config_audit_desc

    @recent_verify_config_audit_desc.setter
    def recent_verify_config_audit_desc(self, value):
        self._recent_verify_config_audit_desc = value
    @property
    def recent_verify_config_id(self):
        return self._recent_verify_config_id

    @recent_verify_config_id.setter
    def recent_verify_config_id(self, value):
        self._recent_verify_config_id = value
    @property
    def recent_verify_config_status(self):
        return self._recent_verify_config_status

    @recent_verify_config_status.setter
    def recent_verify_config_status(self, value):
        self._recent_verify_config_status = value
    @property
    def result_page_config(self):
        return self._result_page_config

    @result_page_config.setter
    def result_page_config(self, value):
        if isinstance(value, VerifyConfigResultPageConfig):
            self._result_page_config = value
        else:
            self._result_page_config = VerifyConfigResultPageConfig.from_alipay_dict(value)
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
        if isinstance(value, VerifyConfigSolutionConfig):
            self._solution_config = value
        else:
            self._solution_config = VerifyConfigSolutionConfig.from_alipay_dict(value)
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def verify_app_id(self):
        return self._verify_app_id

    @verify_app_id.setter
    def verify_app_id(self, value):
        self._verify_app_id = value
    @property
    def verify_config_id(self):
        return self._verify_config_id

    @verify_config_id.setter
    def verify_config_id(self, value):
        self._verify_config_id = value
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

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderNpassporterVerifyconfigQueryResponse, self).parse_response_content(response_content)
        if 'activity_code' in response:
            self.activity_code = response['activity_code']
        if 'activity_name' in response:
            self.activity_name = response['activity_name']
        if 'auth_no' in response:
            self.auth_no = response['auth_no']
        if 'auth_url' in response:
            self.auth_url = response['auth_url']
        if 'authorization_page_config' in response:
            self.authorization_page_config = response['authorization_page_config']
        if 'common_page_config' in response:
            self.common_page_config = response['common_page_config']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'gmt_modified' in response:
            self.gmt_modified = response['gmt_modified']
        if 'location_url' in response:
            self.location_url = response['location_url']
        if 'out_biz_id' in response:
            self.out_biz_id = response['out_biz_id']
        if 'recent_verify_config_audit_desc' in response:
            self.recent_verify_config_audit_desc = response['recent_verify_config_audit_desc']
        if 'recent_verify_config_id' in response:
            self.recent_verify_config_id = response['recent_verify_config_id']
        if 'recent_verify_config_status' in response:
            self.recent_verify_config_status = response['recent_verify_config_status']
        if 'result_page_config' in response:
            self.result_page_config = response['result_page_config']
        if 'solution_code' in response:
            self.solution_code = response['solution_code']
        if 'solution_config' in response:
            self.solution_config = response['solution_config']
        if 'source' in response:
            self.source = response['source']
        if 'status' in response:
            self.status = response['status']
        if 'verify_app_id' in response:
            self.verify_app_id = response['verify_app_id']
        if 'verify_config_id' in response:
            self.verify_config_id = response['verify_config_id']
        if 'verify_pid' in response:
            self.verify_pid = response['verify_pid']
        if 'verify_result_page_source' in response:
            self.verify_result_page_source = response['verify_result_page_source']
