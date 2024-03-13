#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpBasicInfo(object):

    def __init__(self):
        self._ep_address = None
        self._ep_appr_date = None
        self._ep_cert_no = None
        self._ep_name = None
        self._ep_open_to = None
        self._ep_operate_scope = None
        self._ep_reg_captial = None
        self._ep_reg_no = None
        self._ep_reg_org = None
        self._ep_status = None
        self._ep_type = None
        self._establish_date = None
        self._legal_person_name = None
        self._one_id = None

    @property
    def ep_address(self):
        return self._ep_address

    @ep_address.setter
    def ep_address(self, value):
        self._ep_address = value
    @property
    def ep_appr_date(self):
        return self._ep_appr_date

    @ep_appr_date.setter
    def ep_appr_date(self, value):
        self._ep_appr_date = value
    @property
    def ep_cert_no(self):
        return self._ep_cert_no

    @ep_cert_no.setter
    def ep_cert_no(self, value):
        self._ep_cert_no = value
    @property
    def ep_name(self):
        return self._ep_name

    @ep_name.setter
    def ep_name(self, value):
        self._ep_name = value
    @property
    def ep_open_to(self):
        return self._ep_open_to

    @ep_open_to.setter
    def ep_open_to(self, value):
        self._ep_open_to = value
    @property
    def ep_operate_scope(self):
        return self._ep_operate_scope

    @ep_operate_scope.setter
    def ep_operate_scope(self, value):
        self._ep_operate_scope = value
    @property
    def ep_reg_captial(self):
        return self._ep_reg_captial

    @ep_reg_captial.setter
    def ep_reg_captial(self, value):
        self._ep_reg_captial = value
    @property
    def ep_reg_no(self):
        return self._ep_reg_no

    @ep_reg_no.setter
    def ep_reg_no(self, value):
        self._ep_reg_no = value
    @property
    def ep_reg_org(self):
        return self._ep_reg_org

    @ep_reg_org.setter
    def ep_reg_org(self, value):
        self._ep_reg_org = value
    @property
    def ep_status(self):
        return self._ep_status

    @ep_status.setter
    def ep_status(self, value):
        self._ep_status = value
    @property
    def ep_type(self):
        return self._ep_type

    @ep_type.setter
    def ep_type(self, value):
        self._ep_type = value
    @property
    def establish_date(self):
        return self._establish_date

    @establish_date.setter
    def establish_date(self, value):
        self._establish_date = value
    @property
    def legal_person_name(self):
        return self._legal_person_name

    @legal_person_name.setter
    def legal_person_name(self, value):
        self._legal_person_name = value
    @property
    def one_id(self):
        return self._one_id

    @one_id.setter
    def one_id(self, value):
        self._one_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ep_address:
            if hasattr(self.ep_address, 'to_alipay_dict'):
                params['ep_address'] = self.ep_address.to_alipay_dict()
            else:
                params['ep_address'] = self.ep_address
        if self.ep_appr_date:
            if hasattr(self.ep_appr_date, 'to_alipay_dict'):
                params['ep_appr_date'] = self.ep_appr_date.to_alipay_dict()
            else:
                params['ep_appr_date'] = self.ep_appr_date
        if self.ep_cert_no:
            if hasattr(self.ep_cert_no, 'to_alipay_dict'):
                params['ep_cert_no'] = self.ep_cert_no.to_alipay_dict()
            else:
                params['ep_cert_no'] = self.ep_cert_no
        if self.ep_name:
            if hasattr(self.ep_name, 'to_alipay_dict'):
                params['ep_name'] = self.ep_name.to_alipay_dict()
            else:
                params['ep_name'] = self.ep_name
        if self.ep_open_to:
            if hasattr(self.ep_open_to, 'to_alipay_dict'):
                params['ep_open_to'] = self.ep_open_to.to_alipay_dict()
            else:
                params['ep_open_to'] = self.ep_open_to
        if self.ep_operate_scope:
            if hasattr(self.ep_operate_scope, 'to_alipay_dict'):
                params['ep_operate_scope'] = self.ep_operate_scope.to_alipay_dict()
            else:
                params['ep_operate_scope'] = self.ep_operate_scope
        if self.ep_reg_captial:
            if hasattr(self.ep_reg_captial, 'to_alipay_dict'):
                params['ep_reg_captial'] = self.ep_reg_captial.to_alipay_dict()
            else:
                params['ep_reg_captial'] = self.ep_reg_captial
        if self.ep_reg_no:
            if hasattr(self.ep_reg_no, 'to_alipay_dict'):
                params['ep_reg_no'] = self.ep_reg_no.to_alipay_dict()
            else:
                params['ep_reg_no'] = self.ep_reg_no
        if self.ep_reg_org:
            if hasattr(self.ep_reg_org, 'to_alipay_dict'):
                params['ep_reg_org'] = self.ep_reg_org.to_alipay_dict()
            else:
                params['ep_reg_org'] = self.ep_reg_org
        if self.ep_status:
            if hasattr(self.ep_status, 'to_alipay_dict'):
                params['ep_status'] = self.ep_status.to_alipay_dict()
            else:
                params['ep_status'] = self.ep_status
        if self.ep_type:
            if hasattr(self.ep_type, 'to_alipay_dict'):
                params['ep_type'] = self.ep_type.to_alipay_dict()
            else:
                params['ep_type'] = self.ep_type
        if self.establish_date:
            if hasattr(self.establish_date, 'to_alipay_dict'):
                params['establish_date'] = self.establish_date.to_alipay_dict()
            else:
                params['establish_date'] = self.establish_date
        if self.legal_person_name:
            if hasattr(self.legal_person_name, 'to_alipay_dict'):
                params['legal_person_name'] = self.legal_person_name.to_alipay_dict()
            else:
                params['legal_person_name'] = self.legal_person_name
        if self.one_id:
            if hasattr(self.one_id, 'to_alipay_dict'):
                params['one_id'] = self.one_id.to_alipay_dict()
            else:
                params['one_id'] = self.one_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpBasicInfo()
        if 'ep_address' in d:
            o.ep_address = d['ep_address']
        if 'ep_appr_date' in d:
            o.ep_appr_date = d['ep_appr_date']
        if 'ep_cert_no' in d:
            o.ep_cert_no = d['ep_cert_no']
        if 'ep_name' in d:
            o.ep_name = d['ep_name']
        if 'ep_open_to' in d:
            o.ep_open_to = d['ep_open_to']
        if 'ep_operate_scope' in d:
            o.ep_operate_scope = d['ep_operate_scope']
        if 'ep_reg_captial' in d:
            o.ep_reg_captial = d['ep_reg_captial']
        if 'ep_reg_no' in d:
            o.ep_reg_no = d['ep_reg_no']
        if 'ep_reg_org' in d:
            o.ep_reg_org = d['ep_reg_org']
        if 'ep_status' in d:
            o.ep_status = d['ep_status']
        if 'ep_type' in d:
            o.ep_type = d['ep_type']
        if 'establish_date' in d:
            o.establish_date = d['establish_date']
        if 'legal_person_name' in d:
            o.legal_person_name = d['legal_person_name']
        if 'one_id' in d:
            o.one_id = d['one_id']
        return o


