#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AttachmentExplain import AttachmentExplain


class ConfigInfo(object):

    def __init__(self):
        self._attachment_explain = None
        self._collect_attachement = None
        self._collect_cert_types = None
        self._company_no = None
        self._contract_validity = None
        self._jump_url = None
        self._merchant_mini_sign_url = None
        self._notice_developer_url = None
        self._platform_order_no = None
        self._serial_no = None
        self._sign_model = None

    @property
    def attachment_explain(self):
        return self._attachment_explain

    @attachment_explain.setter
    def attachment_explain(self, value):
        if isinstance(value, AttachmentExplain):
            self._attachment_explain = value
        else:
            self._attachment_explain = AttachmentExplain.from_alipay_dict(value)
    @property
    def collect_attachement(self):
        return self._collect_attachement

    @collect_attachement.setter
    def collect_attachement(self, value):
        self._collect_attachement = value
    @property
    def collect_cert_types(self):
        return self._collect_cert_types

    @collect_cert_types.setter
    def collect_cert_types(self, value):
        if isinstance(value, list):
            self._collect_cert_types = list()
            for i in value:
                self._collect_cert_types.append(i)
    @property
    def company_no(self):
        return self._company_no

    @company_no.setter
    def company_no(self, value):
        self._company_no = value
    @property
    def contract_validity(self):
        return self._contract_validity

    @contract_validity.setter
    def contract_validity(self, value):
        self._contract_validity = value
    @property
    def jump_url(self):
        return self._jump_url

    @jump_url.setter
    def jump_url(self, value):
        self._jump_url = value
    @property
    def merchant_mini_sign_url(self):
        return self._merchant_mini_sign_url

    @merchant_mini_sign_url.setter
    def merchant_mini_sign_url(self, value):
        self._merchant_mini_sign_url = value
    @property
    def notice_developer_url(self):
        return self._notice_developer_url

    @notice_developer_url.setter
    def notice_developer_url(self, value):
        self._notice_developer_url = value
    @property
    def platform_order_no(self):
        return self._platform_order_no

    @platform_order_no.setter
    def platform_order_no(self, value):
        self._platform_order_no = value
    @property
    def serial_no(self):
        return self._serial_no

    @serial_no.setter
    def serial_no(self, value):
        self._serial_no = value
    @property
    def sign_model(self):
        return self._sign_model

    @sign_model.setter
    def sign_model(self, value):
        self._sign_model = value


    def to_alipay_dict(self):
        params = dict()
        if self.attachment_explain:
            if hasattr(self.attachment_explain, 'to_alipay_dict'):
                params['attachment_explain'] = self.attachment_explain.to_alipay_dict()
            else:
                params['attachment_explain'] = self.attachment_explain
        if self.collect_attachement:
            if hasattr(self.collect_attachement, 'to_alipay_dict'):
                params['collect_attachement'] = self.collect_attachement.to_alipay_dict()
            else:
                params['collect_attachement'] = self.collect_attachement
        if self.collect_cert_types:
            if isinstance(self.collect_cert_types, list):
                for i in range(0, len(self.collect_cert_types)):
                    element = self.collect_cert_types[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.collect_cert_types[i] = element.to_alipay_dict()
            if hasattr(self.collect_cert_types, 'to_alipay_dict'):
                params['collect_cert_types'] = self.collect_cert_types.to_alipay_dict()
            else:
                params['collect_cert_types'] = self.collect_cert_types
        if self.company_no:
            if hasattr(self.company_no, 'to_alipay_dict'):
                params['company_no'] = self.company_no.to_alipay_dict()
            else:
                params['company_no'] = self.company_no
        if self.contract_validity:
            if hasattr(self.contract_validity, 'to_alipay_dict'):
                params['contract_validity'] = self.contract_validity.to_alipay_dict()
            else:
                params['contract_validity'] = self.contract_validity
        if self.jump_url:
            if hasattr(self.jump_url, 'to_alipay_dict'):
                params['jump_url'] = self.jump_url.to_alipay_dict()
            else:
                params['jump_url'] = self.jump_url
        if self.merchant_mini_sign_url:
            if hasattr(self.merchant_mini_sign_url, 'to_alipay_dict'):
                params['merchant_mini_sign_url'] = self.merchant_mini_sign_url.to_alipay_dict()
            else:
                params['merchant_mini_sign_url'] = self.merchant_mini_sign_url
        if self.notice_developer_url:
            if hasattr(self.notice_developer_url, 'to_alipay_dict'):
                params['notice_developer_url'] = self.notice_developer_url.to_alipay_dict()
            else:
                params['notice_developer_url'] = self.notice_developer_url
        if self.platform_order_no:
            if hasattr(self.platform_order_no, 'to_alipay_dict'):
                params['platform_order_no'] = self.platform_order_no.to_alipay_dict()
            else:
                params['platform_order_no'] = self.platform_order_no
        if self.serial_no:
            if hasattr(self.serial_no, 'to_alipay_dict'):
                params['serial_no'] = self.serial_no.to_alipay_dict()
            else:
                params['serial_no'] = self.serial_no
        if self.sign_model:
            if hasattr(self.sign_model, 'to_alipay_dict'):
                params['sign_model'] = self.sign_model.to_alipay_dict()
            else:
                params['sign_model'] = self.sign_model
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConfigInfo()
        if 'attachment_explain' in d:
            o.attachment_explain = d['attachment_explain']
        if 'collect_attachement' in d:
            o.collect_attachement = d['collect_attachement']
        if 'collect_cert_types' in d:
            o.collect_cert_types = d['collect_cert_types']
        if 'company_no' in d:
            o.company_no = d['company_no']
        if 'contract_validity' in d:
            o.contract_validity = d['contract_validity']
        if 'jump_url' in d:
            o.jump_url = d['jump_url']
        if 'merchant_mini_sign_url' in d:
            o.merchant_mini_sign_url = d['merchant_mini_sign_url']
        if 'notice_developer_url' in d:
            o.notice_developer_url = d['notice_developer_url']
        if 'platform_order_no' in d:
            o.platform_order_no = d['platform_order_no']
        if 'serial_no' in d:
            o.serial_no = d['serial_no']
        if 'sign_model' in d:
            o.sign_model = d['sign_model']
        return o


