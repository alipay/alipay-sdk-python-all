#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenIotmbsIsvhotelModifyModel(object):

    def __init__(self):
        self._project_addr = None
        self._project_flag = None
        self._project_id = None
        self._project_nick_name = None

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
    def project_nick_name(self):
        return self._project_nick_name

    @project_nick_name.setter
    def project_nick_name(self, value):
        self._project_nick_name = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.project_nick_name:
            if hasattr(self.project_nick_name, 'to_alipay_dict'):
                params['project_nick_name'] = self.project_nick_name.to_alipay_dict()
            else:
                params['project_nick_name'] = self.project_nick_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenIotmbsIsvhotelModifyModel()
        if 'project_addr' in d:
            o.project_addr = d['project_addr']
        if 'project_flag' in d:
            o.project_flag = d['project_flag']
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'project_nick_name' in d:
            o.project_nick_name = d['project_nick_name']
        return o


