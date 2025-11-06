#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IdentityMaterials import IdentityMaterials
from alipay.aop.api.domain.SeltInfoList import SeltInfoList


class AlipayCommerceMedicalInsuranceClaimreportModifyModel(object):

    def __init__(self):
        self._apply_no = None
        self._biz_no = None
        self._case_reopened = None
        self._cert_no = None
        self._cert_type = None
        self._claim_no = None
        self._claim_report_no = None
        self._claim_status = None
        self._company_type = None
        self._identity_materials = None
        self._lack_materials_sense = None
        self._name = None
        self._note_url = None
        self._open_id = None
        self._reject_reason = None
        self._report_no = None
        self._selt_info_list = None
        self._source = None
        self._total_claim_amount = None
        self._user_id = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def case_reopened(self):
        return self._case_reopened

    @case_reopened.setter
    def case_reopened(self, value):
        self._case_reopened = value
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
    def claim_no(self):
        return self._claim_no

    @claim_no.setter
    def claim_no(self, value):
        self._claim_no = value
    @property
    def claim_report_no(self):
        return self._claim_report_no

    @claim_report_no.setter
    def claim_report_no(self, value):
        self._claim_report_no = value
    @property
    def claim_status(self):
        return self._claim_status

    @claim_status.setter
    def claim_status(self, value):
        self._claim_status = value
    @property
    def company_type(self):
        return self._company_type

    @company_type.setter
    def company_type(self, value):
        self._company_type = value
    @property
    def identity_materials(self):
        return self._identity_materials

    @identity_materials.setter
    def identity_materials(self, value):
        if isinstance(value, list):
            self._identity_materials = list()
            for i in value:
                if isinstance(i, IdentityMaterials):
                    self._identity_materials.append(i)
                else:
                    self._identity_materials.append(IdentityMaterials.from_alipay_dict(i))
    @property
    def lack_materials_sense(self):
        return self._lack_materials_sense

    @lack_materials_sense.setter
    def lack_materials_sense(self, value):
        self._lack_materials_sense = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def note_url(self):
        return self._note_url

    @note_url.setter
    def note_url(self, value):
        self._note_url = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value
    @property
    def report_no(self):
        return self._report_no

    @report_no.setter
    def report_no(self, value):
        self._report_no = value
    @property
    def selt_info_list(self):
        return self._selt_info_list

    @selt_info_list.setter
    def selt_info_list(self, value):
        if isinstance(value, list):
            self._selt_info_list = list()
            for i in value:
                if isinstance(i, SeltInfoList):
                    self._selt_info_list.append(i)
                else:
                    self._selt_info_list.append(SeltInfoList.from_alipay_dict(i))
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def total_claim_amount(self):
        return self._total_claim_amount

    @total_claim_amount.setter
    def total_claim_amount(self, value):
        self._total_claim_amount = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.case_reopened:
            if hasattr(self.case_reopened, 'to_alipay_dict'):
                params['case_reopened'] = self.case_reopened.to_alipay_dict()
            else:
                params['case_reopened'] = self.case_reopened
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
        if self.claim_no:
            if hasattr(self.claim_no, 'to_alipay_dict'):
                params['claim_no'] = self.claim_no.to_alipay_dict()
            else:
                params['claim_no'] = self.claim_no
        if self.claim_report_no:
            if hasattr(self.claim_report_no, 'to_alipay_dict'):
                params['claim_report_no'] = self.claim_report_no.to_alipay_dict()
            else:
                params['claim_report_no'] = self.claim_report_no
        if self.claim_status:
            if hasattr(self.claim_status, 'to_alipay_dict'):
                params['claim_status'] = self.claim_status.to_alipay_dict()
            else:
                params['claim_status'] = self.claim_status
        if self.company_type:
            if hasattr(self.company_type, 'to_alipay_dict'):
                params['company_type'] = self.company_type.to_alipay_dict()
            else:
                params['company_type'] = self.company_type
        if self.identity_materials:
            if isinstance(self.identity_materials, list):
                for i in range(0, len(self.identity_materials)):
                    element = self.identity_materials[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.identity_materials[i] = element.to_alipay_dict()
            if hasattr(self.identity_materials, 'to_alipay_dict'):
                params['identity_materials'] = self.identity_materials.to_alipay_dict()
            else:
                params['identity_materials'] = self.identity_materials
        if self.lack_materials_sense:
            if hasattr(self.lack_materials_sense, 'to_alipay_dict'):
                params['lack_materials_sense'] = self.lack_materials_sense.to_alipay_dict()
            else:
                params['lack_materials_sense'] = self.lack_materials_sense
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.note_url:
            if hasattr(self.note_url, 'to_alipay_dict'):
                params['note_url'] = self.note_url.to_alipay_dict()
            else:
                params['note_url'] = self.note_url
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.reject_reason:
            if hasattr(self.reject_reason, 'to_alipay_dict'):
                params['reject_reason'] = self.reject_reason.to_alipay_dict()
            else:
                params['reject_reason'] = self.reject_reason
        if self.report_no:
            if hasattr(self.report_no, 'to_alipay_dict'):
                params['report_no'] = self.report_no.to_alipay_dict()
            else:
                params['report_no'] = self.report_no
        if self.selt_info_list:
            if isinstance(self.selt_info_list, list):
                for i in range(0, len(self.selt_info_list)):
                    element = self.selt_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.selt_info_list[i] = element.to_alipay_dict()
            if hasattr(self.selt_info_list, 'to_alipay_dict'):
                params['selt_info_list'] = self.selt_info_list.to_alipay_dict()
            else:
                params['selt_info_list'] = self.selt_info_list
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.total_claim_amount:
            if hasattr(self.total_claim_amount, 'to_alipay_dict'):
                params['total_claim_amount'] = self.total_claim_amount.to_alipay_dict()
            else:
                params['total_claim_amount'] = self.total_claim_amount
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
        o = AlipayCommerceMedicalInsuranceClaimreportModifyModel()
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'case_reopened' in d:
            o.case_reopened = d['case_reopened']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'claim_no' in d:
            o.claim_no = d['claim_no']
        if 'claim_report_no' in d:
            o.claim_report_no = d['claim_report_no']
        if 'claim_status' in d:
            o.claim_status = d['claim_status']
        if 'company_type' in d:
            o.company_type = d['company_type']
        if 'identity_materials' in d:
            o.identity_materials = d['identity_materials']
        if 'lack_materials_sense' in d:
            o.lack_materials_sense = d['lack_materials_sense']
        if 'name' in d:
            o.name = d['name']
        if 'note_url' in d:
            o.note_url = d['note_url']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'reject_reason' in d:
            o.reject_reason = d['reject_reason']
        if 'report_no' in d:
            o.report_no = d['report_no']
        if 'selt_info_list' in d:
            o.selt_info_list = d['selt_info_list']
        if 'source' in d:
            o.source = d['source']
        if 'total_claim_amount' in d:
            o.total_claim_amount = d['total_claim_amount']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


