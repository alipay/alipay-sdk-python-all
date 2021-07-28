#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ParticipantInfoVO import ParticipantInfoVO
from alipay.aop.api.domain.InterTradeFileInfoVO import InterTradeFileInfoVO
from alipay.aop.api.domain.InterTradeFileInfoVO import InterTradeFileInfoVO
from alipay.aop.api.domain.ParticipantInfoVO import ParticipantInfoVO
from alipay.aop.api.domain.InterTradeApprovalWorkflowOperateLogVO import InterTradeApprovalWorkflowOperateLogVO


class ContractStartInfoOpenApiVO(object):

    def __init__(self):
        self._accept_diff_others = None
        self._accept_diff_others_explain = None
        self._amount_type = None
        self._anti_participants = None
        self._applicant_date = None
        self._backdate_report_file = None
        self._committer = None
        self._contract_amount_cent = None
        self._contract_amount_currency = None
        self._contract_amount_extra = None
        self._contract_amount_to_cny = None
        self._contract_category = None
        self._contract_name = None
        self._contract_no = None
        self._contract_status = None
        self._contract_valid_type = None
        self._dept_id = None
        self._end_date = None
        self._files = None
        self._invoice_type = None
        self._is_frame_contract = None
        self._limit_business_area = None
        self._limit_business_area_explain = None
        self._limit_cooperate = None
        self._limit_cooperate_explain = None
        self._lose_effect_method = None
        self._main_contract_no = None
        self._payment_party = None
        self._predict_amount_in_year_cent = None
        self._predict_amount_in_year_currency = None
        self._predict_amount_in_year_extra = None
        self._predict_amount_in_year_to_cny = None
        self._price_type = None
        self._price_type_explain = None
        self._rate = None
        self._remark = None
        self._self_participants = None
        self._start_date = None
        self._take_effect_method = None
        self._template_protocol = None
        self._template_protocol_explain = None
        self._trade_type = None
        self._workflow_log_list = None

    @property
    def accept_diff_others(self):
        return self._accept_diff_others

    @accept_diff_others.setter
    def accept_diff_others(self, value):
        self._accept_diff_others = value
    @property
    def accept_diff_others_explain(self):
        return self._accept_diff_others_explain

    @accept_diff_others_explain.setter
    def accept_diff_others_explain(self, value):
        self._accept_diff_others_explain = value
    @property
    def amount_type(self):
        return self._amount_type

    @amount_type.setter
    def amount_type(self, value):
        self._amount_type = value
    @property
    def anti_participants(self):
        return self._anti_participants

    @anti_participants.setter
    def anti_participants(self, value):
        if isinstance(value, list):
            self._anti_participants = list()
            for i in value:
                if isinstance(i, ParticipantInfoVO):
                    self._anti_participants.append(i)
                else:
                    self._anti_participants.append(ParticipantInfoVO.from_alipay_dict(i))
    @property
    def applicant_date(self):
        return self._applicant_date

    @applicant_date.setter
    def applicant_date(self, value):
        self._applicant_date = value
    @property
    def backdate_report_file(self):
        return self._backdate_report_file

    @backdate_report_file.setter
    def backdate_report_file(self, value):
        if isinstance(value, list):
            self._backdate_report_file = list()
            for i in value:
                if isinstance(i, InterTradeFileInfoVO):
                    self._backdate_report_file.append(i)
                else:
                    self._backdate_report_file.append(InterTradeFileInfoVO.from_alipay_dict(i))
    @property
    def committer(self):
        return self._committer

    @committer.setter
    def committer(self, value):
        self._committer = value
    @property
    def contract_amount_cent(self):
        return self._contract_amount_cent

    @contract_amount_cent.setter
    def contract_amount_cent(self, value):
        self._contract_amount_cent = value
    @property
    def contract_amount_currency(self):
        return self._contract_amount_currency

    @contract_amount_currency.setter
    def contract_amount_currency(self, value):
        self._contract_amount_currency = value
    @property
    def contract_amount_extra(self):
        return self._contract_amount_extra

    @contract_amount_extra.setter
    def contract_amount_extra(self, value):
        self._contract_amount_extra = value
    @property
    def contract_amount_to_cny(self):
        return self._contract_amount_to_cny

    @contract_amount_to_cny.setter
    def contract_amount_to_cny(self, value):
        self._contract_amount_to_cny = value
    @property
    def contract_category(self):
        return self._contract_category

    @contract_category.setter
    def contract_category(self, value):
        self._contract_category = value
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
    def contract_status(self):
        return self._contract_status

    @contract_status.setter
    def contract_status(self, value):
        self._contract_status = value
    @property
    def contract_valid_type(self):
        return self._contract_valid_type

    @contract_valid_type.setter
    def contract_valid_type(self, value):
        self._contract_valid_type = value
    @property
    def dept_id(self):
        return self._dept_id

    @dept_id.setter
    def dept_id(self, value):
        self._dept_id = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def files(self):
        return self._files

    @files.setter
    def files(self, value):
        if isinstance(value, list):
            self._files = list()
            for i in value:
                if isinstance(i, InterTradeFileInfoVO):
                    self._files.append(i)
                else:
                    self._files.append(InterTradeFileInfoVO.from_alipay_dict(i))
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
    @property
    def is_frame_contract(self):
        return self._is_frame_contract

    @is_frame_contract.setter
    def is_frame_contract(self, value):
        self._is_frame_contract = value
    @property
    def limit_business_area(self):
        return self._limit_business_area

    @limit_business_area.setter
    def limit_business_area(self, value):
        self._limit_business_area = value
    @property
    def limit_business_area_explain(self):
        return self._limit_business_area_explain

    @limit_business_area_explain.setter
    def limit_business_area_explain(self, value):
        self._limit_business_area_explain = value
    @property
    def limit_cooperate(self):
        return self._limit_cooperate

    @limit_cooperate.setter
    def limit_cooperate(self, value):
        self._limit_cooperate = value
    @property
    def limit_cooperate_explain(self):
        return self._limit_cooperate_explain

    @limit_cooperate_explain.setter
    def limit_cooperate_explain(self, value):
        self._limit_cooperate_explain = value
    @property
    def lose_effect_method(self):
        return self._lose_effect_method

    @lose_effect_method.setter
    def lose_effect_method(self, value):
        self._lose_effect_method = value
    @property
    def main_contract_no(self):
        return self._main_contract_no

    @main_contract_no.setter
    def main_contract_no(self, value):
        self._main_contract_no = value
    @property
    def payment_party(self):
        return self._payment_party

    @payment_party.setter
    def payment_party(self, value):
        self._payment_party = value
    @property
    def predict_amount_in_year_cent(self):
        return self._predict_amount_in_year_cent

    @predict_amount_in_year_cent.setter
    def predict_amount_in_year_cent(self, value):
        self._predict_amount_in_year_cent = value
    @property
    def predict_amount_in_year_currency(self):
        return self._predict_amount_in_year_currency

    @predict_amount_in_year_currency.setter
    def predict_amount_in_year_currency(self, value):
        self._predict_amount_in_year_currency = value
    @property
    def predict_amount_in_year_extra(self):
        return self._predict_amount_in_year_extra

    @predict_amount_in_year_extra.setter
    def predict_amount_in_year_extra(self, value):
        self._predict_amount_in_year_extra = value
    @property
    def predict_amount_in_year_to_cny(self):
        return self._predict_amount_in_year_to_cny

    @predict_amount_in_year_to_cny.setter
    def predict_amount_in_year_to_cny(self, value):
        self._predict_amount_in_year_to_cny = value
    @property
    def price_type(self):
        return self._price_type

    @price_type.setter
    def price_type(self, value):
        self._price_type = value
    @property
    def price_type_explain(self):
        return self._price_type_explain

    @price_type_explain.setter
    def price_type_explain(self, value):
        self._price_type_explain = value
    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        self._rate = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def self_participants(self):
        return self._self_participants

    @self_participants.setter
    def self_participants(self, value):
        if isinstance(value, list):
            self._self_participants = list()
            for i in value:
                if isinstance(i, ParticipantInfoVO):
                    self._self_participants.append(i)
                else:
                    self._self_participants.append(ParticipantInfoVO.from_alipay_dict(i))
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def take_effect_method(self):
        return self._take_effect_method

    @take_effect_method.setter
    def take_effect_method(self, value):
        self._take_effect_method = value
    @property
    def template_protocol(self):
        return self._template_protocol

    @template_protocol.setter
    def template_protocol(self, value):
        self._template_protocol = value
    @property
    def template_protocol_explain(self):
        return self._template_protocol_explain

    @template_protocol_explain.setter
    def template_protocol_explain(self, value):
        self._template_protocol_explain = value
    @property
    def trade_type(self):
        return self._trade_type

    @trade_type.setter
    def trade_type(self, value):
        self._trade_type = value
    @property
    def workflow_log_list(self):
        return self._workflow_log_list

    @workflow_log_list.setter
    def workflow_log_list(self, value):
        if isinstance(value, list):
            self._workflow_log_list = list()
            for i in value:
                if isinstance(i, InterTradeApprovalWorkflowOperateLogVO):
                    self._workflow_log_list.append(i)
                else:
                    self._workflow_log_list.append(InterTradeApprovalWorkflowOperateLogVO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.accept_diff_others:
            if hasattr(self.accept_diff_others, 'to_alipay_dict'):
                params['accept_diff_others'] = self.accept_diff_others.to_alipay_dict()
            else:
                params['accept_diff_others'] = self.accept_diff_others
        if self.accept_diff_others_explain:
            if hasattr(self.accept_diff_others_explain, 'to_alipay_dict'):
                params['accept_diff_others_explain'] = self.accept_diff_others_explain.to_alipay_dict()
            else:
                params['accept_diff_others_explain'] = self.accept_diff_others_explain
        if self.amount_type:
            if hasattr(self.amount_type, 'to_alipay_dict'):
                params['amount_type'] = self.amount_type.to_alipay_dict()
            else:
                params['amount_type'] = self.amount_type
        if self.anti_participants:
            if isinstance(self.anti_participants, list):
                for i in range(0, len(self.anti_participants)):
                    element = self.anti_participants[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.anti_participants[i] = element.to_alipay_dict()
            if hasattr(self.anti_participants, 'to_alipay_dict'):
                params['anti_participants'] = self.anti_participants.to_alipay_dict()
            else:
                params['anti_participants'] = self.anti_participants
        if self.applicant_date:
            if hasattr(self.applicant_date, 'to_alipay_dict'):
                params['applicant_date'] = self.applicant_date.to_alipay_dict()
            else:
                params['applicant_date'] = self.applicant_date
        if self.backdate_report_file:
            if isinstance(self.backdate_report_file, list):
                for i in range(0, len(self.backdate_report_file)):
                    element = self.backdate_report_file[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.backdate_report_file[i] = element.to_alipay_dict()
            if hasattr(self.backdate_report_file, 'to_alipay_dict'):
                params['backdate_report_file'] = self.backdate_report_file.to_alipay_dict()
            else:
                params['backdate_report_file'] = self.backdate_report_file
        if self.committer:
            if hasattr(self.committer, 'to_alipay_dict'):
                params['committer'] = self.committer.to_alipay_dict()
            else:
                params['committer'] = self.committer
        if self.contract_amount_cent:
            if hasattr(self.contract_amount_cent, 'to_alipay_dict'):
                params['contract_amount_cent'] = self.contract_amount_cent.to_alipay_dict()
            else:
                params['contract_amount_cent'] = self.contract_amount_cent
        if self.contract_amount_currency:
            if hasattr(self.contract_amount_currency, 'to_alipay_dict'):
                params['contract_amount_currency'] = self.contract_amount_currency.to_alipay_dict()
            else:
                params['contract_amount_currency'] = self.contract_amount_currency
        if self.contract_amount_extra:
            if hasattr(self.contract_amount_extra, 'to_alipay_dict'):
                params['contract_amount_extra'] = self.contract_amount_extra.to_alipay_dict()
            else:
                params['contract_amount_extra'] = self.contract_amount_extra
        if self.contract_amount_to_cny:
            if hasattr(self.contract_amount_to_cny, 'to_alipay_dict'):
                params['contract_amount_to_cny'] = self.contract_amount_to_cny.to_alipay_dict()
            else:
                params['contract_amount_to_cny'] = self.contract_amount_to_cny
        if self.contract_category:
            if hasattr(self.contract_category, 'to_alipay_dict'):
                params['contract_category'] = self.contract_category.to_alipay_dict()
            else:
                params['contract_category'] = self.contract_category
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
        if self.contract_status:
            if hasattr(self.contract_status, 'to_alipay_dict'):
                params['contract_status'] = self.contract_status.to_alipay_dict()
            else:
                params['contract_status'] = self.contract_status
        if self.contract_valid_type:
            if hasattr(self.contract_valid_type, 'to_alipay_dict'):
                params['contract_valid_type'] = self.contract_valid_type.to_alipay_dict()
            else:
                params['contract_valid_type'] = self.contract_valid_type
        if self.dept_id:
            if hasattr(self.dept_id, 'to_alipay_dict'):
                params['dept_id'] = self.dept_id.to_alipay_dict()
            else:
                params['dept_id'] = self.dept_id
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.files:
            if isinstance(self.files, list):
                for i in range(0, len(self.files)):
                    element = self.files[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.files[i] = element.to_alipay_dict()
            if hasattr(self.files, 'to_alipay_dict'):
                params['files'] = self.files.to_alipay_dict()
            else:
                params['files'] = self.files
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = self.invoice_type.to_alipay_dict()
            else:
                params['invoice_type'] = self.invoice_type
        if self.is_frame_contract:
            if hasattr(self.is_frame_contract, 'to_alipay_dict'):
                params['is_frame_contract'] = self.is_frame_contract.to_alipay_dict()
            else:
                params['is_frame_contract'] = self.is_frame_contract
        if self.limit_business_area:
            if hasattr(self.limit_business_area, 'to_alipay_dict'):
                params['limit_business_area'] = self.limit_business_area.to_alipay_dict()
            else:
                params['limit_business_area'] = self.limit_business_area
        if self.limit_business_area_explain:
            if hasattr(self.limit_business_area_explain, 'to_alipay_dict'):
                params['limit_business_area_explain'] = self.limit_business_area_explain.to_alipay_dict()
            else:
                params['limit_business_area_explain'] = self.limit_business_area_explain
        if self.limit_cooperate:
            if hasattr(self.limit_cooperate, 'to_alipay_dict'):
                params['limit_cooperate'] = self.limit_cooperate.to_alipay_dict()
            else:
                params['limit_cooperate'] = self.limit_cooperate
        if self.limit_cooperate_explain:
            if hasattr(self.limit_cooperate_explain, 'to_alipay_dict'):
                params['limit_cooperate_explain'] = self.limit_cooperate_explain.to_alipay_dict()
            else:
                params['limit_cooperate_explain'] = self.limit_cooperate_explain
        if self.lose_effect_method:
            if hasattr(self.lose_effect_method, 'to_alipay_dict'):
                params['lose_effect_method'] = self.lose_effect_method.to_alipay_dict()
            else:
                params['lose_effect_method'] = self.lose_effect_method
        if self.main_contract_no:
            if hasattr(self.main_contract_no, 'to_alipay_dict'):
                params['main_contract_no'] = self.main_contract_no.to_alipay_dict()
            else:
                params['main_contract_no'] = self.main_contract_no
        if self.payment_party:
            if hasattr(self.payment_party, 'to_alipay_dict'):
                params['payment_party'] = self.payment_party.to_alipay_dict()
            else:
                params['payment_party'] = self.payment_party
        if self.predict_amount_in_year_cent:
            if hasattr(self.predict_amount_in_year_cent, 'to_alipay_dict'):
                params['predict_amount_in_year_cent'] = self.predict_amount_in_year_cent.to_alipay_dict()
            else:
                params['predict_amount_in_year_cent'] = self.predict_amount_in_year_cent
        if self.predict_amount_in_year_currency:
            if hasattr(self.predict_amount_in_year_currency, 'to_alipay_dict'):
                params['predict_amount_in_year_currency'] = self.predict_amount_in_year_currency.to_alipay_dict()
            else:
                params['predict_amount_in_year_currency'] = self.predict_amount_in_year_currency
        if self.predict_amount_in_year_extra:
            if hasattr(self.predict_amount_in_year_extra, 'to_alipay_dict'):
                params['predict_amount_in_year_extra'] = self.predict_amount_in_year_extra.to_alipay_dict()
            else:
                params['predict_amount_in_year_extra'] = self.predict_amount_in_year_extra
        if self.predict_amount_in_year_to_cny:
            if hasattr(self.predict_amount_in_year_to_cny, 'to_alipay_dict'):
                params['predict_amount_in_year_to_cny'] = self.predict_amount_in_year_to_cny.to_alipay_dict()
            else:
                params['predict_amount_in_year_to_cny'] = self.predict_amount_in_year_to_cny
        if self.price_type:
            if hasattr(self.price_type, 'to_alipay_dict'):
                params['price_type'] = self.price_type.to_alipay_dict()
            else:
                params['price_type'] = self.price_type
        if self.price_type_explain:
            if hasattr(self.price_type_explain, 'to_alipay_dict'):
                params['price_type_explain'] = self.price_type_explain.to_alipay_dict()
            else:
                params['price_type_explain'] = self.price_type_explain
        if self.rate:
            if hasattr(self.rate, 'to_alipay_dict'):
                params['rate'] = self.rate.to_alipay_dict()
            else:
                params['rate'] = self.rate
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.self_participants:
            if isinstance(self.self_participants, list):
                for i in range(0, len(self.self_participants)):
                    element = self.self_participants[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.self_participants[i] = element.to_alipay_dict()
            if hasattr(self.self_participants, 'to_alipay_dict'):
                params['self_participants'] = self.self_participants.to_alipay_dict()
            else:
                params['self_participants'] = self.self_participants
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.take_effect_method:
            if hasattr(self.take_effect_method, 'to_alipay_dict'):
                params['take_effect_method'] = self.take_effect_method.to_alipay_dict()
            else:
                params['take_effect_method'] = self.take_effect_method
        if self.template_protocol:
            if hasattr(self.template_protocol, 'to_alipay_dict'):
                params['template_protocol'] = self.template_protocol.to_alipay_dict()
            else:
                params['template_protocol'] = self.template_protocol
        if self.template_protocol_explain:
            if hasattr(self.template_protocol_explain, 'to_alipay_dict'):
                params['template_protocol_explain'] = self.template_protocol_explain.to_alipay_dict()
            else:
                params['template_protocol_explain'] = self.template_protocol_explain
        if self.trade_type:
            if hasattr(self.trade_type, 'to_alipay_dict'):
                params['trade_type'] = self.trade_type.to_alipay_dict()
            else:
                params['trade_type'] = self.trade_type
        if self.workflow_log_list:
            if isinstance(self.workflow_log_list, list):
                for i in range(0, len(self.workflow_log_list)):
                    element = self.workflow_log_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.workflow_log_list[i] = element.to_alipay_dict()
            if hasattr(self.workflow_log_list, 'to_alipay_dict'):
                params['workflow_log_list'] = self.workflow_log_list.to_alipay_dict()
            else:
                params['workflow_log_list'] = self.workflow_log_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContractStartInfoOpenApiVO()
        if 'accept_diff_others' in d:
            o.accept_diff_others = d['accept_diff_others']
        if 'accept_diff_others_explain' in d:
            o.accept_diff_others_explain = d['accept_diff_others_explain']
        if 'amount_type' in d:
            o.amount_type = d['amount_type']
        if 'anti_participants' in d:
            o.anti_participants = d['anti_participants']
        if 'applicant_date' in d:
            o.applicant_date = d['applicant_date']
        if 'backdate_report_file' in d:
            o.backdate_report_file = d['backdate_report_file']
        if 'committer' in d:
            o.committer = d['committer']
        if 'contract_amount_cent' in d:
            o.contract_amount_cent = d['contract_amount_cent']
        if 'contract_amount_currency' in d:
            o.contract_amount_currency = d['contract_amount_currency']
        if 'contract_amount_extra' in d:
            o.contract_amount_extra = d['contract_amount_extra']
        if 'contract_amount_to_cny' in d:
            o.contract_amount_to_cny = d['contract_amount_to_cny']
        if 'contract_category' in d:
            o.contract_category = d['contract_category']
        if 'contract_name' in d:
            o.contract_name = d['contract_name']
        if 'contract_no' in d:
            o.contract_no = d['contract_no']
        if 'contract_status' in d:
            o.contract_status = d['contract_status']
        if 'contract_valid_type' in d:
            o.contract_valid_type = d['contract_valid_type']
        if 'dept_id' in d:
            o.dept_id = d['dept_id']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'files' in d:
            o.files = d['files']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'is_frame_contract' in d:
            o.is_frame_contract = d['is_frame_contract']
        if 'limit_business_area' in d:
            o.limit_business_area = d['limit_business_area']
        if 'limit_business_area_explain' in d:
            o.limit_business_area_explain = d['limit_business_area_explain']
        if 'limit_cooperate' in d:
            o.limit_cooperate = d['limit_cooperate']
        if 'limit_cooperate_explain' in d:
            o.limit_cooperate_explain = d['limit_cooperate_explain']
        if 'lose_effect_method' in d:
            o.lose_effect_method = d['lose_effect_method']
        if 'main_contract_no' in d:
            o.main_contract_no = d['main_contract_no']
        if 'payment_party' in d:
            o.payment_party = d['payment_party']
        if 'predict_amount_in_year_cent' in d:
            o.predict_amount_in_year_cent = d['predict_amount_in_year_cent']
        if 'predict_amount_in_year_currency' in d:
            o.predict_amount_in_year_currency = d['predict_amount_in_year_currency']
        if 'predict_amount_in_year_extra' in d:
            o.predict_amount_in_year_extra = d['predict_amount_in_year_extra']
        if 'predict_amount_in_year_to_cny' in d:
            o.predict_amount_in_year_to_cny = d['predict_amount_in_year_to_cny']
        if 'price_type' in d:
            o.price_type = d['price_type']
        if 'price_type_explain' in d:
            o.price_type_explain = d['price_type_explain']
        if 'rate' in d:
            o.rate = d['rate']
        if 'remark' in d:
            o.remark = d['remark']
        if 'self_participants' in d:
            o.self_participants = d['self_participants']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'take_effect_method' in d:
            o.take_effect_method = d['take_effect_method']
        if 'template_protocol' in d:
            o.template_protocol = d['template_protocol']
        if 'template_protocol_explain' in d:
            o.template_protocol_explain = d['template_protocol_explain']
        if 'trade_type' in d:
            o.trade_type = d['trade_type']
        if 'workflow_log_list' in d:
            o.workflow_log_list = d['workflow_log_list']
        return o


