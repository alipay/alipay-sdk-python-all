#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SearchPartAgreeInfo import SearchPartAgreeInfo


class ApplyOrderData(object):

    def __init__(self):
        self._access_type = None
        self._app_name = None
        self._appid = None
        self._audit_reason = None
        self._brand_template_id = None
        self._create_time = None
        self._is_old_data = None
        self._latest = None
        self._major_status = None
        self._order_id = None
        self._part_agree_info = None
        self._scene_code = None
        self._scene_name = None
        self._service_code = None
        self._status = None
        self._sub_service_name = None

    @property
    def access_type(self):
        return self._access_type

    @access_type.setter
    def access_type(self, value):
        self._access_type = value
    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def appid(self):
        return self._appid

    @appid.setter
    def appid(self, value):
        self._appid = value
    @property
    def audit_reason(self):
        return self._audit_reason

    @audit_reason.setter
    def audit_reason(self, value):
        self._audit_reason = value
    @property
    def brand_template_id(self):
        return self._brand_template_id

    @brand_template_id.setter
    def brand_template_id(self, value):
        self._brand_template_id = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def is_old_data(self):
        return self._is_old_data

    @is_old_data.setter
    def is_old_data(self, value):
        self._is_old_data = value
    @property
    def latest(self):
        return self._latest

    @latest.setter
    def latest(self, value):
        self._latest = value
    @property
    def major_status(self):
        return self._major_status

    @major_status.setter
    def major_status(self, value):
        self._major_status = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def part_agree_info(self):
        return self._part_agree_info

    @part_agree_info.setter
    def part_agree_info(self, value):
        if isinstance(value, list):
            self._part_agree_info = list()
            for i in value:
                if isinstance(i, SearchPartAgreeInfo):
                    self._part_agree_info.append(i)
                else:
                    self._part_agree_info.append(SearchPartAgreeInfo.from_alipay_dict(i))
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def scene_name(self):
        return self._scene_name

    @scene_name.setter
    def scene_name(self, value):
        self._scene_name = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_service_name(self):
        return self._sub_service_name

    @sub_service_name.setter
    def sub_service_name(self, value):
        self._sub_service_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_type:
            if hasattr(self.access_type, 'to_alipay_dict'):
                params['access_type'] = self.access_type.to_alipay_dict()
            else:
                params['access_type'] = self.access_type
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.appid:
            if hasattr(self.appid, 'to_alipay_dict'):
                params['appid'] = self.appid.to_alipay_dict()
            else:
                params['appid'] = self.appid
        if self.audit_reason:
            if hasattr(self.audit_reason, 'to_alipay_dict'):
                params['audit_reason'] = self.audit_reason.to_alipay_dict()
            else:
                params['audit_reason'] = self.audit_reason
        if self.brand_template_id:
            if hasattr(self.brand_template_id, 'to_alipay_dict'):
                params['brand_template_id'] = self.brand_template_id.to_alipay_dict()
            else:
                params['brand_template_id'] = self.brand_template_id
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.is_old_data:
            if hasattr(self.is_old_data, 'to_alipay_dict'):
                params['is_old_data'] = self.is_old_data.to_alipay_dict()
            else:
                params['is_old_data'] = self.is_old_data
        if self.latest:
            if hasattr(self.latest, 'to_alipay_dict'):
                params['latest'] = self.latest.to_alipay_dict()
            else:
                params['latest'] = self.latest
        if self.major_status:
            if hasattr(self.major_status, 'to_alipay_dict'):
                params['major_status'] = self.major_status.to_alipay_dict()
            else:
                params['major_status'] = self.major_status
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.part_agree_info:
            if isinstance(self.part_agree_info, list):
                for i in range(0, len(self.part_agree_info)):
                    element = self.part_agree_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.part_agree_info[i] = element.to_alipay_dict()
            if hasattr(self.part_agree_info, 'to_alipay_dict'):
                params['part_agree_info'] = self.part_agree_info.to_alipay_dict()
            else:
                params['part_agree_info'] = self.part_agree_info
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.scene_name:
            if hasattr(self.scene_name, 'to_alipay_dict'):
                params['scene_name'] = self.scene_name.to_alipay_dict()
            else:
                params['scene_name'] = self.scene_name
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.sub_service_name:
            if hasattr(self.sub_service_name, 'to_alipay_dict'):
                params['sub_service_name'] = self.sub_service_name.to_alipay_dict()
            else:
                params['sub_service_name'] = self.sub_service_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApplyOrderData()
        if 'access_type' in d:
            o.access_type = d['access_type']
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'appid' in d:
            o.appid = d['appid']
        if 'audit_reason' in d:
            o.audit_reason = d['audit_reason']
        if 'brand_template_id' in d:
            o.brand_template_id = d['brand_template_id']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'is_old_data' in d:
            o.is_old_data = d['is_old_data']
        if 'latest' in d:
            o.latest = d['latest']
        if 'major_status' in d:
            o.major_status = d['major_status']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'part_agree_info' in d:
            o.part_agree_info = d['part_agree_info']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'scene_name' in d:
            o.scene_name = d['scene_name']
        if 'service_code' in d:
            o.service_code = d['service_code']
        if 'status' in d:
            o.status = d['status']
        if 'sub_service_name' in d:
            o.sub_service_name = d['sub_service_name']
        return o


