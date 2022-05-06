#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AuthExtendParams import AuthExtendParams


class AlipayCommerceMedicalAuthinfoAuthQueryModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._call_url = None
        self._extend_params = None
        self._ins_code = None
        self._ol_biz_type_code = None
        self._org_app_id = None
        self._org_chnl_crtf_code = None
        self._org_code = None
        self._req_biz_no = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def call_url(self):
        return self._call_url

    @call_url.setter
    def call_url(self, value):
        self._call_url = value
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        if isinstance(value, AuthExtendParams):
            self._extend_params = value
        else:
            self._extend_params = AuthExtendParams.from_alipay_dict(value)
    @property
    def ins_code(self):
        return self._ins_code

    @ins_code.setter
    def ins_code(self, value):
        self._ins_code = value
    @property
    def ol_biz_type_code(self):
        return self._ol_biz_type_code

    @ol_biz_type_code.setter
    def ol_biz_type_code(self, value):
        self._ol_biz_type_code = value
    @property
    def org_app_id(self):
        return self._org_app_id

    @org_app_id.setter
    def org_app_id(self, value):
        self._org_app_id = value
    @property
    def org_chnl_crtf_code(self):
        return self._org_chnl_crtf_code

    @org_chnl_crtf_code.setter
    def org_chnl_crtf_code(self, value):
        self._org_chnl_crtf_code = value
    @property
    def org_code(self):
        return self._org_code

    @org_code.setter
    def org_code(self, value):
        self._org_code = value
    @property
    def req_biz_no(self):
        return self._req_biz_no

    @req_biz_no.setter
    def req_biz_no(self, value):
        self._req_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.call_url:
            if hasattr(self.call_url, 'to_alipay_dict'):
                params['call_url'] = self.call_url.to_alipay_dict()
            else:
                params['call_url'] = self.call_url
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.ins_code:
            if hasattr(self.ins_code, 'to_alipay_dict'):
                params['ins_code'] = self.ins_code.to_alipay_dict()
            else:
                params['ins_code'] = self.ins_code
        if self.ol_biz_type_code:
            if hasattr(self.ol_biz_type_code, 'to_alipay_dict'):
                params['ol_biz_type_code'] = self.ol_biz_type_code.to_alipay_dict()
            else:
                params['ol_biz_type_code'] = self.ol_biz_type_code
        if self.org_app_id:
            if hasattr(self.org_app_id, 'to_alipay_dict'):
                params['org_app_id'] = self.org_app_id.to_alipay_dict()
            else:
                params['org_app_id'] = self.org_app_id
        if self.org_chnl_crtf_code:
            if hasattr(self.org_chnl_crtf_code, 'to_alipay_dict'):
                params['org_chnl_crtf_code'] = self.org_chnl_crtf_code.to_alipay_dict()
            else:
                params['org_chnl_crtf_code'] = self.org_chnl_crtf_code
        if self.org_code:
            if hasattr(self.org_code, 'to_alipay_dict'):
                params['org_code'] = self.org_code.to_alipay_dict()
            else:
                params['org_code'] = self.org_code
        if self.req_biz_no:
            if hasattr(self.req_biz_no, 'to_alipay_dict'):
                params['req_biz_no'] = self.req_biz_no.to_alipay_dict()
            else:
                params['req_biz_no'] = self.req_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalAuthinfoAuthQueryModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'call_url' in d:
            o.call_url = d['call_url']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'ins_code' in d:
            o.ins_code = d['ins_code']
        if 'ol_biz_type_code' in d:
            o.ol_biz_type_code = d['ol_biz_type_code']
        if 'org_app_id' in d:
            o.org_app_id = d['org_app_id']
        if 'org_chnl_crtf_code' in d:
            o.org_chnl_crtf_code = d['org_chnl_crtf_code']
        if 'org_code' in d:
            o.org_code = d['org_code']
        if 'req_biz_no' in d:
            o.req_biz_no = d['req_biz_no']
        return o


