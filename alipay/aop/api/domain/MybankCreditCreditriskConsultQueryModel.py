#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InvolvedEntity import InvolvedEntity


class MybankCreditCreditriskConsultQueryModel(object):

    def __init__(self):
        self._associate_entitys = None
        self._ext_par = None
        self._ip_id = None
        self._ip_role_id = None
        self._out_uni_code = None
        self._pd_code = None
        self._scen = None
        self._site = None
        self._site_login_id = None
        self._site_user_id = None

    @property
    def associate_entitys(self):
        return self._associate_entitys

    @associate_entitys.setter
    def associate_entitys(self, value):
        if isinstance(value, list):
            self._associate_entitys = list()
            for i in value:
                if isinstance(i, InvolvedEntity):
                    self._associate_entitys.append(i)
                else:
                    self._associate_entitys.append(InvolvedEntity.from_alipay_dict(i))
    @property
    def ext_par(self):
        return self._ext_par

    @ext_par.setter
    def ext_par(self, value):
        self._ext_par = value
    @property
    def ip_id(self):
        return self._ip_id

    @ip_id.setter
    def ip_id(self, value):
        self._ip_id = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def out_uni_code(self):
        return self._out_uni_code

    @out_uni_code.setter
    def out_uni_code(self, value):
        self._out_uni_code = value
    @property
    def pd_code(self):
        return self._pd_code

    @pd_code.setter
    def pd_code(self, value):
        self._pd_code = value
    @property
    def scen(self):
        return self._scen

    @scen.setter
    def scen(self, value):
        self._scen = value
    @property
    def site(self):
        return self._site

    @site.setter
    def site(self, value):
        self._site = value
    @property
    def site_login_id(self):
        return self._site_login_id

    @site_login_id.setter
    def site_login_id(self, value):
        self._site_login_id = value
    @property
    def site_user_id(self):
        return self._site_user_id

    @site_user_id.setter
    def site_user_id(self, value):
        self._site_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.associate_entitys:
            if isinstance(self.associate_entitys, list):
                for i in range(0, len(self.associate_entitys)):
                    element = self.associate_entitys[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.associate_entitys[i] = element.to_alipay_dict()
            if hasattr(self.associate_entitys, 'to_alipay_dict'):
                params['associate_entitys'] = self.associate_entitys.to_alipay_dict()
            else:
                params['associate_entitys'] = self.associate_entitys
        if self.ext_par:
            if hasattr(self.ext_par, 'to_alipay_dict'):
                params['ext_par'] = self.ext_par.to_alipay_dict()
            else:
                params['ext_par'] = self.ext_par
        if self.ip_id:
            if hasattr(self.ip_id, 'to_alipay_dict'):
                params['ip_id'] = self.ip_id.to_alipay_dict()
            else:
                params['ip_id'] = self.ip_id
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.out_uni_code:
            if hasattr(self.out_uni_code, 'to_alipay_dict'):
                params['out_uni_code'] = self.out_uni_code.to_alipay_dict()
            else:
                params['out_uni_code'] = self.out_uni_code
        if self.pd_code:
            if hasattr(self.pd_code, 'to_alipay_dict'):
                params['pd_code'] = self.pd_code.to_alipay_dict()
            else:
                params['pd_code'] = self.pd_code
        if self.scen:
            if hasattr(self.scen, 'to_alipay_dict'):
                params['scen'] = self.scen.to_alipay_dict()
            else:
                params['scen'] = self.scen
        if self.site:
            if hasattr(self.site, 'to_alipay_dict'):
                params['site'] = self.site.to_alipay_dict()
            else:
                params['site'] = self.site
        if self.site_login_id:
            if hasattr(self.site_login_id, 'to_alipay_dict'):
                params['site_login_id'] = self.site_login_id.to_alipay_dict()
            else:
                params['site_login_id'] = self.site_login_id
        if self.site_user_id:
            if hasattr(self.site_user_id, 'to_alipay_dict'):
                params['site_user_id'] = self.site_user_id.to_alipay_dict()
            else:
                params['site_user_id'] = self.site_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditCreditriskConsultQueryModel()
        if 'associate_entitys' in d:
            o.associate_entitys = d['associate_entitys']
        if 'ext_par' in d:
            o.ext_par = d['ext_par']
        if 'ip_id' in d:
            o.ip_id = d['ip_id']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'out_uni_code' in d:
            o.out_uni_code = d['out_uni_code']
        if 'pd_code' in d:
            o.pd_code = d['pd_code']
        if 'scen' in d:
            o.scen = d['scen']
        if 'site' in d:
            o.site = d['site']
        if 'site_login_id' in d:
            o.site_login_id = d['site_login_id']
        if 'site_user_id' in d:
            o.site_user_id = d['site_user_id']
        return o


