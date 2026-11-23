#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DutyResidueAmount import DutyResidueAmount
from alipay.aop.api.domain.PolicyPersonInfo import PolicyPersonInfo


class PolicyInfo(object):

    def __init__(self):
        self._ant_policy_no = None
        self._can_direct_pay = None
        self._can_direct_pay_msg = None
        self._company_type = None
        self._dplan_code = None
        self._dplan_name = None
        self._duty_residue_amount_list = None
        self._electronic_policy_url = None
        self._end_date = None
        self._end_ind = None
        self._ext_json = None
        self._hang_ind = None
        self._hang_reason = None
        self._has_claims = None
        self._has_preservation = None
        self._person_list = None
        self._policy_no = None
        self._policy_type = None
        self._renewed_ind = None
        self._res_deductible_excess = None
        self._serial_no = None
        self._source_policy_no = None
        self._start_date = None
        self._status = None
        self._surrender_reason = None
        self._surrender_time = None
        self._suspended_reason = None
        self._suspended_time = None
        self._valid_ind = None

    @property
    def ant_policy_no(self):
        return self._ant_policy_no

    @ant_policy_no.setter
    def ant_policy_no(self, value):
        self._ant_policy_no = value
    @property
    def can_direct_pay(self):
        return self._can_direct_pay

    @can_direct_pay.setter
    def can_direct_pay(self, value):
        self._can_direct_pay = value
    @property
    def can_direct_pay_msg(self):
        return self._can_direct_pay_msg

    @can_direct_pay_msg.setter
    def can_direct_pay_msg(self, value):
        self._can_direct_pay_msg = value
    @property
    def company_type(self):
        return self._company_type

    @company_type.setter
    def company_type(self, value):
        self._company_type = value
    @property
    def dplan_code(self):
        return self._dplan_code

    @dplan_code.setter
    def dplan_code(self, value):
        self._dplan_code = value
    @property
    def dplan_name(self):
        return self._dplan_name

    @dplan_name.setter
    def dplan_name(self, value):
        self._dplan_name = value
    @property
    def duty_residue_amount_list(self):
        return self._duty_residue_amount_list

    @duty_residue_amount_list.setter
    def duty_residue_amount_list(self, value):
        if isinstance(value, list):
            self._duty_residue_amount_list = list()
            for i in value:
                if isinstance(i, DutyResidueAmount):
                    self._duty_residue_amount_list.append(i)
                else:
                    self._duty_residue_amount_list.append(DutyResidueAmount.from_alipay_dict(i))
    @property
    def electronic_policy_url(self):
        return self._electronic_policy_url

    @electronic_policy_url.setter
    def electronic_policy_url(self, value):
        self._electronic_policy_url = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def end_ind(self):
        return self._end_ind

    @end_ind.setter
    def end_ind(self, value):
        self._end_ind = value
    @property
    def ext_json(self):
        return self._ext_json

    @ext_json.setter
    def ext_json(self, value):
        self._ext_json = value
    @property
    def hang_ind(self):
        return self._hang_ind

    @hang_ind.setter
    def hang_ind(self, value):
        self._hang_ind = value
    @property
    def hang_reason(self):
        return self._hang_reason

    @hang_reason.setter
    def hang_reason(self, value):
        self._hang_reason = value
    @property
    def has_claims(self):
        return self._has_claims

    @has_claims.setter
    def has_claims(self, value):
        self._has_claims = value
    @property
    def has_preservation(self):
        return self._has_preservation

    @has_preservation.setter
    def has_preservation(self, value):
        self._has_preservation = value
    @property
    def person_list(self):
        return self._person_list

    @person_list.setter
    def person_list(self, value):
        if isinstance(value, list):
            self._person_list = list()
            for i in value:
                if isinstance(i, PolicyPersonInfo):
                    self._person_list.append(i)
                else:
                    self._person_list.append(PolicyPersonInfo.from_alipay_dict(i))
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value
    @property
    def policy_type(self):
        return self._policy_type

    @policy_type.setter
    def policy_type(self, value):
        self._policy_type = value
    @property
    def renewed_ind(self):
        return self._renewed_ind

    @renewed_ind.setter
    def renewed_ind(self, value):
        self._renewed_ind = value
    @property
    def res_deductible_excess(self):
        return self._res_deductible_excess

    @res_deductible_excess.setter
    def res_deductible_excess(self, value):
        self._res_deductible_excess = value
    @property
    def serial_no(self):
        return self._serial_no

    @serial_no.setter
    def serial_no(self, value):
        self._serial_no = value
    @property
    def source_policy_no(self):
        return self._source_policy_no

    @source_policy_no.setter
    def source_policy_no(self, value):
        self._source_policy_no = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def surrender_reason(self):
        return self._surrender_reason

    @surrender_reason.setter
    def surrender_reason(self, value):
        self._surrender_reason = value
    @property
    def surrender_time(self):
        return self._surrender_time

    @surrender_time.setter
    def surrender_time(self, value):
        self._surrender_time = value
    @property
    def suspended_reason(self):
        return self._suspended_reason

    @suspended_reason.setter
    def suspended_reason(self, value):
        self._suspended_reason = value
    @property
    def suspended_time(self):
        return self._suspended_time

    @suspended_time.setter
    def suspended_time(self, value):
        self._suspended_time = value
    @property
    def valid_ind(self):
        return self._valid_ind

    @valid_ind.setter
    def valid_ind(self, value):
        self._valid_ind = value


    def to_alipay_dict(self):
        params = dict()
        if self.ant_policy_no:
            if hasattr(self.ant_policy_no, 'to_alipay_dict'):
                params['ant_policy_no'] = self.ant_policy_no.to_alipay_dict()
            else:
                params['ant_policy_no'] = self.ant_policy_no
        if self.can_direct_pay:
            if hasattr(self.can_direct_pay, 'to_alipay_dict'):
                params['can_direct_pay'] = self.can_direct_pay.to_alipay_dict()
            else:
                params['can_direct_pay'] = self.can_direct_pay
        if self.can_direct_pay_msg:
            if hasattr(self.can_direct_pay_msg, 'to_alipay_dict'):
                params['can_direct_pay_msg'] = self.can_direct_pay_msg.to_alipay_dict()
            else:
                params['can_direct_pay_msg'] = self.can_direct_pay_msg
        if self.company_type:
            if hasattr(self.company_type, 'to_alipay_dict'):
                params['company_type'] = self.company_type.to_alipay_dict()
            else:
                params['company_type'] = self.company_type
        if self.dplan_code:
            if hasattr(self.dplan_code, 'to_alipay_dict'):
                params['dplan_code'] = self.dplan_code.to_alipay_dict()
            else:
                params['dplan_code'] = self.dplan_code
        if self.dplan_name:
            if hasattr(self.dplan_name, 'to_alipay_dict'):
                params['dplan_name'] = self.dplan_name.to_alipay_dict()
            else:
                params['dplan_name'] = self.dplan_name
        if self.duty_residue_amount_list:
            if isinstance(self.duty_residue_amount_list, list):
                for i in range(0, len(self.duty_residue_amount_list)):
                    element = self.duty_residue_amount_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.duty_residue_amount_list[i] = element.to_alipay_dict()
            if hasattr(self.duty_residue_amount_list, 'to_alipay_dict'):
                params['duty_residue_amount_list'] = self.duty_residue_amount_list.to_alipay_dict()
            else:
                params['duty_residue_amount_list'] = self.duty_residue_amount_list
        if self.electronic_policy_url:
            if hasattr(self.electronic_policy_url, 'to_alipay_dict'):
                params['electronic_policy_url'] = self.electronic_policy_url.to_alipay_dict()
            else:
                params['electronic_policy_url'] = self.electronic_policy_url
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.end_ind:
            if hasattr(self.end_ind, 'to_alipay_dict'):
                params['end_ind'] = self.end_ind.to_alipay_dict()
            else:
                params['end_ind'] = self.end_ind
        if self.ext_json:
            if hasattr(self.ext_json, 'to_alipay_dict'):
                params['ext_json'] = self.ext_json.to_alipay_dict()
            else:
                params['ext_json'] = self.ext_json
        if self.hang_ind:
            if hasattr(self.hang_ind, 'to_alipay_dict'):
                params['hang_ind'] = self.hang_ind.to_alipay_dict()
            else:
                params['hang_ind'] = self.hang_ind
        if self.hang_reason:
            if hasattr(self.hang_reason, 'to_alipay_dict'):
                params['hang_reason'] = self.hang_reason.to_alipay_dict()
            else:
                params['hang_reason'] = self.hang_reason
        if self.has_claims:
            if hasattr(self.has_claims, 'to_alipay_dict'):
                params['has_claims'] = self.has_claims.to_alipay_dict()
            else:
                params['has_claims'] = self.has_claims
        if self.has_preservation:
            if hasattr(self.has_preservation, 'to_alipay_dict'):
                params['has_preservation'] = self.has_preservation.to_alipay_dict()
            else:
                params['has_preservation'] = self.has_preservation
        if self.person_list:
            if isinstance(self.person_list, list):
                for i in range(0, len(self.person_list)):
                    element = self.person_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.person_list[i] = element.to_alipay_dict()
            if hasattr(self.person_list, 'to_alipay_dict'):
                params['person_list'] = self.person_list.to_alipay_dict()
            else:
                params['person_list'] = self.person_list
        if self.policy_no:
            if hasattr(self.policy_no, 'to_alipay_dict'):
                params['policy_no'] = self.policy_no.to_alipay_dict()
            else:
                params['policy_no'] = self.policy_no
        if self.policy_type:
            if hasattr(self.policy_type, 'to_alipay_dict'):
                params['policy_type'] = self.policy_type.to_alipay_dict()
            else:
                params['policy_type'] = self.policy_type
        if self.renewed_ind:
            if hasattr(self.renewed_ind, 'to_alipay_dict'):
                params['renewed_ind'] = self.renewed_ind.to_alipay_dict()
            else:
                params['renewed_ind'] = self.renewed_ind
        if self.res_deductible_excess:
            if hasattr(self.res_deductible_excess, 'to_alipay_dict'):
                params['res_deductible_excess'] = self.res_deductible_excess.to_alipay_dict()
            else:
                params['res_deductible_excess'] = self.res_deductible_excess
        if self.serial_no:
            if hasattr(self.serial_no, 'to_alipay_dict'):
                params['serial_no'] = self.serial_no.to_alipay_dict()
            else:
                params['serial_no'] = self.serial_no
        if self.source_policy_no:
            if hasattr(self.source_policy_no, 'to_alipay_dict'):
                params['source_policy_no'] = self.source_policy_no.to_alipay_dict()
            else:
                params['source_policy_no'] = self.source_policy_no
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.surrender_reason:
            if hasattr(self.surrender_reason, 'to_alipay_dict'):
                params['surrender_reason'] = self.surrender_reason.to_alipay_dict()
            else:
                params['surrender_reason'] = self.surrender_reason
        if self.surrender_time:
            if hasattr(self.surrender_time, 'to_alipay_dict'):
                params['surrender_time'] = self.surrender_time.to_alipay_dict()
            else:
                params['surrender_time'] = self.surrender_time
        if self.suspended_reason:
            if hasattr(self.suspended_reason, 'to_alipay_dict'):
                params['suspended_reason'] = self.suspended_reason.to_alipay_dict()
            else:
                params['suspended_reason'] = self.suspended_reason
        if self.suspended_time:
            if hasattr(self.suspended_time, 'to_alipay_dict'):
                params['suspended_time'] = self.suspended_time.to_alipay_dict()
            else:
                params['suspended_time'] = self.suspended_time
        if self.valid_ind:
            if hasattr(self.valid_ind, 'to_alipay_dict'):
                params['valid_ind'] = self.valid_ind.to_alipay_dict()
            else:
                params['valid_ind'] = self.valid_ind
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PolicyInfo()
        if 'ant_policy_no' in d:
            o.ant_policy_no = d['ant_policy_no']
        if 'can_direct_pay' in d:
            o.can_direct_pay = d['can_direct_pay']
        if 'can_direct_pay_msg' in d:
            o.can_direct_pay_msg = d['can_direct_pay_msg']
        if 'company_type' in d:
            o.company_type = d['company_type']
        if 'dplan_code' in d:
            o.dplan_code = d['dplan_code']
        if 'dplan_name' in d:
            o.dplan_name = d['dplan_name']
        if 'duty_residue_amount_list' in d:
            o.duty_residue_amount_list = d['duty_residue_amount_list']
        if 'electronic_policy_url' in d:
            o.electronic_policy_url = d['electronic_policy_url']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'end_ind' in d:
            o.end_ind = d['end_ind']
        if 'ext_json' in d:
            o.ext_json = d['ext_json']
        if 'hang_ind' in d:
            o.hang_ind = d['hang_ind']
        if 'hang_reason' in d:
            o.hang_reason = d['hang_reason']
        if 'has_claims' in d:
            o.has_claims = d['has_claims']
        if 'has_preservation' in d:
            o.has_preservation = d['has_preservation']
        if 'person_list' in d:
            o.person_list = d['person_list']
        if 'policy_no' in d:
            o.policy_no = d['policy_no']
        if 'policy_type' in d:
            o.policy_type = d['policy_type']
        if 'renewed_ind' in d:
            o.renewed_ind = d['renewed_ind']
        if 'res_deductible_excess' in d:
            o.res_deductible_excess = d['res_deductible_excess']
        if 'serial_no' in d:
            o.serial_no = d['serial_no']
        if 'source_policy_no' in d:
            o.source_policy_no = d['source_policy_no']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'status' in d:
            o.status = d['status']
        if 'surrender_reason' in d:
            o.surrender_reason = d['surrender_reason']
        if 'surrender_time' in d:
            o.surrender_time = d['surrender_time']
        if 'suspended_reason' in d:
            o.suspended_reason = d['suspended_reason']
        if 'suspended_time' in d:
            o.suspended_time = d['suspended_time']
        if 'valid_ind' in d:
            o.valid_ind = d['valid_ind']
        return o


