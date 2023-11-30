#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EntBasicInfo(object):

    def __init__(self):
        self._address = None
        self._appr_date = None
        self._cancel_date = None
        self._credit_code = None
        self._ent_name = None
        self._ent_status = None
        self._ent_type = None
        self._es_date = None
        self._fr_name = None
        self._industry_code = None
        self._industry_name = None
        self._industry_phy_code = None
        self._industry_phy_name = None
        self._open_from = None
        self._open_to = None
        self._operate_scope = None
        self._reg_cap = None
        self._reg_cap_cur = None
        self._reg_no = None
        self._reg_org = None
        self._revoke_date = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def appr_date(self):
        return self._appr_date

    @appr_date.setter
    def appr_date(self, value):
        self._appr_date = value
    @property
    def cancel_date(self):
        return self._cancel_date

    @cancel_date.setter
    def cancel_date(self, value):
        self._cancel_date = value
    @property
    def credit_code(self):
        return self._credit_code

    @credit_code.setter
    def credit_code(self, value):
        self._credit_code = value
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
    def industry_code(self):
        return self._industry_code

    @industry_code.setter
    def industry_code(self, value):
        self._industry_code = value
    @property
    def industry_name(self):
        return self._industry_name

    @industry_name.setter
    def industry_name(self, value):
        self._industry_name = value
    @property
    def industry_phy_code(self):
        return self._industry_phy_code

    @industry_phy_code.setter
    def industry_phy_code(self, value):
        self._industry_phy_code = value
    @property
    def industry_phy_name(self):
        return self._industry_phy_name

    @industry_phy_name.setter
    def industry_phy_name(self, value):
        self._industry_phy_name = value
    @property
    def open_from(self):
        return self._open_from

    @open_from.setter
    def open_from(self, value):
        self._open_from = value
    @property
    def open_to(self):
        return self._open_to

    @open_to.setter
    def open_to(self, value):
        self._open_to = value
    @property
    def operate_scope(self):
        return self._operate_scope

    @operate_scope.setter
    def operate_scope(self, value):
        self._operate_scope = value
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
    def reg_org(self):
        return self._reg_org

    @reg_org.setter
    def reg_org(self, value):
        self._reg_org = value
    @property
    def revoke_date(self):
        return self._revoke_date

    @revoke_date.setter
    def revoke_date(self, value):
        self._revoke_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.appr_date:
            if hasattr(self.appr_date, 'to_alipay_dict'):
                params['appr_date'] = self.appr_date.to_alipay_dict()
            else:
                params['appr_date'] = self.appr_date
        if self.cancel_date:
            if hasattr(self.cancel_date, 'to_alipay_dict'):
                params['cancel_date'] = self.cancel_date.to_alipay_dict()
            else:
                params['cancel_date'] = self.cancel_date
        if self.credit_code:
            if hasattr(self.credit_code, 'to_alipay_dict'):
                params['credit_code'] = self.credit_code.to_alipay_dict()
            else:
                params['credit_code'] = self.credit_code
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
        if self.industry_code:
            if hasattr(self.industry_code, 'to_alipay_dict'):
                params['industry_code'] = self.industry_code.to_alipay_dict()
            else:
                params['industry_code'] = self.industry_code
        if self.industry_name:
            if hasattr(self.industry_name, 'to_alipay_dict'):
                params['industry_name'] = self.industry_name.to_alipay_dict()
            else:
                params['industry_name'] = self.industry_name
        if self.industry_phy_code:
            if hasattr(self.industry_phy_code, 'to_alipay_dict'):
                params['industry_phy_code'] = self.industry_phy_code.to_alipay_dict()
            else:
                params['industry_phy_code'] = self.industry_phy_code
        if self.industry_phy_name:
            if hasattr(self.industry_phy_name, 'to_alipay_dict'):
                params['industry_phy_name'] = self.industry_phy_name.to_alipay_dict()
            else:
                params['industry_phy_name'] = self.industry_phy_name
        if self.open_from:
            if hasattr(self.open_from, 'to_alipay_dict'):
                params['open_from'] = self.open_from.to_alipay_dict()
            else:
                params['open_from'] = self.open_from
        if self.open_to:
            if hasattr(self.open_to, 'to_alipay_dict'):
                params['open_to'] = self.open_to.to_alipay_dict()
            else:
                params['open_to'] = self.open_to
        if self.operate_scope:
            if hasattr(self.operate_scope, 'to_alipay_dict'):
                params['operate_scope'] = self.operate_scope.to_alipay_dict()
            else:
                params['operate_scope'] = self.operate_scope
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
        if self.reg_org:
            if hasattr(self.reg_org, 'to_alipay_dict'):
                params['reg_org'] = self.reg_org.to_alipay_dict()
            else:
                params['reg_org'] = self.reg_org
        if self.revoke_date:
            if hasattr(self.revoke_date, 'to_alipay_dict'):
                params['revoke_date'] = self.revoke_date.to_alipay_dict()
            else:
                params['revoke_date'] = self.revoke_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EntBasicInfo()
        if 'address' in d:
            o.address = d['address']
        if 'appr_date' in d:
            o.appr_date = d['appr_date']
        if 'cancel_date' in d:
            o.cancel_date = d['cancel_date']
        if 'credit_code' in d:
            o.credit_code = d['credit_code']
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
        if 'industry_code' in d:
            o.industry_code = d['industry_code']
        if 'industry_name' in d:
            o.industry_name = d['industry_name']
        if 'industry_phy_code' in d:
            o.industry_phy_code = d['industry_phy_code']
        if 'industry_phy_name' in d:
            o.industry_phy_name = d['industry_phy_name']
        if 'open_from' in d:
            o.open_from = d['open_from']
        if 'open_to' in d:
            o.open_to = d['open_to']
        if 'operate_scope' in d:
            o.operate_scope = d['operate_scope']
        if 'reg_cap' in d:
            o.reg_cap = d['reg_cap']
        if 'reg_cap_cur' in d:
            o.reg_cap_cur = d['reg_cap_cur']
        if 'reg_no' in d:
            o.reg_no = d['reg_no']
        if 'reg_org' in d:
            o.reg_org = d['reg_org']
        if 'revoke_date' in d:
            o.revoke_date = d['revoke_date']
        return o


