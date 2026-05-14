#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalInsuranceTpaeventSyncModel(object):

    def __init__(self):
        self._code_value = None
        self._event_action = None
        self._ext_data = None
        self._hospital_branch_code = None
        self._hospital_branch_name = None
        self._hospital_code = None
        self._hospital_name = None
        self._individual_policy_no = None
        self._open_id = None
        self._outlet_code = None
        self._outlet_name = None
        self._outlet_type = None
        self._policy_no = None
        self._tpa_id = None
        self._user_id = None
        self._visit_date = None

    @property
    def code_value(self):
        return self._code_value

    @code_value.setter
    def code_value(self, value):
        self._code_value = value
    @property
    def event_action(self):
        return self._event_action

    @event_action.setter
    def event_action(self, value):
        self._event_action = value
    @property
    def ext_data(self):
        return self._ext_data

    @ext_data.setter
    def ext_data(self, value):
        self._ext_data = value
    @property
    def hospital_branch_code(self):
        return self._hospital_branch_code

    @hospital_branch_code.setter
    def hospital_branch_code(self, value):
        self._hospital_branch_code = value
    @property
    def hospital_branch_name(self):
        return self._hospital_branch_name

    @hospital_branch_name.setter
    def hospital_branch_name(self, value):
        self._hospital_branch_name = value
    @property
    def hospital_code(self):
        return self._hospital_code

    @hospital_code.setter
    def hospital_code(self, value):
        self._hospital_code = value
    @property
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self._hospital_name = value
    @property
    def individual_policy_no(self):
        return self._individual_policy_no

    @individual_policy_no.setter
    def individual_policy_no(self, value):
        self._individual_policy_no = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def outlet_code(self):
        return self._outlet_code

    @outlet_code.setter
    def outlet_code(self, value):
        self._outlet_code = value
    @property
    def outlet_name(self):
        return self._outlet_name

    @outlet_name.setter
    def outlet_name(self, value):
        self._outlet_name = value
    @property
    def outlet_type(self):
        return self._outlet_type

    @outlet_type.setter
    def outlet_type(self, value):
        self._outlet_type = value
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value
    @property
    def tpa_id(self):
        return self._tpa_id

    @tpa_id.setter
    def tpa_id(self, value):
        self._tpa_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def visit_date(self):
        return self._visit_date

    @visit_date.setter
    def visit_date(self, value):
        self._visit_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.code_value:
            if hasattr(self.code_value, 'to_alipay_dict'):
                params['code_value'] = self.code_value.to_alipay_dict()
            else:
                params['code_value'] = self.code_value
        if self.event_action:
            if hasattr(self.event_action, 'to_alipay_dict'):
                params['event_action'] = self.event_action.to_alipay_dict()
            else:
                params['event_action'] = self.event_action
        if self.ext_data:
            if hasattr(self.ext_data, 'to_alipay_dict'):
                params['ext_data'] = self.ext_data.to_alipay_dict()
            else:
                params['ext_data'] = self.ext_data
        if self.hospital_branch_code:
            if hasattr(self.hospital_branch_code, 'to_alipay_dict'):
                params['hospital_branch_code'] = self.hospital_branch_code.to_alipay_dict()
            else:
                params['hospital_branch_code'] = self.hospital_branch_code
        if self.hospital_branch_name:
            if hasattr(self.hospital_branch_name, 'to_alipay_dict'):
                params['hospital_branch_name'] = self.hospital_branch_name.to_alipay_dict()
            else:
                params['hospital_branch_name'] = self.hospital_branch_name
        if self.hospital_code:
            if hasattr(self.hospital_code, 'to_alipay_dict'):
                params['hospital_code'] = self.hospital_code.to_alipay_dict()
            else:
                params['hospital_code'] = self.hospital_code
        if self.hospital_name:
            if hasattr(self.hospital_name, 'to_alipay_dict'):
                params['hospital_name'] = self.hospital_name.to_alipay_dict()
            else:
                params['hospital_name'] = self.hospital_name
        if self.individual_policy_no:
            if hasattr(self.individual_policy_no, 'to_alipay_dict'):
                params['individual_policy_no'] = self.individual_policy_no.to_alipay_dict()
            else:
                params['individual_policy_no'] = self.individual_policy_no
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.outlet_code:
            if hasattr(self.outlet_code, 'to_alipay_dict'):
                params['outlet_code'] = self.outlet_code.to_alipay_dict()
            else:
                params['outlet_code'] = self.outlet_code
        if self.outlet_name:
            if hasattr(self.outlet_name, 'to_alipay_dict'):
                params['outlet_name'] = self.outlet_name.to_alipay_dict()
            else:
                params['outlet_name'] = self.outlet_name
        if self.outlet_type:
            if hasattr(self.outlet_type, 'to_alipay_dict'):
                params['outlet_type'] = self.outlet_type.to_alipay_dict()
            else:
                params['outlet_type'] = self.outlet_type
        if self.policy_no:
            if hasattr(self.policy_no, 'to_alipay_dict'):
                params['policy_no'] = self.policy_no.to_alipay_dict()
            else:
                params['policy_no'] = self.policy_no
        if self.tpa_id:
            if hasattr(self.tpa_id, 'to_alipay_dict'):
                params['tpa_id'] = self.tpa_id.to_alipay_dict()
            else:
                params['tpa_id'] = self.tpa_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.visit_date:
            if hasattr(self.visit_date, 'to_alipay_dict'):
                params['visit_date'] = self.visit_date.to_alipay_dict()
            else:
                params['visit_date'] = self.visit_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalInsuranceTpaeventSyncModel()
        if 'code_value' in d:
            o.code_value = d['code_value']
        if 'event_action' in d:
            o.event_action = d['event_action']
        if 'ext_data' in d:
            o.ext_data = d['ext_data']
        if 'hospital_branch_code' in d:
            o.hospital_branch_code = d['hospital_branch_code']
        if 'hospital_branch_name' in d:
            o.hospital_branch_name = d['hospital_branch_name']
        if 'hospital_code' in d:
            o.hospital_code = d['hospital_code']
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        if 'individual_policy_no' in d:
            o.individual_policy_no = d['individual_policy_no']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'outlet_code' in d:
            o.outlet_code = d['outlet_code']
        if 'outlet_name' in d:
            o.outlet_name = d['outlet_name']
        if 'outlet_type' in d:
            o.outlet_type = d['outlet_type']
        if 'policy_no' in d:
            o.policy_no = d['policy_no']
        if 'tpa_id' in d:
            o.tpa_id = d['tpa_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'visit_date' in d:
            o.visit_date = d['visit_date']
        return o


