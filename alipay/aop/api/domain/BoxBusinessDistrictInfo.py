#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BoxBusinessDistrictInfo(object):

    def __init__(self):
        self._app_name = None
        self._business_district_id = None
        self._business_district_name = None
        self._relate_appid = None
        self._service_code = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def business_district_id(self):
        return self._business_district_id

    @business_district_id.setter
    def business_district_id(self, value):
        self._business_district_id = value
    @property
    def business_district_name(self):
        return self._business_district_name

    @business_district_name.setter
    def business_district_name(self, value):
        self._business_district_name = value
    @property
    def relate_appid(self):
        return self._relate_appid

    @relate_appid.setter
    def relate_appid(self, value):
        self._relate_appid = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.business_district_id:
            if hasattr(self.business_district_id, 'to_alipay_dict'):
                params['business_district_id'] = self.business_district_id.to_alipay_dict()
            else:
                params['business_district_id'] = self.business_district_id
        if self.business_district_name:
            if hasattr(self.business_district_name, 'to_alipay_dict'):
                params['business_district_name'] = self.business_district_name.to_alipay_dict()
            else:
                params['business_district_name'] = self.business_district_name
        if self.relate_appid:
            if hasattr(self.relate_appid, 'to_alipay_dict'):
                params['relate_appid'] = self.relate_appid.to_alipay_dict()
            else:
                params['relate_appid'] = self.relate_appid
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BoxBusinessDistrictInfo()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'business_district_id' in d:
            o.business_district_id = d['business_district_id']
        if 'business_district_name' in d:
            o.business_district_name = d['business_district_name']
        if 'relate_appid' in d:
            o.relate_appid = d['relate_appid']
        if 'service_code' in d:
            o.service_code = d['service_code']
        return o


