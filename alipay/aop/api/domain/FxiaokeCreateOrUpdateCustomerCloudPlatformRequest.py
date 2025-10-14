#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FxiaokeCreateOrUpdateCustomerCloudPlatformRequest(object):

    def __init__(self):
        self._cid = None
        self._crm_code = None
        self._current_cloud_platform = None
        self._current_cloud_platform_db = None
        self._current_data_size = None
        self._current_db_consumption = None
        self._current_month_consumption_total = None
        self._life_status = None

    @property
    def cid(self):
        return self._cid

    @cid.setter
    def cid(self, value):
        self._cid = value
    @property
    def crm_code(self):
        return self._crm_code

    @crm_code.setter
    def crm_code(self, value):
        self._crm_code = value
    @property
    def current_cloud_platform(self):
        return self._current_cloud_platform

    @current_cloud_platform.setter
    def current_cloud_platform(self, value):
        self._current_cloud_platform = value
    @property
    def current_cloud_platform_db(self):
        return self._current_cloud_platform_db

    @current_cloud_platform_db.setter
    def current_cloud_platform_db(self, value):
        if isinstance(value, list):
            self._current_cloud_platform_db = list()
            for i in value:
                self._current_cloud_platform_db.append(i)
    @property
    def current_data_size(self):
        return self._current_data_size

    @current_data_size.setter
    def current_data_size(self, value):
        self._current_data_size = value
    @property
    def current_db_consumption(self):
        return self._current_db_consumption

    @current_db_consumption.setter
    def current_db_consumption(self, value):
        self._current_db_consumption = value
    @property
    def current_month_consumption_total(self):
        return self._current_month_consumption_total

    @current_month_consumption_total.setter
    def current_month_consumption_total(self, value):
        self._current_month_consumption_total = value
    @property
    def life_status(self):
        return self._life_status

    @life_status.setter
    def life_status(self, value):
        self._life_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.cid:
            if hasattr(self.cid, 'to_alipay_dict'):
                params['cid'] = self.cid.to_alipay_dict()
            else:
                params['cid'] = self.cid
        if self.crm_code:
            if hasattr(self.crm_code, 'to_alipay_dict'):
                params['crm_code'] = self.crm_code.to_alipay_dict()
            else:
                params['crm_code'] = self.crm_code
        if self.current_cloud_platform:
            if hasattr(self.current_cloud_platform, 'to_alipay_dict'):
                params['current_cloud_platform'] = self.current_cloud_platform.to_alipay_dict()
            else:
                params['current_cloud_platform'] = self.current_cloud_platform
        if self.current_cloud_platform_db:
            if isinstance(self.current_cloud_platform_db, list):
                for i in range(0, len(self.current_cloud_platform_db)):
                    element = self.current_cloud_platform_db[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.current_cloud_platform_db[i] = element.to_alipay_dict()
            if hasattr(self.current_cloud_platform_db, 'to_alipay_dict'):
                params['current_cloud_platform_db'] = self.current_cloud_platform_db.to_alipay_dict()
            else:
                params['current_cloud_platform_db'] = self.current_cloud_platform_db
        if self.current_data_size:
            if hasattr(self.current_data_size, 'to_alipay_dict'):
                params['current_data_size'] = self.current_data_size.to_alipay_dict()
            else:
                params['current_data_size'] = self.current_data_size
        if self.current_db_consumption:
            if hasattr(self.current_db_consumption, 'to_alipay_dict'):
                params['current_db_consumption'] = self.current_db_consumption.to_alipay_dict()
            else:
                params['current_db_consumption'] = self.current_db_consumption
        if self.current_month_consumption_total:
            if hasattr(self.current_month_consumption_total, 'to_alipay_dict'):
                params['current_month_consumption_total'] = self.current_month_consumption_total.to_alipay_dict()
            else:
                params['current_month_consumption_total'] = self.current_month_consumption_total
        if self.life_status:
            if hasattr(self.life_status, 'to_alipay_dict'):
                params['life_status'] = self.life_status.to_alipay_dict()
            else:
                params['life_status'] = self.life_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FxiaokeCreateOrUpdateCustomerCloudPlatformRequest()
        if 'cid' in d:
            o.cid = d['cid']
        if 'crm_code' in d:
            o.crm_code = d['crm_code']
        if 'current_cloud_platform' in d:
            o.current_cloud_platform = d['current_cloud_platform']
        if 'current_cloud_platform_db' in d:
            o.current_cloud_platform_db = d['current_cloud_platform_db']
        if 'current_data_size' in d:
            o.current_data_size = d['current_data_size']
        if 'current_db_consumption' in d:
            o.current_db_consumption = d['current_db_consumption']
        if 'current_month_consumption_total' in d:
            o.current_month_consumption_total = d['current_month_consumption_total']
        if 'life_status' in d:
            o.life_status = d['life_status']
        return o


