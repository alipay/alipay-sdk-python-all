#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditLoanapplyInsturlQueryModel(object):

    def __init__(self):
        self._arrangement_no = None
        self._biz_type = None
        self._cert_no = None
        self._cust_group_code = None
        self._ext_business_license_no = None
        self._ext_user_id = None
        self._mobile = None
        self._op_pd_code = None
        self._org_channel_code = None
        self._url_type = None
        self._user_id = None
        self._user_name = None

    @property
    def arrangement_no(self):
        return self._arrangement_no

    @arrangement_no.setter
    def arrangement_no(self, value):
        self._arrangement_no = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cust_group_code(self):
        return self._cust_group_code

    @cust_group_code.setter
    def cust_group_code(self, value):
        self._cust_group_code = value
    @property
    def ext_business_license_no(self):
        return self._ext_business_license_no

    @ext_business_license_no.setter
    def ext_business_license_no(self, value):
        self._ext_business_license_no = value
    @property
    def ext_user_id(self):
        return self._ext_user_id

    @ext_user_id.setter
    def ext_user_id(self, value):
        self._ext_user_id = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def op_pd_code(self):
        return self._op_pd_code

    @op_pd_code.setter
    def op_pd_code(self, value):
        self._op_pd_code = value
    @property
    def org_channel_code(self):
        return self._org_channel_code

    @org_channel_code.setter
    def org_channel_code(self, value):
        self._org_channel_code = value
    @property
    def url_type(self):
        return self._url_type

    @url_type.setter
    def url_type(self, value):
        self._url_type = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.arrangement_no:
            if hasattr(self.arrangement_no, 'to_alipay_dict'):
                params['arrangement_no'] = self.arrangement_no.to_alipay_dict()
            else:
                params['arrangement_no'] = self.arrangement_no
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cust_group_code:
            if hasattr(self.cust_group_code, 'to_alipay_dict'):
                params['cust_group_code'] = self.cust_group_code.to_alipay_dict()
            else:
                params['cust_group_code'] = self.cust_group_code
        if self.ext_business_license_no:
            if hasattr(self.ext_business_license_no, 'to_alipay_dict'):
                params['ext_business_license_no'] = self.ext_business_license_no.to_alipay_dict()
            else:
                params['ext_business_license_no'] = self.ext_business_license_no
        if self.ext_user_id:
            if hasattr(self.ext_user_id, 'to_alipay_dict'):
                params['ext_user_id'] = self.ext_user_id.to_alipay_dict()
            else:
                params['ext_user_id'] = self.ext_user_id
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.op_pd_code:
            if hasattr(self.op_pd_code, 'to_alipay_dict'):
                params['op_pd_code'] = self.op_pd_code.to_alipay_dict()
            else:
                params['op_pd_code'] = self.op_pd_code
        if self.org_channel_code:
            if hasattr(self.org_channel_code, 'to_alipay_dict'):
                params['org_channel_code'] = self.org_channel_code.to_alipay_dict()
            else:
                params['org_channel_code'] = self.org_channel_code
        if self.url_type:
            if hasattr(self.url_type, 'to_alipay_dict'):
                params['url_type'] = self.url_type.to_alipay_dict()
            else:
                params['url_type'] = self.url_type
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoanapplyInsturlQueryModel()
        if 'arrangement_no' in d:
            o.arrangement_no = d['arrangement_no']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cust_group_code' in d:
            o.cust_group_code = d['cust_group_code']
        if 'ext_business_license_no' in d:
            o.ext_business_license_no = d['ext_business_license_no']
        if 'ext_user_id' in d:
            o.ext_user_id = d['ext_user_id']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'op_pd_code' in d:
            o.op_pd_code = d['op_pd_code']
        if 'org_channel_code' in d:
            o.org_channel_code = d['org_channel_code']
        if 'url_type' in d:
            o.url_type = d['url_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


