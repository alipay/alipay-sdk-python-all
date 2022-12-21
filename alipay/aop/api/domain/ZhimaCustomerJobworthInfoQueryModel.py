#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCustomerJobworthInfoQueryModel(object):

    def __init__(self):
        self._back_url = None
        self._cert_no = None
        self._cert_type = None
        self._cloud_resume_scene = None
        self._company_certificate = None
        self._conn_key = None
        self._has_button = None
        self._has_html = None
        self._has_number = None
        self._has_qr_code = None
        self._industry_id = None
        self._job_id = None
        self._ka_visitor_id = None
        self._open_id = None
        self._user_id = None
        self._user_name = None
        self._visitor_name = None
        self._visitor_type = None
        self._visitor_url = None

    @property
    def back_url(self):
        return self._back_url

    @back_url.setter
    def back_url(self, value):
        self._back_url = value
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
    def cloud_resume_scene(self):
        return self._cloud_resume_scene

    @cloud_resume_scene.setter
    def cloud_resume_scene(self, value):
        self._cloud_resume_scene = value
    @property
    def company_certificate(self):
        return self._company_certificate

    @company_certificate.setter
    def company_certificate(self, value):
        self._company_certificate = value
    @property
    def conn_key(self):
        return self._conn_key

    @conn_key.setter
    def conn_key(self, value):
        self._conn_key = value
    @property
    def has_button(self):
        return self._has_button

    @has_button.setter
    def has_button(self, value):
        self._has_button = value
    @property
    def has_html(self):
        return self._has_html

    @has_html.setter
    def has_html(self, value):
        self._has_html = value
    @property
    def has_number(self):
        return self._has_number

    @has_number.setter
    def has_number(self, value):
        self._has_number = value
    @property
    def has_qr_code(self):
        return self._has_qr_code

    @has_qr_code.setter
    def has_qr_code(self, value):
        self._has_qr_code = value
    @property
    def industry_id(self):
        return self._industry_id

    @industry_id.setter
    def industry_id(self, value):
        self._industry_id = value
    @property
    def job_id(self):
        return self._job_id

    @job_id.setter
    def job_id(self, value):
        self._job_id = value
    @property
    def ka_visitor_id(self):
        return self._ka_visitor_id

    @ka_visitor_id.setter
    def ka_visitor_id(self, value):
        self._ka_visitor_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value
    @property
    def visitor_name(self):
        return self._visitor_name

    @visitor_name.setter
    def visitor_name(self, value):
        self._visitor_name = value
    @property
    def visitor_type(self):
        return self._visitor_type

    @visitor_type.setter
    def visitor_type(self, value):
        self._visitor_type = value
    @property
    def visitor_url(self):
        return self._visitor_url

    @visitor_url.setter
    def visitor_url(self, value):
        self._visitor_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.back_url:
            if hasattr(self.back_url, 'to_alipay_dict'):
                params['back_url'] = self.back_url.to_alipay_dict()
            else:
                params['back_url'] = self.back_url
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
        if self.cloud_resume_scene:
            if hasattr(self.cloud_resume_scene, 'to_alipay_dict'):
                params['cloud_resume_scene'] = self.cloud_resume_scene.to_alipay_dict()
            else:
                params['cloud_resume_scene'] = self.cloud_resume_scene
        if self.company_certificate:
            if hasattr(self.company_certificate, 'to_alipay_dict'):
                params['company_certificate'] = self.company_certificate.to_alipay_dict()
            else:
                params['company_certificate'] = self.company_certificate
        if self.conn_key:
            if hasattr(self.conn_key, 'to_alipay_dict'):
                params['conn_key'] = self.conn_key.to_alipay_dict()
            else:
                params['conn_key'] = self.conn_key
        if self.has_button:
            if hasattr(self.has_button, 'to_alipay_dict'):
                params['has_button'] = self.has_button.to_alipay_dict()
            else:
                params['has_button'] = self.has_button
        if self.has_html:
            if hasattr(self.has_html, 'to_alipay_dict'):
                params['has_html'] = self.has_html.to_alipay_dict()
            else:
                params['has_html'] = self.has_html
        if self.has_number:
            if hasattr(self.has_number, 'to_alipay_dict'):
                params['has_number'] = self.has_number.to_alipay_dict()
            else:
                params['has_number'] = self.has_number
        if self.has_qr_code:
            if hasattr(self.has_qr_code, 'to_alipay_dict'):
                params['has_qr_code'] = self.has_qr_code.to_alipay_dict()
            else:
                params['has_qr_code'] = self.has_qr_code
        if self.industry_id:
            if hasattr(self.industry_id, 'to_alipay_dict'):
                params['industry_id'] = self.industry_id.to_alipay_dict()
            else:
                params['industry_id'] = self.industry_id
        if self.job_id:
            if hasattr(self.job_id, 'to_alipay_dict'):
                params['job_id'] = self.job_id.to_alipay_dict()
            else:
                params['job_id'] = self.job_id
        if self.ka_visitor_id:
            if hasattr(self.ka_visitor_id, 'to_alipay_dict'):
                params['ka_visitor_id'] = self.ka_visitor_id.to_alipay_dict()
            else:
                params['ka_visitor_id'] = self.ka_visitor_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        if self.visitor_name:
            if hasattr(self.visitor_name, 'to_alipay_dict'):
                params['visitor_name'] = self.visitor_name.to_alipay_dict()
            else:
                params['visitor_name'] = self.visitor_name
        if self.visitor_type:
            if hasattr(self.visitor_type, 'to_alipay_dict'):
                params['visitor_type'] = self.visitor_type.to_alipay_dict()
            else:
                params['visitor_type'] = self.visitor_type
        if self.visitor_url:
            if hasattr(self.visitor_url, 'to_alipay_dict'):
                params['visitor_url'] = self.visitor_url.to_alipay_dict()
            else:
                params['visitor_url'] = self.visitor_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCustomerJobworthInfoQueryModel()
        if 'back_url' in d:
            o.back_url = d['back_url']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'cloud_resume_scene' in d:
            o.cloud_resume_scene = d['cloud_resume_scene']
        if 'company_certificate' in d:
            o.company_certificate = d['company_certificate']
        if 'conn_key' in d:
            o.conn_key = d['conn_key']
        if 'has_button' in d:
            o.has_button = d['has_button']
        if 'has_html' in d:
            o.has_html = d['has_html']
        if 'has_number' in d:
            o.has_number = d['has_number']
        if 'has_qr_code' in d:
            o.has_qr_code = d['has_qr_code']
        if 'industry_id' in d:
            o.industry_id = d['industry_id']
        if 'job_id' in d:
            o.job_id = d['job_id']
        if 'ka_visitor_id' in d:
            o.ka_visitor_id = d['ka_visitor_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_name' in d:
            o.user_name = d['user_name']
        if 'visitor_name' in d:
            o.visitor_name = d['visitor_name']
        if 'visitor_type' in d:
            o.visitor_type = d['visitor_type']
        if 'visitor_url' in d:
            o.visitor_url = d['visitor_url']
        return o


