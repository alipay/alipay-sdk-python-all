#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CreateESignTaskFileVO import CreateESignTaskFileVO
from alipay.aop.api.domain.CreateESignTaskFileVO import CreateESignTaskFileVO
from alipay.aop.api.domain.CreateESignTaskFileVO import CreateESignTaskFileVO
from alipay.aop.api.domain.RecipientSignStatusResultVo import RecipientSignStatusResultVo


class AlipayBossProdAntlescenterDocusignresultQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossProdAntlescenterDocusignresultQueryResponse, self).__init__()
        self._application_id = None
        self._application_system = None
        self._business_line_code = None
        self._combined_file_vo = None
        self._contract_id = None
        self._create_e_sign_task_file_vo = None
        self._fail_info = None
        self._scene_code = None
        self._sign_file_list = None
        self._sign_task_id = None
        self._signer_dto = None
        self._status = None
        self._tenant = None

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
    def business_line_code(self):
        return self._business_line_code

    @business_line_code.setter
    def business_line_code(self, value):
        self._business_line_code = value
    @property
    def combined_file_vo(self):
        return self._combined_file_vo

    @combined_file_vo.setter
    def combined_file_vo(self, value):
        if isinstance(value, CreateESignTaskFileVO):
            self._combined_file_vo = value
        else:
            self._combined_file_vo = CreateESignTaskFileVO.from_alipay_dict(value)
    @property
    def contract_id(self):
        return self._contract_id

    @contract_id.setter
    def contract_id(self, value):
        self._contract_id = value
    @property
    def create_e_sign_task_file_vo(self):
        return self._create_e_sign_task_file_vo

    @create_e_sign_task_file_vo.setter
    def create_e_sign_task_file_vo(self, value):
        if isinstance(value, CreateESignTaskFileVO):
            self._create_e_sign_task_file_vo = value
        else:
            self._create_e_sign_task_file_vo = CreateESignTaskFileVO.from_alipay_dict(value)
    @property
    def fail_info(self):
        return self._fail_info

    @fail_info.setter
    def fail_info(self, value):
        self._fail_info = value
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
    def sign_task_id(self):
        return self._sign_task_id

    @sign_task_id.setter
    def sign_task_id(self, value):
        self._sign_task_id = value
    @property
    def signer_dto(self):
        return self._signer_dto

    @signer_dto.setter
    def signer_dto(self, value):
        if isinstance(value, list):
            self._signer_dto = list()
            for i in value:
                if isinstance(i, RecipientSignStatusResultVo):
                    self._signer_dto.append(i)
                else:
                    self._signer_dto.append(RecipientSignStatusResultVo.from_alipay_dict(i))
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossProdAntlescenterDocusignresultQueryResponse, self).parse_response_content(response_content)
        if 'application_id' in response:
            self.application_id = response['application_id']
        if 'application_system' in response:
            self.application_system = response['application_system']
        if 'business_line_code' in response:
            self.business_line_code = response['business_line_code']
        if 'combined_file_vo' in response:
            self.combined_file_vo = response['combined_file_vo']
        if 'contract_id' in response:
            self.contract_id = response['contract_id']
        if 'create_e_sign_task_file_vo' in response:
            self.create_e_sign_task_file_vo = response['create_e_sign_task_file_vo']
        if 'fail_info' in response:
            self.fail_info = response['fail_info']
        if 'scene_code' in response:
            self.scene_code = response['scene_code']
        if 'sign_file_list' in response:
            self.sign_file_list = response['sign_file_list']
        if 'sign_task_id' in response:
            self.sign_task_id = response['sign_task_id']
        if 'signer_dto' in response:
            self.signer_dto = response['signer_dto']
        if 'status' in response:
            self.status = response['status']
        if 'tenant' in response:
            self.tenant = response['tenant']
