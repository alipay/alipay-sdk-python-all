#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IdentityMaterials import IdentityMaterials
from alipay.aop.api.domain.PostInfo import PostInfo


class AlipayCommerceMedicalInsuranceClaimSyncModel(object):

    def __init__(self):
        self._advance_amount = None
        self._advance_apply_no = None
        self._ant_apply_no = None
        self._ant_claim_no = None
        self._business_no = None
        self._claim_amount = None
        self._claim_detail = None
        self._claim_no = None
        self._claim_status = None
        self._claim_status_desc = None
        self._claim_type = None
        self._company_type = None
        self._identity_materials = None
        self._lack_materials_sense = None
        self._open_id = None
        self._pay_account = None
        self._pay_amount = None
        self._pay_time = None
        self._source = None
        self._to_send_info = None
        self._user_id = None

    @property
    def advance_amount(self):
        return self._advance_amount

    @advance_amount.setter
    def advance_amount(self, value):
        self._advance_amount = value
    @property
    def advance_apply_no(self):
        return self._advance_apply_no

    @advance_apply_no.setter
    def advance_apply_no(self, value):
        self._advance_apply_no = value
    @property
    def ant_apply_no(self):
        return self._ant_apply_no

    @ant_apply_no.setter
    def ant_apply_no(self, value):
        self._ant_apply_no = value
    @property
    def ant_claim_no(self):
        return self._ant_claim_no

    @ant_claim_no.setter
    def ant_claim_no(self, value):
        self._ant_claim_no = value
    @property
    def business_no(self):
        return self._business_no

    @business_no.setter
    def business_no(self, value):
        self._business_no = value
    @property
    def claim_amount(self):
        return self._claim_amount

    @claim_amount.setter
    def claim_amount(self, value):
        self._claim_amount = value
    @property
    def claim_detail(self):
        return self._claim_detail

    @claim_detail.setter
    def claim_detail(self, value):
        self._claim_detail = value
    @property
    def claim_no(self):
        return self._claim_no

    @claim_no.setter
    def claim_no(self, value):
        self._claim_no = value
    @property
    def claim_status(self):
        return self._claim_status

    @claim_status.setter
    def claim_status(self, value):
        self._claim_status = value
    @property
    def claim_status_desc(self):
        return self._claim_status_desc

    @claim_status_desc.setter
    def claim_status_desc(self, value):
        self._claim_status_desc = value
    @property
    def claim_type(self):
        return self._claim_type

    @claim_type.setter
    def claim_type(self, value):
        self._claim_type = value
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
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def pay_account(self):
        return self._pay_account

    @pay_account.setter
    def pay_account(self, value):
        self._pay_account = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def to_send_info(self):
        return self._to_send_info

    @to_send_info.setter
    def to_send_info(self, value):
        if isinstance(value, PostInfo):
            self._to_send_info = value
        else:
            self._to_send_info = PostInfo.from_alipay_dict(value)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.advance_amount:
            if hasattr(self.advance_amount, 'to_alipay_dict'):
                params['advance_amount'] = self.advance_amount.to_alipay_dict()
            else:
                params['advance_amount'] = self.advance_amount
        if self.advance_apply_no:
            if hasattr(self.advance_apply_no, 'to_alipay_dict'):
                params['advance_apply_no'] = self.advance_apply_no.to_alipay_dict()
            else:
                params['advance_apply_no'] = self.advance_apply_no
        if self.ant_apply_no:
            if hasattr(self.ant_apply_no, 'to_alipay_dict'):
                params['ant_apply_no'] = self.ant_apply_no.to_alipay_dict()
            else:
                params['ant_apply_no'] = self.ant_apply_no
        if self.ant_claim_no:
            if hasattr(self.ant_claim_no, 'to_alipay_dict'):
                params['ant_claim_no'] = self.ant_claim_no.to_alipay_dict()
            else:
                params['ant_claim_no'] = self.ant_claim_no
        if self.business_no:
            if hasattr(self.business_no, 'to_alipay_dict'):
                params['business_no'] = self.business_no.to_alipay_dict()
            else:
                params['business_no'] = self.business_no
        if self.claim_amount:
            if hasattr(self.claim_amount, 'to_alipay_dict'):
                params['claim_amount'] = self.claim_amount.to_alipay_dict()
            else:
                params['claim_amount'] = self.claim_amount
        if self.claim_detail:
            if hasattr(self.claim_detail, 'to_alipay_dict'):
                params['claim_detail'] = self.claim_detail.to_alipay_dict()
            else:
                params['claim_detail'] = self.claim_detail
        if self.claim_no:
            if hasattr(self.claim_no, 'to_alipay_dict'):
                params['claim_no'] = self.claim_no.to_alipay_dict()
            else:
                params['claim_no'] = self.claim_no
        if self.claim_status:
            if hasattr(self.claim_status, 'to_alipay_dict'):
                params['claim_status'] = self.claim_status.to_alipay_dict()
            else:
                params['claim_status'] = self.claim_status
        if self.claim_status_desc:
            if hasattr(self.claim_status_desc, 'to_alipay_dict'):
                params['claim_status_desc'] = self.claim_status_desc.to_alipay_dict()
            else:
                params['claim_status_desc'] = self.claim_status_desc
        if self.claim_type:
            if hasattr(self.claim_type, 'to_alipay_dict'):
                params['claim_type'] = self.claim_type.to_alipay_dict()
            else:
                params['claim_type'] = self.claim_type
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
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.pay_account:
            if hasattr(self.pay_account, 'to_alipay_dict'):
                params['pay_account'] = self.pay_account.to_alipay_dict()
            else:
                params['pay_account'] = self.pay_account
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.to_send_info:
            if hasattr(self.to_send_info, 'to_alipay_dict'):
                params['to_send_info'] = self.to_send_info.to_alipay_dict()
            else:
                params['to_send_info'] = self.to_send_info
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
        o = AlipayCommerceMedicalInsuranceClaimSyncModel()
        if 'advance_amount' in d:
            o.advance_amount = d['advance_amount']
        if 'advance_apply_no' in d:
            o.advance_apply_no = d['advance_apply_no']
        if 'ant_apply_no' in d:
            o.ant_apply_no = d['ant_apply_no']
        if 'ant_claim_no' in d:
            o.ant_claim_no = d['ant_claim_no']
        if 'business_no' in d:
            o.business_no = d['business_no']
        if 'claim_amount' in d:
            o.claim_amount = d['claim_amount']
        if 'claim_detail' in d:
            o.claim_detail = d['claim_detail']
        if 'claim_no' in d:
            o.claim_no = d['claim_no']
        if 'claim_status' in d:
            o.claim_status = d['claim_status']
        if 'claim_status_desc' in d:
            o.claim_status_desc = d['claim_status_desc']
        if 'claim_type' in d:
            o.claim_type = d['claim_type']
        if 'company_type' in d:
            o.company_type = d['company_type']
        if 'identity_materials' in d:
            o.identity_materials = d['identity_materials']
        if 'lack_materials_sense' in d:
            o.lack_materials_sense = d['lack_materials_sense']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'pay_account' in d:
            o.pay_account = d['pay_account']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'source' in d:
            o.source = d['source']
        if 'to_send_info' in d:
            o.to_send_info = d['to_send_info']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


