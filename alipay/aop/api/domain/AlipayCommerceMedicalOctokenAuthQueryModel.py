#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalOctokenAuthQueryModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._call_url = None
        self._ch_info = None
        self._extend_params = None
        self._ol_biz_type_code = None
        self._org_cfc_id = None
        self._org_chnl_crtf_code = None
        self._partner_city_code = None
        self._partner_id = None
        self._req_biz_no = None
        self._total_amount = None

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
    def ch_info(self):
        return self._ch_info

    @ch_info.setter
    def ch_info(self, value):
        self._ch_info = value
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        self._extend_params = value
    @property
    def ol_biz_type_code(self):
        return self._ol_biz_type_code

    @ol_biz_type_code.setter
    def ol_biz_type_code(self, value):
        self._ol_biz_type_code = value
    @property
    def org_cfc_id(self):
        return self._org_cfc_id

    @org_cfc_id.setter
    def org_cfc_id(self, value):
        self._org_cfc_id = value
    @property
    def org_chnl_crtf_code(self):
        return self._org_chnl_crtf_code

    @org_chnl_crtf_code.setter
    def org_chnl_crtf_code(self, value):
        self._org_chnl_crtf_code = value
    @property
    def partner_city_code(self):
        return self._partner_city_code

    @partner_city_code.setter
    def partner_city_code(self, value):
        self._partner_city_code = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def req_biz_no(self):
        return self._req_biz_no

    @req_biz_no.setter
    def req_biz_no(self, value):
        self._req_biz_no = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


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
        if self.ch_info:
            if hasattr(self.ch_info, 'to_alipay_dict'):
                params['ch_info'] = self.ch_info.to_alipay_dict()
            else:
                params['ch_info'] = self.ch_info
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.ol_biz_type_code:
            if hasattr(self.ol_biz_type_code, 'to_alipay_dict'):
                params['ol_biz_type_code'] = self.ol_biz_type_code.to_alipay_dict()
            else:
                params['ol_biz_type_code'] = self.ol_biz_type_code
        if self.org_cfc_id:
            if hasattr(self.org_cfc_id, 'to_alipay_dict'):
                params['org_cfc_id'] = self.org_cfc_id.to_alipay_dict()
            else:
                params['org_cfc_id'] = self.org_cfc_id
        if self.org_chnl_crtf_code:
            if hasattr(self.org_chnl_crtf_code, 'to_alipay_dict'):
                params['org_chnl_crtf_code'] = self.org_chnl_crtf_code.to_alipay_dict()
            else:
                params['org_chnl_crtf_code'] = self.org_chnl_crtf_code
        if self.partner_city_code:
            if hasattr(self.partner_city_code, 'to_alipay_dict'):
                params['partner_city_code'] = self.partner_city_code.to_alipay_dict()
            else:
                params['partner_city_code'] = self.partner_city_code
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.req_biz_no:
            if hasattr(self.req_biz_no, 'to_alipay_dict'):
                params['req_biz_no'] = self.req_biz_no.to_alipay_dict()
            else:
                params['req_biz_no'] = self.req_biz_no
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalOctokenAuthQueryModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'call_url' in d:
            o.call_url = d['call_url']
        if 'ch_info' in d:
            o.ch_info = d['ch_info']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'ol_biz_type_code' in d:
            o.ol_biz_type_code = d['ol_biz_type_code']
        if 'org_cfc_id' in d:
            o.org_cfc_id = d['org_cfc_id']
        if 'org_chnl_crtf_code' in d:
            o.org_chnl_crtf_code = d['org_chnl_crtf_code']
        if 'partner_city_code' in d:
            o.partner_city_code = d['partner_city_code']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'req_biz_no' in d:
            o.req_biz_no = d['req_biz_no']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


