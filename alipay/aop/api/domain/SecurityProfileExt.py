#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SecurityCertProfileExt import SecurityCertProfileExt


class SecurityProfileExt(object):

    def __init__(self):
        self._enc_style = None
        self._gmt_create = None
        self._gmt_disable = None
        self._gmt_enable = None
        self._gmt_modified = None
        self._partner_id = None
        self._req_dec_algo = None
        self._req_dec_key = None
        self._req_verify_algo = None
        self._req_verify_key = None
        self._res_dec_key = None
        self._res_enc_algo = None
        self._res_enc_key = None
        self._res_sign_algo = None
        self._res_sign_alias = None
        self._res_sign_key = None
        self._res_verify_alias = None
        self._res_verify_key = None
        self._sec_des = None
        self._sec_id = None
        self._security_cert_profile_ext = None
        self._sign_style = None
        self._status = None
        self._sub_sec_id = None

    @property
    def enc_style(self):
        return self._enc_style

    @enc_style.setter
    def enc_style(self, value):
        self._enc_style = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_disable(self):
        return self._gmt_disable

    @gmt_disable.setter
    def gmt_disable(self, value):
        self._gmt_disable = value
    @property
    def gmt_enable(self):
        return self._gmt_enable

    @gmt_enable.setter
    def gmt_enable(self, value):
        self._gmt_enable = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def req_dec_algo(self):
        return self._req_dec_algo

    @req_dec_algo.setter
    def req_dec_algo(self, value):
        self._req_dec_algo = value
    @property
    def req_dec_key(self):
        return self._req_dec_key

    @req_dec_key.setter
    def req_dec_key(self, value):
        self._req_dec_key = value
    @property
    def req_verify_algo(self):
        return self._req_verify_algo

    @req_verify_algo.setter
    def req_verify_algo(self, value):
        self._req_verify_algo = value
    @property
    def req_verify_key(self):
        return self._req_verify_key

    @req_verify_key.setter
    def req_verify_key(self, value):
        self._req_verify_key = value
    @property
    def res_dec_key(self):
        return self._res_dec_key

    @res_dec_key.setter
    def res_dec_key(self, value):
        self._res_dec_key = value
    @property
    def res_enc_algo(self):
        return self._res_enc_algo

    @res_enc_algo.setter
    def res_enc_algo(self, value):
        self._res_enc_algo = value
    @property
    def res_enc_key(self):
        return self._res_enc_key

    @res_enc_key.setter
    def res_enc_key(self, value):
        self._res_enc_key = value
    @property
    def res_sign_algo(self):
        return self._res_sign_algo

    @res_sign_algo.setter
    def res_sign_algo(self, value):
        self._res_sign_algo = value
    @property
    def res_sign_alias(self):
        return self._res_sign_alias

    @res_sign_alias.setter
    def res_sign_alias(self, value):
        self._res_sign_alias = value
    @property
    def res_sign_key(self):
        return self._res_sign_key

    @res_sign_key.setter
    def res_sign_key(self, value):
        self._res_sign_key = value
    @property
    def res_verify_alias(self):
        return self._res_verify_alias

    @res_verify_alias.setter
    def res_verify_alias(self, value):
        self._res_verify_alias = value
    @property
    def res_verify_key(self):
        return self._res_verify_key

    @res_verify_key.setter
    def res_verify_key(self, value):
        self._res_verify_key = value
    @property
    def sec_des(self):
        return self._sec_des

    @sec_des.setter
    def sec_des(self, value):
        self._sec_des = value
    @property
    def sec_id(self):
        return self._sec_id

    @sec_id.setter
    def sec_id(self, value):
        self._sec_id = value
    @property
    def security_cert_profile_ext(self):
        return self._security_cert_profile_ext

    @security_cert_profile_ext.setter
    def security_cert_profile_ext(self, value):
        if isinstance(value, SecurityCertProfileExt):
            self._security_cert_profile_ext = value
        else:
            self._security_cert_profile_ext = SecurityCertProfileExt.from_alipay_dict(value)
    @property
    def sign_style(self):
        return self._sign_style

    @sign_style.setter
    def sign_style(self, value):
        self._sign_style = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_sec_id(self):
        return self._sub_sec_id

    @sub_sec_id.setter
    def sub_sec_id(self, value):
        self._sub_sec_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.enc_style:
            if hasattr(self.enc_style, 'to_alipay_dict'):
                params['enc_style'] = self.enc_style.to_alipay_dict()
            else:
                params['enc_style'] = self.enc_style
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_disable:
            if hasattr(self.gmt_disable, 'to_alipay_dict'):
                params['gmt_disable'] = self.gmt_disable.to_alipay_dict()
            else:
                params['gmt_disable'] = self.gmt_disable
        if self.gmt_enable:
            if hasattr(self.gmt_enable, 'to_alipay_dict'):
                params['gmt_enable'] = self.gmt_enable.to_alipay_dict()
            else:
                params['gmt_enable'] = self.gmt_enable
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.req_dec_algo:
            if hasattr(self.req_dec_algo, 'to_alipay_dict'):
                params['req_dec_algo'] = self.req_dec_algo.to_alipay_dict()
            else:
                params['req_dec_algo'] = self.req_dec_algo
        if self.req_dec_key:
            if hasattr(self.req_dec_key, 'to_alipay_dict'):
                params['req_dec_key'] = self.req_dec_key.to_alipay_dict()
            else:
                params['req_dec_key'] = self.req_dec_key
        if self.req_verify_algo:
            if hasattr(self.req_verify_algo, 'to_alipay_dict'):
                params['req_verify_algo'] = self.req_verify_algo.to_alipay_dict()
            else:
                params['req_verify_algo'] = self.req_verify_algo
        if self.req_verify_key:
            if hasattr(self.req_verify_key, 'to_alipay_dict'):
                params['req_verify_key'] = self.req_verify_key.to_alipay_dict()
            else:
                params['req_verify_key'] = self.req_verify_key
        if self.res_dec_key:
            if hasattr(self.res_dec_key, 'to_alipay_dict'):
                params['res_dec_key'] = self.res_dec_key.to_alipay_dict()
            else:
                params['res_dec_key'] = self.res_dec_key
        if self.res_enc_algo:
            if hasattr(self.res_enc_algo, 'to_alipay_dict'):
                params['res_enc_algo'] = self.res_enc_algo.to_alipay_dict()
            else:
                params['res_enc_algo'] = self.res_enc_algo
        if self.res_enc_key:
            if hasattr(self.res_enc_key, 'to_alipay_dict'):
                params['res_enc_key'] = self.res_enc_key.to_alipay_dict()
            else:
                params['res_enc_key'] = self.res_enc_key
        if self.res_sign_algo:
            if hasattr(self.res_sign_algo, 'to_alipay_dict'):
                params['res_sign_algo'] = self.res_sign_algo.to_alipay_dict()
            else:
                params['res_sign_algo'] = self.res_sign_algo
        if self.res_sign_alias:
            if hasattr(self.res_sign_alias, 'to_alipay_dict'):
                params['res_sign_alias'] = self.res_sign_alias.to_alipay_dict()
            else:
                params['res_sign_alias'] = self.res_sign_alias
        if self.res_sign_key:
            if hasattr(self.res_sign_key, 'to_alipay_dict'):
                params['res_sign_key'] = self.res_sign_key.to_alipay_dict()
            else:
                params['res_sign_key'] = self.res_sign_key
        if self.res_verify_alias:
            if hasattr(self.res_verify_alias, 'to_alipay_dict'):
                params['res_verify_alias'] = self.res_verify_alias.to_alipay_dict()
            else:
                params['res_verify_alias'] = self.res_verify_alias
        if self.res_verify_key:
            if hasattr(self.res_verify_key, 'to_alipay_dict'):
                params['res_verify_key'] = self.res_verify_key.to_alipay_dict()
            else:
                params['res_verify_key'] = self.res_verify_key
        if self.sec_des:
            if hasattr(self.sec_des, 'to_alipay_dict'):
                params['sec_des'] = self.sec_des.to_alipay_dict()
            else:
                params['sec_des'] = self.sec_des
        if self.sec_id:
            if hasattr(self.sec_id, 'to_alipay_dict'):
                params['sec_id'] = self.sec_id.to_alipay_dict()
            else:
                params['sec_id'] = self.sec_id
        if self.security_cert_profile_ext:
            if hasattr(self.security_cert_profile_ext, 'to_alipay_dict'):
                params['security_cert_profile_ext'] = self.security_cert_profile_ext.to_alipay_dict()
            else:
                params['security_cert_profile_ext'] = self.security_cert_profile_ext
        if self.sign_style:
            if hasattr(self.sign_style, 'to_alipay_dict'):
                params['sign_style'] = self.sign_style.to_alipay_dict()
            else:
                params['sign_style'] = self.sign_style
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.sub_sec_id:
            if hasattr(self.sub_sec_id, 'to_alipay_dict'):
                params['sub_sec_id'] = self.sub_sec_id.to_alipay_dict()
            else:
                params['sub_sec_id'] = self.sub_sec_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SecurityProfileExt()
        if 'enc_style' in d:
            o.enc_style = d['enc_style']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_disable' in d:
            o.gmt_disable = d['gmt_disable']
        if 'gmt_enable' in d:
            o.gmt_enable = d['gmt_enable']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'req_dec_algo' in d:
            o.req_dec_algo = d['req_dec_algo']
        if 'req_dec_key' in d:
            o.req_dec_key = d['req_dec_key']
        if 'req_verify_algo' in d:
            o.req_verify_algo = d['req_verify_algo']
        if 'req_verify_key' in d:
            o.req_verify_key = d['req_verify_key']
        if 'res_dec_key' in d:
            o.res_dec_key = d['res_dec_key']
        if 'res_enc_algo' in d:
            o.res_enc_algo = d['res_enc_algo']
        if 'res_enc_key' in d:
            o.res_enc_key = d['res_enc_key']
        if 'res_sign_algo' in d:
            o.res_sign_algo = d['res_sign_algo']
        if 'res_sign_alias' in d:
            o.res_sign_alias = d['res_sign_alias']
        if 'res_sign_key' in d:
            o.res_sign_key = d['res_sign_key']
        if 'res_verify_alias' in d:
            o.res_verify_alias = d['res_verify_alias']
        if 'res_verify_key' in d:
            o.res_verify_key = d['res_verify_key']
        if 'sec_des' in d:
            o.sec_des = d['sec_des']
        if 'sec_id' in d:
            o.sec_id = d['sec_id']
        if 'security_cert_profile_ext' in d:
            o.security_cert_profile_ext = d['security_cert_profile_ext']
        if 'sign_style' in d:
            o.sign_style = d['sign_style']
        if 'status' in d:
            o.status = d['status']
        if 'sub_sec_id' in d:
            o.sub_sec_id = d['sub_sec_id']
        return o


