#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenIotmbsIsvhotelCreateModel(object):

    def __init__(self):
        self._appid = None
        self._area_code = None
        self._project_addr = None
        self._project_flag = None
        self._project_id = None
        self._project_name = None
        self._shop_id = None
        self._solution = None

    @property
    def appid(self):
        return self._appid

    @appid.setter
    def appid(self, value):
        self._appid = value
    @property
    def area_code(self):
        return self._area_code

    @area_code.setter
    def area_code(self, value):
        self._area_code = value
    @property
    def project_addr(self):
        return self._project_addr

    @project_addr.setter
    def project_addr(self, value):
        self._project_addr = value
    @property
    def project_flag(self):
        return self._project_flag

    @project_flag.setter
    def project_flag(self, value):
        self._project_flag = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def project_name(self):
        return self._project_name

    @project_name.setter
    def project_name(self, value):
        self._project_name = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def solution(self):
        return self._solution

    @solution.setter
    def solution(self, value):
        self._solution = value


    def to_alipay_dict(self):
        params = dict()
        if self.appid:
            if hasattr(self.appid, 'to_alipay_dict'):
                params['appid'] = self.appid.to_alipay_dict()
            else:
                params['appid'] = self.appid
        if self.area_code:
            if hasattr(self.area_code, 'to_alipay_dict'):
                params['area_code'] = self.area_code.to_alipay_dict()
            else:
                params['area_code'] = self.area_code
        if self.project_addr:
            if hasattr(self.project_addr, 'to_alipay_dict'):
                params['project_addr'] = self.project_addr.to_alipay_dict()
            else:
                params['project_addr'] = self.project_addr
        if self.project_flag:
            if hasattr(self.project_flag, 'to_alipay_dict'):
                params['project_flag'] = self.project_flag.to_alipay_dict()
            else:
                params['project_flag'] = self.project_flag
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        if self.project_name:
            if hasattr(self.project_name, 'to_alipay_dict'):
                params['project_name'] = self.project_name.to_alipay_dict()
            else:
                params['project_name'] = self.project_name
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.solution:
            if hasattr(self.solution, 'to_alipay_dict'):
                params['solution'] = self.solution.to_alipay_dict()
            else:
                params['solution'] = self.solution
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenIotmbsIsvhotelCreateModel()
        if 'appid' in d:
            o.appid = d['appid']
        if 'area_code' in d:
            o.area_code = d['area_code']
        if 'project_addr' in d:
            o.project_addr = d['project_addr']
        if 'project_flag' in d:
            o.project_flag = d['project_flag']
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'project_name' in d:
            o.project_name = d['project_name']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'solution' in d:
            o.solution = d['solution']
        return o


