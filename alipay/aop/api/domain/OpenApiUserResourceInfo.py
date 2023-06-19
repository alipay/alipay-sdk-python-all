#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenApiUserResourceInfo(object):

    def __init__(self):
        self._alipay_uid = None
        self._busvc_cloud_id = None
        self._busvc_domain = None
        self._busvc_id = None
        self._busvc_no = None
        self._clv_user_id = None
        self._ur_id = None

    @property
    def alipay_uid(self):
        return self._alipay_uid

    @alipay_uid.setter
    def alipay_uid(self, value):
        self._alipay_uid = value
    @property
    def busvc_cloud_id(self):
        return self._busvc_cloud_id

    @busvc_cloud_id.setter
    def busvc_cloud_id(self, value):
        self._busvc_cloud_id = value
    @property
    def busvc_domain(self):
        return self._busvc_domain

    @busvc_domain.setter
    def busvc_domain(self, value):
        self._busvc_domain = value
    @property
    def busvc_id(self):
        return self._busvc_id

    @busvc_id.setter
    def busvc_id(self, value):
        self._busvc_id = value
    @property
    def busvc_no(self):
        return self._busvc_no

    @busvc_no.setter
    def busvc_no(self, value):
        self._busvc_no = value
    @property
    def clv_user_id(self):
        return self._clv_user_id

    @clv_user_id.setter
    def clv_user_id(self, value):
        self._clv_user_id = value
    @property
    def ur_id(self):
        return self._ur_id

    @ur_id.setter
    def ur_id(self, value):
        self._ur_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_uid:
            if hasattr(self.alipay_uid, 'to_alipay_dict'):
                params['alipay_uid'] = self.alipay_uid.to_alipay_dict()
            else:
                params['alipay_uid'] = self.alipay_uid
        if self.busvc_cloud_id:
            if hasattr(self.busvc_cloud_id, 'to_alipay_dict'):
                params['busvc_cloud_id'] = self.busvc_cloud_id.to_alipay_dict()
            else:
                params['busvc_cloud_id'] = self.busvc_cloud_id
        if self.busvc_domain:
            if hasattr(self.busvc_domain, 'to_alipay_dict'):
                params['busvc_domain'] = self.busvc_domain.to_alipay_dict()
            else:
                params['busvc_domain'] = self.busvc_domain
        if self.busvc_id:
            if hasattr(self.busvc_id, 'to_alipay_dict'):
                params['busvc_id'] = self.busvc_id.to_alipay_dict()
            else:
                params['busvc_id'] = self.busvc_id
        if self.busvc_no:
            if hasattr(self.busvc_no, 'to_alipay_dict'):
                params['busvc_no'] = self.busvc_no.to_alipay_dict()
            else:
                params['busvc_no'] = self.busvc_no
        if self.clv_user_id:
            if hasattr(self.clv_user_id, 'to_alipay_dict'):
                params['clv_user_id'] = self.clv_user_id.to_alipay_dict()
            else:
                params['clv_user_id'] = self.clv_user_id
        if self.ur_id:
            if hasattr(self.ur_id, 'to_alipay_dict'):
                params['ur_id'] = self.ur_id.to_alipay_dict()
            else:
                params['ur_id'] = self.ur_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiUserResourceInfo()
        if 'alipay_uid' in d:
            o.alipay_uid = d['alipay_uid']
        if 'busvc_cloud_id' in d:
            o.busvc_cloud_id = d['busvc_cloud_id']
        if 'busvc_domain' in d:
            o.busvc_domain = d['busvc_domain']
        if 'busvc_id' in d:
            o.busvc_id = d['busvc_id']
        if 'busvc_no' in d:
            o.busvc_no = d['busvc_no']
        if 'clv_user_id' in d:
            o.clv_user_id = d['clv_user_id']
        if 'ur_id' in d:
            o.ur_id = d['ur_id']
        return o


