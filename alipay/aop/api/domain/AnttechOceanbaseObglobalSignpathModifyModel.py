#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbaseObglobalSignpathModifyModel(object):

    def __init__(self):
        self._alicloud_settlement_mode = None
        self._approval_status = None
        self._final_customer_sign_other_party_subject_id = None
        self._final_customer_sign_other_party_subject_name = None
        self._general_agent_cooperation_type = None
        self._leads_code = None
        self._leads_other_partners = None
        self._leads_other_partners_name = None
        self._modifier = None
        self._ob_sign_other_party_subject_id = None
        self._ob_sign_other_party_subject_name = None
        self._sign_path = None

    @property
    def alicloud_settlement_mode(self):
        return self._alicloud_settlement_mode

    @alicloud_settlement_mode.setter
    def alicloud_settlement_mode(self, value):
        self._alicloud_settlement_mode = value
    @property
    def approval_status(self):
        return self._approval_status

    @approval_status.setter
    def approval_status(self, value):
        self._approval_status = value
    @property
    def final_customer_sign_other_party_subject_id(self):
        return self._final_customer_sign_other_party_subject_id

    @final_customer_sign_other_party_subject_id.setter
    def final_customer_sign_other_party_subject_id(self, value):
        self._final_customer_sign_other_party_subject_id = value
    @property
    def final_customer_sign_other_party_subject_name(self):
        return self._final_customer_sign_other_party_subject_name

    @final_customer_sign_other_party_subject_name.setter
    def final_customer_sign_other_party_subject_name(self, value):
        self._final_customer_sign_other_party_subject_name = value
    @property
    def general_agent_cooperation_type(self):
        return self._general_agent_cooperation_type

    @general_agent_cooperation_type.setter
    def general_agent_cooperation_type(self, value):
        self._general_agent_cooperation_type = value
    @property
    def leads_code(self):
        return self._leads_code

    @leads_code.setter
    def leads_code(self, value):
        self._leads_code = value
    @property
    def leads_other_partners(self):
        return self._leads_other_partners

    @leads_other_partners.setter
    def leads_other_partners(self, value):
        self._leads_other_partners = value
    @property
    def leads_other_partners_name(self):
        return self._leads_other_partners_name

    @leads_other_partners_name.setter
    def leads_other_partners_name(self, value):
        self._leads_other_partners_name = value
    @property
    def modifier(self):
        return self._modifier

    @modifier.setter
    def modifier(self, value):
        self._modifier = value
    @property
    def ob_sign_other_party_subject_id(self):
        return self._ob_sign_other_party_subject_id

    @ob_sign_other_party_subject_id.setter
    def ob_sign_other_party_subject_id(self, value):
        self._ob_sign_other_party_subject_id = value
    @property
    def ob_sign_other_party_subject_name(self):
        return self._ob_sign_other_party_subject_name

    @ob_sign_other_party_subject_name.setter
    def ob_sign_other_party_subject_name(self, value):
        self._ob_sign_other_party_subject_name = value
    @property
    def sign_path(self):
        return self._sign_path

    @sign_path.setter
    def sign_path(self, value):
        self._sign_path = value


    def to_alipay_dict(self):
        params = dict()
        if self.alicloud_settlement_mode:
            if hasattr(self.alicloud_settlement_mode, 'to_alipay_dict'):
                params['alicloud_settlement_mode'] = self.alicloud_settlement_mode.to_alipay_dict()
            else:
                params['alicloud_settlement_mode'] = self.alicloud_settlement_mode
        if self.approval_status:
            if hasattr(self.approval_status, 'to_alipay_dict'):
                params['approval_status'] = self.approval_status.to_alipay_dict()
            else:
                params['approval_status'] = self.approval_status
        if self.final_customer_sign_other_party_subject_id:
            if hasattr(self.final_customer_sign_other_party_subject_id, 'to_alipay_dict'):
                params['final_customer_sign_other_party_subject_id'] = self.final_customer_sign_other_party_subject_id.to_alipay_dict()
            else:
                params['final_customer_sign_other_party_subject_id'] = self.final_customer_sign_other_party_subject_id
        if self.final_customer_sign_other_party_subject_name:
            if hasattr(self.final_customer_sign_other_party_subject_name, 'to_alipay_dict'):
                params['final_customer_sign_other_party_subject_name'] = self.final_customer_sign_other_party_subject_name.to_alipay_dict()
            else:
                params['final_customer_sign_other_party_subject_name'] = self.final_customer_sign_other_party_subject_name
        if self.general_agent_cooperation_type:
            if hasattr(self.general_agent_cooperation_type, 'to_alipay_dict'):
                params['general_agent_cooperation_type'] = self.general_agent_cooperation_type.to_alipay_dict()
            else:
                params['general_agent_cooperation_type'] = self.general_agent_cooperation_type
        if self.leads_code:
            if hasattr(self.leads_code, 'to_alipay_dict'):
                params['leads_code'] = self.leads_code.to_alipay_dict()
            else:
                params['leads_code'] = self.leads_code
        if self.leads_other_partners:
            if hasattr(self.leads_other_partners, 'to_alipay_dict'):
                params['leads_other_partners'] = self.leads_other_partners.to_alipay_dict()
            else:
                params['leads_other_partners'] = self.leads_other_partners
        if self.leads_other_partners_name:
            if hasattr(self.leads_other_partners_name, 'to_alipay_dict'):
                params['leads_other_partners_name'] = self.leads_other_partners_name.to_alipay_dict()
            else:
                params['leads_other_partners_name'] = self.leads_other_partners_name
        if self.modifier:
            if hasattr(self.modifier, 'to_alipay_dict'):
                params['modifier'] = self.modifier.to_alipay_dict()
            else:
                params['modifier'] = self.modifier
        if self.ob_sign_other_party_subject_id:
            if hasattr(self.ob_sign_other_party_subject_id, 'to_alipay_dict'):
                params['ob_sign_other_party_subject_id'] = self.ob_sign_other_party_subject_id.to_alipay_dict()
            else:
                params['ob_sign_other_party_subject_id'] = self.ob_sign_other_party_subject_id
        if self.ob_sign_other_party_subject_name:
            if hasattr(self.ob_sign_other_party_subject_name, 'to_alipay_dict'):
                params['ob_sign_other_party_subject_name'] = self.ob_sign_other_party_subject_name.to_alipay_dict()
            else:
                params['ob_sign_other_party_subject_name'] = self.ob_sign_other_party_subject_name
        if self.sign_path:
            if hasattr(self.sign_path, 'to_alipay_dict'):
                params['sign_path'] = self.sign_path.to_alipay_dict()
            else:
                params['sign_path'] = self.sign_path
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalSignpathModifyModel()
        if 'alicloud_settlement_mode' in d:
            o.alicloud_settlement_mode = d['alicloud_settlement_mode']
        if 'approval_status' in d:
            o.approval_status = d['approval_status']
        if 'final_customer_sign_other_party_subject_id' in d:
            o.final_customer_sign_other_party_subject_id = d['final_customer_sign_other_party_subject_id']
        if 'final_customer_sign_other_party_subject_name' in d:
            o.final_customer_sign_other_party_subject_name = d['final_customer_sign_other_party_subject_name']
        if 'general_agent_cooperation_type' in d:
            o.general_agent_cooperation_type = d['general_agent_cooperation_type']
        if 'leads_code' in d:
            o.leads_code = d['leads_code']
        if 'leads_other_partners' in d:
            o.leads_other_partners = d['leads_other_partners']
        if 'leads_other_partners_name' in d:
            o.leads_other_partners_name = d['leads_other_partners_name']
        if 'modifier' in d:
            o.modifier = d['modifier']
        if 'ob_sign_other_party_subject_id' in d:
            o.ob_sign_other_party_subject_id = d['ob_sign_other_party_subject_id']
        if 'ob_sign_other_party_subject_name' in d:
            o.ob_sign_other_party_subject_name = d['ob_sign_other_party_subject_name']
        if 'sign_path' in d:
            o.sign_path = d['sign_path']
        return o


