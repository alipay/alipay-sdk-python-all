#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CompanyRelationInfo(object):

    def __init__(self):
        self._check_date = None
        self._credit_code = None
        self._ent_id = None
        self._ent_name = None
        self._ent_status = None
        self._ent_type = None
        self._es_date = None
        self._fr_name = None
        self._reg_addr = None
        self._reg_cap = None
        self._reg_cap_cur = None
        self._reg_no = None
        self._rel_type_code = None

    @property
    def check_date(self):
        return self._check_date

    @check_date.setter
    def check_date(self, value):
        self._check_date = value
    @property
    def credit_code(self):
        return self._credit_code

    @credit_code.setter
    def credit_code(self, value):
        self._credit_code = value
    @property
    def ent_id(self):
        return self._ent_id

    @ent_id.setter
    def ent_id(self, value):
        self._ent_id = value
    @property
    def ent_name(self):
        return self._ent_name

    @ent_name.setter
    def ent_name(self, value):
        self._ent_name = value
    @property
    def ent_status(self):
        return self._ent_status

    @ent_status.setter
    def ent_status(self, value):
        self._ent_status = value
    @property
    def ent_type(self):
        return self._ent_type

    @ent_type.setter
    def ent_type(self, value):
        self._ent_type = value
    @property
    def es_date(self):
        return self._es_date

    @es_date.setter
    def es_date(self, value):
        self._es_date = value
    @property
    def fr_name(self):
        return self._fr_name

    @fr_name.setter
    def fr_name(self, value):
        self._fr_name = value
    @property
    def reg_addr(self):
        return self._reg_addr

    @reg_addr.setter
    def reg_addr(self, value):
        self._reg_addr = value
    @property
    def reg_cap(self):
        return self._reg_cap

    @reg_cap.setter
    def reg_cap(self, value):
        self._reg_cap = value
    @property
    def reg_cap_cur(self):
        return self._reg_cap_cur

    @reg_cap_cur.setter
    def reg_cap_cur(self, value):
        self._reg_cap_cur = value
    @property
    def reg_no(self):
        return self._reg_no

    @reg_no.setter
    def reg_no(self, value):
        self._reg_no = value
    @property
    def rel_type_code(self):
        return self._rel_type_code

    @rel_type_code.setter
    def rel_type_code(self, value):
        self._rel_type_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.check_date:
            if hasattr(self.check_date, 'to_alipay_dict'):
                params['check_date'] = self.check_date.to_alipay_dict()
            else:
                params['check_date'] = self.check_date
        if self.credit_code:
            if hasattr(self.credit_code, 'to_alipay_dict'):
                params['credit_code'] = self.credit_code.to_alipay_dict()
            else:
                params['credit_code'] = self.credit_code
        if self.ent_id:
            if hasattr(self.ent_id, 'to_alipay_dict'):
                params['ent_id'] = self.ent_id.to_alipay_dict()
            else:
                params['ent_id'] = self.ent_id
        if self.ent_name:
            if hasattr(self.ent_name, 'to_alipay_dict'):
                params['ent_name'] = self.ent_name.to_alipay_dict()
            else:
                params['ent_name'] = self.ent_name
        if self.ent_status:
            if hasattr(self.ent_status, 'to_alipay_dict'):
                params['ent_status'] = self.ent_status.to_alipay_dict()
            else:
                params['ent_status'] = self.ent_status
        if self.ent_type:
            if hasattr(self.ent_type, 'to_alipay_dict'):
                params['ent_type'] = self.ent_type.to_alipay_dict()
            else:
                params['ent_type'] = self.ent_type
        if self.es_date:
            if hasattr(self.es_date, 'to_alipay_dict'):
                params['es_date'] = self.es_date.to_alipay_dict()
            else:
                params['es_date'] = self.es_date
        if self.fr_name:
            if hasattr(self.fr_name, 'to_alipay_dict'):
                params['fr_name'] = self.fr_name.to_alipay_dict()
            else:
                params['fr_name'] = self.fr_name
        if self.reg_addr:
            if hasattr(self.reg_addr, 'to_alipay_dict'):
                params['reg_addr'] = self.reg_addr.to_alipay_dict()
            else:
                params['reg_addr'] = self.reg_addr
        if self.reg_cap:
            if hasattr(self.reg_cap, 'to_alipay_dict'):
                params['reg_cap'] = self.reg_cap.to_alipay_dict()
            else:
                params['reg_cap'] = self.reg_cap
        if self.reg_cap_cur:
            if hasattr(self.reg_cap_cur, 'to_alipay_dict'):
                params['reg_cap_cur'] = self.reg_cap_cur.to_alipay_dict()
            else:
                params['reg_cap_cur'] = self.reg_cap_cur
        if self.reg_no:
            if hasattr(self.reg_no, 'to_alipay_dict'):
                params['reg_no'] = self.reg_no.to_alipay_dict()
            else:
                params['reg_no'] = self.reg_no
        if self.rel_type_code:
            if hasattr(self.rel_type_code, 'to_alipay_dict'):
                params['rel_type_code'] = self.rel_type_code.to_alipay_dict()
            else:
                params['rel_type_code'] = self.rel_type_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CompanyRelationInfo()
        if 'check_date' in d:
            o.check_date = d['check_date']
        if 'credit_code' in d:
            o.credit_code = d['credit_code']
        if 'ent_id' in d:
            o.ent_id = d['ent_id']
        if 'ent_name' in d:
            o.ent_name = d['ent_name']
        if 'ent_status' in d:
            o.ent_status = d['ent_status']
        if 'ent_type' in d:
            o.ent_type = d['ent_type']
        if 'es_date' in d:
            o.es_date = d['es_date']
        if 'fr_name' in d:
            o.fr_name = d['fr_name']
        if 'reg_addr' in d:
            o.reg_addr = d['reg_addr']
        if 'reg_cap' in d:
            o.reg_cap = d['reg_cap']
        if 'reg_cap_cur' in d:
            o.reg_cap_cur = d['reg_cap_cur']
        if 'reg_no' in d:
            o.reg_no = d['reg_no']
        if 'rel_type_code' in d:
            o.rel_type_code = d['rel_type_code']
        return o


