#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentAgreementInfo(object):

    def __init__(self):
        self._agreement_no = None
        self._deduct_agreement_no = None
        self._rent_logon_id = None
        self._rent_user_id = None
        self._rent_user_open_id = None

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
    def rent_logon_id(self):
        return self._rent_logon_id

    @rent_logon_id.setter
    def rent_logon_id(self, value):
        self._rent_logon_id = value
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
        if self.rent_logon_id:
            if hasattr(self.rent_logon_id, 'to_alipay_dict'):
                params['rent_logon_id'] = self.rent_logon_id.to_alipay_dict()
            else:
                params['rent_logon_id'] = self.rent_logon_id
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentAgreementInfo()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'deduct_agreement_no' in d:
            o.deduct_agreement_no = d['deduct_agreement_no']
        if 'rent_logon_id' in d:
            o.rent_logon_id = d['rent_logon_id']
        if 'rent_user_id' in d:
            o.rent_user_id = d['rent_user_id']
        if 'rent_user_open_id' in d:
            o.rent_user_open_id = d['rent_user_open_id']
        return o


