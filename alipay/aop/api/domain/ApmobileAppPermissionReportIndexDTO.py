#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ApmobileAppPermissionReportIndexDTO(object):

    def __init__(self):
        self._app_version = None
        self._cert_md_5 = None
        self._detect_report_pdf_url = None
        self._detect_time = None
        self._developer = None
        self._md_5 = None
        self._name = None
        self._package_name = None
        self._platform = None
        self._privacy_policy = None
        self._sdk_sum = None
        self._sign_certificate = None
        self._size = None
        self._target_sdk_version = None
        self._task_id = None
        self._ut_name = None

    @property
    def app_version(self):
        return self._app_version

    @app_version.setter
    def app_version(self, value):
        self._app_version = value
    @property
    def cert_md_5(self):
        return self._cert_md_5

    @cert_md_5.setter
    def cert_md_5(self, value):
        self._cert_md_5 = value
    @property
    def detect_report_pdf_url(self):
        return self._detect_report_pdf_url

    @detect_report_pdf_url.setter
    def detect_report_pdf_url(self, value):
        self._detect_report_pdf_url = value
    @property
    def detect_time(self):
        return self._detect_time

    @detect_time.setter
    def detect_time(self, value):
        self._detect_time = value
    @property
    def developer(self):
        return self._developer

    @developer.setter
    def developer(self, value):
        self._developer = value
    @property
    def md_5(self):
        return self._md_5

    @md_5.setter
    def md_5(self, value):
        self._md_5 = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def package_name(self):
        return self._package_name

    @package_name.setter
    def package_name(self, value):
        self._package_name = value
    @property
    def platform(self):
        return self._platform

    @platform.setter
    def platform(self, value):
        self._platform = value
    @property
    def privacy_policy(self):
        return self._privacy_policy

    @privacy_policy.setter
    def privacy_policy(self, value):
        self._privacy_policy = value
    @property
    def sdk_sum(self):
        return self._sdk_sum

    @sdk_sum.setter
    def sdk_sum(self, value):
        self._sdk_sum = value
    @property
    def sign_certificate(self):
        return self._sign_certificate

    @sign_certificate.setter
    def sign_certificate(self, value):
        self._sign_certificate = value
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
    @property
    def target_sdk_version(self):
        return self._target_sdk_version

    @target_sdk_version.setter
    def target_sdk_version(self, value):
        self._target_sdk_version = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def ut_name(self):
        return self._ut_name

    @ut_name.setter
    def ut_name(self, value):
        self._ut_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_version:
            if hasattr(self.app_version, 'to_alipay_dict'):
                params['app_version'] = self.app_version.to_alipay_dict()
            else:
                params['app_version'] = self.app_version
        if self.cert_md_5:
            if hasattr(self.cert_md_5, 'to_alipay_dict'):
                params['cert_md_5'] = self.cert_md_5.to_alipay_dict()
            else:
                params['cert_md_5'] = self.cert_md_5
        if self.detect_report_pdf_url:
            if hasattr(self.detect_report_pdf_url, 'to_alipay_dict'):
                params['detect_report_pdf_url'] = self.detect_report_pdf_url.to_alipay_dict()
            else:
                params['detect_report_pdf_url'] = self.detect_report_pdf_url
        if self.detect_time:
            if hasattr(self.detect_time, 'to_alipay_dict'):
                params['detect_time'] = self.detect_time.to_alipay_dict()
            else:
                params['detect_time'] = self.detect_time
        if self.developer:
            if hasattr(self.developer, 'to_alipay_dict'):
                params['developer'] = self.developer.to_alipay_dict()
            else:
                params['developer'] = self.developer
        if self.md_5:
            if hasattr(self.md_5, 'to_alipay_dict'):
                params['md_5'] = self.md_5.to_alipay_dict()
            else:
                params['md_5'] = self.md_5
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.package_name:
            if hasattr(self.package_name, 'to_alipay_dict'):
                params['package_name'] = self.package_name.to_alipay_dict()
            else:
                params['package_name'] = self.package_name
        if self.platform:
            if hasattr(self.platform, 'to_alipay_dict'):
                params['platform'] = self.platform.to_alipay_dict()
            else:
                params['platform'] = self.platform
        if self.privacy_policy:
            if hasattr(self.privacy_policy, 'to_alipay_dict'):
                params['privacy_policy'] = self.privacy_policy.to_alipay_dict()
            else:
                params['privacy_policy'] = self.privacy_policy
        if self.sdk_sum:
            if hasattr(self.sdk_sum, 'to_alipay_dict'):
                params['sdk_sum'] = self.sdk_sum.to_alipay_dict()
            else:
                params['sdk_sum'] = self.sdk_sum
        if self.sign_certificate:
            if hasattr(self.sign_certificate, 'to_alipay_dict'):
                params['sign_certificate'] = self.sign_certificate.to_alipay_dict()
            else:
                params['sign_certificate'] = self.sign_certificate
        if self.size:
            if hasattr(self.size, 'to_alipay_dict'):
                params['size'] = self.size.to_alipay_dict()
            else:
                params['size'] = self.size
        if self.target_sdk_version:
            if hasattr(self.target_sdk_version, 'to_alipay_dict'):
                params['target_sdk_version'] = self.target_sdk_version.to_alipay_dict()
            else:
                params['target_sdk_version'] = self.target_sdk_version
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        if self.ut_name:
            if hasattr(self.ut_name, 'to_alipay_dict'):
                params['ut_name'] = self.ut_name.to_alipay_dict()
            else:
                params['ut_name'] = self.ut_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApmobileAppPermissionReportIndexDTO()
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'cert_md_5' in d:
            o.cert_md_5 = d['cert_md_5']
        if 'detect_report_pdf_url' in d:
            o.detect_report_pdf_url = d['detect_report_pdf_url']
        if 'detect_time' in d:
            o.detect_time = d['detect_time']
        if 'developer' in d:
            o.developer = d['developer']
        if 'md_5' in d:
            o.md_5 = d['md_5']
        if 'name' in d:
            o.name = d['name']
        if 'package_name' in d:
            o.package_name = d['package_name']
        if 'platform' in d:
            o.platform = d['platform']
        if 'privacy_policy' in d:
            o.privacy_policy = d['privacy_policy']
        if 'sdk_sum' in d:
            o.sdk_sum = d['sdk_sum']
        if 'sign_certificate' in d:
            o.sign_certificate = d['sign_certificate']
        if 'size' in d:
            o.size = d['size']
        if 'target_sdk_version' in d:
            o.target_sdk_version = d['target_sdk_version']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'ut_name' in d:
            o.ut_name = d['ut_name']
        return o


