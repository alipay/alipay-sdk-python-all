#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MiniAppClientVersionInfo import MiniAppClientVersionInfo
from alipay.aop.api.domain.MiniAppPackageInfo import MiniAppPackageInfo
from alipay.aop.api.domain.MiniAppPackageInfo import MiniAppPackageInfo
from alipay.aop.api.domain.MiniAppClientVersionInfo import MiniAppClientVersionInfo
from alipay.aop.api.domain.MiniAppPackageInfo import MiniAppPackageInfo
from alipay.aop.api.domain.MiniAppPackageInfo import MiniAppPackageInfo


class MiniAppVersionInfo(object):

    def __init__(self):
        self._android_client_version_info = None
        self._app_version = None
        self._audit_package = None
        self._build_task_log = None
        self._coverage_package = None
        self._coverage_rate = None
        self._error_msg = None
        self._ios_client_version_info = None
        self._preonline_package = None
        self._security_scan_result = None
        self._status = None
        self._trial_package = None

    @property
    def android_client_version_info(self):
        return self._android_client_version_info

    @android_client_version_info.setter
    def android_client_version_info(self, value):
        if isinstance(value, MiniAppClientVersionInfo):
            self._android_client_version_info = value
        else:
            self._android_client_version_info = MiniAppClientVersionInfo.from_alipay_dict(value)
    @property
    def app_version(self):
        return self._app_version

    @app_version.setter
    def app_version(self, value):
        self._app_version = value
    @property
    def audit_package(self):
        return self._audit_package

    @audit_package.setter
    def audit_package(self, value):
        if isinstance(value, MiniAppPackageInfo):
            self._audit_package = value
        else:
            self._audit_package = MiniAppPackageInfo.from_alipay_dict(value)
    @property
    def build_task_log(self):
        return self._build_task_log

    @build_task_log.setter
    def build_task_log(self, value):
        self._build_task_log = value
    @property
    def coverage_package(self):
        return self._coverage_package

    @coverage_package.setter
    def coverage_package(self, value):
        if isinstance(value, MiniAppPackageInfo):
            self._coverage_package = value
        else:
            self._coverage_package = MiniAppPackageInfo.from_alipay_dict(value)
    @property
    def coverage_rate(self):
        return self._coverage_rate

    @coverage_rate.setter
    def coverage_rate(self, value):
        self._coverage_rate = value
    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value
    @property
    def ios_client_version_info(self):
        return self._ios_client_version_info

    @ios_client_version_info.setter
    def ios_client_version_info(self, value):
        if isinstance(value, MiniAppClientVersionInfo):
            self._ios_client_version_info = value
        else:
            self._ios_client_version_info = MiniAppClientVersionInfo.from_alipay_dict(value)
    @property
    def preonline_package(self):
        return self._preonline_package

    @preonline_package.setter
    def preonline_package(self, value):
        if isinstance(value, MiniAppPackageInfo):
            self._preonline_package = value
        else:
            self._preonline_package = MiniAppPackageInfo.from_alipay_dict(value)
    @property
    def security_scan_result(self):
        return self._security_scan_result

    @security_scan_result.setter
    def security_scan_result(self, value):
        self._security_scan_result = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def trial_package(self):
        return self._trial_package

    @trial_package.setter
    def trial_package(self, value):
        if isinstance(value, MiniAppPackageInfo):
            self._trial_package = value
        else:
            self._trial_package = MiniAppPackageInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.android_client_version_info:
            if hasattr(self.android_client_version_info, 'to_alipay_dict'):
                params['android_client_version_info'] = self.android_client_version_info.to_alipay_dict()
            else:
                params['android_client_version_info'] = self.android_client_version_info
        if self.app_version:
            if hasattr(self.app_version, 'to_alipay_dict'):
                params['app_version'] = self.app_version.to_alipay_dict()
            else:
                params['app_version'] = self.app_version
        if self.audit_package:
            if hasattr(self.audit_package, 'to_alipay_dict'):
                params['audit_package'] = self.audit_package.to_alipay_dict()
            else:
                params['audit_package'] = self.audit_package
        if self.build_task_log:
            if hasattr(self.build_task_log, 'to_alipay_dict'):
                params['build_task_log'] = self.build_task_log.to_alipay_dict()
            else:
                params['build_task_log'] = self.build_task_log
        if self.coverage_package:
            if hasattr(self.coverage_package, 'to_alipay_dict'):
                params['coverage_package'] = self.coverage_package.to_alipay_dict()
            else:
                params['coverage_package'] = self.coverage_package
        if self.coverage_rate:
            if hasattr(self.coverage_rate, 'to_alipay_dict'):
                params['coverage_rate'] = self.coverage_rate.to_alipay_dict()
            else:
                params['coverage_rate'] = self.coverage_rate
        if self.error_msg:
            if hasattr(self.error_msg, 'to_alipay_dict'):
                params['error_msg'] = self.error_msg.to_alipay_dict()
            else:
                params['error_msg'] = self.error_msg
        if self.ios_client_version_info:
            if hasattr(self.ios_client_version_info, 'to_alipay_dict'):
                params['ios_client_version_info'] = self.ios_client_version_info.to_alipay_dict()
            else:
                params['ios_client_version_info'] = self.ios_client_version_info
        if self.preonline_package:
            if hasattr(self.preonline_package, 'to_alipay_dict'):
                params['preonline_package'] = self.preonline_package.to_alipay_dict()
            else:
                params['preonline_package'] = self.preonline_package
        if self.security_scan_result:
            if hasattr(self.security_scan_result, 'to_alipay_dict'):
                params['security_scan_result'] = self.security_scan_result.to_alipay_dict()
            else:
                params['security_scan_result'] = self.security_scan_result
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.trial_package:
            if hasattr(self.trial_package, 'to_alipay_dict'):
                params['trial_package'] = self.trial_package.to_alipay_dict()
            else:
                params['trial_package'] = self.trial_package
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MiniAppVersionInfo()
        if 'android_client_version_info' in d:
            o.android_client_version_info = d['android_client_version_info']
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'audit_package' in d:
            o.audit_package = d['audit_package']
        if 'build_task_log' in d:
            o.build_task_log = d['build_task_log']
        if 'coverage_package' in d:
            o.coverage_package = d['coverage_package']
        if 'coverage_rate' in d:
            o.coverage_rate = d['coverage_rate']
        if 'error_msg' in d:
            o.error_msg = d['error_msg']
        if 'ios_client_version_info' in d:
            o.ios_client_version_info = d['ios_client_version_info']
        if 'preonline_package' in d:
            o.preonline_package = d['preonline_package']
        if 'security_scan_result' in d:
            o.security_scan_result = d['security_scan_result']
        if 'status' in d:
            o.status = d['status']
        if 'trial_package' in d:
            o.trial_package = d['trial_package']
        return o


