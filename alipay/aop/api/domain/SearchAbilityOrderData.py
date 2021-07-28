#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SearchAbilityOrderInfoOpenApi import SearchAbilityOrderInfoOpenApi


class SearchAbilityOrderData(object):

    def __init__(self):
        self._access_type = None
        self._app_name = None
        self._app_status = None
        self._appid = None
        self._apply_id = None
        self._apply_type = None
        self._audit_status = None
        self._biz_id = None
        self._box_status = None
        self._brand_template_id = None
        self._children = None
        self._data_key = None
        self._gmt_modified = None
        self._id = None
        self._is_old_data = None
        self._major_status = None
        self._online_time = None
        self._open_status = None
        self._operator = None
        self._reject_reason = None
        self._scene_code = None
        self._scene_name = None
        self._service_code = None
        self._sub_service_desc = None
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
    def app_status(self):
        return self._app_status

    @app_status.setter
    def app_status(self, value):
        self._app_status = value
    @property
    def appid(self):
        return self._appid

    @appid.setter
    def appid(self, value):
        self._appid = value
    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def apply_type(self):
        return self._apply_type

    @apply_type.setter
    def apply_type(self, value):
        self._apply_type = value
    @property
    def audit_status(self):
        return self._audit_status

    @audit_status.setter
    def audit_status(self, value):
        self._audit_status = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def box_status(self):
        return self._box_status

    @box_status.setter
    def box_status(self, value):
        self._box_status = value
    @property
    def brand_template_id(self):
        return self._brand_template_id

    @brand_template_id.setter
    def brand_template_id(self, value):
        self._brand_template_id = value
    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, value):
        if isinstance(value, list):
            self._children = list()
            for i in value:
                if isinstance(i, SearchAbilityOrderInfoOpenApi):
                    self._children.append(i)
                else:
                    self._children.append(SearchAbilityOrderInfoOpenApi.from_alipay_dict(i))
    @property
    def data_key(self):
        return self._data_key

    @data_key.setter
    def data_key(self, value):
        self._data_key = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def is_old_data(self):
        return self._is_old_data

    @is_old_data.setter
    def is_old_data(self, value):
        self._is_old_data = value
    @property
    def major_status(self):
        return self._major_status

    @major_status.setter
    def major_status(self, value):
        self._major_status = value
    @property
    def online_time(self):
        return self._online_time

    @online_time.setter
    def online_time(self, value):
        self._online_time = value
    @property
    def open_status(self):
        return self._open_status

    @open_status.setter
    def open_status(self, value):
        self._open_status = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value
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
    def sub_service_desc(self):
        return self._sub_service_desc

    @sub_service_desc.setter
    def sub_service_desc(self, value):
        self._sub_service_desc = value
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
        if self.app_status:
            if hasattr(self.app_status, 'to_alipay_dict'):
                params['app_status'] = self.app_status.to_alipay_dict()
            else:
                params['app_status'] = self.app_status
        if self.appid:
            if hasattr(self.appid, 'to_alipay_dict'):
                params['appid'] = self.appid.to_alipay_dict()
            else:
                params['appid'] = self.appid
        if self.apply_id:
            if hasattr(self.apply_id, 'to_alipay_dict'):
                params['apply_id'] = self.apply_id.to_alipay_dict()
            else:
                params['apply_id'] = self.apply_id
        if self.apply_type:
            if hasattr(self.apply_type, 'to_alipay_dict'):
                params['apply_type'] = self.apply_type.to_alipay_dict()
            else:
                params['apply_type'] = self.apply_type
        if self.audit_status:
            if hasattr(self.audit_status, 'to_alipay_dict'):
                params['audit_status'] = self.audit_status.to_alipay_dict()
            else:
                params['audit_status'] = self.audit_status
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.box_status:
            if hasattr(self.box_status, 'to_alipay_dict'):
                params['box_status'] = self.box_status.to_alipay_dict()
            else:
                params['box_status'] = self.box_status
        if self.brand_template_id:
            if hasattr(self.brand_template_id, 'to_alipay_dict'):
                params['brand_template_id'] = self.brand_template_id.to_alipay_dict()
            else:
                params['brand_template_id'] = self.brand_template_id
        if self.children:
            if isinstance(self.children, list):
                for i in range(0, len(self.children)):
                    element = self.children[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.children[i] = element.to_alipay_dict()
            if hasattr(self.children, 'to_alipay_dict'):
                params['children'] = self.children.to_alipay_dict()
            else:
                params['children'] = self.children
        if self.data_key:
            if hasattr(self.data_key, 'to_alipay_dict'):
                params['data_key'] = self.data_key.to_alipay_dict()
            else:
                params['data_key'] = self.data_key
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.is_old_data:
            if hasattr(self.is_old_data, 'to_alipay_dict'):
                params['is_old_data'] = self.is_old_data.to_alipay_dict()
            else:
                params['is_old_data'] = self.is_old_data
        if self.major_status:
            if hasattr(self.major_status, 'to_alipay_dict'):
                params['major_status'] = self.major_status.to_alipay_dict()
            else:
                params['major_status'] = self.major_status
        if self.online_time:
            if hasattr(self.online_time, 'to_alipay_dict'):
                params['online_time'] = self.online_time.to_alipay_dict()
            else:
                params['online_time'] = self.online_time
        if self.open_status:
            if hasattr(self.open_status, 'to_alipay_dict'):
                params['open_status'] = self.open_status.to_alipay_dict()
            else:
                params['open_status'] = self.open_status
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.reject_reason:
            if hasattr(self.reject_reason, 'to_alipay_dict'):
                params['reject_reason'] = self.reject_reason.to_alipay_dict()
            else:
                params['reject_reason'] = self.reject_reason
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
        if self.sub_service_desc:
            if hasattr(self.sub_service_desc, 'to_alipay_dict'):
                params['sub_service_desc'] = self.sub_service_desc.to_alipay_dict()
            else:
                params['sub_service_desc'] = self.sub_service_desc
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
        o = SearchAbilityOrderData()
        if 'access_type' in d:
            o.access_type = d['access_type']
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'app_status' in d:
            o.app_status = d['app_status']
        if 'appid' in d:
            o.appid = d['appid']
        if 'apply_id' in d:
            o.apply_id = d['apply_id']
        if 'apply_type' in d:
            o.apply_type = d['apply_type']
        if 'audit_status' in d:
            o.audit_status = d['audit_status']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'box_status' in d:
            o.box_status = d['box_status']
        if 'brand_template_id' in d:
            o.brand_template_id = d['brand_template_id']
        if 'children' in d:
            o.children = d['children']
        if 'data_key' in d:
            o.data_key = d['data_key']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'id' in d:
            o.id = d['id']
        if 'is_old_data' in d:
            o.is_old_data = d['is_old_data']
        if 'major_status' in d:
            o.major_status = d['major_status']
        if 'online_time' in d:
            o.online_time = d['online_time']
        if 'open_status' in d:
            o.open_status = d['open_status']
        if 'operator' in d:
            o.operator = d['operator']
        if 'reject_reason' in d:
            o.reject_reason = d['reject_reason']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'scene_name' in d:
            o.scene_name = d['scene_name']
        if 'service_code' in d:
            o.service_code = d['service_code']
        if 'sub_service_desc' in d:
            o.sub_service_desc = d['sub_service_desc']
        if 'sub_service_name' in d:
            o.sub_service_name = d['sub_service_name']
        return o


