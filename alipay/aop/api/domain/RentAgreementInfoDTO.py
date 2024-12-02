#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentAgreementInfoDTO(object):

    def __init__(self):
        self._agreement_no = None
        self._deduct_agreement_no = None
        self._personal_product_code = None
        self._rent_user_id = None
        self._rent_user_open_id = None
        self._status = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def deduct_agreement_no(self):
        return self._deduct_agreement_no

    @deduct_agreement_no.setter
    def deduct_agreement_no(self, value):
        self._deduct_agreement_no = value
    @property
    def personal_product_code(self):
        return self._personal_product_code

    @personal_product_code.setter
    def personal_product_code(self, value):
        self._personal_product_code = value
    @property
    def rent_user_id(self):
        return self._rent_user_id

    @rent_user_id.setter
    def rent_user_id(self, value):
        self._rent_user_id = value
    @property
    def rent_user_open_id(self):
        return self._rent_user_open_id

    @rent_user_open_id.setter
    def rent_user_open_id(self, value):
        self._rent_user_open_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.deduct_agreement_no:
            if hasattr(self.deduct_agreement_no, 'to_alipay_dict'):
                params['deduct_agreement_no'] = self.deduct_agreement_no.to_alipay_dict()
            else:
                params['deduct_agreement_no'] = self.deduct_agreement_no
        if self.personal_product_code:
            if hasattr(self.personal_product_code, 'to_alipay_dict'):
                params['personal_product_code'] = self.personal_product_code.to_alipay_dict()
            else:
                params['personal_product_code'] = self.personal_product_code
        if self.rent_user_id:
            if hasattr(self.rent_user_id, 'to_alipay_dict'):
                params['rent_user_id'] = self.rent_user_id.to_alipay_dict()
            else:
                params['rent_user_id'] = self.rent_user_id
        if self.rent_user_open_id:
            if hasattr(self.rent_user_open_id, 'to_alipay_dict'):
                params['rent_user_open_id'] = self.rent_user_open_id.to_alipay_dict()
            else:
                params['rent_user_open_id'] = self.rent_user_open_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentAgreementInfoDTO()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'deduct_agreement_no' in d:
            o.deduct_agreement_no = d['deduct_agreement_no']
        if 'personal_product_code' in d:
            o.personal_product_code = d['personal_product_code']
        if 'rent_user_id' in d:
            o.rent_user_id = d['rent_user_id']
        if 'rent_user_open_id' in d:
            o.rent_user_open_id = d['rent_user_open_id']
        if 'status' in d:
            o.status = d['status']
        return o


