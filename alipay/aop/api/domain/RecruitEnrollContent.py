#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecruitContentAppItem import RecruitContentAppItem
from alipay.aop.api.domain.RecruitContentMiniApp import RecruitContentMiniApp
from alipay.aop.api.domain.RecruitContentVoucherActivity import RecruitContentVoucherActivity


class RecruitEnrollContent(object):

    def __init__(self):
        self._app_items = None
        self._mini_apps = None
        self._voucher_activities = None

    @property
    def app_items(self):
        return self._app_items

    @app_items.setter
    def app_items(self, value):
        if isinstance(value, list):
            self._app_items = list()
            for i in value:
                if isinstance(i, RecruitContentAppItem):
                    self._app_items.append(i)
                else:
                    self._app_items.append(RecruitContentAppItem.from_alipay_dict(i))
    @property
    def mini_apps(self):
        return self._mini_apps

    @mini_apps.setter
    def mini_apps(self, value):
        if isinstance(value, list):
            self._mini_apps = list()
            for i in value:
                if isinstance(i, RecruitContentMiniApp):
                    self._mini_apps.append(i)
                else:
                    self._mini_apps.append(RecruitContentMiniApp.from_alipay_dict(i))
    @property
    def voucher_activities(self):
        return self._voucher_activities

    @voucher_activities.setter
    def voucher_activities(self, value):
        if isinstance(value, list):
            self._voucher_activities = list()
            for i in value:
                if isinstance(i, RecruitContentVoucherActivity):
                    self._voucher_activities.append(i)
                else:
                    self._voucher_activities.append(RecruitContentVoucherActivity.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.app_items:
            if isinstance(self.app_items, list):
                for i in range(0, len(self.app_items)):
                    element = self.app_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.app_items[i] = element.to_alipay_dict()
            if hasattr(self.app_items, 'to_alipay_dict'):
                params['app_items'] = self.app_items.to_alipay_dict()
            else:
                params['app_items'] = self.app_items
        if self.mini_apps:
            if isinstance(self.mini_apps, list):
                for i in range(0, len(self.mini_apps)):
                    element = self.mini_apps[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.mini_apps[i] = element.to_alipay_dict()
            if hasattr(self.mini_apps, 'to_alipay_dict'):
                params['mini_apps'] = self.mini_apps.to_alipay_dict()
            else:
                params['mini_apps'] = self.mini_apps
        if self.voucher_activities:
            if isinstance(self.voucher_activities, list):
                for i in range(0, len(self.voucher_activities)):
                    element = self.voucher_activities[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.voucher_activities[i] = element.to_alipay_dict()
            if hasattr(self.voucher_activities, 'to_alipay_dict'):
                params['voucher_activities'] = self.voucher_activities.to_alipay_dict()
            else:
                params['voucher_activities'] = self.voucher_activities
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecruitEnrollContent()
        if 'app_items' in d:
            o.app_items = d['app_items']
        if 'mini_apps' in d:
            o.mini_apps = d['mini_apps']
        if 'voucher_activities' in d:
            o.voucher_activities = d['voucher_activities']
        return o


