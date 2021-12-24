#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecruitEnrollMerchant import RecruitEnrollMerchant
from alipay.aop.api.domain.RecruitMaterial import RecruitMaterial
from alipay.aop.api.domain.RecruitMiniApp import RecruitMiniApp
from alipay.aop.api.domain.RecruitVoucher import RecruitVoucher


class RecruitEnrollInfo(object):

    def __init__(self):
        self._cities = None
        self._enroll_merchant = None
        self._materials = None
        self._mini_apps = None
        self._vouchers = None

    @property
    def cities(self):
        return self._cities

    @cities.setter
    def cities(self, value):
        if isinstance(value, list):
            self._cities = list()
            for i in value:
                self._cities.append(i)
    @property
    def enroll_merchant(self):
        return self._enroll_merchant

    @enroll_merchant.setter
    def enroll_merchant(self, value):
        if isinstance(value, RecruitEnrollMerchant):
            self._enroll_merchant = value
        else:
            self._enroll_merchant = RecruitEnrollMerchant.from_alipay_dict(value)
    @property
    def materials(self):
        return self._materials

    @materials.setter
    def materials(self, value):
        if isinstance(value, list):
            self._materials = list()
            for i in value:
                if isinstance(i, RecruitMaterial):
                    self._materials.append(i)
                else:
                    self._materials.append(RecruitMaterial.from_alipay_dict(i))
    @property
    def mini_apps(self):
        return self._mini_apps

    @mini_apps.setter
    def mini_apps(self, value):
        if isinstance(value, list):
            self._mini_apps = list()
            for i in value:
                if isinstance(i, RecruitMiniApp):
                    self._mini_apps.append(i)
                else:
                    self._mini_apps.append(RecruitMiniApp.from_alipay_dict(i))
    @property
    def vouchers(self):
        return self._vouchers

    @vouchers.setter
    def vouchers(self, value):
        if isinstance(value, list):
            self._vouchers = list()
            for i in value:
                if isinstance(i, RecruitVoucher):
                    self._vouchers.append(i)
                else:
                    self._vouchers.append(RecruitVoucher.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.cities:
            if isinstance(self.cities, list):
                for i in range(0, len(self.cities)):
                    element = self.cities[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.cities[i] = element.to_alipay_dict()
            if hasattr(self.cities, 'to_alipay_dict'):
                params['cities'] = self.cities.to_alipay_dict()
            else:
                params['cities'] = self.cities
        if self.enroll_merchant:
            if hasattr(self.enroll_merchant, 'to_alipay_dict'):
                params['enroll_merchant'] = self.enroll_merchant.to_alipay_dict()
            else:
                params['enroll_merchant'] = self.enroll_merchant
        if self.materials:
            if isinstance(self.materials, list):
                for i in range(0, len(self.materials)):
                    element = self.materials[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.materials[i] = element.to_alipay_dict()
            if hasattr(self.materials, 'to_alipay_dict'):
                params['materials'] = self.materials.to_alipay_dict()
            else:
                params['materials'] = self.materials
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
        if self.vouchers:
            if isinstance(self.vouchers, list):
                for i in range(0, len(self.vouchers)):
                    element = self.vouchers[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.vouchers[i] = element.to_alipay_dict()
            if hasattr(self.vouchers, 'to_alipay_dict'):
                params['vouchers'] = self.vouchers.to_alipay_dict()
            else:
                params['vouchers'] = self.vouchers
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecruitEnrollInfo()
        if 'cities' in d:
            o.cities = d['cities']
        if 'enroll_merchant' in d:
            o.enroll_merchant = d['enroll_merchant']
        if 'materials' in d:
            o.materials = d['materials']
        if 'mini_apps' in d:
            o.mini_apps = d['mini_apps']
        if 'vouchers' in d:
            o.vouchers = d['vouchers']
        return o


