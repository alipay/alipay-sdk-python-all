#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AntlescenterFileDTO import AntlescenterFileDTO
from alipay.aop.api.domain.AntlescenterFileDTO import AntlescenterFileDTO
from alipay.aop.api.domain.AntlescenterProcessDTO import AntlescenterProcessDTO


class AlipayBossProdAntlescenterPartcontractInitializeModel(object):

    def __init__(self):
        self._app_name = None
        self._applicant = None
        self._applicant_sector = None
        self._application_time = None
        self._application_type = None
        self._archive_no = None
        self._archive_time = None
        self._contract_name = None
        self._contract_no = None
        self._contract_tag = None
        self._effect_end_time = None
        self._effect_start_time = None
        self._expect_time = None
        self._file_no = None
        self._nick_name = None
        self._operator_time = None
        self._operator_type = None
        self._ori_attachment_file_addr = None
        self._ori_contract_file_addr = None
        self._other_company = None
        self._our_company = None
        self._process_d_t_o = None
        self._process_source = None
        self._real_name = None
        self._seal_order = None
        self._seal_type = None
        self._sign_task_type = None
        self._source_id = None
        self._source_no = None
        self._source_url = None
        self._tenant = None
        self._work_no = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def applicant(self):
        return self._applicant

    @applicant.setter
    def applicant(self, value):
        self._applicant = value
    @property
    def applicant_sector(self):
        return self._applicant_sector

    @applicant_sector.setter
    def applicant_sector(self, value):
        self._applicant_sector = value
    @property
    def application_time(self):
        return self._application_time

    @application_time.setter
    def application_time(self, value):
        self._application_time = value
    @property
    def application_type(self):
        return self._application_type

    @application_type.setter
    def application_type(self, value):
        self._application_type = value
    @property
    def archive_no(self):
        return self._archive_no

    @archive_no.setter
    def archive_no(self, value):
        self._archive_no = value
    @property
    def archive_time(self):
        return self._archive_time

    @archive_time.setter
    def archive_time(self, value):
        self._archive_time = value
    @property
    def contract_name(self):
        return self._contract_name

    @contract_name.setter
    def contract_name(self, value):
        self._contract_name = value
    @property
    def contract_no(self):
        return self._contract_no

    @contract_no.setter
    def contract_no(self, value):
        self._contract_no = value
    @property
    def contract_tag(self):
        return self._contract_tag

    @contract_tag.setter
    def contract_tag(self, value):
        self._contract_tag = value
    @property
    def effect_end_time(self):
        return self._effect_end_time

    @effect_end_time.setter
    def effect_end_time(self, value):
        self._effect_end_time = value
    @property
    def effect_start_time(self):
        return self._effect_start_time

    @effect_start_time.setter
    def effect_start_time(self, value):
        self._effect_start_time = value
    @property
    def expect_time(self):
        return self._expect_time

    @expect_time.setter
    def expect_time(self, value):
        self._expect_time = value
    @property
    def file_no(self):
        return self._file_no

    @file_no.setter
    def file_no(self, value):
        self._file_no = value
    @property
    def nick_name(self):
        return self._nick_name

    @nick_name.setter
    def nick_name(self, value):
        self._nick_name = value
    @property
    def operator_time(self):
        return self._operator_time

    @operator_time.setter
    def operator_time(self, value):
        self._operator_time = value
    @property
    def operator_type(self):
        return self._operator_type

    @operator_type.setter
    def operator_type(self, value):
        self._operator_type = value
    @property
    def ori_attachment_file_addr(self):
        return self._ori_attachment_file_addr

    @ori_attachment_file_addr.setter
    def ori_attachment_file_addr(self, value):
        if isinstance(value, list):
            self._ori_attachment_file_addr = list()
            for i in value:
                if isinstance(i, AntlescenterFileDTO):
                    self._ori_attachment_file_addr.append(i)
                else:
                    self._ori_attachment_file_addr.append(AntlescenterFileDTO.from_alipay_dict(i))
    @property
    def ori_contract_file_addr(self):
        return self._ori_contract_file_addr

    @ori_contract_file_addr.setter
    def ori_contract_file_addr(self, value):
        if isinstance(value, list):
            self._ori_contract_file_addr = list()
            for i in value:
                if isinstance(i, AntlescenterFileDTO):
                    self._ori_contract_file_addr.append(i)
                else:
                    self._ori_contract_file_addr.append(AntlescenterFileDTO.from_alipay_dict(i))
    @property
    def other_company(self):
        return self._other_company

    @other_company.setter
    def other_company(self, value):
        self._other_company = value
    @property
    def our_company(self):
        return self._our_company

    @our_company.setter
    def our_company(self, value):
        self._our_company = value
    @property
    def process_d_t_o(self):
        return self._process_d_t_o

    @process_d_t_o.setter
    def process_d_t_o(self, value):
        if isinstance(value, AntlescenterProcessDTO):
            self._process_d_t_o = value
        else:
            self._process_d_t_o = AntlescenterProcessDTO.from_alipay_dict(value)
    @property
    def process_source(self):
        return self._process_source

    @process_source.setter
    def process_source(self, value):
        self._process_source = value
    @property
    def real_name(self):
        return self._real_name

    @real_name.setter
    def real_name(self, value):
        self._real_name = value
    @property
    def seal_order(self):
        return self._seal_order

    @seal_order.setter
    def seal_order(self, value):
        self._seal_order = value
    @property
    def seal_type(self):
        return self._seal_type

    @seal_type.setter
    def seal_type(self, value):
        self._seal_type = value
    @property
    def sign_task_type(self):
        return self._sign_task_type

    @sign_task_type.setter
    def sign_task_type(self, value):
        self._sign_task_type = value
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value
    @property
    def source_no(self):
        return self._source_no

    @source_no.setter
    def source_no(self, value):
        self._source_no = value
    @property
    def source_url(self):
        return self._source_url

    @source_url.setter
    def source_url(self, value):
        self._source_url = value
    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value
    @property
    def work_no(self):
        return self._work_no

    @work_no.setter
    def work_no(self, value):
        self._work_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.applicant:
            if hasattr(self.applicant, 'to_alipay_dict'):
                params['applicant'] = self.applicant.to_alipay_dict()
            else:
                params['applicant'] = self.applicant
        if self.applicant_sector:
            if hasattr(self.applicant_sector, 'to_alipay_dict'):
                params['applicant_sector'] = self.applicant_sector.to_alipay_dict()
            else:
                params['applicant_sector'] = self.applicant_sector
        if self.application_time:
            if hasattr(self.application_time, 'to_alipay_dict'):
                params['application_time'] = self.application_time.to_alipay_dict()
            else:
                params['application_time'] = self.application_time
        if self.application_type:
            if hasattr(self.application_type, 'to_alipay_dict'):
                params['application_type'] = self.application_type.to_alipay_dict()
            else:
                params['application_type'] = self.application_type
        if self.archive_no:
            if hasattr(self.archive_no, 'to_alipay_dict'):
                params['archive_no'] = self.archive_no.to_alipay_dict()
            else:
                params['archive_no'] = self.archive_no
        if self.archive_time:
            if hasattr(self.archive_time, 'to_alipay_dict'):
                params['archive_time'] = self.archive_time.to_alipay_dict()
            else:
                params['archive_time'] = self.archive_time
        if self.contract_name:
            if hasattr(self.contract_name, 'to_alipay_dict'):
                params['contract_name'] = self.contract_name.to_alipay_dict()
            else:
                params['contract_name'] = self.contract_name
        if self.contract_no:
            if hasattr(self.contract_no, 'to_alipay_dict'):
                params['contract_no'] = self.contract_no.to_alipay_dict()
            else:
                params['contract_no'] = self.contract_no
        if self.contract_tag:
            if hasattr(self.contract_tag, 'to_alipay_dict'):
                params['contract_tag'] = self.contract_tag.to_alipay_dict()
            else:
                params['contract_tag'] = self.contract_tag
        if self.effect_end_time:
            if hasattr(self.effect_end_time, 'to_alipay_dict'):
                params['effect_end_time'] = self.effect_end_time.to_alipay_dict()
            else:
                params['effect_end_time'] = self.effect_end_time
        if self.effect_start_time:
            if hasattr(self.effect_start_time, 'to_alipay_dict'):
                params['effect_start_time'] = self.effect_start_time.to_alipay_dict()
            else:
                params['effect_start_time'] = self.effect_start_time
        if self.expect_time:
            if hasattr(self.expect_time, 'to_alipay_dict'):
                params['expect_time'] = self.expect_time.to_alipay_dict()
            else:
                params['expect_time'] = self.expect_time
        if self.file_no:
            if hasattr(self.file_no, 'to_alipay_dict'):
                params['file_no'] = self.file_no.to_alipay_dict()
            else:
                params['file_no'] = self.file_no
        if self.nick_name:
            if hasattr(self.nick_name, 'to_alipay_dict'):
                params['nick_name'] = self.nick_name.to_alipay_dict()
            else:
                params['nick_name'] = self.nick_name
        if self.operator_time:
            if hasattr(self.operator_time, 'to_alipay_dict'):
                params['operator_time'] = self.operator_time.to_alipay_dict()
            else:
                params['operator_time'] = self.operator_time
        if self.operator_type:
            if hasattr(self.operator_type, 'to_alipay_dict'):
                params['operator_type'] = self.operator_type.to_alipay_dict()
            else:
                params['operator_type'] = self.operator_type
        if self.ori_attachment_file_addr:
            if isinstance(self.ori_attachment_file_addr, list):
                for i in range(0, len(self.ori_attachment_file_addr)):
                    element = self.ori_attachment_file_addr[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ori_attachment_file_addr[i] = element.to_alipay_dict()
            if hasattr(self.ori_attachment_file_addr, 'to_alipay_dict'):
                params['ori_attachment_file_addr'] = self.ori_attachment_file_addr.to_alipay_dict()
            else:
                params['ori_attachment_file_addr'] = self.ori_attachment_file_addr
        if self.ori_contract_file_addr:
            if isinstance(self.ori_contract_file_addr, list):
                for i in range(0, len(self.ori_contract_file_addr)):
                    element = self.ori_contract_file_addr[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ori_contract_file_addr[i] = element.to_alipay_dict()
            if hasattr(self.ori_contract_file_addr, 'to_alipay_dict'):
                params['ori_contract_file_addr'] = self.ori_contract_file_addr.to_alipay_dict()
            else:
                params['ori_contract_file_addr'] = self.ori_contract_file_addr
        if self.other_company:
            if hasattr(self.other_company, 'to_alipay_dict'):
                params['other_company'] = self.other_company.to_alipay_dict()
            else:
                params['other_company'] = self.other_company
        if self.our_company:
            if hasattr(self.our_company, 'to_alipay_dict'):
                params['our_company'] = self.our_company.to_alipay_dict()
            else:
                params['our_company'] = self.our_company
        if self.process_d_t_o:
            if hasattr(self.process_d_t_o, 'to_alipay_dict'):
                params['process_d_t_o'] = self.process_d_t_o.to_alipay_dict()
            else:
                params['process_d_t_o'] = self.process_d_t_o
        if self.process_source:
            if hasattr(self.process_source, 'to_alipay_dict'):
                params['process_source'] = self.process_source.to_alipay_dict()
            else:
                params['process_source'] = self.process_source
        if self.real_name:
            if hasattr(self.real_name, 'to_alipay_dict'):
                params['real_name'] = self.real_name.to_alipay_dict()
            else:
                params['real_name'] = self.real_name
        if self.seal_order:
            if hasattr(self.seal_order, 'to_alipay_dict'):
                params['seal_order'] = self.seal_order.to_alipay_dict()
            else:
                params['seal_order'] = self.seal_order
        if self.seal_type:
            if hasattr(self.seal_type, 'to_alipay_dict'):
                params['seal_type'] = self.seal_type.to_alipay_dict()
            else:
                params['seal_type'] = self.seal_type
        if self.sign_task_type:
            if hasattr(self.sign_task_type, 'to_alipay_dict'):
                params['sign_task_type'] = self.sign_task_type.to_alipay_dict()
            else:
                params['sign_task_type'] = self.sign_task_type
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
        if self.source_no:
            if hasattr(self.source_no, 'to_alipay_dict'):
                params['source_no'] = self.source_no.to_alipay_dict()
            else:
                params['source_no'] = self.source_no
        if self.source_url:
            if hasattr(self.source_url, 'to_alipay_dict'):
                params['source_url'] = self.source_url.to_alipay_dict()
            else:
                params['source_url'] = self.source_url
        if self.tenant:
            if hasattr(self.tenant, 'to_alipay_dict'):
                params['tenant'] = self.tenant.to_alipay_dict()
            else:
                params['tenant'] = self.tenant
        if self.work_no:
            if hasattr(self.work_no, 'to_alipay_dict'):
                params['work_no'] = self.work_no.to_alipay_dict()
            else:
                params['work_no'] = self.work_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossProdAntlescenterPartcontractInitializeModel()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'applicant' in d:
            o.applicant = d['applicant']
        if 'applicant_sector' in d:
            o.applicant_sector = d['applicant_sector']
        if 'application_time' in d:
            o.application_time = d['application_time']
        if 'application_type' in d:
            o.application_type = d['application_type']
        if 'archive_no' in d:
            o.archive_no = d['archive_no']
        if 'archive_time' in d:
            o.archive_time = d['archive_time']
        if 'contract_name' in d:
            o.contract_name = d['contract_name']
        if 'contract_no' in d:
            o.contract_no = d['contract_no']
        if 'contract_tag' in d:
            o.contract_tag = d['contract_tag']
        if 'effect_end_time' in d:
            o.effect_end_time = d['effect_end_time']
        if 'effect_start_time' in d:
            o.effect_start_time = d['effect_start_time']
        if 'expect_time' in d:
            o.expect_time = d['expect_time']
        if 'file_no' in d:
            o.file_no = d['file_no']
        if 'nick_name' in d:
            o.nick_name = d['nick_name']
        if 'operator_time' in d:
            o.operator_time = d['operator_time']
        if 'operator_type' in d:
            o.operator_type = d['operator_type']
        if 'ori_attachment_file_addr' in d:
            o.ori_attachment_file_addr = d['ori_attachment_file_addr']
        if 'ori_contract_file_addr' in d:
            o.ori_contract_file_addr = d['ori_contract_file_addr']
        if 'other_company' in d:
            o.other_company = d['other_company']
        if 'our_company' in d:
            o.our_company = d['our_company']
        if 'process_d_t_o' in d:
            o.process_d_t_o = d['process_d_t_o']
        if 'process_source' in d:
            o.process_source = d['process_source']
        if 'real_name' in d:
            o.real_name = d['real_name']
        if 'seal_order' in d:
            o.seal_order = d['seal_order']
        if 'seal_type' in d:
            o.seal_type = d['seal_type']
        if 'sign_task_type' in d:
            o.sign_task_type = d['sign_task_type']
        if 'source_id' in d:
            o.source_id = d['source_id']
        if 'source_no' in d:
            o.source_no = d['source_no']
        if 'source_url' in d:
            o.source_url = d['source_url']
        if 'tenant' in d:
            o.tenant = d['tenant']
        if 'work_no' in d:
            o.work_no = d['work_no']
        return o


