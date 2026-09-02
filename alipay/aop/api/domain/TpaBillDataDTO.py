#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TpaBillDataDTO(object):

    def __init__(self):
        self._bill_status = None
        self._biz_type = None
        self._cert_no = None
        self._cert_type = None
        self._channel = None
        self._claim_application_form_url = None
        self._claim_no = None
        self._claim_status = None
        self._claim_type = None
        self._code_value = None
        self._ext_info = None
        self._hospital_branch_code = None
        self._hospital_branch_name = None
        self._hospital_code = None
        self._hospital_name = None
        self._name = None
        self._policy_id = None
        self._policy_no = None
        self._visit_time = None

    @property
    def bill_status(self):
        return self._bill_status

    @bill_status.setter
    def bill_status(self, value):
        self._bill_status = value
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
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def claim_application_form_url(self):
        return self._claim_application_form_url

    @claim_application_form_url.setter
    def claim_application_form_url(self, value):
        self._claim_application_form_url = value
    @property
    def claim_no(self):
        return self._claim_no

    @claim_no.setter
    def claim_no(self, value):
        self._claim_no = value
    @property
    def claim_status(self):
        return self._claim_status

    @claim_status.setter
    def claim_status(self, value):
        self._claim_status = value
    @property
    def claim_type(self):
        return self._claim_type

    @claim_type.setter
    def claim_type(self, value):
        self._claim_type = value
    @property
    def code_value(self):
        return self._code_value

    @code_value.setter
    def code_value(self, value):
        self._code_value = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def hospital_branch_code(self):
        return self._hospital_branch_code

    @hospital_branch_code.setter
    def hospital_branch_code(self, value):
        self._hospital_branch_code = value
    @property
    def hospital_branch_name(self):
        return self._hospital_branch_name

    @hospital_branch_name.setter
    def hospital_branch_name(self, value):
        self._hospital_branch_name = value
    @property
    def hospital_code(self):
        return self._hospital_code

    @hospital_code.setter
    def hospital_code(self, value):
        self._hospital_code = value
    @property
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self._hospital_name = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def policy_id(self):
        return self._policy_id

    @policy_id.setter
    def policy_id(self, value):
        self._policy_id = value
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value
    @property
    def visit_time(self):
        return self._visit_time

    @visit_time.setter
    def visit_time(self, value):
        self._visit_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_status:
            if hasattr(self.bill_status, 'to_alipay_dict'):
                params['bill_status'] = self.bill_status.to_alipay_dict()
            else:
                params['bill_status'] = self.bill_status
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
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.claim_application_form_url:
            if hasattr(self.claim_application_form_url, 'to_alipay_dict'):
                params['claim_application_form_url'] = self.claim_application_form_url.to_alipay_dict()
            else:
                params['claim_application_form_url'] = self.claim_application_form_url
        if self.claim_no:
            if hasattr(self.claim_no, 'to_alipay_dict'):
                params['claim_no'] = self.claim_no.to_alipay_dict()
            else:
                params['claim_no'] = self.claim_no
        if self.claim_status:
            if hasattr(self.claim_status, 'to_alipay_dict'):
                params['claim_status'] = self.claim_status.to_alipay_dict()
            else:
                params['claim_status'] = self.claim_status
        if self.claim_type:
            if hasattr(self.claim_type, 'to_alipay_dict'):
                params['claim_type'] = self.claim_type.to_alipay_dict()
            else:
                params['claim_type'] = self.claim_type
        if self.code_value:
            if hasattr(self.code_value, 'to_alipay_dict'):
                params['code_value'] = self.code_value.to_alipay_dict()
            else:
                params['code_value'] = self.code_value
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.hospital_branch_code:
            if hasattr(self.hospital_branch_code, 'to_alipay_dict'):
                params['hospital_branch_code'] = self.hospital_branch_code.to_alipay_dict()
            else:
                params['hospital_branch_code'] = self.hospital_branch_code
        if self.hospital_branch_name:
            if hasattr(self.hospital_branch_name, 'to_alipay_dict'):
                params['hospital_branch_name'] = self.hospital_branch_name.to_alipay_dict()
            else:
                params['hospital_branch_name'] = self.hospital_branch_name
        if self.hospital_code:
            if hasattr(self.hospital_code, 'to_alipay_dict'):
                params['hospital_code'] = self.hospital_code.to_alipay_dict()
            else:
                params['hospital_code'] = self.hospital_code
        if self.hospital_name:
            if hasattr(self.hospital_name, 'to_alipay_dict'):
                params['hospital_name'] = self.hospital_name.to_alipay_dict()
            else:
                params['hospital_name'] = self.hospital_name
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.policy_id:
            if hasattr(self.policy_id, 'to_alipay_dict'):
                params['policy_id'] = self.policy_id.to_alipay_dict()
            else:
                params['policy_id'] = self.policy_id
        if self.policy_no:
            if hasattr(self.policy_no, 'to_alipay_dict'):
                params['policy_no'] = self.policy_no.to_alipay_dict()
            else:
                params['policy_no'] = self.policy_no
        if self.visit_time:
            if hasattr(self.visit_time, 'to_alipay_dict'):
                params['visit_time'] = self.visit_time.to_alipay_dict()
            else:
                params['visit_time'] = self.visit_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TpaBillDataDTO()
        if 'bill_status' in d:
            o.bill_status = d['bill_status']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'channel' in d:
            o.channel = d['channel']
        if 'claim_application_form_url' in d:
            o.claim_application_form_url = d['claim_application_form_url']
        if 'claim_no' in d:
            o.claim_no = d['claim_no']
        if 'claim_status' in d:
            o.claim_status = d['claim_status']
        if 'claim_type' in d:
            o.claim_type = d['claim_type']
        if 'code_value' in d:
            o.code_value = d['code_value']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'hospital_branch_code' in d:
            o.hospital_branch_code = d['hospital_branch_code']
        if 'hospital_branch_name' in d:
            o.hospital_branch_name = d['hospital_branch_name']
        if 'hospital_code' in d:
            o.hospital_code = d['hospital_code']
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        if 'name' in d:
            o.name = d['name']
        if 'policy_id' in d:
            o.policy_id = d['policy_id']
        if 'policy_no' in d:
            o.policy_no = d['policy_no']
        if 'visit_time' in d:
            o.visit_time = d['visit_time']
        return o


