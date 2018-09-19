#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InvolvedEntity import InvolvedEntity


class MybankCreditLoanapplyApplyCreateModel(object):

    def __init__(self):
        self._alipay_id = None
        self._apply_lmt = None
        self._associate_entitys = None
        self._biz_no = None
        self._biz_scene_no = None
        self._biz_tag = None
        self._cert_no = None
        self._cert_type = None
        self._email = None
        self._ext_par = None
        self._ip_id = None
        self._ip_role_id = None
        self._login_id = None
        self._mobile = None
        self._name = None
        self._op_pd_code = None
        self._out_mem_id = None
        self._out_uni_code = None
        self._request_id = None
        self._site = None
        self._site_user_id = None

    @property
    def alipay_id(self):
        return self._alipay_id

    @alipay_id.setter
    def alipay_id(self, value):
        self._alipay_id = value
    @property
    def apply_lmt(self):
        return self._apply_lmt

    @apply_lmt.setter
    def apply_lmt(self, value):
        self._apply_lmt = value
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
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def biz_scene_no(self):
        return self._biz_scene_no

    @biz_scene_no.setter
    def biz_scene_no(self, value):
        self._biz_scene_no = value
    @property
    def biz_tag(self):
        return self._biz_tag

    @biz_tag.setter
    def biz_tag(self, value):
        self._biz_tag = value
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
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
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
    def login_id(self):
        return self._login_id

    @login_id.setter
    def login_id(self, value):
        self._login_id = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def op_pd_code(self):
        return self._op_pd_code

    @op_pd_code.setter
    def op_pd_code(self, value):
        self._op_pd_code = value
    @property
    def out_mem_id(self):
        return self._out_mem_id

    @out_mem_id.setter
    def out_mem_id(self, value):
        self._out_mem_id = value
    @property
    def out_uni_code(self):
        return self._out_uni_code

    @out_uni_code.setter
    def out_uni_code(self, value):
        self._out_uni_code = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def site(self):
        return self._site

    @site.setter
    def site(self, value):
        self._site = value
    @property
    def site_user_id(self):
        return self._site_user_id

    @site_user_id.setter
    def site_user_id(self, value):
        self._site_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_id:
            if hasattr(self.alipay_id, 'to_alipay_dict'):
                params['alipay_id'] = self.alipay_id.to_alipay_dict()
            else:
                params['alipay_id'] = self.alipay_id
        if self.apply_lmt:
            if hasattr(self.apply_lmt, 'to_alipay_dict'):
                params['apply_lmt'] = self.apply_lmt.to_alipay_dict()
            else:
                params['apply_lmt'] = self.apply_lmt
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
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.biz_scene_no:
            if hasattr(self.biz_scene_no, 'to_alipay_dict'):
                params['biz_scene_no'] = self.biz_scene_no.to_alipay_dict()
            else:
                params['biz_scene_no'] = self.biz_scene_no
        if self.biz_tag:
            if hasattr(self.biz_tag, 'to_alipay_dict'):
                params['biz_tag'] = self.biz_tag.to_alipay_dict()
            else:
                params['biz_tag'] = self.biz_tag
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
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
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
        if self.login_id:
            if hasattr(self.login_id, 'to_alipay_dict'):
                params['login_id'] = self.login_id.to_alipay_dict()
            else:
                params['login_id'] = self.login_id
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.op_pd_code:
            if hasattr(self.op_pd_code, 'to_alipay_dict'):
                params['op_pd_code'] = self.op_pd_code.to_alipay_dict()
            else:
                params['op_pd_code'] = self.op_pd_code
        if self.out_mem_id:
            if hasattr(self.out_mem_id, 'to_alipay_dict'):
                params['out_mem_id'] = self.out_mem_id.to_alipay_dict()
            else:
                params['out_mem_id'] = self.out_mem_id
        if self.out_uni_code:
            if hasattr(self.out_uni_code, 'to_alipay_dict'):
                params['out_uni_code'] = self.out_uni_code.to_alipay_dict()
            else:
                params['out_uni_code'] = self.out_uni_code
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.site:
            if hasattr(self.site, 'to_alipay_dict'):
                params['site'] = self.site.to_alipay_dict()
            else:
                params['site'] = self.site
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
        o = MybankCreditLoanapplyApplyCreateModel()
        if 'alipay_id' in d:
            o.alipay_id = d['alipay_id']
        if 'apply_lmt' in d:
            o.apply_lmt = d['apply_lmt']
        if 'associate_entitys' in d:
            o.associate_entitys = d['associate_entitys']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'biz_scene_no' in d:
            o.biz_scene_no = d['biz_scene_no']
        if 'biz_tag' in d:
            o.biz_tag = d['biz_tag']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'email' in d:
            o.email = d['email']
        if 'ext_par' in d:
            o.ext_par = d['ext_par']
        if 'ip_id' in d:
            o.ip_id = d['ip_id']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'login_id' in d:
            o.login_id = d['login_id']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'name' in d:
            o.name = d['name']
        if 'op_pd_code' in d:
            o.op_pd_code = d['op_pd_code']
        if 'out_mem_id' in d:
            o.out_mem_id = d['out_mem_id']
        if 'out_uni_code' in d:
            o.out_uni_code = d['out_uni_code']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'site' in d:
            o.site = d['site']
        if 'site_user_id' in d:
            o.site_user_id = d['site_user_id']
        return o


