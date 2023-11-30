#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenApiPersonSaDTO import OpenApiPersonSaDTO
from alipay.aop.api.domain.OpenApiCommentDTO import OpenApiCommentDTO
from alipay.aop.api.domain.OpenApiContractFileSaDTO import OpenApiContractFileSaDTO
from alipay.aop.api.domain.OpenApiContractCoordinatorDTO import OpenApiContractCoordinatorDTO
from alipay.aop.api.domain.OpenApiContractFileSaDTO import OpenApiContractFileSaDTO
from alipay.aop.api.domain.OpenApiContractFileDTO import OpenApiContractFileDTO
from alipay.aop.api.domain.OpenApiPartnerSaDTO import OpenApiPartnerSaDTO
from alipay.aop.api.domain.OpenApiPartnerSaDTO import OpenApiPartnerSaDTO
from alipay.aop.api.domain.OpenApiPersonSaDTO import OpenApiPersonSaDTO
from alipay.aop.api.domain.OpenApiPersonSaDTO import OpenApiPersonSaDTO
from alipay.aop.api.domain.OpenApiContractFileDTO import OpenApiContractFileDTO
from alipay.aop.api.domain.OpenApiMatterCommentDTO import OpenApiMatterCommentDTO
from alipay.aop.api.domain.OpenApiPersonSaDTO import OpenApiPersonSaDTO
from alipay.aop.api.domain.OpenApiRelateMatterDTO import OpenApiRelateMatterDTO


