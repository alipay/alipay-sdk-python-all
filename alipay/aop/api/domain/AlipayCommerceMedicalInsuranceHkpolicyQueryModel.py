#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalInsuranceHkpolicyQueryModel(object):

    def __init__(self):
        self._cert_no = None
        self._cert_type = None
        self._company_type = None
        self._hk_scene = None
        self._insured_cert_no = None
        self._insured_cert_type = None
        self._insured_name = None
        self._name = None
        self._policy_no_list = None
        self._source = None
        self._tpa_id = None
        self._user_id = None

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
    def hk_scene(self):
        return self._hk_scene

    @hk_scene.setter
    def hk_scene(self, value):
        self._hk_scene = value
    @property
    def insured_cert_no(self):
        return self._insured_cert_no

    @insured_cert_no.setter
    def insured_cert_no(self, value):
        self._insured_cert_no = value
    @property
    def insured_cert_type(self):
        return self._insured_cert_type

    @insured_cert_type.setter
    def insured_cert_type(self, value):
        self._insured_cert_type = value
    @property
    def insured_name(self):
        return self._insured_name

    @insured_name.setter
    def insured_name(self, value):
        self._insured_name = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def policy_no_list(self):
        return self._policy_no_list

    @policy_no_list.setter
    def policy_no_list(self, value):
        if isinstance(value, list):
            self._policy_no_list = list()
            for i in value:
                self._policy_no_list.append(i)
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
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


    def to_alipay_dict(self):
        params = dict()
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
        if self.hk_scene:
            if hasattr(self.hk_scene, 'to_alipay_dict'):
                params['hk_scene'] = self.hk_scene.to_alipay_dict()
            else:
                params['hk_scene'] = self.hk_scene
        if self.insured_cert_no:
            if hasattr(self.insured_cert_no, 'to_alipay_dict'):
                params['insured_cert_no'] = self.insured_cert_no.to_alipay_dict()
            else:
                params['insured_cert_no'] = self.insured_cert_no
        if self.insured_cert_type:
            if hasattr(self.insured_cert_type, 'to_alipay_dict'):
                params['insured_cert_type'] = self.insured_cert_type.to_alipay_dict()
            else:
                params['insured_cert_type'] = self.insured_cert_type
        if self.insured_name:
            if hasattr(self.insured_name, 'to_alipay_dict'):
                params['insured_name'] = self.insured_name.to_alipay_dict()
            else:
                params['insured_name'] = self.insured_name
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.policy_no_list:
            if isinstance(self.policy_no_list, list):
                for i in range(0, len(self.policy_no_list)):
                    element = self.policy_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.policy_no_list[i] = element.to_alipay_dict()
            if hasattr(self.policy_no_list, 'to_alipay_dict'):
                params['policy_no_list'] = self.policy_no_list.to_alipay_dict()
            else:
                params['policy_no_list'] = self.policy_no_list
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalInsuranceHkpolicyQueryModel()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'company_type' in d:
            o.company_type = d['company_type']
        if 'hk_scene' in d:
            o.hk_scene = d['hk_scene']
        if 'insured_cert_no' in d:
            o.insured_cert_no = d['insured_cert_no']
        if 'insured_cert_type' in d:
            o.insured_cert_type = d['insured_cert_type']
        if 'insured_name' in d:
            o.insured_name = d['insured_name']
        if 'name' in d:
            o.name = d['name']
        if 'policy_no_list' in d:
            o.policy_no_list = d['policy_no_list']
        if 'source' in d:
            o.source = d['source']
        if 'tpa_id' in d:
            o.tpa_id = d['tpa_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


