#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceEmailOriginalinfoUploadModel(object):

    def __init__(self):
        self._email_address = None
        self._email_header = None
        self._email_subject = None
        self._eml_file_download_url = None
        self._out_email_id = None
        self._parse_fail_reason = None
        self._parse_tag = None
        self._receive_date = None

    @property
    def email_address(self):
        return self._email_address

    @email_address.setter
    def email_address(self, value):
        self._email_address = value
    @property
    def email_header(self):
        return self._email_header

    @email_header.setter
    def email_header(self, value):
        self._email_header = value
    @property
    def email_subject(self):
        return self._email_subject

    @email_subject.setter
    def email_subject(self, value):
        self._email_subject = value
    @property
    def eml_file_download_url(self):
        return self._eml_file_download_url

    @eml_file_download_url.setter
    def eml_file_download_url(self, value):
        self._eml_file_download_url = value
    @property
    def out_email_id(self):
        return self._out_email_id

    @out_email_id.setter
    def out_email_id(self, value):
        self._out_email_id = value
    @property
    def parse_fail_reason(self):
        return self._parse_fail_reason

    @parse_fail_reason.setter
    def parse_fail_reason(self, value):
        self._parse_fail_reason = value
    @property
    def parse_tag(self):
        return self._parse_tag

    @parse_tag.setter
    def parse_tag(self, value):
        self._parse_tag = value
    @property
    def receive_date(self):
        return self._receive_date

    @receive_date.setter
    def receive_date(self, value):
        self._receive_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.email_address:
            if hasattr(self.email_address, 'to_alipay_dict'):
                params['email_address'] = self.email_address.to_alipay_dict()
            else:
                params['email_address'] = self.email_address
        if self.email_header:
            if hasattr(self.email_header, 'to_alipay_dict'):
                params['email_header'] = self.email_header.to_alipay_dict()
            else:
                params['email_header'] = self.email_header
        if self.email_subject:
            if hasattr(self.email_subject, 'to_alipay_dict'):
                params['email_subject'] = self.email_subject.to_alipay_dict()
            else:
                params['email_subject'] = self.email_subject
        if self.eml_file_download_url:
            if hasattr(self.eml_file_download_url, 'to_alipay_dict'):
                params['eml_file_download_url'] = self.eml_file_download_url.to_alipay_dict()
            else:
                params['eml_file_download_url'] = self.eml_file_download_url
        if self.out_email_id:
            if hasattr(self.out_email_id, 'to_alipay_dict'):
                params['out_email_id'] = self.out_email_id.to_alipay_dict()
            else:
                params['out_email_id'] = self.out_email_id
        if self.parse_fail_reason:
            if hasattr(self.parse_fail_reason, 'to_alipay_dict'):
                params['parse_fail_reason'] = self.parse_fail_reason.to_alipay_dict()
            else:
                params['parse_fail_reason'] = self.parse_fail_reason
        if self.parse_tag:
            if hasattr(self.parse_tag, 'to_alipay_dict'):
                params['parse_tag'] = self.parse_tag.to_alipay_dict()
            else:
                params['parse_tag'] = self.parse_tag
        if self.receive_date:
            if hasattr(self.receive_date, 'to_alipay_dict'):
                params['receive_date'] = self.receive_date.to_alipay_dict()
            else:
                params['receive_date'] = self.receive_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceEmailOriginalinfoUploadModel()
        if 'email_address' in d:
            o.email_address = d['email_address']
        if 'email_header' in d:
            o.email_header = d['email_header']
        if 'email_subject' in d:
            o.email_subject = d['email_subject']
        if 'eml_file_download_url' in d:
            o.eml_file_download_url = d['eml_file_download_url']
        if 'out_email_id' in d:
            o.out_email_id = d['out_email_id']
        if 'parse_fail_reason' in d:
            o.parse_fail_reason = d['parse_fail_reason']
        if 'parse_tag' in d:
            o.parse_tag = d['parse_tag']
        if 'receive_date' in d:
            o.receive_date = d['receive_date']
        return o


