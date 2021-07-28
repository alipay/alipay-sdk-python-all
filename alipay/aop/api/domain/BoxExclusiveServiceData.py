#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BoxExclusiveServiceData(object):

    def __init__(self):
        self._serv_code = None
        self._serv_desc = None
        self._serv_id = None
        self._serv_link = None
        self._serv_logo = None
        self._serv_name = None

    @property
    def serv_code(self):
        return self._serv_code

    @serv_code.setter
    def serv_code(self, value):
        self._serv_code = value
    @property
    def serv_desc(self):
        return self._serv_desc

    @serv_desc.setter
    def serv_desc(self, value):
        self._serv_desc = value
    @property
    def serv_id(self):
        return self._serv_id

    @serv_id.setter
    def serv_id(self, value):
        self._serv_id = value
    @property
    def serv_link(self):
        return self._serv_link

    @serv_link.setter
    def serv_link(self, value):
        self._serv_link = value
    @property
    def serv_logo(self):
        return self._serv_logo

    @serv_logo.setter
    def serv_logo(self, value):
        self._serv_logo = value
    @property
    def serv_name(self):
        return self._serv_name

    @serv_name.setter
    def serv_name(self, value):
        self._serv_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.serv_code:
            if hasattr(self.serv_code, 'to_alipay_dict'):
                params['serv_code'] = self.serv_code.to_alipay_dict()
            else:
                params['serv_code'] = self.serv_code
        if self.serv_desc:
            if hasattr(self.serv_desc, 'to_alipay_dict'):
                params['serv_desc'] = self.serv_desc.to_alipay_dict()
            else:
                params['serv_desc'] = self.serv_desc
        if self.serv_id:
            if hasattr(self.serv_id, 'to_alipay_dict'):
                params['serv_id'] = self.serv_id.to_alipay_dict()
            else:
                params['serv_id'] = self.serv_id
        if self.serv_link:
            if hasattr(self.serv_link, 'to_alipay_dict'):
                params['serv_link'] = self.serv_link.to_alipay_dict()
            else:
                params['serv_link'] = self.serv_link
        if self.serv_logo:
            if hasattr(self.serv_logo, 'to_alipay_dict'):
                params['serv_logo'] = self.serv_logo.to_alipay_dict()
            else:
                params['serv_logo'] = self.serv_logo
        if self.serv_name:
            if hasattr(self.serv_name, 'to_alipay_dict'):
                params['serv_name'] = self.serv_name.to_alipay_dict()
            else:
                params['serv_name'] = self.serv_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BoxExclusiveServiceData()
        if 'serv_code' in d:
            o.serv_code = d['serv_code']
        if 'serv_desc' in d:
            o.serv_desc = d['serv_desc']
        if 'serv_id' in d:
            o.serv_id = d['serv_id']
        if 'serv_link' in d:
            o.serv_link = d['serv_link']
        if 'serv_logo' in d:
            o.serv_logo = d['serv_logo']
        if 'serv_name' in d:
            o.serv_name = d['serv_name']
        return o


