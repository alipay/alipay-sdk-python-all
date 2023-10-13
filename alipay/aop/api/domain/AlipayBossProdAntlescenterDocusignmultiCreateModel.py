#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApprovalFlowInfo import ApprovalFlowInfo
from alipay.aop.api.domain.CreateESignTaskFileVO import CreateESignTaskFileVO
from alipay.aop.api.domain.ContractInformation import ContractInformation
from alipay.aop.api.domain.MultiSignerAndTabVosDTO import MultiSignerAndTabVosDTO
from alipay.aop.api.domain.CreateESignTaskFileVO import CreateESignTaskFileVO


class AlipayBossProdAntlescenterDocusignmultiCreateModel(object):

    def __init__(self):
        self._applicant = None
        self._applicant_real_name = None
        self._application_id = None
        self._application_system = None
        self._application_time = None
        self._approval_flow_info_list = None
        self._attachement_file_list = None
        self._business_line_code = None
        self._contract_id = None
        self._contract_information = None
        self._contract_version = None
        self._description = None
        self._flow_id = None
        self._hash_value = None
        self._is_test = None
        self._multi_signer_and_tab_vos_dto_list = None
        self._region_code = None
        self._scene_code = None
        self._sign_file_list = None
        self._source_sys_url = None
        self._tenant = None
        self._tnt_inst_id = None

    @property
    def applicant(self):
        return self._applicant

    @applicant.setter
    def applicant(self, value):
        self._applicant = value
    @property
    def applicant_real_name(self):
        return self._applicant_real_name

    @applicant_real_name.setter
    def applicant_real_name(self, value):
        self._applicant_real_name = value
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
                if isinstance(i, ApprovalFlowInfo):
                    self._approval_flow_info_list.append(i)
                else:
                    self._approval_flow_info_list.append(ApprovalFlowInfo.from_alipay_dict(i))
    @property
    def attachement_file_list(self):
        return self._attachement_file_list

    @attachement_file_list.setter
    def attachement_file_list(self, value):
        if isinstance(value, list):
            self._attachement_file_list = list()
            for i in value:
                if isinstance(i, CreateESignTaskFileVO):
                    self._attachement_file_list.append(i)
                else:
                    self._attachement_file_list.append(CreateESignTaskFileVO.from_alipay_dict(i))
    @property
    def business_line_code(self):
        return self._business_line_code

    @business_line_code.setter
    def business_line_code(self, value):
        self._business_line_code = value
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
        if isinstance(value, ContractInformation):
            self._contract_information = value
        else:
            self._contract_information = ContractInformation.from_alipay_dict(value)
    @property
    def contract_version(self):
        return self._contract_version

    @contract_version.setter
    def contract_version(self, value):
        self._contract_version = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def flow_id(self):
        return self._flow_id

    @flow_id.setter
    def flow_id(self, value):
        self._flow_id = value
    @property
    def hash_value(self):
        return self._hash_value

    @hash_value.setter
    def hash_value(self, value):
        self._hash_value = value
    @property
    def is_test(self):
        return self._is_test

    @is_test.setter
    def is_test(self, value):
        self._is_test = value
    @property
    def multi_signer_and_tab_vos_dto_list(self):
        return self._multi_signer_and_tab_vos_dto_list

    @multi_signer_and_tab_vos_dto_list.setter
    def multi_signer_and_tab_vos_dto_list(self, value):
        if isinstance(value, list):
            self._multi_signer_and_tab_vos_dto_list = list()
            for i in value:
                if isinstance(i, MultiSignerAndTabVosDTO):
                    self._multi_signer_and_tab_vos_dto_list.append(i)
                else:
                    self._multi_signer_and_tab_vos_dto_list.append(MultiSignerAndTabVosDTO.from_alipay_dict(i))
    @property
    def region_code(self):
        return self._region_code

    @region_code.setter
    def region_code(self, value):
        self._region_code = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
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
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value
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
        if self.applicant_real_name:
            if hasattr(self.applicant_real_name, 'to_alipay_dict'):
                params['applicant_real_name'] = self.applicant_real_name.to_alipay_dict()
            else:
                params['applicant_real_name'] = self.applicant_real_name
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
        if self.attachement_file_list:
            if isinstance(self.attachement_file_list, list):
                for i in range(0, len(self.attachement_file_list)):
                    element = self.attachement_file_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attachement_file_list[i] = element.to_alipay_dict()
            if hasattr(self.attachement_file_list, 'to_alipay_dict'):
                params['attachement_file_list'] = self.attachement_file_list.to_alipay_dict()
            else:
                params['attachement_file_list'] = self.attachement_file_list
        if self.business_line_code:
            if hasattr(self.business_line_code, 'to_alipay_dict'):
                params['business_line_code'] = self.business_line_code.to_alipay_dict()
            else:
                params['business_line_code'] = self.business_line_code
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
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.flow_id:
            if hasattr(self.flow_id, 'to_alipay_dict'):
                params['flow_id'] = self.flow_id.to_alipay_dict()
            else:
                params['flow_id'] = self.flow_id
        if self.hash_value:
            if hasattr(self.hash_value, 'to_alipay_dict'):
                params['hash_value'] = self.hash_value.to_alipay_dict()
            else:
                params['hash_value'] = self.hash_value
        if self.is_test:
            if hasattr(self.is_test, 'to_alipay_dict'):
                params['is_test'] = self.is_test.to_alipay_dict()
            else:
                params['is_test'] = self.is_test
        if self.multi_signer_and_tab_vos_dto_list:
            if isinstance(self.multi_signer_and_tab_vos_dto_list, list):
                for i in range(0, len(self.multi_signer_and_tab_vos_dto_list)):
                    element = self.multi_signer_and_tab_vos_dto_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.multi_signer_and_tab_vos_dto_list[i] = element.to_alipay_dict()
            if hasattr(self.multi_signer_and_tab_vos_dto_list, 'to_alipay_dict'):
                params['multi_signer_and_tab_vos_dto_list'] = self.multi_signer_and_tab_vos_dto_list.to_alipay_dict()
            else:
                params['multi_signer_and_tab_vos_dto_list'] = self.multi_signer_and_tab_vos_dto_list
        if self.region_code:
            if hasattr(self.region_code, 'to_alipay_dict'):
                params['region_code'] = self.region_code.to_alipay_dict()
            else:
                params['region_code'] = self.region_code
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
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
        if self.tenant:
            if hasattr(self.tenant, 'to_alipay_dict'):
                params['tenant'] = self.tenant.to_alipay_dict()
            else:
                params['tenant'] = self.tenant
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
        o = AlipayBossProdAntlescenterDocusignmultiCreateModel()
        if 'applicant' in d:
            o.applicant = d['applicant']
        if 'applicant_real_name' in d:
            o.applicant_real_name = d['applicant_real_name']
        if 'application_id' in d:
            o.application_id = d['application_id']
        if 'application_system' in d:
            o.application_system = d['application_system']
        if 'application_time' in d:
            o.application_time = d['application_time']
        if 'approval_flow_info_list' in d:
            o.approval_flow_info_list = d['approval_flow_info_list']
        if 'attachement_file_list' in d:
            o.attachement_file_list = d['attachement_file_list']
        if 'business_line_code' in d:
            o.business_line_code = d['business_line_code']
        if 'contract_id' in d:
            o.contract_id = d['contract_id']
        if 'contract_information' in d:
            o.contract_information = d['contract_information']
        if 'contract_version' in d:
            o.contract_version = d['contract_version']
        if 'description' in d:
            o.description = d['description']
        if 'flow_id' in d:
            o.flow_id = d['flow_id']
        if 'hash_value' in d:
            o.hash_value = d['hash_value']
        if 'is_test' in d:
            o.is_test = d['is_test']
        if 'multi_signer_and_tab_vos_dto_list' in d:
            o.multi_signer_and_tab_vos_dto_list = d['multi_signer_and_tab_vos_dto_list']
        if 'region_code' in d:
            o.region_code = d['region_code']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'sign_file_list' in d:
            o.sign_file_list = d['sign_file_list']
        if 'source_sys_url' in d:
            o.source_sys_url = d['source_sys_url']
        if 'tenant' in d:
            o.tenant = d['tenant']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o


