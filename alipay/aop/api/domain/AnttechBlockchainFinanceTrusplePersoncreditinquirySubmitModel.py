#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FinAttachment import FinAttachment


class AnttechBlockchainFinanceTrusplePersoncreditinquirySubmitModel(object):

    def __init__(self):
        self._attachments = None
        self._cert_no = None
        self._cert_type = None
        self._customer_name = None
        self._external_product_code = None
        self._external_user_id = None
        self._inquiry_reason = None
        self._inquiry_template = None
        self._inst_code = None
        self._request_id = None

    @property
    def attachments(self):
        return self._attachments

    @attachments.setter
    def attachments(self, value):
        if isinstance(value, list):
            self._attachments = list()
            for i in value:
                if isinstance(i, FinAttachment):
                    self._attachments.append(i)
                else:
                    self._attachments.append(FinAttachment.from_alipay_dict(i))
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
    def customer_name(self):
        return self._customer_name

    @customer_name.setter
    def customer_name(self, value):
        self._customer_name = value
    @property
    def external_product_code(self):
        return self._external_product_code

    @external_product_code.setter
    def external_product_code(self, value):
        self._external_product_code = value
    @property
    def external_user_id(self):
        return self._external_user_id

    @external_user_id.setter
    def external_user_id(self, value):
        self._external_user_id = value
    @property
    def inquiry_reason(self):
        return self._inquiry_reason

    @inquiry_reason.setter
    def inquiry_reason(self, value):
        self._inquiry_reason = value
    @property
    def inquiry_template(self):
        return self._inquiry_template

    @inquiry_template.setter
    def inquiry_template(self, value):
        self._inquiry_template = value
    @property
    def inst_code(self):
        return self._inst_code

    @inst_code.setter
    def inst_code(self, value):
        self._inst_code = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.attachments:
            if isinstance(self.attachments, list):
                for i in range(0, len(self.attachments)):
                    element = self.attachments[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attachments[i] = element.to_alipay_dict()
            if hasattr(self.attachments, 'to_alipay_dict'):
                params['attachments'] = self.attachments.to_alipay_dict()
            else:
                params['attachments'] = self.attachments
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
        if self.customer_name:
            if hasattr(self.customer_name, 'to_alipay_dict'):
                params['customer_name'] = self.customer_name.to_alipay_dict()
            else:
                params['customer_name'] = self.customer_name
        if self.external_product_code:
            if hasattr(self.external_product_code, 'to_alipay_dict'):
                params['external_product_code'] = self.external_product_code.to_alipay_dict()
            else:
                params['external_product_code'] = self.external_product_code
        if self.external_user_id:
            if hasattr(self.external_user_id, 'to_alipay_dict'):
                params['external_user_id'] = self.external_user_id.to_alipay_dict()
            else:
                params['external_user_id'] = self.external_user_id
        if self.inquiry_reason:
            if hasattr(self.inquiry_reason, 'to_alipay_dict'):
                params['inquiry_reason'] = self.inquiry_reason.to_alipay_dict()
            else:
                params['inquiry_reason'] = self.inquiry_reason
        if self.inquiry_template:
            if hasattr(self.inquiry_template, 'to_alipay_dict'):
                params['inquiry_template'] = self.inquiry_template.to_alipay_dict()
            else:
                params['inquiry_template'] = self.inquiry_template
        if self.inst_code:
            if hasattr(self.inst_code, 'to_alipay_dict'):
                params['inst_code'] = self.inst_code.to_alipay_dict()
            else:
                params['inst_code'] = self.inst_code
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceTrusplePersoncreditinquirySubmitModel()
        if 'attachments' in d:
            o.attachments = d['attachments']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'customer_name' in d:
            o.customer_name = d['customer_name']
        if 'external_product_code' in d:
            o.external_product_code = d['external_product_code']
        if 'external_user_id' in d:
            o.external_user_id = d['external_user_id']
        if 'inquiry_reason' in d:
            o.inquiry_reason = d['inquiry_reason']
        if 'inquiry_template' in d:
            o.inquiry_template = d['inquiry_template']
        if 'inst_code' in d:
            o.inst_code = d['inst_code']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


