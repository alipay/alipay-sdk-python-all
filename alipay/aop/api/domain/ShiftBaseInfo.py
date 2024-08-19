#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShiftBaseInfo(object):

    def __init__(self):
        self._code = None
        self._nebula_user_id = None
        self._pb_end_time = None
        self._pb_start_time = None
        self._shift_type = None
        self._skill_group_id_list = None
        self._tnt_inst_id = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def nebula_user_id(self):
        return self._nebula_user_id

    @nebula_user_id.setter
    def nebula_user_id(self, value):
        self._nebula_user_id = value
    @property
    def pb_end_time(self):
        return self._pb_end_time

    @pb_end_time.setter
    def pb_end_time(self, value):
        self._pb_end_time = value
    @property
    def pb_start_time(self):
        return self._pb_start_time

    @pb_start_time.setter
    def pb_start_time(self, value):
        self._pb_start_time = value
    @property
    def shift_type(self):
        return self._shift_type

    @shift_type.setter
    def shift_type(self, value):
        self._shift_type = value
    @property
    def skill_group_id_list(self):
        return self._skill_group_id_list

    @skill_group_id_list.setter
    def skill_group_id_list(self, value):
        if isinstance(value, list):
            self._skill_group_id_list = list()
            for i in value:
                self._skill_group_id_list.append(i)
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.nebula_user_id:
            if hasattr(self.nebula_user_id, 'to_alipay_dict'):
                params['nebula_user_id'] = self.nebula_user_id.to_alipay_dict()
            else:
                params['nebula_user_id'] = self.nebula_user_id
        if self.pb_end_time:
            if hasattr(self.pb_end_time, 'to_alipay_dict'):
                params['pb_end_time'] = self.pb_end_time.to_alipay_dict()
            else:
                params['pb_end_time'] = self.pb_end_time
        if self.pb_start_time:
            if hasattr(self.pb_start_time, 'to_alipay_dict'):
                params['pb_start_time'] = self.pb_start_time.to_alipay_dict()
            else:
                params['pb_start_time'] = self.pb_start_time
        if self.shift_type:
            if hasattr(self.shift_type, 'to_alipay_dict'):
                params['shift_type'] = self.shift_type.to_alipay_dict()
            else:
                params['shift_type'] = self.shift_type
        if self.skill_group_id_list:
            if isinstance(self.skill_group_id_list, list):
                for i in range(0, len(self.skill_group_id_list)):
                    element = self.skill_group_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.skill_group_id_list[i] = element.to_alipay_dict()
            if hasattr(self.skill_group_id_list, 'to_alipay_dict'):
                params['skill_group_id_list'] = self.skill_group_id_list.to_alipay_dict()
            else:
                params['skill_group_id_list'] = self.skill_group_id_list
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShiftBaseInfo()
        if 'code' in d:
            o.code = d['code']
        if 'nebula_user_id' in d:
            o.nebula_user_id = d['nebula_user_id']
        if 'pb_end_time' in d:
            o.pb_end_time = d['pb_end_time']
        if 'pb_start_time' in d:
            o.pb_start_time = d['pb_start_time']
        if 'shift_type' in d:
            o.shift_type = d['shift_type']
        if 'skill_group_id_list' in d:
            o.skill_group_id_list = d['skill_group_id_list']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o


