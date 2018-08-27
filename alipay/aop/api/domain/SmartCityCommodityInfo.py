#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SmartCityCommodityInfo(object):

    def __init__(self):
        self._affiliation = None
        self._auth_file = None
        self._test_detail = None
        self._test_report = None
        self._user_guide = None

    @property
    def affiliation(self):
        return self._affiliation

    @affiliation.setter
    def affiliation(self, value):
        self._affiliation = value
    @property
    def auth_file(self):
        return self._auth_file

    @auth_file.setter
    def auth_file(self, value):
        self._auth_file = value
    @property
    def test_detail(self):
        return self._test_detail

    @test_detail.setter
    def test_detail(self, value):
        self._test_detail = value
    @property
    def test_report(self):
        return self._test_report

    @test_report.setter
    def test_report(self, value):
        self._test_report = value
    @property
    def user_guide(self):
        return self._user_guide

    @user_guide.setter
    def user_guide(self, value):
        self._user_guide = value


    def to_alipay_dict(self):
        params = dict()
        if self.affiliation:
            if hasattr(self.affiliation, 'to_alipay_dict'):
                params['affiliation'] = self.affiliation.to_alipay_dict()
            else:
                params['affiliation'] = self.affiliation
        if self.auth_file:
            if hasattr(self.auth_file, 'to_alipay_dict'):
                params['auth_file'] = self.auth_file.to_alipay_dict()
            else:
                params['auth_file'] = self.auth_file
        if self.test_detail:
            if hasattr(self.test_detail, 'to_alipay_dict'):
                params['test_detail'] = self.test_detail.to_alipay_dict()
            else:
                params['test_detail'] = self.test_detail
        if self.test_report:
            if hasattr(self.test_report, 'to_alipay_dict'):
                params['test_report'] = self.test_report.to_alipay_dict()
            else:
                params['test_report'] = self.test_report
        if self.user_guide:
            if hasattr(self.user_guide, 'to_alipay_dict'):
                params['user_guide'] = self.user_guide.to_alipay_dict()
            else:
                params['user_guide'] = self.user_guide
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SmartCityCommodityInfo()
        if 'affiliation' in d:
            o.affiliation = d['affiliation']
        if 'auth_file' in d:
            o.auth_file = d['auth_file']
        if 'test_detail' in d:
            o.test_detail = d['test_detail']
        if 'test_report' in d:
            o.test_report = d['test_report']
        if 'user_guide' in d:
            o.user_guide = d['user_guide']
        return o