class OpenApiContractMatterDetailDTO(object):

    def __init__(self):
        self._applicant = None
        self._apply_end_time = None
        self._apply_start_time = None
        self._biz_status = None
        self._business_id = None
        self._business_line = None
        self._comment = None
        self._confirm_comment_list = None
        self._contract_attach_list = None
        self._contract_code = None
        self._contract_coordinator_list = None
        self._contract_create_time = None
        self._contract_doc_list = None
        self._contract_file_results = None
        self._contract_name = None
        self._contract_partner_a_dto_list = None
        self._contract_partner_b_dto_list = None
        self._contract_sign_type = None
        self._contract_template_code = None
        self._detail_url = None
        self._effect_time = None
        self._expire_time = None
        self._finance_people = None
        self._is_template = None
        self._legal_people = None
        self._matter_attachment_results = None
        self._matter_code = None
        self._matter_comment_list = None
        self._number = None
        self._origin_biz_status = None
        self._owners = None
        self._relate_matter_list = None
        self._show_biz_status = None
        self._source_system_id = None
        self._tenant = None

    @property
    def applicant(self):
        return self._applicant

    @applicant.setter
    def applicant(self, value):
        if isinstance(value, OpenApiPersonSaDTO):
            self._applicant = value
        else:
            self._applicant = OpenApiPersonSaDTO.from_alipay_dict(value)
    @property
    def apply_end_time(self):
        return self._apply_end_time

    @apply_end_time.setter
    def apply_end_time(self, value):
        self._apply_end_time = value
    @property
    def apply_start_time(self):
        return self._apply_start_time

    @apply_start_time.setter
    def apply_start_time(self, value):
        self._apply_start_time = value
    @property
    def biz_status(self):
        return self._biz_status

    @biz_status.setter
    def biz_status(self, value):
        self._biz_status = value
    @property
    def business_id(self):
        return self._business_id

    @business_id.setter
    def business_id(self, value):
        self._business_id = value
    @property
    def business_line(self):
        return self._business_line

    @business_line.setter
    def business_line(self, value):
        self._business_line = value
    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        self._comment = value
    @property
    def confirm_comment_list(self):
        return self._confirm_comment_list

    @confirm_comment_list.setter
    def confirm_comment_list(self, value):
        if isinstance(value, list):
            self._confirm_comment_list = list()
            for i in value:
                if isinstance(i, OpenApiCommentDTO):
                    self._confirm_comment_list.append(i)
                else:
                    self._confirm_comment_list.append(OpenApiCommentDTO.from_alipay_dict(i))
    @property
    def contract_attach_list(self):
        return self._contract_attach_list

    @contract_attach_list.setter
    def contract_attach_list(self, value):
        if isinstance(value, list):
            self._contract_attach_list = list()
            for i in value:
                if isinstance(i, OpenApiContractFileSaDTO):
                    self._contract_attach_list.append(i)
                else:
                    self._contract_attach_list.append(OpenApiContractFileSaDTO.from_alipay_dict(i))
    @property
    def contract_code(self):
        return self._contract_code

    @contract_code.setter
    def contract_code(self, value):
        self._contract_code = value
    @property
    def contract_coordinator_list(self):
        return self._contract_coordinator_list

    @contract_coordinator_list.setter
    def contract_coordinator_list(self, value):
        if isinstance(value, list):
            self._contract_coordinator_list = list()
            for i in value:
                if isinstance(i, OpenApiContractCoordinatorDTO):
                    self._contract_coordinator_list.append(i)
                else:
                    self._contract_coordinator_list.append(OpenApiContractCoordinatorDTO.from_alipay_dict(i))
    @property
    def contract_create_time(self):
        return self._contract_create_time

    @contract_create_time.setter
    def contract_create_time(self, value):
        self._contract_create_time = value
    @property
    def contract_doc_list(self):
        return self._contract_doc_list

    @contract_doc_list.setter
    def contract_doc_list(self, value):
        if isinstance(value, list):
            self._contract_doc_list = list()
            for i in value:
                if isinstance(i, OpenApiContractFileSaDTO):
                    self._contract_doc_list.append(i)
                else:
                    self._contract_doc_list.append(OpenApiContractFileSaDTO.from_alipay_dict(i))
    @property
    def contract_file_results(self):
        return self._contract_file_results

    @contract_file_results.setter
    def contract_file_results(self, value):
        if isinstance(value, list):
            self._contract_file_results = list()
            for i in value:
                if isinstance(i, OpenApiContractFileDTO):
                    self._contract_file_results.append(i)
                else:
                    self._contract_file_results.append(OpenApiContractFileDTO.from_alipay_dict(i))
    @property
    def contract_name(self):
        return self._contract_name

    @contract_name.setter
    def contract_name(self, value):
        self._contract_name = value
    @property
    def contract_partner_a_dto_list(self):
        return self._contract_partner_a_dto_list

    @contract_partner_a_dto_list.setter
    def contract_partner_a_dto_list(self, value):
        if isinstance(value, list):
            self._contract_partner_a_dto_list = list()
            for i in value:
                if isinstance(i, OpenApiPartnerSaDTO):
                    self._contract_partner_a_dto_list.append(i)
                else:
                    self._contract_partner_a_dto_list.append(OpenApiPartnerSaDTO.from_alipay_dict(i))
    @property
    def contract_partner_b_dto_list(self):
        return self._contract_partner_b_dto_list

    @contract_partner_b_dto_list.setter
    def contract_partner_b_dto_list(self, value):
        if isinstance(value, list):
            self._contract_partner_b_dto_list = list()
            for i in value:
                if isinstance(i, OpenApiPartnerSaDTO):
                    self._contract_partner_b_dto_list.append(i)
                else:
                    self._contract_partner_b_dto_list.append(OpenApiPartnerSaDTO.from_alipay_dict(i))
    @property
    def contract_sign_type(self):
        return self._contract_sign_type

    @contract_sign_type.setter
    def contract_sign_type(self, value):
        self._contract_sign_type = value
    @property
    def contract_template_code(self):
        return self._contract_template_code

    @contract_template_code.setter
    def contract_template_code(self, value):
        self._contract_template_code = value
    @property
    def detail_url(self):
        return self._detail_url

    @detail_url.setter
    def detail_url(self, value):
        self._detail_url = value
    @property
    def effect_time(self):
        return self._effect_time

    @effect_time.setter
    def effect_time(self, value):
        self._effect_time = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def finance_people(self):
        return self._finance_people

    @finance_people.setter
    def finance_people(self, value):
        if isinstance(value, list):
            self._finance_people = list()
            for i in value:
                if isinstance(i, OpenApiPersonSaDTO):
                    self._finance_people.append(i)
                else:
                    self._finance_people.append(OpenApiPersonSaDTO.from_alipay_dict(i))
    @property
    def is_template(self):
        return self._is_template

    @is_template.setter
    def is_template(self, value):
        self._is_template = value
    @property
    def legal_people(self):
        return self._legal_people

    @legal_people.setter
    def legal_people(self, value):
        if isinstance(value, list):
            self._legal_people = list()
            for i in value:
                if isinstance(i, OpenApiPersonSaDTO):
                    self._legal_people.append(i)
                else:
                    self._legal_people.append(OpenApiPersonSaDTO.from_alipay_dict(i))
    @property
    def matter_attachment_results(self):
        return self._matter_attachment_results

    @matter_attachment_results.setter
    def matter_attachment_results(self, value):
        if isinstance(value, list):
            self._matter_attachment_results = list()
            for i in value:
                if isinstance(i, OpenApiContractFileDTO):
                    self._matter_attachment_results.append(i)
                else:
                    self._matter_attachment_results.append(OpenApiContractFileDTO.from_alipay_dict(i))
    @property
    def matter_code(self):
        return self._matter_code

    @matter_code.setter
    def matter_code(self, value):
        self._matter_code = value
    @property
    def matter_comment_list(self):
        return self._matter_comment_list

    @matter_comment_list.setter
    def matter_comment_list(self, value):
        if isinstance(value, list):
            self._matter_comment_list = list()
            for i in value:
                if isinstance(i, OpenApiMatterCommentDTO):
                    self._matter_comment_list.append(i)
                else:
                    self._matter_comment_list.append(OpenApiMatterCommentDTO.from_alipay_dict(i))
    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value
    @property
    def origin_biz_status(self):
        return self._origin_biz_status

    @origin_biz_status.setter
    def origin_biz_status(self, value):
        self._origin_biz_status = value
    @property
    def owners(self):
        return self._owners

    @owners.setter
    def owners(self, value):
        if isinstance(value, list):
            self._owners = list()
            for i in value:
                if isinstance(i, OpenApiPersonSaDTO):
                    self._owners.append(i)
                else:
                    self._owners.append(OpenApiPersonSaDTO.from_alipay_dict(i))
    @property
    def relate_matter_list(self):
        return self._relate_matter_list

    @relate_matter_list.setter
    def relate_matter_list(self, value):
        if isinstance(value, list):
            self._relate_matter_list = list()
            for i in value:
                if isinstance(i, OpenApiRelateMatterDTO):
                    self._relate_matter_list.append(i)
                else:
                    self._relate_matter_list.append(OpenApiRelateMatterDTO.from_alipay_dict(i))
    @property
    def show_biz_status(self):
        return self._show_biz_status

    @show_biz_status.setter
    def show_biz_status(self, value):
        self._show_biz_status = value
    @property
    def source_system_id(self):
        return self._source_system_id

    @source_system_id.setter
    def source_system_id(self, value):
        self._source_system_id = value
    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value


    def to_alipay_dict(self):
        params = dict()
        if self.applicant:
            if hasattr(self.applicant, 'to_alipay_dict'):
                params['applicant'] = self.applicant.to_alipay_dict()
            else:
                params['applicant'] = self.applicant
        if self.apply_end_time:
            if hasattr(self.apply_end_time, 'to_alipay_dict'):
                params['apply_end_time'] = self.apply_end_time.to_alipay_dict()
            else:
                params['apply_end_time'] = self.apply_end_time
        if self.apply_start_time:
            if hasattr(self.apply_start_time, 'to_alipay_dict'):
                params['apply_start_time'] = self.apply_start_time.to_alipay_dict()
            else:
                params['apply_start_time'] = self.apply_start_time
        if self.biz_status:
            if hasattr(self.biz_status, 'to_alipay_dict'):
                params['biz_status'] = self.biz_status.to_alipay_dict()
            else:
                params['biz_status'] = self.biz_status
        if self.business_id:
            if hasattr(self.business_id, 'to_alipay_dict'):
                params['business_id'] = self.business_id.to_alipay_dict()
            else:
                params['business_id'] = self.business_id
        if self.business_line:
            if hasattr(self.business_line, 'to_alipay_dict'):
                params['business_line'] = self.business_line.to_alipay_dict()
            else:
                params['business_line'] = self.business_line
        if self.comment:
            if hasattr(self.comment, 'to_alipay_dict'):
                params['comment'] = self.comment.to_alipay_dict()
            else:
                params['comment'] = self.comment
        if self.confirm_comment_list:
            if isinstance(self.confirm_comment_list, list):
                for i in range(0, len(self.confirm_comment_list)):
                    element = self.confirm_comment_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.confirm_comment_list[i] = element.to_alipay_dict()
            if hasattr(self.confirm_comment_list, 'to_alipay_dict'):
                params['confirm_comment_list'] = self.confirm_comment_list.to_alipay_dict()
            else:
                params['confirm_comment_list'] = self.confirm_comment_list
        if self.contract_attach_list:
            if isinstance(self.contract_attach_list, list):
                for i in range(0, len(self.contract_attach_list)):
                    element = self.contract_attach_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contract_attach_list[i] = element.to_alipay_dict()
            if hasattr(self.contract_attach_list, 'to_alipay_dict'):
                params['contract_attach_list'] = self.contract_attach_list.to_alipay_dict()
            else:
                params['contract_attach_list'] = self.contract_attach_list
        if self.contract_code:
            if hasattr(self.contract_code, 'to_alipay_dict'):
                params['contract_code'] = self.contract_code.to_alipay_dict()
            else:
                params['contract_code'] = self.contract_code
        if self.contract_coordinator_list:
            if isinstance(self.contract_coordinator_list, list):
                for i in range(0, len(self.contract_coordinator_list)):
                    element = self.contract_coordinator_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contract_coordinator_list[i] = element.to_alipay_dict()
            if hasattr(self.contract_coordinator_list, 'to_alipay_dict'):
                params['contract_coordinator_list'] = self.contract_coordinator_list.to_alipay_dict()
            else:
                params['contract_coordinator_list'] = self.contract_coordinator_list
        if self.contract_create_time:
            if hasattr(self.contract_create_time, 'to_alipay_dict'):
                params['contract_create_time'] = self.contract_create_time.to_alipay_dict()
            else:
                params['contract_create_time'] = self.contract_create_time
        if self.contract_doc_list:
            if isinstance(self.contract_doc_list, list):
                for i in range(0, len(self.contract_doc_list)):
                    element = self.contract_doc_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contract_doc_list[i] = element.to_alipay_dict()
            if hasattr(self.contract_doc_list, 'to_alipay_dict'):
                params['contract_doc_list'] = self.contract_doc_list.to_alipay_dict()
            else:
                params['contract_doc_list'] = self.contract_doc_list
        if self.contract_file_results:
            if isinstance(self.contract_file_results, list):
                for i in range(0, len(self.contract_file_results)):
                    element = self.contract_file_results[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contract_file_results[i] = element.to_alipay_dict()
            if hasattr(self.contract_file_results, 'to_alipay_dict'):
                params['contract_file_results'] = self.contract_file_results.to_alipay_dict()
            else:
                params['contract_file_results'] = self.contract_file_results
        if self.contract_name:
            if hasattr(self.contract_name, 'to_alipay_dict'):
                params['contract_name'] = self.contract_name.to_alipay_dict()
            else:
                params['contract_name'] = self.contract_name
        if self.contract_partner_a_dto_list:
            if isinstance(self.contract_partner_a_dto_list, list):
                for i in range(0, len(self.contract_partner_a_dto_list)):
                    element = self.contract_partner_a_dto_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contract_partner_a_dto_list[i] = element.to_alipay_dict()
            if hasattr(self.contract_partner_a_dto_list, 'to_alipay_dict'):
                params['contract_partner_a_dto_list'] = self.contract_partner_a_dto_list.to_alipay_dict()
            else:
                params['contract_partner_a_dto_list'] = self.contract_partner_a_dto_list
        if self.contract_partner_b_dto_list:
            if isinstance(self.contract_partner_b_dto_list, list):
                for i in range(0, len(self.contract_partner_b_dto_list)):
                    element = self.contract_partner_b_dto_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contract_partner_b_dto_list[i] = element.to_alipay_dict()
            if hasattr(self.contract_partner_b_dto_list, 'to_alipay_dict'):
                params['contract_partner_b_dto_list'] = self.contract_partner_b_dto_list.to_alipay_dict()
            else:
                params['contract_partner_b_dto_list'] = self.contract_partner_b_dto_list
        if self.contract_sign_type:
            if hasattr(self.contract_sign_type, 'to_alipay_dict'):
                params['contract_sign_type'] = self.contract_sign_type.to_alipay_dict()
            else:
                params['contract_sign_type'] = self.contract_sign_type
        if self.contract_template_code:
            if hasattr(self.contract_template_code, 'to_alipay_dict'):
                params['contract_template_code'] = self.contract_template_code.to_alipay_dict()
            else:
                params['contract_template_code'] = self.contract_template_code
        if self.detail_url:
            if hasattr(self.detail_url, 'to_alipay_dict'):
                params['detail_url'] = self.detail_url.to_alipay_dict()
            else:
                params['detail_url'] = self.detail_url
        if self.effect_time:
            if hasattr(self.effect_time, 'to_alipay_dict'):
                params['effect_time'] = self.effect_time.to_alipay_dict()
            else:
                params['effect_time'] = self.effect_time
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.finance_people:
            if isinstance(self.finance_people, list):
                for i in range(0, len(self.finance_people)):
                    element = self.finance_people[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.finance_people[i] = element.to_alipay_dict()
            if hasattr(self.finance_people, 'to_alipay_dict'):
                params['finance_people'] = self.finance_people.to_alipay_dict()
            else:
                params['finance_people'] = self.finance_people
        if self.is_template:
            if hasattr(self.is_template, 'to_alipay_dict'):
                params['is_template'] = self.is_template.to_alipay_dict()
            else:
                params['is_template'] = self.is_template
        if self.legal_people:
            if isinstance(self.legal_people, list):
                for i in range(0, len(self.legal_people)):
                    element = self.legal_people[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.legal_people[i] = element.to_alipay_dict()
            if hasattr(self.legal_people, 'to_alipay_dict'):
                params['legal_people'] = self.legal_people.to_alipay_dict()
            else:
                params['legal_people'] = self.legal_people
        if self.matter_attachment_results:
            if isinstance(self.matter_attachment_results, list):
                for i in range(0, len(self.matter_attachment_results)):
                    element = self.matter_attachment_results[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.matter_attachment_results[i] = element.to_alipay_dict()
            if hasattr(self.matter_attachment_results, 'to_alipay_dict'):
                params['matter_attachment_results'] = self.matter_attachment_results.to_alipay_dict()
            else:
                params['matter_attachment_results'] = self.matter_attachment_results
        if self.matter_code:
            if hasattr(self.matter_code, 'to_alipay_dict'):
                params['matter_code'] = self.matter_code.to_alipay_dict()
            else:
                params['matter_code'] = self.matter_code
        if self.matter_comment_list:
            if isinstance(self.matter_comment_list, list):
                for i in range(0, len(self.matter_comment_list)):
                    element = self.matter_comment_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.matter_comment_list[i] = element.to_alipay_dict()
            if hasattr(self.matter_comment_list, 'to_alipay_dict'):
                params['matter_comment_list'] = self.matter_comment_list.to_alipay_dict()
            else:
                params['matter_comment_list'] = self.matter_comment_list
        if self.number:
            if hasattr(self.number, 'to_alipay_dict'):
                params['number'] = self.number.to_alipay_dict()
            else:
                params['number'] = self.number
        if self.origin_biz_status:
            if hasattr(self.origin_biz_status, 'to_alipay_dict'):
                params['origin_biz_status'] = self.origin_biz_status.to_alipay_dict()
            else:
                params['origin_biz_status'] = self.origin_biz_status
        if self.owners:
            if isinstance(self.owners, list):
                for i in range(0, len(self.owners)):
                    element = self.owners[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.owners[i] = element.to_alipay_dict()
            if hasattr(self.owners, 'to_alipay_dict'):
                params['owners'] = self.owners.to_alipay_dict()
            else:
                params['owners'] = self.owners
        if self.relate_matter_list:
            if isinstance(self.relate_matter_list, list):
                for i in range(0, len(self.relate_matter_list)):
                    element = self.relate_matter_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.relate_matter_list[i] = element.to_alipay_dict()
            if hasattr(self.relate_matter_list, 'to_alipay_dict'):
                params['relate_matter_list'] = self.relate_matter_list.to_alipay_dict()
            else:
                params['relate_matter_list'] = self.relate_matter_list
        if self.show_biz_status:
            if hasattr(self.show_biz_status, 'to_alipay_dict'):
                params['show_biz_status'] = self.show_biz_status.to_alipay_dict()
            else:
                params['show_biz_status'] = self.show_biz_status
        if self.source_system_id:
            if hasattr(self.source_system_id, 'to_alipay_dict'):
                params['source_system_id'] = self.source_system_id.to_alipay_dict()
            else:
                params['source_system_id'] = self.source_system_id
        if self.tenant:
            if hasattr(self.tenant, 'to_alipay_dict'):
                params['tenant'] = self.tenant.to_alipay_dict()
            else:
                params['tenant'] = self.tenant
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiContractMatterDetailDTO()
        if 'applicant' in d:
            o.applicant = d['applicant']
        if 'apply_end_time' in d:
            o.apply_end_time = d['apply_end_time']
        if 'apply_start_time' in d:
            o.apply_start_time = d['apply_start_time']
        if 'biz_status' in d:
            o.biz_status = d['biz_status']
        if 'business_id' in d:
            o.business_id = d['business_id']
        if 'business_line' in d:
            o.business_line = d['business_line']
        if 'comment' in d:
            o.comment = d['comment']
        if 'confirm_comment_list' in d:
            o.confirm_comment_list = d['confirm_comment_list']
        if 'contract_attach_list' in d:
            o.contract_attach_list = d['contract_attach_list']
        if 'contract_code' in d:
            o.contract_code = d['contract_code']
        if 'contract_coordinator_list' in d:
            o.contract_coordinator_list = d['contract_coordinator_list']
        if 'contract_create_time' in d:
            o.contract_create_time = d['contract_create_time']
        if 'contract_doc_list' in d:
            o.contract_doc_list = d['contract_doc_list']
        if 'contract_file_results' in d:
            o.contract_file_results = d['contract_file_results']
        if 'contract_name' in d:
            o.contract_name = d['contract_name']
        if 'contract_partner_a_dto_list' in d:
            o.contract_partner_a_dto_list = d['contract_partner_a_dto_list']
        if 'contract_partner_b_dto_list' in d:
            o.contract_partner_b_dto_list = d['contract_partner_b_dto_list']
        if 'contract_sign_type' in d:
            o.contract_sign_type = d['contract_sign_type']
        if 'contract_template_code' in d:
            o.contract_template_code = d['contract_template_code']
        if 'detail_url' in d:
            o.detail_url = d['detail_url']
        if 'effect_time' in d:
            o.effect_time = d['effect_time']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'finance_people' in d:
            o.finance_people = d['finance_people']
        if 'is_template' in d:
            o.is_template = d['is_template']
        if 'legal_people' in d:
            o.legal_people = d['legal_people']
        if 'matter_attachment_results' in d:
            o.matter_attachment_results = d['matter_attachment_results']
        if 'matter_code' in d:
            o.matter_code = d['matter_code']
        if 'matter_comment_list' in d:
            o.matter_comment_list = d['matter_comment_list']
        if 'number' in d:
            o.number = d['number']
        if 'origin_biz_status' in d:
            o.origin_biz_status = d['origin_biz_status']
        if 'owners' in d:
            o.owners = d['owners']
        if 'relate_matter_list' in d:
            o.relate_matter_list = d['relate_matter_list']
        if 'show_biz_status' in d:
            o.show_biz_status = d['show_biz_status']
        if 'source_system_id' in d:
            o.source_system_id = d['source_system_id']
        if 'tenant' in d:
            o.tenant = d['tenant']
        return o


