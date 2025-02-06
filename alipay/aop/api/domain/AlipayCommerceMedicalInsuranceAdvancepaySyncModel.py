#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LackMaterial import LackMaterial


class AlipayCommerceMedicalInsuranceAdvancepaySyncModel(object):

    def __init__(self):
        self._advance_apply_desc = None
        self._advance_apply_no = None
        self._advance_apply_status = None
        self._ant_apply_no = None
        self._ant_policy_no = None
        self._available_advance_amount = None
        self._business_no = None
        self._business_time = None
        self._cert_no = None
        self._cert_type = None
        self._company_type = None
        self._grant_serial_no = None
        self._lack_materials = None
        self._name = None
        self._open_id = None
        self._out_hospital_id = None
        self._policy_no = None
        self._source = None
        self._status = None
        self._supplement_tag = None
        self._user_id = None

    @property
    def advance_apply_desc(self):
        return self._advance_apply_desc

    @advance_apply_desc.setter
    def advance_apply_desc(self, value):
        self._advance_apply_desc = value
    @property
    def advance_apply_no(self):
        return self._advance_apply_no

    @advance_apply_no.setter
    def advance_apply_no(self, value):
        self._advance_apply_no = value
    @property
    def advance_apply_status(self):
        return self._advance_apply_status

    @advance_apply_status.setter
    def advance_apply_status(self, value):
        self._advance_apply_status = value
    @property
    def ant_apply_no(self):
        return self._ant_apply_no

    @ant_apply_no.setter
    def ant_apply_no(self, value):
        self._ant_apply_no = value
    @property
    def ant_policy_no(self):
        return self._ant_policy_no

    @ant_policy_no.setter
    def ant_policy_no(self, value):
        self._ant_policy_no = value
    @property
    def available_advance_amount(self):
        return self._available_advance_amount

    @available_advance_amount.setter
    def available_advance_amount(self, value):
        self._available_advance_amount = value
    @property
    def business_no(self):
        return self._business_no

    @business_no.setter
    def business_no(self, value):
        self._business_no = value
    @property
    def business_time(self):
        return self._business_time

    @business_time.setter
    def business_time(self, value):
        self._business_time = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def company_type(self):
        return self._company_type

    @company_type.setter
    def company_type(self, value):
        self._company_type = value
    @property
    def grant_serial_no(self):
        return self._grant_serial_no

    @grant_serial_no.setter
    def grant_serial_no(self, value):
        self._grant_serial_no = value
    @property
    def lack_materials(self):
        return self._lack_materials

    @lack_materials.setter
    def lack_materials(self, value):
        if isinstance(value, list):
            self._lack_materials = list()
            for i in value:
                if isinstance(i, LackMaterial):
                    self._lack_materials.append(i)
                else:
                    self._lack_materials.append(LackMaterial.from_alipay_dict(i))
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_hospital_id(self):
        return self._out_hospital_id

    @out_hospital_id.setter
    def out_hospital_id(self, value):
        self._out_hospital_id = value
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def supplement_tag(self):
        return self._supplement_tag

    @supplement_tag.setter
    def supplement_tag(self, value):
        self._supplement_tag = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.advance_apply_desc:
            if hasattr(self.advance_apply_desc, 'to_alipay_dict'):
                params['advance_apply_desc'] = self.advance_apply_desc.to_alipay_dict()
            else:
                params['advance_apply_desc'] = self.advance_apply_desc
        if self.advance_apply_no:
            if hasattr(self.advance_apply_no, 'to_alipay_dict'):
                params['advance_apply_no'] = self.advance_apply_no.to_alipay_dict()
            else:
                params['advance_apply_no'] = self.advance_apply_no
        if self.advance_apply_status:
            if hasattr(self.advance_apply_status, 'to_alipay_dict'):
                params['advance_apply_status'] = self.advance_apply_status.to_alipay_dict()
            else:
                params['advance_apply_status'] = self.advance_apply_status
        if self.ant_apply_no:
            if hasattr(self.ant_apply_no, 'to_alipay_dict'):
                params['ant_apply_no'] = self.ant_apply_no.to_alipay_dict()
            else:
                params['ant_apply_no'] = self.ant_apply_no
        if self.ant_policy_no:
            if hasattr(self.ant_policy_no, 'to_alipay_dict'):
                params['ant_policy_no'] = self.ant_policy_no.to_alipay_dict()
            else:
                params['ant_policy_no'] = self.ant_policy_no
        if self.available_advance_amount:
            if hasattr(self.available_advance_amount, 'to_alipay_dict'):
                params['available_advance_amount'] = self.available_advance_amount.to_alipay_dict()
            else:
                params['available_advance_amount'] = self.available_advance_amount
        if self.business_no:
            if hasattr(self.business_no, 'to_alipay_dict'):
                params['business_no'] = self.business_no.to_alipay_dict()
            else:
                params['business_no'] = self.business_no
        if self.business_time:
            if hasattr(self.business_time, 'to_alipay_dict'):
                params['business_time'] = self.business_time.to_alipay_dict()
            else:
                params['business_time'] = self.business_time
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.company_type:
            if hasattr(self.company_type, 'to_alipay_dict'):
                params['company_type'] = self.company_type.to_alipay_dict()
            else:
                params['company_type'] = self.company_type
        if self.grant_serial_no:
            if hasattr(self.grant_serial_no, 'to_alipay_dict'):
                params['grant_serial_no'] = self.grant_serial_no.to_alipay_dict()
            else:
                params['grant_serial_no'] = self.grant_serial_no
        if self.lack_materials:
            if isinstance(self.lack_materials, list):
                for i in range(0, len(self.lack_materials)):
                    element = self.lack_materials[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.lack_materials[i] = element.to_alipay_dict()
            if hasattr(self.lack_materials, 'to_alipay_dict'):
                params['lack_materials'] = self.lack_materials.to_alipay_dict()
            else:
                params['lack_materials'] = self.lack_materials
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_hospital_id:
            if hasattr(self.out_hospital_id, 'to_alipay_dict'):
                params['out_hospital_id'] = self.out_hospital_id.to_alipay_dict()
            else:
                params['out_hospital_id'] = self.out_hospital_id
        if self.policy_no:
            if hasattr(self.policy_no, 'to_alipay_dict'):
                params['policy_no'] = self.policy_no.to_alipay_dict()
            else:
                params['policy_no'] = self.policy_no
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.supplement_tag:
            if hasattr(self.supplement_tag, 'to_alipay_dict'):
                params['supplement_tag'] = self.supplement_tag.to_alipay_dict()
            else:
                params['supplement_tag'] = self.supplement_tag
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
        o = AlipayCommerceMedicalInsuranceAdvancepaySyncModel()
        if 'advance_apply_desc' in d:
            o.advance_apply_desc = d['advance_apply_desc']
        if 'advance_apply_no' in d:
            o.advance_apply_no = d['advance_apply_no']
        if 'advance_apply_status' in d:
            o.advance_apply_status = d['advance_apply_status']
        if 'ant_apply_no' in d:
            o.ant_apply_no = d['ant_apply_no']
        if 'ant_policy_no' in d:
            o.ant_policy_no = d['ant_policy_no']
        if 'available_advance_amount' in d:
            o.available_advance_amount = d['available_advance_amount']
        if 'business_no' in d:
            o.business_no = d['business_no']
        if 'business_time' in d:
            o.business_time = d['business_time']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'company_type' in d:
            o.company_type = d['company_type']
        if 'grant_serial_no' in d:
            o.grant_serial_no = d['grant_serial_no']
        if 'lack_materials' in d:
            o.lack_materials = d['lack_materials']
        if 'name' in d:
            o.name = d['name']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_hospital_id' in d:
            o.out_hospital_id = d['out_hospital_id']
        if 'policy_no' in d:
            o.policy_no = d['policy_no']
        if 'source' in d:
            o.source = d['source']
        if 'status' in d:
            o.status = d['status']
        if 'supplement_tag' in d:
            o.supplement_tag = d['supplement_tag']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


