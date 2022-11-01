#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenidComplex(object):

    def __init__(self):
        self._json_string = None
        self._open_id_list = None
        self._openid = None
        self._uid = None
        self._uid_list = None

    @property
    def json_string(self):
        return self._json_string

    @json_string.setter
    def json_string(self, value):
        self._json_string = value
    @property
    def open_id_list(self):
        return self._open_id_list

    @open_id_list.setter
    def open_id_list(self, value):
        if isinstance(value, list):
            self._open_id_list = list()
            for i in value:
                self._open_id_list.append(i)
    @property
    def openid(self):
        return self._openid

    @openid.setter
    def openid(self, value):
        self._openid = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value
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
        if self.json_string:
            if hasattr(self.json_string, 'to_alipay_dict'):
                params['json_string'] = self.json_string.to_alipay_dict()
            else:
                params['json_string'] = self.json_string
        if self.open_id_list:
            if isinstance(self.open_id_list, list):
                for i in range(0, len(self.open_id_list)):
                    element = self.open_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.open_id_list[i] = element.to_alipay_dict()
            if hasattr(self.open_id_list, 'to_alipay_dict'):
                params['open_id_list'] = self.open_id_list.to_alipay_dict()
            else:
                params['open_id_list'] = self.open_id_list
        if self.openid:
            if hasattr(self.openid, 'to_alipay_dict'):
                params['openid'] = self.openid.to_alipay_dict()
            else:
                params['openid'] = self.openid
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
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
        o = OpenidComplex()
        if 'json_string' in d:
            o.json_string = d['json_string']
        if 'open_id_list' in d:
            o.open_id_list = d['open_id_list']
        if 'openid' in d:
            o.openid = d['openid']
        if 'uid' in d:
            o.uid = d['uid']
        if 'uid_list' in d:
            o.uid_list = d['uid_list']
        return o


