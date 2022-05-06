#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InterTradeCompanyConsultOpenApiResult(object):

    def __init__(self):
        self._belong_group = None
        self._cid_list = None
        self._mid_list = None
        self._name = None
        self._ou = None
        self._pid_list = None
        self._related_flag = None
        self._uid_list = None

    @property
    def belong_group(self):
        return self._belong_group

    @belong_group.setter
    def belong_group(self, value):
        self._belong_group = value
    @property
    def cid_list(self):
        return self._cid_list

    @cid_list.setter
    def cid_list(self, value):
        if isinstance(value, list):
            self._cid_list = list()
            for i in value:
                self._cid_list.append(i)
    @property
    def mid_list(self):
        return self._mid_list

    @mid_list.setter
    def mid_list(self, value):
        if isinstance(value, list):
            self._mid_list = list()
            for i in value:
                self._mid_list.append(i)
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def ou(self):
        return self._ou

    @ou.setter
    def ou(self, value):
        self._ou = value
    @property
    def pid_list(self):
        return self._pid_list

    @pid_list.setter
    def pid_list(self, value):
        if isinstance(value, list):
            self._pid_list = list()
            for i in value:
                self._pid_list.append(i)
    @property
    def related_flag(self):
        return self._related_flag

    @related_flag.setter
    def related_flag(self, value):
        self._related_flag = value
    @property
    def uid_list(self):
        return self._uid_list

    @uid_list.setter
    def uid_list(self, value):
        if isinstance(value, list):
            self._uid_list = list()
            for i in value:
                self._uid_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.belong_group:
            if hasattr(self.belong_group, 'to_alipay_dict'):
                params['belong_group'] = self.belong_group.to_alipay_dict()
            else:
                params['belong_group'] = self.belong_group
        if self.cid_list:
            if isinstance(self.cid_list, list):
                for i in range(0, len(self.cid_list)):
                    element = self.cid_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.cid_list[i] = element.to_alipay_dict()
            if hasattr(self.cid_list, 'to_alipay_dict'):
                params['cid_list'] = self.cid_list.to_alipay_dict()
            else:
                params['cid_list'] = self.cid_list
        if self.mid_list:
            if isinstance(self.mid_list, list):
                for i in range(0, len(self.mid_list)):
                    element = self.mid_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.mid_list[i] = element.to_alipay_dict()
            if hasattr(self.mid_list, 'to_alipay_dict'):
                params['mid_list'] = self.mid_list.to_alipay_dict()
            else:
                params['mid_list'] = self.mid_list
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.ou:
            if hasattr(self.ou, 'to_alipay_dict'):
                params['ou'] = self.ou.to_alipay_dict()
            else:
                params['ou'] = self.ou
        if self.pid_list:
            if isinstance(self.pid_list, list):
                for i in range(0, len(self.pid_list)):
                    element = self.pid_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pid_list[i] = element.to_alipay_dict()
            if hasattr(self.pid_list, 'to_alipay_dict'):
                params['pid_list'] = self.pid_list.to_alipay_dict()
            else:
                params['pid_list'] = self.pid_list
        if self.related_flag:
            if hasattr(self.related_flag, 'to_alipay_dict'):
                params['related_flag'] = self.related_flag.to_alipay_dict()
            else:
                params['related_flag'] = self.related_flag
        if self.uid_list:
            if isinstance(self.uid_list, list):
                for i in range(0, len(self.uid_list)):
                    element = self.uid_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.uid_list[i] = element.to_alipay_dict()
            if hasattr(self.uid_list, 'to_alipay_dict'):
                params['uid_list'] = self.uid_list.to_alipay_dict()
            else:
                params['uid_list'] = self.uid_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InterTradeCompanyConsultOpenApiResult()
        if 'belong_group' in d:
            o.belong_group = d['belong_group']
        if 'cid_list' in d:
            o.cid_list = d['cid_list']
        if 'mid_list' in d:
            o.mid_list = d['mid_list']
        if 'name' in d:
            o.name = d['name']
        if 'ou' in d:
            o.ou = d['ou']
        if 'pid_list' in d:
            o.pid_list = d['pid_list']
        if 'related_flag' in d:
            o.related_flag = d['related_flag']
        if 'uid_list' in d:
            o.uid_list = d['uid_list']
        return o


