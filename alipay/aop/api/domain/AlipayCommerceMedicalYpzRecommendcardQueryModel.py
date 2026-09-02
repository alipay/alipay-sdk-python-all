#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalYpzRecommendcardQueryModel(object):

    def __init__(self):
        self._biz_id = None
        self._card_code = None
        self._case_details_url = None
        self._ch_info = None
        self._config_id = None
        self._delivery_scene = None
        self._department_name = None
        self._doctor_name = None
        self._hos_code = None
        self._hospital_name = None
        self._isv_code = None
        self._mini_app_id = None
        self._open_id = None
        self._org_id = None
        self._org_name = None
        self._patient_id = None
        self._scene_code = None
        self._self = None
        self._status_card_code = None
        self._table_type = None
        self._uscc = None
        self._user_id = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def card_code(self):
        return self._card_code

    @card_code.setter
    def card_code(self, value):
        self._card_code = value
    @property
    def case_details_url(self):
        return self._case_details_url

    @case_details_url.setter
    def case_details_url(self, value):
        self._case_details_url = value
    @property
    def ch_info(self):
        return self._ch_info

    @ch_info.setter
    def ch_info(self, value):
        self._ch_info = value
    @property
    def config_id(self):
        return self._config_id

    @config_id.setter
    def config_id(self, value):
        self._config_id = value
    @property
    def delivery_scene(self):
        return self._delivery_scene

    @delivery_scene.setter
    def delivery_scene(self, value):
        self._delivery_scene = value
    @property
    def department_name(self):
        return self._department_name

    @department_name.setter
    def department_name(self, value):
        self._department_name = value
    @property
    def doctor_name(self):
        return self._doctor_name

    @doctor_name.setter
    def doctor_name(self, value):
        self._doctor_name = value
    @property
    def hos_code(self):
        return self._hos_code

    @hos_code.setter
    def hos_code(self, value):
        self._hos_code = value
    @property
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self._hospital_name = value
    @property
    def isv_code(self):
        return self._isv_code

    @isv_code.setter
    def isv_code(self, value):
        self._isv_code = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def org_id(self):
        return self._org_id

    @org_id.setter
    def org_id(self, value):
        self._org_id = value
    @property
    def org_name(self):
        return self._org_name

    @org_name.setter
    def org_name(self, value):
        self._org_name = value
    @property
    def patient_id(self):
        return self._patient_id

    @patient_id.setter
    def patient_id(self, value):
        self._patient_id = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def self(self):
        return self._self

    @self.setter
    def self(self, value):
        self._self = value
    @property
    def status_card_code(self):
        return self._status_card_code

    @status_card_code.setter
    def status_card_code(self, value):
        self._status_card_code = value
    @property
    def table_type(self):
        return self._table_type

    @table_type.setter
    def table_type(self, value):
        self._table_type = value
    @property
    def uscc(self):
        return self._uscc

    @uscc.setter
    def uscc(self, value):
        self._uscc = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.card_code:
            if hasattr(self.card_code, 'to_alipay_dict'):
                params['card_code'] = self.card_code.to_alipay_dict()
            else:
                params['card_code'] = self.card_code
        if self.case_details_url:
            if hasattr(self.case_details_url, 'to_alipay_dict'):
                params['case_details_url'] = self.case_details_url.to_alipay_dict()
            else:
                params['case_details_url'] = self.case_details_url
        if self.ch_info:
            if hasattr(self.ch_info, 'to_alipay_dict'):
                params['ch_info'] = self.ch_info.to_alipay_dict()
            else:
                params['ch_info'] = self.ch_info
        if self.config_id:
            if hasattr(self.config_id, 'to_alipay_dict'):
                params['config_id'] = self.config_id.to_alipay_dict()
            else:
                params['config_id'] = self.config_id
        if self.delivery_scene:
            if hasattr(self.delivery_scene, 'to_alipay_dict'):
                params['delivery_scene'] = self.delivery_scene.to_alipay_dict()
            else:
                params['delivery_scene'] = self.delivery_scene
        if self.department_name:
            if hasattr(self.department_name, 'to_alipay_dict'):
                params['department_name'] = self.department_name.to_alipay_dict()
            else:
                params['department_name'] = self.department_name
        if self.doctor_name:
            if hasattr(self.doctor_name, 'to_alipay_dict'):
                params['doctor_name'] = self.doctor_name.to_alipay_dict()
            else:
                params['doctor_name'] = self.doctor_name
        if self.hos_code:
            if hasattr(self.hos_code, 'to_alipay_dict'):
                params['hos_code'] = self.hos_code.to_alipay_dict()
            else:
                params['hos_code'] = self.hos_code
        if self.hospital_name:
            if hasattr(self.hospital_name, 'to_alipay_dict'):
                params['hospital_name'] = self.hospital_name.to_alipay_dict()
            else:
                params['hospital_name'] = self.hospital_name
        if self.isv_code:
            if hasattr(self.isv_code, 'to_alipay_dict'):
                params['isv_code'] = self.isv_code.to_alipay_dict()
            else:
                params['isv_code'] = self.isv_code
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.org_id:
            if hasattr(self.org_id, 'to_alipay_dict'):
                params['org_id'] = self.org_id.to_alipay_dict()
            else:
                params['org_id'] = self.org_id
        if self.org_name:
            if hasattr(self.org_name, 'to_alipay_dict'):
                params['org_name'] = self.org_name.to_alipay_dict()
            else:
                params['org_name'] = self.org_name
        if self.patient_id:
            if hasattr(self.patient_id, 'to_alipay_dict'):
                params['patient_id'] = self.patient_id.to_alipay_dict()
            else:
                params['patient_id'] = self.patient_id
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.self:
            if hasattr(self.self, 'to_alipay_dict'):
                params['self'] = self.self.to_alipay_dict()
            else:
                params['self'] = self.self
        if self.status_card_code:
            if hasattr(self.status_card_code, 'to_alipay_dict'):
                params['status_card_code'] = self.status_card_code.to_alipay_dict()
            else:
                params['status_card_code'] = self.status_card_code
        if self.table_type:
            if hasattr(self.table_type, 'to_alipay_dict'):
                params['table_type'] = self.table_type.to_alipay_dict()
            else:
                params['table_type'] = self.table_type
        if self.uscc:
            if hasattr(self.uscc, 'to_alipay_dict'):
                params['uscc'] = self.uscc.to_alipay_dict()
            else:
                params['uscc'] = self.uscc
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalYpzRecommendcardQueryModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'card_code' in d:
            o.card_code = d['card_code']
        if 'case_details_url' in d:
            o.case_details_url = d['case_details_url']
        if 'ch_info' in d:
            o.ch_info = d['ch_info']
        if 'config_id' in d:
            o.config_id = d['config_id']
        if 'delivery_scene' in d:
            o.delivery_scene = d['delivery_scene']
        if 'department_name' in d:
            o.department_name = d['department_name']
        if 'doctor_name' in d:
            o.doctor_name = d['doctor_name']
        if 'hos_code' in d:
            o.hos_code = d['hos_code']
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        if 'isv_code' in d:
            o.isv_code = d['isv_code']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'org_id' in d:
            o.org_id = d['org_id']
        if 'org_name' in d:
            o.org_name = d['org_name']
        if 'patient_id' in d:
            o.patient_id = d['patient_id']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'self' in d:
            o.self = d['self']
        if 'status_card_code' in d:
            o.status_card_code = d['status_card_code']
        if 'table_type' in d:
            o.table_type = d['table_type']
        if 'uscc' in d:
            o.uscc = d['uscc']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


