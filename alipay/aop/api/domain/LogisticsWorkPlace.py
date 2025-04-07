#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BusinessAddress import BusinessAddress


class LogisticsWorkPlace(object):

    def __init__(self):
        self._desc = None
        self._mini_app_redirect_url = None
        self._work_place_address = None
        self._work_place_id = None
        self._work_place_name = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def mini_app_redirect_url(self):
        return self._mini_app_redirect_url

    @mini_app_redirect_url.setter
    def mini_app_redirect_url(self, value):
        self._mini_app_redirect_url = value
    @property
    def work_place_address(self):
        return self._work_place_address

    @work_place_address.setter
    def work_place_address(self, value):
        if isinstance(value, BusinessAddress):
            self._work_place_address = value
        else:
            self._work_place_address = BusinessAddress.from_alipay_dict(value)
    @property
    def work_place_id(self):
        return self._work_place_id

    @work_place_id.setter
    def work_place_id(self, value):
        self._work_place_id = value
    @property
    def work_place_name(self):
        return self._work_place_name

    @work_place_name.setter
    def work_place_name(self, value):
        self._work_place_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.mini_app_redirect_url:
            if hasattr(self.mini_app_redirect_url, 'to_alipay_dict'):
                params['mini_app_redirect_url'] = self.mini_app_redirect_url.to_alipay_dict()
            else:
                params['mini_app_redirect_url'] = self.mini_app_redirect_url
        if self.work_place_address:
            if hasattr(self.work_place_address, 'to_alipay_dict'):
                params['work_place_address'] = self.work_place_address.to_alipay_dict()
            else:
                params['work_place_address'] = self.work_place_address
        if self.work_place_id:
            if hasattr(self.work_place_id, 'to_alipay_dict'):
                params['work_place_id'] = self.work_place_id.to_alipay_dict()
            else:
                params['work_place_id'] = self.work_place_id
        if self.work_place_name:
            if hasattr(self.work_place_name, 'to_alipay_dict'):
                params['work_place_name'] = self.work_place_name.to_alipay_dict()
            else:
                params['work_place_name'] = self.work_place_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LogisticsWorkPlace()
        if 'desc' in d:
            o.desc = d['desc']
        if 'mini_app_redirect_url' in d:
            o.mini_app_redirect_url = d['mini_app_redirect_url']
        if 'work_place_address' in d:
            o.work_place_address = d['work_place_address']
        if 'work_place_id' in d:
            o.work_place_id = d['work_place_id']
        if 'work_place_name' in d:
            o.work_place_name = d['work_place_name']
        return o


