#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApprovalFlowInfoDTO import ApprovalFlowInfoDTO
from alipay.aop.api.domain.ContractInformationVo import ContractInformationVo
from alipay.aop.api.domain.CreateESignTaskFileVO import CreateESignTaskFileVO


class AlipayBossProdAntlescenterDocusignApplyModel(object):

    def __init__(self):
        self._applicant = None
        self._application_id = None
        self._application_system = None
        self._application_time = None
        self._approval_flow_info_list = None
        self._contract_id = None
        self._contract_information = None
        self._contract_version = None
        self._hash_value = None
        self._ip_role_id = None
        self._region_code = None
        self._sign_file_list = None
        self._source_sys_url = None
        self._tnt_inst_id = None

    @property
    def applicant(self):
        return self._applicant

    @applicant.setter
    def applicant(self, value):
        self._applicant = value
    @property
    def application_id(self):
        return self._application_id

    @application_id.setter
    def application_id(self, value):
        self._application_id = value
    @property
    def application_system(self):
        return self._application_system

    @application_system.setter
    def application_system(self, value):
        self._application_system = value
    @property
    def application_time(self):
        return self._application_time

    @application_time.setter
    def application_time(self, value):
        self._application_time = value
    @property
    def approval_flow_info_list(self):
        return self._approval_flow_info_list

    @approval_flow_info_list.setter
    def approval_flow_info_list(self, value):
        if isinstance(value, list):
            self._approval_flow_info_list = list()
            for i in value:
                if isinstance(i, ApprovalFlowInfoDTO):
                    self._approval_flow_info_list.append(i)
                else:
                    self._approval_flow_info_list.append(ApprovalFlowInfoDTO.from_alipay_dict(i))
    @property
    def contract_id(self):
        return self._contract_id

    @contract_id.setter
    def contract_id(self, value):
        self._contract_id = value
    @property
    def contract_information(self):
        return self._contract_information

    @contract_information.setter
    def contract_information(self, value):
        if isinstance(value, ContractInformationVo):
            self._contract_information = value
        else:
            self._contract_information = ContractInformationVo.from_alipay_dict(value)
    @property
    def contract_version(self):
        return self._contract_version

    @contract_version.setter
    def contract_version(self, value):
        self._contract_version = value
    @property
    def hash_value(self):
        return self._hash_value

    @hash_value.setter
    def hash_value(self, value):
        self._hash_value = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def region_code(self):
        return self._region_code

    @region_code.setter
    def region_code(self, value):
        self._region_code = value
    @property
    def sign_file_list(self):
        return self._sign_file_list

    @sign_file_list.setter
    def sign_file_list(self, value):
        if isinstance(value, list):
            self._sign_file_list = list()
            for i in value:
                if isinstance(i, CreateESignTaskFileVO):
                    self._sign_file_list.append(i)
                else:
                    self._sign_file_list.append(CreateESignTaskFileVO.from_alipay_dict(i))
    @property
    def source_sys_url(self):
        return self._source_sys_url

    @source_sys_url.setter
    def source_sys_url(self, value):
        self._source_sys_url = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.applicant:
            if hasattr(self.applicant, 'to_alipay_dict'):
                params['applicant'] = self.applicant.to_alipay_dict()
            else:
                params['applicant'] = self.applicant
        if self.application_id:
            if hasattr(self.application_id, 'to_alipay_dict'):
                params['application_id'] = self.application_id.to_alipay_dict()
            else:
                params['application_id'] = self.application_id
        if self.application_system:
            if hasattr(self.application_system, 'to_alipay_dict'):
                params['application_system'] = self.application_system.to_alipay_dict()
            else:
                params['application_system'] = self.application_system
        if self.application_time:
            if hasattr(self.application_time, 'to_alipay_dict'):
                params['application_time'] = self.application_time.to_alipay_dict()
            else:
                params['application_time'] = self.application_time
        if self.approval_flow_info_list:
            if isinstance(self.approval_flow_info_list, list):
                for i in range(0, len(self.approval_flow_info_list)):
                    element = self.approval_flow_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.approval_flow_info_list[i] = element.to_alipay_dict()
            if hasattr(self.approval_flow_info_list, 'to_alipay_dict'):
                params['approval_flow_info_list'] = self.approval_flow_info_list.to_alipay_dict()
            else:
                params['approval_flow_info_list'] = self.approval_flow_info_list
        if self.contract_id:
            if hasattr(self.contract_id, 'to_alipay_dict'):
                params['contract_id'] = self.contract_id.to_alipay_dict()
            else:
                params['contract_id'] = self.contract_id
        if self.contract_information:
            if hasattr(self.contract_information, 'to_alipay_dict'):
                params['contract_information'] = self.contract_information.to_alipay_dict()
            else:
                params['contract_information'] = self.contract_information
        if self.contract_version:
            if hasattr(self.contract_version, 'to_alipay_dict'):
                params['contract_version'] = self.contract_version.to_alipay_dict()
            else:
                params['contract_version'] = self.contract_version
        if self.hash_value:
            if hasattr(self.hash_value, 'to_alipay_dict'):
                params['hash_value'] = self.hash_value.to_alipay_dict()
            else:
                params['hash_value'] = self.hash_value
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.region_code:
            if hasattr(self.region_code, 'to_alipay_dict'):
                params['region_code'] = self.region_code.to_alipay_dict()
            else:
                params['region_code'] = self.region_code
        if self.sign_file_list:
            if isinstance(self.sign_file_list, list):
                for i in range(0, len(self.sign_file_list)):
                    element = self.sign_file_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sign_file_list[i] = element.to_alipay_dict()
            if hasattr(self.sign_file_list, 'to_alipay_dict'):
                params['sign_file_list'] = self.sign_file_list.to_alipay_dict()
            else:
                params['sign_file_list'] = self.sign_file_list
        if self.source_sys_url:
            if hasattr(self.source_sys_url, 'to_alipay_dict'):
                params['source_sys_url'] = self.source_sys_url.to_alipay_dict()
            else:
                params['source_sys_url'] = self.source_sys_url
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
        o = AlipayBossProdAntlescenterDocusignApplyModel()
        if 'applicant' in d:
            o.applicant = d['applicant']
        if 'application_id' in d:
            o.application_id = d['application_id']
        if 'application_system' in d:
            o.application_system = d['application_system']
        if 'application_time' in d:
            o.application_time = d['application_time']
        if 'approval_flow_info_list' in d:
            o.approval_flow_info_list = d['approval_flow_info_list']
        if 'contract_id' in d:
            o.contract_id = d['contract_id']
        if 'contract_information' in d:
            o.contract_information = d['contract_information']
        if 'contract_version' in d:
            o.contract_version = d['contract_version']
        if 'hash_value' in d:
            o.hash_value = d['hash_value']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'region_code' in d:
            o.region_code = d['region_code']
        if 'sign_file_list' in d:
            o.sign_file_list = d['sign_file_list']
        if 'source_sys_url' in d:
            o.source_sys_url = d['source_sys_url']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o


