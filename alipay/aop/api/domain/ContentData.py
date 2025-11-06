#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HealthHistory import HealthHistory
from alipay.aop.api.domain.HealthReport import HealthReport
from alipay.aop.api.domain.HealthcareData import HealthcareData
from alipay.aop.api.domain.Userbase import Userbase


class ContentData(object):

    def __init__(self):
        self._health_history = None
        self._health_report_list = None
        self._user_folder = None
        self._userbase = None

    @property
    def health_history(self):
        return self._health_history

    @health_history.setter
    def health_history(self, value):
        if isinstance(value, HealthHistory):
            self._health_history = value
        else:
            self._health_history = HealthHistory.from_alipay_dict(value)
    @property
    def health_report_list(self):
        return self._health_report_list

    @health_report_list.setter
    def health_report_list(self, value):
        if isinstance(value, list):
            self._health_report_list = list()
            for i in value:
                if isinstance(i, HealthReport):
                    self._health_report_list.append(i)
                else:
                    self._health_report_list.append(HealthReport.from_alipay_dict(i))
    @property
    def user_folder(self):
        return self._user_folder

    @user_folder.setter
    def user_folder(self, value):
        if isinstance(value, HealthcareData):
            self._user_folder = value
        else:
            self._user_folder = HealthcareData.from_alipay_dict(value)
    @property
    def userbase(self):
        return self._userbase

    @userbase.setter
    def userbase(self, value):
        if isinstance(value, Userbase):
            self._userbase = value
        else:
            self._userbase = Userbase.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.health_history:
            if hasattr(self.health_history, 'to_alipay_dict'):
                params['health_history'] = self.health_history.to_alipay_dict()
            else:
                params['health_history'] = self.health_history
        if self.health_report_list:
            if isinstance(self.health_report_list, list):
                for i in range(0, len(self.health_report_list)):
                    element = self.health_report_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.health_report_list[i] = element.to_alipay_dict()
            if hasattr(self.health_report_list, 'to_alipay_dict'):
                params['health_report_list'] = self.health_report_list.to_alipay_dict()
            else:
                params['health_report_list'] = self.health_report_list
        if self.user_folder:
            if hasattr(self.user_folder, 'to_alipay_dict'):
                params['user_folder'] = self.user_folder.to_alipay_dict()
            else:
                params['user_folder'] = self.user_folder
        if self.userbase:
            if hasattr(self.userbase, 'to_alipay_dict'):
                params['userbase'] = self.userbase.to_alipay_dict()
            else:
                params['userbase'] = self.userbase
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContentData()
        if 'health_history' in d:
            o.health_history = d['health_history']
        if 'health_report_list' in d:
            o.health_report_list = d['health_report_list']
        if 'user_folder' in d:
            o.user_folder = d['user_folder']
        if 'userbase' in d:
            o.userbase = d['userbase']
        return o


