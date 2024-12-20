#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RainyComplexTypesTheFourth(object):

    def __init__(self):
        self._idtye_open_id = None
        self._idtype_user_id = None
        self._json_open_id_json = None
        self._json_user_id = None
        self._open_id = None
        self._tc_case = None
        self._user_id = None

    @property
    def idtye_open_id(self):
        return self._idtye_open_id

    @idtye_open_id.setter
    def idtye_open_id(self, value):
        self._idtye_open_id = value
    @property
    def idtype_user_id(self):
        return self._idtype_user_id

    @idtype_user_id.setter
    def idtype_user_id(self, value):
        self._idtype_user_id = value
    @property
    def json_open_id_json(self):
        return self._json_open_id_json

    @json_open_id_json.setter
    def json_open_id_json(self, value):
        if isinstance(value, list):
            self._json_open_id_json = list()
            for i in value:
                self._json_open_id_json.append(i)
    @property
    def json_user_id(self):
        return self._json_user_id

    @json_user_id.setter
    def json_user_id(self, value):
        if isinstance(value, list):
            self._json_user_id = list()
            for i in value:
                self._json_user_id.append(i)
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def tc_case(self):
        return self._tc_case

    @tc_case.setter
    def tc_case(self, value):
        self._tc_case = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.idtye_open_id:
            if hasattr(self.idtye_open_id, 'to_alipay_dict'):
                params['idtye_open_id'] = self.idtye_open_id.to_alipay_dict()
            else:
                params['idtye_open_id'] = self.idtye_open_id
        if self.idtype_user_id:
            if hasattr(self.idtype_user_id, 'to_alipay_dict'):
                params['idtype_user_id'] = self.idtype_user_id.to_alipay_dict()
            else:
                params['idtype_user_id'] = self.idtype_user_id
        if self.json_open_id_json:
            if isinstance(self.json_open_id_json, list):
                for i in range(0, len(self.json_open_id_json)):
                    element = self.json_open_id_json[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.json_open_id_json[i] = element.to_alipay_dict()
            if hasattr(self.json_open_id_json, 'to_alipay_dict'):
                params['json_open_id_json'] = self.json_open_id_json.to_alipay_dict()
            else:
                params['json_open_id_json'] = self.json_open_id_json
        if self.json_user_id:
            if isinstance(self.json_user_id, list):
                for i in range(0, len(self.json_user_id)):
                    element = self.json_user_id[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.json_user_id[i] = element.to_alipay_dict()
            if hasattr(self.json_user_id, 'to_alipay_dict'):
                params['json_user_id'] = self.json_user_id.to_alipay_dict()
            else:
                params['json_user_id'] = self.json_user_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.tc_case:
            if hasattr(self.tc_case, 'to_alipay_dict'):
                params['tc_case'] = self.tc_case.to_alipay_dict()
            else:
                params['tc_case'] = self.tc_case
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
        o = RainyComplexTypesTheFourth()
        if 'idtye_open_id' in d:
            o.idtye_open_id = d['idtye_open_id']
        if 'idtype_user_id' in d:
            o.idtype_user_id = d['idtype_user_id']
        if 'json_open_id_json' in d:
            o.json_open_id_json = d['json_open_id_json']
        if 'json_user_id' in d:
            o.json_user_id = d['json_user_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'tc_case' in d:
            o.tc_case = d['tc_case']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


