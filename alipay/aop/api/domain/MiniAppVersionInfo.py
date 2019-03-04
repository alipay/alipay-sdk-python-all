#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MiniAppPackageInfo import MiniAppPackageInfo
from alipay.aop.api.domain.MiniAppPackageInfo import MiniAppPackageInfo


class MiniAppVersionInfo(object):

    def __init__(self):
        self._app_version = None
        self._build_task_log = None
        self._coverage_package = None
        self._coverage_rate = None
        self._preonline_package = None
        self._security_scan_result = None
        self._status = None

    @property
    def app_version(self):
        return self._app_version

    @app_version.setter
    def app_version(self, value):
        self._app_version = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.app_version:
            if hasattr(self.app_version, 'to_alipay_dict'):
                params['app_version'] = self.app_version.to_alipay_dict()
            else:
                params['app_version'] = self.app_version
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MiniAppVersionInfo()
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'build_task_log' in d:
            o.build_task_log = d['build_task_log']
        if 'coverage_package' in d:
            o.coverage_package = d['coverage_package']
        if 'coverage_rate' in d:
            o.coverage_rate = d['coverage_rate']
        if 'preonline_package' in d:
            o.preonline_package = d['preonline_package']
        if 'security_scan_result' in d:
            o.security_scan_result = d['security_scan_result']
        if 'status' in d:
            o.status = d['status']
        return o


